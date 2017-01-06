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

''':mod:`process_population_queue`
==================================

:Synopsis:
  Iterate over queue of objects registered for population and attempt to
  create them on GMN.
:Author:
  Roger Dahl
'''

# Stdlib.
import StringIO
import fcntl
import hashlib
import logging
import os
import stat
import sys
import tempfile
import time

# Django.
from django.core.management.base import NoArgsCommand

# D1.
import d1_client.cnclient
import d1_client.mnclient
import d1_client.data_package

import d1_common.checksum
import d1_common.const
import d1_common.types.exceptions
import d1_common.types.generated.dataoneTypes as dataoneTypes

# Add some PASTA GMN Adapter paths to include path.
_here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
sys.path.append(_here('../'))
sys.path.append(_here('../types/generated'))

# App.
import settings
import data_package_manager_client
import pasta_gmn_adapter.adapter.sql
import pasta_gmn_adapter.api_types.eml_access


class Command(NoArgsCommand):
  help = 'Process the population queue'

  def handle_noargs(self, **options):
    self.log_setup()

    self.abort_if_other_instance_is_running()

    logging.info('Running management command: '
                 'process_population_queue')

    verbosity = int(options.get('verbosity', 0))

    if verbosity >= 1:
      logging.getLogger('').setLevel(logging.DEBUG)
    else:
      logging.getLogger('').setLevel(logging.INFO)

    #pasta_gmn_adapter.adapter.sql.clear_database()

    population_queue_processor = PopulationQueueProcessor()
    population_queue_processor.process_population_queue()


  def log_setup(self):
    # Set up logging. We output only to stdout. Instead of also writing to a log
    # file, redirect stdout to a log file when the script is executed from cron.
    formatter = logging.Formatter(
      '%(asctime)s %(levelname)-8s %(name)s %(module)s %(message)s',
      '%Y-%m-%d %H:%M:%S')
    console_logger = logging.StreamHandler(sys.stdout)
    console_logger.setFormatter(formatter)
    logging.getLogger('').addHandler(console_logger)


  def abort_if_other_instance_is_running(self):
    single_path = os.path.join(tempfile.gettempdir(),
                               os.path.basename(os.path.splitext(__file__)[0] +
                                                '.single'))
    f = open(single_path, 'w')
    try:
      fcntl.lockf(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
      self.logger.info('Aborted: Another instance is still running')
      exit(0)


#===============================================================================

class PopulationQueueProcessor(object):
  def __init__(self):
    self.logger = logging.getLogger(self.__class__.__name__)


  def process_population_queue(self):
    # Debug: Try a single package without catching any exceptions.
    #package = {
    #  'package_scope': 'knb-lter-hbs',
    #  'package_identifier': 27,
    #  'package_revision': 6,
    #}
    #self._process_package(package)
    #exit()

    population_queue = self._get_uncompleted_packages()
    for package in population_queue:
      try:
        self._process_package(package)
      except (data_package_manager_client.DataPackageManagerException,
              pasta_gmn_adapter.api_types.eml_access.EMLAccessException) as e:
        self.logger.error('Failed: {0}'.format(str(e)))
        if e.status == 401:
          self._insert_package_processing_status(package, 'private',
            e.status, u'msg({0}) body({1})'.format(e.msg, e.body))
        else:
          self._insert_package_processing_status(package, 'error',
            e.status, u'msg({0}) body({1})'.format(e.msg, e.body))
      except d1_common.types.exceptions.DataONEException as e:
        self.logger.exception('Population failed with DataONE Exception:')
        self._insert_package_processing_status(package, 'error',
          e.errorCode, u'description({0}) body({1})'.format(e.description, e.traceInformation))
      except (PopulateError, Exception, object) as e:
        self.logger.exception('Population failed with internal exception:')
        self._insert_package_processing_status(package, 'error', return_body=str(e))
      else:
        self._insert_package_processing_status(package, 'completed')


  def _get_uncompleted_packages(self):
    return pasta_gmn_adapter.adapter.sql.select_population_queue_uncompleted()


  def _process_package(self, package):
    self.logger.info('-' * 40)
    package_id = PackageID(package['package_scope'], package['package_identifier'], package['package_revision'])
    self.logger.info('Processing Package: {0}'.format(package_id))
    data_package_info_collector = DataPackageInfoCollector()
    package_info = data_package_info_collector.collect_package_info(package_id)
    ###package_info = settings.package_info
    #self.logger.info(pprint.pformat(package_info))
    previous_revision = pasta_gmn_adapter.adapter.sql.select_latest_package_revision(
      package['package_scope'], package['package_identifier'])
    gmn_package_creator = GMNPackageCreator()
    if previous_revision is None:
      gmn_package_creator.create_package(package_info)
    else:
      previous_package_id = PackageID(package['package_scope'], package['package_identifier'], previous_revision)
      previous_package_info = data_package_info_collector.collect_package_info(previous_package_id)
      gmn_package_creator.update_package(package_info, previous_package_info)


  def _insert_package_processing_status(self, package, status, return_code=0, return_body=''):
    pasta_gmn_adapter.adapter.sql.insert_process_status(package['id'], status,
      return_code, return_body[:pasta_gmn_adapter.adapter.sql.VCHAR_LENGTH])

#===============================================================================

class DataPackageInfoCollector(object):
  '''Collect all the information about the data package and its entities that
  is required for exposing the objects to DataONE.

  Cardinality of a PASTA data package:
  Metadata: 1
  Quality report: 1
  Data: 1 to many
  '''
  def __init__(self):
    self._pasta_client = data_package_manager_client.DataPackageManagerClient()
    self._pasta_client_public_access = \
      data_package_manager_client.DataPackageManagerClient(add_basic_auth_header=False)


  def collect_package_info(self, package_id):
    entity_ids = self._pasta_client.list_data_entities(package_id)
    self._raise_if_not_authorized_for_all_entities(package_id, entity_ids)

    return {
      'package': self._get_package_info(package_id),
      'entities': self._get_package_entities_info(package_id, entity_ids),
      'report': self._get_quality_report_info(package_id),
      'metadata': self._get_metadata_info(package_id),
    }


  def _raise_if_not_authorized_for_all_entities(self, package_id, entity_ids):
    for entity_id in entity_ids:
      self._raise_if_not_authorized(package_id, entity_id)


  def _raise_if_not_authorized(self, package_id, entity_id):
    self._pasta_client_public_access.is_authorized(package_id, entity_id)


  def _get_package_info(self, package_id):
    return {
      'doi': self._pasta_client.read_data_package_doi(package_id),
      'permissions': self._pasta_client.read_data_package_acl(package_id)
    }


  def _get_package_entities_info(self, package_id, entity_ids):
    entity_info = []
    for entity_id in entity_ids:
      resource_id = self._pasta_client.entity_uri(package_id, entity_id)
      entity_info.append(
        {
          'entity_id': entity_id,
          'resource_id': resource_id,
          'header': self._pasta_client.get_data_entry_header(resource_id),
          'permissions': self._pasta_client.read_data_entity_acl(package_id, entity_id),
          'checksum': self._pasta_client.read_data_entity_checksum(package_id, entity_id),
        }
      )
    return entity_info


  def _get_quality_report_info(self, package_id):
    report_uri = self._pasta_client.report_uri(package_id)
    return {
      'resource_id': report_uri,
      'header': self._pasta_client.get_data_entry_header(report_uri),
      'permissions': self._pasta_client.read_quality_report_acl(package_id),
      'checksum': self._pasta_client.read_data_package_report_checksum(package_id),
    }


  def _get_metadata_info(self, package_id):
    metadata_uri = self._pasta_client.metadata_uri(package_id)
    return {
      'resource_id': metadata_uri,
      'header': self._pasta_client.get_data_entry_header(metadata_uri),
      'permissions': self._pasta_client.read_metadata_acl(package_id),
      'format_id': self._pasta_client.read_metadata_format_id(package_id),
      'checksum': self._pasta_client.read_metadata_checksum(package_id),
    }

#===============================================================================

class GMNPackageCreator(object):
  def __init__(self):
    self._gmn_client = self._create_gmn_client()
    self._sys_meta_creator = SysmetaCreator()


  def create_package(self, package_info):
    self._create_data_entities(package_info['entities'])
    self._create_quality_report(package_info['report'])
    self._create_metadata(package_info['metadata'])
    resource_map, resource_map_meta = self._generate_resource_map_with_meta(package_info)
    # Resource maps contain created and modified timestamps. The Foresite
    # library allows setting the created timestamp but always sets the modified
    # timestamp to the current date and time. So, without modifying Foresite
    # itself, it's not possible to have it generate resource maps that have the
    # same checksum each time. So we just assume that any existing resource map
    # is for the correct package.
    self._create_managed_object(resource_map, resource_map_meta, verify_checksum=False)


  def update_package(self, package_info, previous_package_info):
    self._create_data_entities(package_info['entities'])
    self._create_quality_report(package_info['report'])
    self._create_metadata(package_info['metadata'])
    resource_map, resource_map_meta = self._generate_resource_map_with_meta(package_info)
    previous_package_pid = previous_package_info['package']['doi']
    self._update_managed_object(resource_map, resource_map_meta, previous_package_pid)


  def _create_data_entities(self, entities):
    for data_entity_meta in entities:
      self._create_wrapped_object(data_entity_meta)


  def _create_quality_report(self, report_meta):
    self._create_wrapped_object(report_meta)


  def _create_metadata(self, metadata_meta):
    self._create_wrapped_object(metadata_meta)


  def _generate_resource_map_with_meta(self, package_info):
    package_pid = package_info['package']['doi']
    metadata_pid = package_info['metadata']['resource_id']
    report_pid = package_info['report']['resource_id']
    entity_pids = [e['resource_id'] for e in package_info['entities']]
    resource_map = self._generate_resource_map(package_pid, metadata_pid,
                                               [report_pid] + entity_pids)
    resource_map_meta = {
      'resource_id': package_pid,
      'header': {
        'content-length': len(resource_map),
        'content-type': 'http://www.openarchives.org/ore/terms',
      },
      # The permissions for the resource map are generated from the permissions
      # on the PASTA package itself.
      'permissions': package_info['package']['permissions']
    }
    return resource_map, resource_map_meta


  def _generate_resource_map(self, package_pid, metadata_pid, entity_pids):
    resource_map_generator = d1_client.data_package.ResourceMapGenerator(
      settings.DATAONE_ROOT_URL)
    return resource_map_generator.simple_generate_resource_map(package_pid,
      metadata_pid, entity_pids)


  def _create_wrapped_object(self, object_meta, verify_checksum=True):
    pid = object_meta['resource_id']
    sci_obj_placeholder = StringIO.StringIO()
    sys_meta = self._generate_sys_meta_for_object(object_meta)
    header = self._generate_vendor_extension_remote_url(object_meta['resource_id'])
    if not self._object_exists(sys_meta, verify_checksum):
      self._gmn_client.create(pid, sci_obj_placeholder, sys_meta, header)


  def _create_managed_object(self, sci_obj, object_meta, verify_checksum=True):
    pid = object_meta['resource_id']
    sys_meta = self._generate_sys_meta_for_object(object_meta, sci_obj)
    if not self._object_exists(sys_meta, verify_checksum):
      sci_obj_flo = StringIO.StringIO(sci_obj)
      self._gmn_client.create(pid, sci_obj_flo, sys_meta)


  def _update_managed_object(self, sci_obj, object_meta, previous_package_pid,
                             verify_checksum=True):
    pid = object_meta['resource_id']
    sys_meta = self._generate_sys_meta_for_object(object_meta, sci_obj)
    if not self._object_exists(sys_meta, verify_checksum):
      sys_meta.obsoletes = previous_package_pid
      sci_obj_flo = StringIO.StringIO(sci_obj)
      self._gmn_client.update(previous_package_pid, sci_obj_flo, pid, sys_meta)


  def _object_exists(self, sys_meta, verify_checksum):
    pid = sys_meta.identifier.value()
    try:
      sys_meta_existing = self._gmn_client.getSystemMetadata(pid)
    except d1_common.types.exceptions.NotFound:
      return False
    if verify_checksum and not d1_common.checksum.checksums_are_equal(
      sys_meta.checksum, sys_meta_existing.checksum):
        raise PopulateError('Object already exists but has a different checksum.'
                            'pid={}, existing={}/{}, new={}/{}'.format(
                            pid,
                            sys_meta_existing.checksum.algorithm,
                            sys_meta_existing.checksum.value(),
                            sys_meta.checksum.algorithm,
                            sys_meta.checksum.value()))
    return True

  def _generate_sys_meta_for_object(self, object_meta, sci_obj=None):
    pid = object_meta['resource_id']
    size = object_meta['header']['content-length']
    content_type = object_meta['header']['content-type']
    if sci_obj is None:
      sha1_checksum = object_meta['checksum']
    else:
      sha1_checksum = hashlib.sha1(sci_obj).hexdigest()
    permissions = object_meta['permissions']
    format_id = object_meta.get('format_id', None)
    sys_meta = self._sys_meta_creator.create_sys_meta_for_resource(
      pid, size, content_type, sha1_checksum, permissions, format_id)
    return sys_meta


  def _generate_vendor_extension_remote_url(self, object_url):
    '''GMN has a "vendor specific extension" that allows it to stream data
    from a web server instead of storing it locally. This generates the header
    that enables the extension.'''
    return {
      'VENDOR-GMN-REMOTE-URL': object_url
    }


  def _create_gmn_client(self):
    return d1_client.mnclient.MemberNodeClient(
      base_url=settings.GMN_BASE_URL,
      cert_path=settings.CLIENT_CERT_PATH,
      key_path=settings.CLIENT_CERT_PRIVATE_KEY_PATH,
      timeout=settings.GMN_RESPONSE_TIMEOUT,
    )

#===============================================================================

class SysmetaCreator(object):
  def __init__(self):
    self._media_type_mapper = self._create_media_type_mapper()


  def create_sys_meta_for_resource(self, pid, size, content_type, sha1_checksum,
                                   eml_access_rules, format_id=None):
    if format_id is None:
      format_id = self._media_type_mapper.format_id_from_media_type(content_type)
    d1_access_rules = eml_access_rules.get_as_dataone_rules()
    return self._generate_sys_meta(pid, size, format_id, sha1_checksum, d1_access_rules)


  def _generate_sys_meta(self, pid, size, format_id, sha1_checksum, d1_access_rules):
    sys_meta = dataoneTypes.systemMetadata()
    sys_meta.serialVersion = 1
    sys_meta.identifier = pid
    sys_meta.size = size
    sys_meta.formatId = format_id
    sys_meta.rightsHolder = settings.DATAONE_OWNER_IDENTITY
    sys_meta.checksum = dataoneTypes.checksum(sha1_checksum)
    sys_meta.checksum.algorithm = 'SHA-1'
    sys_meta.accessPolicy = d1_access_rules
    return sys_meta


  def _generate_public_access_policy(self):
    accessPolicy = dataoneTypes.accessPolicy()
    accessRule = dataoneTypes.AccessRule()
    accessRule.subject.append(d1_common.const.SUBJECT_PUBLIC)
    permission = dataoneTypes.Permission('read')
    accessRule.permission.append(permission)
    accessPolicy.append(accessRule)
    return accessPolicy


  def _create_media_type_mapper(self):
    return MediaTypeToFormatIDMapper()

#===============================================================================

class MediaTypeToFormatIDMapper():
  def __init__(self):
    self._format_ids = self._get_valid_format_ids()


  def format_id_from_media_type(self, media_type):
    if media_type in settings.ASYNC_MEDIA_TYPE_MAP:
      return settings.ASYNC_MEDIA_TYPE_MAP[media_type]
    if media_type in self._format_ids:
      return media_type
    return settings.DEFAULT_MEDIA_TYPE


  def _get_valid_format_ids(self):
    refresh = False
    try:
      if self._format_id_cache_file_is_stale():
        refresh = True
    except OSError:
      refresh = True
    if refresh:
      self._refresh_format_id_cache_file()
    return self._read_format_ids_from_cache_file()


  def _read_format_ids_from_cache_file(self):
    p = self._get_format_id_cache_file_path()
    return [line.strip() for line in open(p).readlines()]


  def _refresh_format_id_cache_file(self):
    cn_client = d1_client.cnclient.CoordinatingNodeClient()
    format_ids = cn_client.listFormats()
    p = self._get_format_id_cache_file_path()
    open(p, 'w').write('\n'.join([o.formatId for o in format_ids.objectFormat]))


  def _format_id_cache_file_is_stale(self):
    p = self._get_format_id_cache_file_path()
    file_age_seconds = time.time() - os.stat(p)[stat.ST_MTIME]
    return file_age_seconds > settings.ASYNC_MAX_FORMAT_ID_AGE_SECONDS


  def _get_format_id_cache_file_path(self):
    return os.path.join(tempfile.gettempdir(), settings.FORMAT_ID_CACHE_FILENAME)

# ==============================================================================

#class GMNUncheckedCreateClient(d1_client.mnclient.MemberNodeClient):
#  '''Extend the d1_client.MemberNodeClient class with wrappers for GMN's
#  unchecked create interface.
#  '''
#  def __init__(self, base_url, timeout=d1_common.const.RESPONSE_TIMEOUT,
#    defaultHeaders=None, cert_path=None, key_path=None, strict=True,
#    capture_response_body=False, version='internal', types=gmn_types):
#
#    d1_client.mnclient.MemberNodeClient.__init__(self, base_url=base_url,
#      timeout=timeout, defaultHeaders=defaultHeaders, cert_path=cert_path,
#      key_path=key_path, strict=strict,
#      capture_response_body=capture_response_body, version=version, types=types)
#
#    self.logger = logging.getLogger(self.__class__.__name__)
#
#
#  def internal_get_setting(self, setting):
#    url = self._rest_url('get_setting/%(setting)s', setting=setting)
#    response = self.GET(url)
#    return self._read_dataone_type_response(response)
#
#
#  #@util.utf8_to_unicode
#  def internal_unchecked_create(self, pid, sci_obj, sysmeta,
#                                vendorSpecific=None):
#    if vendorSpecific is None:
#      vendorSpecific = {}
#    url = self._rest_url('unchecked_create/create/%(pid)s', pid=pid)
#    mime_multipart_fields = [
#      ('pid', pid.encode('utf-8')),
#    ]
#    mime_multipart_files = [
#      ('object', 'content.bin', sci_obj),
#      ('sysmeta', 'sysmeta.xml', sysmeta),
#    ]
#    response = self.POST(url, fields=mime_multipart_fields,
#                         files=mime_multipart_files, headers=vendorSpecific)
#    return self._read_boolean_response(response)

# ==============================================================================

class UncheckedCreateError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return str(self.value)

# ==============================================================================

class PopulateError(Exception):
  def __init__(self, value):
    self.value = value


  def __str__(self):
    return str(self.value)

#===============================================================================

class PackageID():
  def __init__(self, scope, identifier, revision):
    self._scope = scope
    self._identifier = identifier
    self._revision = revision


  def __str__(self):
    return u'{0}({1}, {2}, {3})'.format(self.__class__.__name__, self._scope,
                                        self._identifier, self._revision)


  def scope(self):
    return self._scope


  def identifier(self):
    return self._identifier


  def revision(self):
    return self._revision
