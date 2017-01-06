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

''':mod:`Module data_package_manager_client`
============================================

:Synopsis:
  This module implements a client for the PASTA Package Manager REST API.
:Author:
  Roger Dahl
'''

# Stdlib.
import base64
import logging
import httplib
import urlparse
import StringIO
import sys

# D1.
try:
  import d1_common.const
  import d1_common.restclient
  import d1_common.util
  import d1_common.url
except ImportError as e:
  sys.stderr.write('Import error: {0}\n'.format(str(e)))
  sys.stderr.write('Try: easy_install DataONE_Common\n')
  raise

import settings
import pasta_gmn_adapter.api_types.eml_access


# Raised when the Data Package Manager returns an error response.
class DataPackageManagerException(Exception):
  def __init__(self, msg, status, body):
    self.msg = msg
    self.status = status
    self.body = body


  def __str__(self):
    return ('DataPackageManagerException: message({0}) status({1}) body({2})'
      .format(self.msg, self.status, self.body))

#=============================================================================

class DataPackageManagerClient(d1_common.restclient.RESTClient):
  '''PASTA Data Package Manager web service API methods that are used by the
  PASTA GMN Adapter.

  Error responses are translated into exceptions.
  '''
  def __init__(self,
               base_url=settings.PASTA_BASE_URL,
               timeout=settings.PASTA_RESPONSE_TIMEOUT,
               defaultHeaders=None,
               cert_path=None,
               key_path=None,
               strict=True,
               capture_response_body=False,
               add_basic_auth_header=True):
    '''Connect to the PASTA Data Package Manager web service API.

    :param base_url: Data Package Manager web service API Base URL
    :type host: string
    :param timeout: Time in seconds that requests will wait for a response.
    :type timeout: integer
    :param defaultHeaders: headers that will be sent with all requests.
    :type defaultHeaders: dictionary
    :param cert_path: Path to a PEM formatted certificate file.
    :type cert_path: string
    :param key_path: Path to a PEM formatted file that contains the private key
      for the certificate file. Only required if the certificate file does not
      itself contain a private key.
    :type key_path: string
    :param strict: Raise BadStatusLine if the status line can’t be parsed
      as a valid HTTP/1.0 or 1.1 status line.
    :type strict: boolean
    :param capture_response_body: Capture the response body from the last
      operation and make it available in last_response_body.
    :type capture_response_body: boolean
    '''
    self.logger = logging.getLogger('DataPackageManagerClient')
    self.logger.debug('baseURL: {0}'.format(base_url))
    # Set default headers.
    if defaultHeaders is None:
      defaultHeaders = {
        # Workaround for issue where PASTA appears to return an invalid response
        # after the connection has been reused many times (only happens for
        # packages with many data entities).
        'Connection': 'close',
      }
    if 'User-Agent' not in defaultHeaders:
      defaultHeaders['User-Agent'] = settings.PASTA_GMN_ADAPTER_USER_AGENT
    if 'Charset' not in defaultHeaders:
      defaultHeaders['Charset'] = d1_common.const.DEFAULT_CHARSET
    if add_basic_auth_header:
      defaultHeaders.update((self._mk_http_basic_auth_header(),))
    # Init the RESTClient base class.
    scheme, host, port, selector = self._parse_url(base_url)[:4]
    d1_common.restclient.RESTClient.__init__(self, host=host, scheme=scheme,
      port=port, timeout=timeout, defaultHeaders=defaultHeaders,
      cert_path=cert_path, key_path=key_path, strict=strict)
    self.base_url = base_url
    self.selector = selector
    self.version = ''
    #self.types = types
    self.last_response_body = None
    # Set this to True to preserve a copy of the last response.read() as the
    # body attribute of self.last_response_body
    self.capture_response_body = capture_response_body


  def _mk_http_basic_auth_header(self):
    return ('Authorization', 'Basic {0}'.format(
      base64.standard_b64encode('{0}:{1}'.format(
        settings.PASTA_API_USERNAME, settings.PASTA_API_PASSWORD))))


  def _parse_url(self, url):
    parts = urlparse.urlsplit(url)
    if parts.port is None:
      port = 443 if parts.scheme == 'https' else 80
    else:
      port = parts.port
    host = parts.netloc.split(':')[0]
    return parts.scheme, host, port, parts.path, parts.query, parts.fragment

  # ----------------------------------------------------------------------------
  # Response handling.
  # ----------------------------------------------------------------------------

  # When expecting boolean response:
  #
  #   If status is 200:
  #     -> Ignore content_type and return True
  #
  #   If status is NOT 200:
  #     -> ERROR
  #
  # When expecting an XML document:
  #
  #   If status is 200 and content_type is "application/xml":
  #     - Return XML document
  #   Else:
  #     - Raise exception with body of response as error message.
  #
  # When expecting a text document:
  #
  #   If status is 200 and content_type is "text/plain":
  #     - Return text document.
  #   Else:
  #     - Raise exception with body of response as error message.
  
  def _get_data_redirect_header(self, redirect_url):
    urlsplit = urlparse.urlparse(redirect_url)
    full_path = urlsplit.path + '?' + urlsplit.query
    conn = httplib.HTTPConnection(urlsplit.netloc)
    conn.request('HEAD', full_path)
    return conn.getresponse()

  def _read_and_capture(self, response):
    response_body = response.read()
    if self.capture_response_body:
      self.last_response_body = response_body
    return response_body


  def _raise_data_package_manager_exception(self, msg, response):
    response_body = self._read_and_capture(response)
    raise DataPackageManagerException(msg, response.status, response_body)


  def _raise_service_failure_invalid_content_type(self, response):
    msg = StringIO.StringIO()
    msg.write('Data Package Manager responded with a valid status code but '
              'failed to include the expected Content-Type\n')
    msg.write('Status code: {0}\n'.format(response.status))
    msg.write('Content-Type: {0}\n'.format(response.getheader('Content-Type')))
    self._raise_data_package_manager_exception(msg.getvalue(), response)


  def _content_type_is_xml(self, response):
    return d1_common.util.get_content_type(
      response.getheader('Content-Type')) \
        in d1_common.const.CONTENT_TYPE_XML_MEDIA_TYPES


  def _content_type_is_text(self, response):
    return d1_common.util.get_content_type(
      response.getheader('Content-Type')) == 'text/plain'


  def _status_is_200_ok(self, response):
    return response.status == httplib.OK

  def _status_is_307_temporary_redirect(self, response):
    return response.status == httplib.TEMPORARY_REDIRECT

  def _read_boolean_response(self, response):
    if self._status_is_200_ok(response):
      self._read_and_capture(response)
      return True
    self._error(response)


  def _read_xml_response(self, response):
    if not self._status_is_200_ok(response):
      return self._raise_data_package_manager_exception('Error', response)
    if not self._content_type_is_xml(response):
      self._raise_service_failure_invalid_content_type(response)
    return response.read()


  def _read_text_response(self, response):
    if not self._status_is_200_ok(response):
      return self._raise_data_package_manager_exception('Error', response)
    if not self._content_type_is_text(response):
      self._raise_service_failure_invalid_content_type(response)
    return response.read()


  def _read_raw_response(self, response):
    if not self._status_is_200_ok(response):
      return self._raise_data_package_manager_exception('Error', response)
    return response.read()


  def _read_header_response(self, response):
    if not self._status_is_200_ok(response):
      return self._raise_data_package_manager_exception('Error', response)
    # Must empty the response body to ready the connection for another
    # request. Since a HEAD request was used, the body should be empty.
    response.read()
    return dict(response.getheaders())


  def _read_eml_access_response(self, response):
    if not self._status_is_200_ok(response):
      return self._raise_data_package_manager_exception('Error', response)
    eml_access_xml_doc = response.read()
    return pasta_gmn_adapter.api_types.eml_access.EMLAccess(eml_access_xml_doc)

  # ----------------------------------------------------------------------------
  # Misc.
  # ----------------------------------------------------------------------------

  def _rest_url(self, path_format, **args):
    for k in args.keys():
      args[k] = d1_common.url.encodePathElement(args[k])
    path = path_format % args
    url = '/' + d1_common.url.joinPathElements(self.selector, self.version, path)
    return url

  # ----------------------------------------------------------------------------
  # Data Package Manager web service API wrappers
  # ----------------------------------------------------------------------------

  # List Data Entities

  @d1_common.util.utf8_to_unicode
  def list_data_entities(self, package_id):
    '''List the entity IDs of the data members of a package'''
    response = self.list_data_entities_response(package_id)
    identifiers = self._read_text_response(response)
    return sorted(identifiers.strip().split('\n'))


  @d1_common.util.utf8_to_unicode
  def list_data_entities_response(self, package_id):
    url = self._rest_url('data/eml/%(scope)s/%(identifier)s/%(revision)s',
                         scope=package_id.scope(),
                         identifier=str(package_id.identifier()),
                         revision=str(package_id.revision()))
    return self.GET(url)

  # List Data Package Identifiers

  @d1_common.util.utf8_to_unicode
  def list_data_package_identifiers(self, scope):
    response = self.list_data_package_identifiers_response(scope)
    identifiers = self._read_text_response(response)
    return sorted(map(int, identifiers.strip().split('\n')))


  @d1_common.util.utf8_to_unicode
  def list_data_package_identifiers_response(self, scope):
    url = self._rest_url('/eml/%(scope)s', scope=scope)
    return self.GET(url)

  # List Data Package Revisions

  @d1_common.util.utf8_to_unicode
  def list_data_package_revisions(self, scope, identifier):
    response = self.list_data_package_revisions_response(scope, identifier)
    identifiers = self._read_text_response(response)
    return sorted(map(int, identifiers.strip().split('\n')))


  @d1_common.util.utf8_to_unicode
  def list_data_package_revisions_response(self, scope, identifier):
    url = self._rest_url('/eml/%(scope)s/%(identifier)s',
                         scope=scope, identifier=str(identifier))
    return self.GET(url)

  # List Data Package Scopes

  @d1_common.util.utf8_to_unicode
  def list_data_package_scopes(self):
    response = self.list_data_package_scopes_response()
    identifiers = self._read_text_response(response)
    return sorted(identifiers.strip().split('\n'))


  @d1_common.util.utf8_to_unicode
  def list_data_package_scopes_response(self):
    url = self._rest_url('/eml')
    return self.GET(url)

  # List Deleted Data Packages

  @d1_common.util.utf8_to_unicode
  def list_deleted_packages(self):
    response = self.list_deleted_packages_response()
    identifiers = self._read_text_response(response)
    return sorted(identifiers.strip().split('\n'))


  @d1_common.util.utf8_to_unicode
  def list_deleted_packages_response(self):
    url = self._rest_url('/eml/deleted')
    return self.GET(url)

  # Read Data Entity Name

  @d1_common.util.utf8_to_unicode
  def read_data_entity_name(self, package_id, entity_id):
    response = self.read_data_entity_name_response(package_id, entity_id)
    return self._read_raw_response(response)


  @d1_common.util.utf8_to_unicode
  def read_data_entity_name_response(self, package_id, entity_id):
    url = self._rest_url('data/eml/%(scope)s/%(identifier)s/%(revision)s/%(entity_id)s',
                         scope=package_id.scope(),
                         identifier=str(package_id.identifier()),
                         revision=str(package_id.revision()),
                         entity_id=entity_id)
    return self.GET(url)

#   # List Data Package Identifiers
#
#   @d1_common.util.utf8_to_unicode
#   def list_data_package_identifiers(self, package_id):
#     response = self.list_data_package_identifiers_response(package_id)
#     identifiers = self._read_text_response(response)
#     return identifiers.strip().split('\n')
#
#
#   @d1_common.util.utf8_to_unicode
#   def list_data_package_identifiers_response(self, package_id):
#     url = self._rest_url('eml/%(scope)s/%(identifier)s/%(revision)s',
#                          scope=package_id.scope(),
#                          identifier=str(package_id.identifier()),
#                          revision=str(package_id.revision()))
#     return self.GET(url)

  # Read Data Package DOI

  @d1_common.util.utf8_to_unicode
  def read_data_package_doi(self, package_id):
    response = self.read_data_package_doi_response(package_id)
    return self._read_text_response(response).strip()


  @d1_common.util.utf8_to_unicode
  def read_data_package_doi_response(self, package_id):
    url = self._rest_url('doi/eml/%(scope)s/%(identifier)s/%(revision)s',
                         scope=package_id.scope(),
                         identifier=str(package_id.identifier()),
                         revision=str(package_id.revision()))
    return self.GET(url)

  # Is Authorized

  @d1_common.util.utf8_to_unicode
  def is_authorized(self, package_id, entity_id):
    '''Determine if read access to data entity is authorized'''
    response = self.is_authorized_response(package_id, entity_id)
    return self._read_text_response(response)


  @d1_common.util.utf8_to_unicode
  def is_authorized_response(self, package_id, entity_id):
    url_encoded_resource_id = self.entity_uri(package_id, entity_id)
    url = self._rest_url('authz?resourceId=') + url_encoded_resource_id
    return self.GET(url)

  # Read Data Package ACL

  @d1_common.util.utf8_to_unicode
  def read_data_package_acl(self, package_id):
    response = self.read_data_package_acl_response(package_id)
    return self._read_eml_access_response(response)


  @d1_common.util.utf8_to_unicode
  def read_data_package_acl_response(self, package_id):
    url = self._rest_url('acl/eml/%(scope)s/%(identifier)s/%(revision)s',
                         scope=package_id.scope(),
                         identifier=str(package_id.identifier()),
                         revision=str(package_id.revision()))
    return self.GET(url)

  # Read Data Entity ACL

  @d1_common.util.utf8_to_unicode
  def read_data_entity_acl(self, package_id, entity_id):
    response = self.read_data_entity_acl_response(package_id, entity_id)
    return self._read_eml_access_response(response)


  @d1_common.util.utf8_to_unicode
  def read_data_entity_acl_response(self, package_id, entity_id):
    url = self._rest_url('data/acl/eml/%(scope)s/%(identifier)s/%(revision)s/%(entity_id)s',
                         scope=package_id.scope(),
                         identifier=str(package_id.identifier()),
                         revision=str(package_id.revision()),
                         entity_id=entity_id)
    return self.GET(url)

  # Read Data Package Report ACL

  @d1_common.util.utf8_to_unicode
  def read_quality_report_acl(self, package_id):
    response = self.read_quality_report_acl_response(package_id)
    return self._read_eml_access_response(response)


  @d1_common.util.utf8_to_unicode
  def read_quality_report_acl_response(self, package_id):
    url = self._rest_url('report/acl/eml/%(scope)s/%(identifier)s/%(revision)s',
                         scope=package_id.scope(),
                         identifier=str(package_id.identifier()),
                         revision=str(package_id.revision()))
    return self.GET(url)

  # Read Metadata ACL

  @d1_common.util.utf8_to_unicode
  def read_metadata_acl(self, package_id):
    response = self.read_metadata_acl_response(package_id)
    return self._read_eml_access_response(response)


  @d1_common.util.utf8_to_unicode
  def read_metadata_acl_response(self, package_id):
    url = self._rest_url('metadata/acl/eml/%(scope)s/%(identifier)s/%(revision)s',
                         scope=package_id.scope(),
                         identifier=str(package_id.identifier()),
                         revision=str(package_id.revision()))
    return self.GET(url)

  # Read Data Entity Checksum (SHA-1)

  @d1_common.util.utf8_to_unicode
  def read_data_entity_checksum(self, package_id, entity_id):
    response = self.read_data_entity_checksum_response(package_id, entity_id)
    return self._read_text_response(response).strip()


  @d1_common.util.utf8_to_unicode
  def read_data_entity_checksum_response(self, package_id, entity_id):
    url = self._rest_url('data/checksum/eml/%(scope)s/%(identifier)s/%(revision)s/%(entity_id)s',
                         scope=package_id.scope(),
                         identifier=str(package_id.identifier()),
                         revision=str(package_id.revision()),
                         entity_id=str(entity_id))
    return self.GET(url)


  # Read Data Package Report Checksum (SHA-1)

  @d1_common.util.utf8_to_unicode
  def read_data_package_report_checksum(self, package_id):
    response = self.read_data_package_report_checksum_response(package_id)
    return self._read_text_response(response).strip()


  @d1_common.util.utf8_to_unicode
  def read_data_package_report_checksum_response(self, package_id):
    url = self._rest_url('report/checksum/eml/%(scope)s/%(identifier)s/%(revision)s',
                         scope=package_id.scope(),
                         identifier=str(package_id.identifier()),
                         revision=str(package_id.revision()))
    return self.GET(url)

  # Read Metadata Checksum (SHA-1)

  @d1_common.util.utf8_to_unicode
  def read_metadata_checksum(self, package_id):
    response = self.read_metadata_checksum_response(package_id)
    return self._read_text_response(response).strip()


  @d1_common.util.utf8_to_unicode
  def read_metadata_checksum_response(self, package_id):
    url = self._rest_url('metadata/checksum/eml/%(scope)s/%(identifier)s/%(revision)s',
                         scope=package_id.scope(),
                         identifier=str(package_id.identifier()),
                         revision=str(package_id.revision()))
    return self.GET(url)


  # Read Metadata Format ID

  @d1_common.util.utf8_to_unicode
  def read_metadata_format_id(self, package_id):
    '''Returns the Format ID, e.g., "eml://ecoinformatics.org/eml-2.1.0"'''
    response = self.read_metadata_format_id_response(package_id)
    return self._read_text_response(response).strip()


  @d1_common.util.utf8_to_unicode
  def read_metadata_format_id_response(self, package_id):
    url = self._rest_url('metadata/format/eml/%(scope)s/%(identifier)s/%(revision)s',
                         scope=package_id.scope(),
                         identifier=str(package_id.identifier()),
                         revision=str(package_id.revision()))
    return self.GET(url)

  # misc

  @d1_common.util.utf8_to_unicode
  def get_data_entry_header(self, resource_url):
    response = self.get_data_entry_header_response(resource_url)
    logging.info('Resource URL: ' + resource_url + '\n')
    if self._status_is_307_temporary_redirect(response):
      headers = dict(response.getheaders())
      temporary_url = response.getheader('location')
      response = self._get_data_redirect_header(temporary_url)
    return self._read_header_response(response)


  @d1_common.util.utf8_to_unicode
  def get_data_entry_header_response(self, resource_url):
    return self.HEAD(resource_url)


  @d1_common.util.utf8_to_unicode
  def entity_uri(self, package_id, entity_id):
    # TODO: Check that resource IDs will always be the base id + package id + entity id.
    return '{0}/data/eml/{1}/{2}/{3}/{4}'.format(self.base_url,
      d1_common.url.encodePathElement(package_id.scope()), package_id.identifier(),
      package_id.revision(), d1_common.url.encodePathElement(entity_id))


  @d1_common.util.utf8_to_unicode
  def report_uri(self, package_id):
    return '{0}/report/eml/{1}/{2}/{3}'.format(self.base_url,
      d1_common.url.encodePathElement(package_id.scope()), package_id.identifier(),
      package_id.revision())


  @d1_common.util.utf8_to_unicode
  def metadata_uri(self, package_id):
    return '{0}/metadata/eml/{1}/{2}/{3}'.format(self.base_url,
      d1_common.url.encodePathElement(package_id.scope()), package_id.identifier(),
      package_id.revision())


  # Metadata DOIs are not yet implemented in PASTA.

  #@d1_common.util.utf8_to_unicode
  #def get_metadata_doi_response(self, scope, identifier, revision):
  #  url = self._rest_url('metadata/doi/eml/%(scope)s/%(identifier)s/%(revision)s',
  #                       scope=scope, identifier=str(identifier),
  #                       revision=str(revision))
  #  print url
  #  return self.GET(url)
  #
  #
  #@d1_common.util.utf8_to_unicode
  #def get_metadata_doi(self, scope, identifier, revision):
  #  response = self.get_metadata_doi_response(scope, identifier, revision)
  #  return self._read_text_response(response).strip()
  #
  #
  #@d1_common.util.utf8_to_unicode
  #def get_data_package_doi_response(self, scope, identifier, revision, entity_id):
  #  url = self._rest_url('data/doi/%(scope)s/%(identifier)s/%(revision)s/%(entity_id)s',
  #                       scope=scope, identifier=str(identifier),
  #                       revision=str(revision), entity_id=entity_id)
  #  return self.GET(url)
  #
  #
  #@d1_common.util.utf8_to_unicode
  #def get_data_package_doi(self, scope, identifier, revision, entity_id):
  #  response = self.get_data_package_doi_response(scope, identifier, revision, entity_id)
  #  return self._read_text_response(response).strip()
