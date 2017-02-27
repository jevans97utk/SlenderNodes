#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
''':mod:`register_existing_packages`
====================================

:Synopsis:
  Populate the queue with packages that already exist on PASTA. For use when
  initially deploying PASTA-GMN.

:Author:
  Roger Dahl
'''

# Stdlib.
import httplib
import logging
import os
import sys
import urlparse

# Django.
from django.core.management.base import NoArgsCommand

# Add some PASTA GMN Adapter paths to include path.
_here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
sys.path.append(_here('../'))
sys.path.append(_here('../types/generated'))

# App.
import settings
import data_package_manager_client
import adapter.sql

debug_filter = (
  ('knb-lter-mcr', 5008),
  ('knb-lter-mcr', 32),
  ('knb-lter-luq', 107),
  ('knb-lter-knz', 205),
  ('knb-lter-knz', 205),
  ('knb-lter-cap', 514),
  ('knb-lter-cap', 514),
  ('knb-lter-sev', 190),
  ('knb-lter-knz', 33),
  ('knb-lter-knz', 9),
  ('knb-lter-kbs', 23),
  ('knb-lter-hfr', 4),
  ('knb-lter-arc', 10134),
)


class Command(NoArgsCommand):
  help = 'Register existing packages'

  def handle_noargs(self, **options):
    self.log_setup()

    logging.info('Running management command: ' 'register_existing_packages')

    verbosity = int(options.get('verbosity', 0))

    if verbosity < 1:
      logging.getLogger('').setLevel(logging.ERROR)

    self.register_existing_packages()

  def register_existing_packages(self):
    self._clear_database()
    self._register_packages()

  def _register_packages(self):
    c = data_package_manager_client.DataPackageManagerClient()
    for scope in c.list_data_package_scopes():
      ####################################################################################
      # for now, ignore ecotrends because all the packages are private.
      #if 'ecotrends' in scope:
      #  logging.info('Skipped ecotrends')
      #  continue
      for identifier in c.list_data_package_identifiers(scope):
        ##################################################################################
        # For debugging, filter all but packages that are being debugged.
        #if (scope, identifier) not in debug_filter:
        #  logging.info('Skipped {0} {1}'.format(scope, identifier))
        #  continue
        for revision in c.list_data_package_revisions(scope, identifier):
          package_id = '{0}.{1}.{2}'.format(scope, identifier, revision)
          self._add_to_queue(package_id)

  def _add_to_queue(self, package_id):
    o = urlparse.urlparse(settings.ADAPTER_BASE_URL)
    c = httplib.HTTPConnection(o.netloc)
    headers = {"INTERNAL_CLIENT": '1'}
    c.request('POST', o.path + '/pasta/new_package', package_id, headers)
    response = c.getresponse()
    logging.info('ADD RESPONSE: {0}'.format(response.read()))

  def _clear_database(self):
    adapter.sql.clear_database()
    #o = urlparse.urlparse(settings.ADAPTER_BASE_URL)
    #c = httplib.HTTPConnection(o.netloc)
    #headers = {"INTERNAL_CLIENT": '1'}
    #c.request('GET', o.path + '/admin?clear_database')
    #response = c.getresponse()
    #print response.read()

  def log_setup(self):
    # Set up logging. We output only to stdout. Instead of also writing to a log
    # file, redirect stdout to a log file when the script is executed from cron.
    logging.getLogger('').setLevel(logging.DEBUG)
    formatter = logging.Formatter(
      '%(asctime)s %(levelname)-8s %(name)s %(module)s %(message)s',
      '%Y-%m-%d %H:%M:%S'
    )
    console_logger = logging.StreamHandler(sys.stdout)
    console_logger.setFormatter(formatter)
    logging.getLogger('').addHandler(console_logger)
