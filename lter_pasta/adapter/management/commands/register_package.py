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

''':mod:`register_package`
==========================

:Synopsis:
  Manually add a package to the queue. For use if package registration fails.
  For instance, PASTA does not retry a failed package registration. So, if
  PASTA-GMN was down when a new package got registered in PASTA, the package
  can be registered manually with this command. Note that this will not work
  if a newer revision of the package has already been registered.

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
from django.core.management.base import LabelCommand

# Add some PASTA GMN Adapter paths to include path.
_here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
sys.path.append(_here('../'))
sys.path.append(_here('../types/generated'))

# App.
import settings
import data_package_manager_client
import adapter.sql

class Command(LabelCommand):
  help = 'Register package'

  def handle_label(self, package_id, **options):
    self.log_setup()

    logging.info('Running management command: '
                 'register_package')

    verbosity = int(options.get('verbosity', 0))

    if verbosity < 1:
      logging.getLogger('').setLevel(logging.ERROR)

    self._register_package(package_id)


  def _register_package(self, package_id):
    self._add_to_queue(package_id)


  def _add_to_queue(self, package_id):
    o = urlparse.urlparse(settings.ADAPTER_BASE_URL)
    c = httplib.HTTPConnection(o.netloc)
    headers = {"INTERNAL_CLIENT": '1'}
    c.request('POST', o.path + '/pasta/new_package', package_id, headers)
    response = c.getresponse()
    logging.info('ADD RESPONSE: {0}'.format(response.read()))


  def log_setup(self):
    # Set up logging. We output only to stdout. Instead of also writing to a log
    # file, redirect stdout to a log file when the script is executed from cron.
    logging.getLogger('').setLevel(logging.DEBUG)
    formatter = logging.Formatter(
      '%(asctime)s %(levelname)-8s %(name)s %(module)s %(message)s',
      '%Y-%m-%d %H:%M:%S')
    console_logger = logging.StreamHandler(sys.stdout)
    console_logger.setFormatter(formatter)
    logging.getLogger('').addHandler(console_logger)
