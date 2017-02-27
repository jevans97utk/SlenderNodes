#!/usr/bin/env python

# -*- coding: utf-8 -*-

# This work was created by participants in the DataONE project, and is
# jointly copyrighted by participating institutions in DataONE. For
# more information on DataONE, see our web site at http://dataone.org.
#
#   Copyright 2009-2016 DataONE
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

"""R2R to GMN slendernode connector.
"""

# Stdlib
import datetime
import fcntl
import logging
import os
import pprint
import sys
import tempfile
import xml.dom.minidom
import xml.etree.ElementTree as ET

# 3rd party
import requests

# D1
import d1_client.mnclient_2_0
import d1_common.date_time
import d1_common.util
import d1_common.checksum
import d1_common.types.dataoneTypes_v2_0 as v2
import d1_common.types.exceptions

# App

# Constants
MAX_RECORDS_INT = 10 # R2R seems to clamp this to 10.
SUBMITTER_SUBJECT_STR = 'CN=Roger Dahl A1779,O=Google,C=US,DC=cilogon,DC=org'
OWNER_SUBJECT_STR = 'CN=Roger Dahl A1779,O=Google,C=US,DC=cilogon,DC=org'
AUTHORITATIVE_MEMBER_NODE_URN = 'urn:node:mnTestR2R'
ORIGIN_MEMBER_NODE_URN = 'urn:node:mnTestR2R'
SCIOBJ_FORMAT_STR = 'http://www.isotc211.org/2005/gmd-noaa'
CERT_PUB_PATH = './client_cert.pem'
CERT_KEY_PATH = './client_key_nopassword.pem'
GMN_BASE_URL = 'https://r2r-node.test.dataone.org/mn'
DEBUG_LOG_BOOL = True

NS_DICT = {
  'csw': 'http://www.opengis.net/cat/csw/2.0.2',
  'csw30': 'http://www.opengis.net/cat/csw/3.0',
  'dc': 'http://purl.org/dc/elements/1.1/',
  'dct': 'http://purl.org/dc/terms/',
  'gco': 'http://www.isotc211.org/2005/gco',
  'gmd': 'http://www.isotc211.org/2005/gmd',
  'gmi': 'http://www.isotc211.org/2005/gmi',
  # 'gml': 'http://www.opengis.net/gml',
  # gml is declared twice, with diffent URIs in the original XML doc
  'gml': 'http://www.opengis.net/gml/3.2',
  'mx': 'http://www.isotc211.org/2005/gmx',
  'ows': 'http://www.opengis.net/ows',
  'xlink': 'http://www.w3.org/1999/xlink',
  'xs': 'http://www.w3.org/2001/XMLSchema',
  'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
}

# Module scope vars
single_instance_lock_file = None


def main():
  log_setup(DEBUG_LOG_BOOL)
  logging.info(u'Running: {}'.format(get_command_name()))
  abort_if_other_instance_is_running()
  try:
    r2r_processor = R2RConnector()
    r2r_processor.run()
  except Exception:
    logging.exception('R2RConnector failed with exception:')


def log_setup(debug_bool):
  """Set up logging. We output only to stdout. Instead of also writing to a log
  file, redirect stdout to a log file when the script is executed from cron.
  """
  logging.basicConfig(level=logging.DEBUG)
  formatter = logging.Formatter(
    u'%(asctime)s %(levelname)-8s %(name)s %(module)s %(message)s',
    u'%Y-%m-%d %H:%M:%S',
  )
  console_logger = logging.StreamHandler(sys.stdout)
  console_logger.setFormatter(formatter)
  logging.getLogger('').addHandler(console_logger)
  if debug_bool:
    logging.getLogger('').setLevel(logging.DEBUG)
  else:
    logging.getLogger('').setLevel(logging.INFO)


def abort_if_other_instance_is_running():
  global single_instance_lock_file
  command_name_str = get_command_name()
  single_path = os.path.join(
    tempfile.gettempdir(), command_name_str + '.single'
  )
  single_instance_lock_file = open(single_path, 'w')
  try:
    fcntl.lockf(single_instance_lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
  except IOError:
    logging.info(u'Aborted: Another instance is still running')
    sys.exit(0)


def get_command_src_path():
  try:
    return os.path.abspath(sys.modules['__main__'].__file__)
  except KeyError:
    return sys.executable


def get_command_name():
  return os.path.splitext(os.path.basename(get_command_src_path()))[0]


def make_absolute(p):
  return os.path.join(
    os.path.abspath(os.path.dirname(get_command_src_path())), p
  )

#===============================================================================


class R2RConnector(object):
  def __init__(self):
    self._event_dict = {}
    self._disable_insecure_platform_warnings()
    self._register_namespaces()
    self._gmn_client = self._create_gmn_client()

  def run(self):
    self._process_all()
    self._log_status()

  def _log_status(self):
    if not self._event_dict:
      logging.debug('Nothing to do')
      return
    logging.info('Events:')
    for event_str in sorted(self._event_dict):
      value = self._event_dict[event_str]
      logging.info('{}: {}'.format(event_str, value))

  def _count_event(self, event_str):
    try:
      self._event_dict[event_str] += 1
    except LookupError:
      self._event_dict[event_str] = 1

  def _disable_insecure_platform_warnings(self):
    # from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings() # InsecureRequestWarning

  def _register_namespaces(self):
    """Register namespaces in global registry. Unfortunately, the global
    registry is only taken into account when serializing to XML. The NS_DICT
    still has to be passed to ET functions, such as findall().
    """
    for prefix_str, uri_str in NS_DICT.items():
      ET.register_namespace(prefix_str, uri_str)

  def _process_all(self):
    record_idx = 1
    while record_idx:
      xml_str = self._get_page(record_idx) # .encode('utf-8')
      root_et = ET.fromstring(xml_str)
      self._process_page(root_et)
      # nextRecord is 0 when there are no more pages.
      record_idx = int(
        root_et.find('./csw30:SearchResults', NS_DICT).attrib['nextRecord']
      )

  def _get_page(self, record_idx):
    response = requests.get(
      'http://api.rvdata.us/catalog', params={
        'service': 'CSW',
        'version': '3.0.0',
        'request': 'GetRecords',
        'typenames': 'gmd:MD_Metadata',
        'outputSchema': 'http://www.isotc211.org/2005/gmd',
        'elementSetName': 'full',
        'maxRecords': MAX_RECORDS_INT,
        'startPosition': record_idx,
      }, headers={
        'accept': 'application/xml',
      }
    )
    return response.content

  def _process_page(self, root_et):
    for metadata_et in root_et.findall(
      './csw30:SearchResults/gmi:MI_Metadata', NS_DICT
    ):
      # logging.debug(self._serialize_pretty(metadata_et))
      try:
        self._process_metadata(metadata_et)
      except Exception:
        # We just record the event and move on to the next metadata doc. The
        # operation that failed will be retried the next time the process is
        # launched by cron
        logging.exception('R2R metadata processing failed with exception:')
        self._count_event('R2R metadata processing failure')

  def _process_metadata(self, metadata_et):
    xml_str = self._serialize_pretty(metadata_et)
    sha1_checksum_pyxb = d1_common.checksum.create_checksum_object(xml_str)
    sysmeta_pyxb = self._generate_sysmeta_pyxb(
      metadata_et, xml_str, sha1_checksum_pyxb, None
    )
    pid = sysmeta_pyxb.identifier.value()
    if self._pid_exists(pid):
      # This version of this metadata doc already exists on GMN so there's
      # nothing to do.
      return
    self._process_new_object(pid, sysmeta_pyxb, xml_str)

  def _process_new_object(self, pid, sysmeta_pyxb, xml_str):
    sid = sysmeta_pyxb.seriesId.value()
    obsoleted_pid = self._resolve_sid(sid)
    if obsoleted_pid:
      self._update_sciobj(pid, obsoleted_pid, sysmeta_pyxb, xml_str)
    else:
      self._create_sciobj(pid, sysmeta_pyxb, xml_str)

  def _update_sciobj(self, pid, obsoleted_pid, sysmeta_pyxb, xml_str):
    self._gmn_client.update(obsoleted_pid, xml_str, pid, sysmeta_pyxb)
    self._count_event('Object update')
    logging.info(
      'Updated object. obsoleted_pid="{}", new_pid="{}"'.
        format(obsoleted_pid, pid)
    )

  def _create_sciobj(self, pid, sysmeta_pyxb, xml_str):
    self._gmn_client.create(pid, xml_str, sysmeta_pyxb)
    self._count_event('Object create')
    logging.info(
      'Created object. pid="{}"'.format(pid)
    )

  def _pid_exists(self, pid):
    """Check if {pid} exists on GMN"""
    try:
      self._gmn_client.getSystemMetadata(pid)
    except d1_common.types.exceptions.NotFound:
      return False
    else:
      return True

  def _resolve_sid(self, sid):
    """Resolve {sid} on GMN. Return the PID or None"""
    try:
      sysmeta_pyxb = self._gmn_client.getSystemMetadata(sid)
    except d1_common.types.exceptions.NotFound:
      return None
    else:
      return sysmeta_pyxb.identifier.value()

  def _create_gmn_client(self):
    return d1_client.mnclient_2_0.MemberNodeClient_2_0(
      GMN_BASE_URL,
      cert_path=CERT_PUB_PATH,
      key_path=CERT_KEY_PATH,
    )

  def _serialize_pretty(self, xml_et):
    """Serialize and normalize the XML subtree"""
    return d1_common.util.pretty_xml(ET.tostring(xml_et)).encode('utf-8')

  def _generate_sysmeta_pyxb(self, metadata_et, xml_str, checksum_pyxb, obsoletes_pid):
    now = datetime.datetime.now()
    sysmeta_pyxb = v2.systemMetadata()
    sysmeta_pyxb.serialVersion = 1
    sysmeta_pyxb.identifier = checksum_pyxb.value()
    sysmeta_pyxb.seriesId = metadata_et.find(
      './gmd:fileIdentifier/gco:CharacterString', NS_DICT
    ).text
    sysmeta_pyxb.formatId = SCIOBJ_FORMAT_STR
    sysmeta_pyxb.size = len(xml_str)
    sysmeta_pyxb.submitter = SUBMITTER_SUBJECT_STR
    sysmeta_pyxb.rightsHolder = OWNER_SUBJECT_STR
    sysmeta_pyxb.checksum = checksum_pyxb
    sysmeta_pyxb.dateUploaded = d1_common.date_time.from_iso8601(
      metadata_et.find('./gmd:dateStamp/gco:DateTime', NS_DICT).text
    )
    sysmeta_pyxb.dateSysMetadataModified = now
    sysmeta_pyxb.originMemberNode = ORIGIN_MEMBER_NODE_URN
    sysmeta_pyxb.authoritativeMemberNode = AUTHORITATIVE_MEMBER_NODE_URN
    sysmeta_pyxb.obsoletes = obsoletes_pid
    sysmeta_pyxb.accessPolicy = self._generate_public_access_policy_pyxb()
    return sysmeta_pyxb

  def _generate_public_access_policy_pyxb(self):
    access_policy_pyxb = v2.AccessPolicy()
    access_rule_pyxb = v2.AccessRule()
    access_rule_pyxb.permission = [v2.Permission.read, ]
    access_rule_pyxb.subject = ["public", ]
    access_policy_pyxb.allow = [access_rule_pyxb, ]
    return access_policy_pyxb


if __name__ == '__main__':
  main()
