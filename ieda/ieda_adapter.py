#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This work was created by participants in the DataONE project, and is
# jointly copyrighted by participating institutions in DataONE. For
# more information on DataONE, see our web site at http://dataone.org.
#
#   Copyright 2009-2017 DataONE
#
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
"""IEDA Slender Node Adapter

Sitemap index: http://get.iedadata.org/sitemaps/

Sitemap index has links to separate sitemap docs for each IEDA partner. The
links on the sitemap pages get dataset landing pages that have the SDO JSON-LD
scripts in the html header.

Note that there's no ability to support archival in this approach (unless one
attempts to track when a record identifier used to appear but no longer does).

IEDA receives content from 3 contributing repositories. For now, MN will only
hold objects from EarthChem.
"""
import datetime
import io
import logging
import pprint
import requests
import sys
import xml.etree.ElementTree as ET

import d1_client.mnclient_2_0
import d1_common.checksum
import d1_common.const
import d1_common.date_time
import d1_common.system_metadata
import d1_common.types.dataoneTypes_v2_0 as v2
import d1_common.types.exceptions
import d1_common.wrap.access_policy
import d1_common.xml

import d1_client
import schema_org


IEDA_SITE_MAP = "http://get.iedadata.org/sitemaps/usap_sitemap.xml"
SCIMETA_FORMAT_ID = 'http://www.isotc211.org/2005/gmd'
SCIMETA_RIGHTS_HOLDER = 'CN=urn:node:mnTestIEDA,DC=dataone,DC=org'
SCIMETA_SUBMITTER = 'CN=urn:node:mnTestIEDA,DC=dataone,DC=org'
SCIMETA_AUTHORITATIVE_MEMBER_NODE = 'urn:node:mnTestIEDA'

# BASE_URL = 'https://gmn.dataone.org/ieda'
BASE_URL = 'https://gmn.test.dataone.org/mn'

# CERT_PEM_PATH = './client_cert.pem'
# CERT_KEY_PATH = './client_key_nopassword.pem'

CERT_PEM_PATH = './urn_node_mnTestIEDA.pem'
CERT_KEY_PATH = './urn_node_mnTestIEDA.key'

NS_DICT = {
  'gmd': 'http://www.isotc211.org/2005/gmd',
  'gco': 'http://www.isotc211.org/2005/gco',
}


def main():
  logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
  )

  resource_list = schema_org.load_resources_from_sitemap(IEDA_SITE_MAP)

  logging.info('Found resources: {}'.format(len(resource_list)))

  gmn_client = create_gmn_client()

  for resource_dict in resource_list:
    logging.info('-' * 80)
    entry_dict = schema_org.load_schema_org(resource_dict)

    result_dict = {
      **resource_dict,
      **entry_dict,
    }

    logging.info(pprint.pformat(result_dict))

    if 'error' in result_dict:
      logging.error(
        'error="{}" url="{}"'.format(result_dict['error'], result_dict['url'])
      )
      continue

    # {
    #   'date_modified': '2018-01-25T15:55:08-05:00',
    #   'id': 'doi:10.7265/N5F47M23',
    #   'metadata_format': None,
    #   'metadata_url': 'http://get.iedadata.org/metadata/iso/usap/609539iso.xml',
    #   'url': 'http://get.iedadata.org/metadata/iso/609539'
    # }

    sid = result_dict['id']
    pid = result_dict['url']

    logging.info('schema.org. sid="{}" pid="{}"'.format(sid, pid))

    if is_in_gmn(gmn_client, pid):
      logging.info('Skipped. Already in GMN.')
      continue

    scimeta_xml_bytes = download_scimeta_xml(result_dict['metadata_url'])

    pid_sysmeta_pyxb = generate_system_metadata(scimeta_xml_bytes, pid, sid)

    head_sysmeta_pyxb = get_sysmeta(gmn_client, sid)

    # logging.info(sysmeta_pyxb.toxml('utf-8'))

    if head_sysmeta_pyxb:
      head_pid = head_sysmeta_pyxb.identifier.value()
      logging.info(
        'SID already exists on GMN. Adding to chain. head_pid="{}"'
        .format(head_pid)
      )
      gmn_client.update(
        head_pid, io.BytesIO(scimeta_xml_bytes), pid, pid_sysmeta_pyxb
      )
    else:
      logging.info(
        'SID does not exist on GMN. Starting new chain. pid="{}"'.format(pid)
      )
      gmn_client.create(pid, io.BytesIO(scimeta_xml_bytes), pid_sysmeta_pyxb)


def download_scimeta_xml(scimeta_url):
  try:
    return requests.get(scimeta_url).content
  except requests.HTTPError as e:
    raise AdapterException(
      'Unable to download SciMeta. error="{}"'.format(str(e))
    )


def parse_doi(iso_xml):
  """Get the DOI from an ISO XML doc"""
  tree = ET.parse('iso.xml')
  root = tree.getroot()
  doi_el = root.findall(
    '.gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/'
    'gmd:CI_Citation/gmd:identifier/gmd:MD_Identifier/gmd:code/'
    'gco:CharacterString', NS_DICT
  )[0]
  return doi_el.text.strip()


def create_gmn_client():
  return d1_client.mnclient_2_0.MemberNodeClient_2_0(
    base_url=BASE_URL,
    cert_pem_path=CERT_PEM_PATH,
    cert_key_path=CERT_KEY_PATH,
    retries=1,
  )


def is_in_gmn(gmn_client, did):
  try:
    gmn_client.getSystemMetadata(did)
  except d1_common.types.exceptions.NotFound:
    return False
  return True


def get_sysmeta(gmn_client, sid):
  try:
    return gmn_client.getSystemMetadata(sid)
  except d1_common.types.exceptions.NotFound:
    return None


def generate_system_metadata(scimeta_bytes, pid, sid):
  """
  :param scimeta_bytes: Bytes of the node's original metadata document.
  :param native_identifier_sid: Node's system identifier for this object, which
  becomes the series ID.
  :param record_date: Date metadata document was created/modified in the source
  system. Becomes dateUploaded.
  :param sysmeta_settings_dict: A dict containing node-specific system metadata
  properties that will apply to all science metadata documents loaded into GMN.

  This function generates a system metadata document for describing the science
  metadata record being loaded. Some of the fields, such as checksum and size,
  are based off the bytes of the science metadata object itself. Other system
  metadata fields are passed to D1ClientManager in a dict which is configured in
  the main adapter program. Note that the checksum is assigned as an arbitrary
  version identifier to accommodate the source system's mutable content
  represented in the target system's immutable content standard.
  """
  sysmeta_pyxb = v2.systemMetadata()
  sysmeta_pyxb.seriesId = sid
  sysmeta_pyxb.formatId = SCIMETA_FORMAT_ID
  sysmeta_pyxb.size = len(scimeta_bytes)
  sysmeta_pyxb.checksum = d1_common.checksum.create_checksum_object_from_string(
    scimeta_bytes
  )
  sysmeta_pyxb.identifier = pid
  sysmeta_pyxb.dateUploaded = d1_common.date_time.utc_now()
  sysmeta_pyxb.dateSysMetadataModified = datetime.datetime.now()
  sysmeta_pyxb.rightsHolder = SCIMETA_RIGHTS_HOLDER
  sysmeta_pyxb.submitter = SCIMETA_SUBMITTER
  sysmeta_pyxb.authoritativeMemberNode = SCIMETA_AUTHORITATIVE_MEMBER_NODE
  sysmeta_pyxb.originMemberNode = SCIMETA_AUTHORITATIVE_MEMBER_NODE
  sysmeta_pyxb.accessPolicy = v2.AccessPolicy()

  with d1_common.wrap.access_policy.wrap_sysmeta_pyxb(sysmeta_pyxb) as ap:
    ap.clear()
    ap.add_public_read()

  return sysmeta_pyxb


class AdapterException(Exception):
  pass


if __name__ == '__main__':
  sys.exit(main())
