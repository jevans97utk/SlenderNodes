# requires PyYAML
# no oai-pmh support for deleted records, so no record archival functionality

import yaml
import requests
import xml.etree.ElementTree as ET
import re
import datetime
import pytz
import logging
import datetime
import StringIO
import hashlib
import sys

# D1.
import d1_common.types.dataoneTypes_v2_0 as v2
import d1_common.const
import d1_client.mnclient_2_0
import d1_common.checksum
import d1_common.types.dataoneTypes_v2_0 as dataoneTypes

logging.basicConfig(filename='adapter-errors.log',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.ERROR)
logger = logging.getLogger(__name__)

start = 1 # tracks if first oai-pmh for a node or not
rtoken = None # for storing resumption token
record_count = 0
create_count = 0
update_count = 0

def main():
  global start
  global rtoken
  global record_count
  global create_count
  global update_count
  regex = re.compile(r'[.][v]\d*')

  with open('mnconfig.yaml') as f:
    mnconfig = yaml.load(f)

  for node in mnconfig:
    start = 1  # reset at first request for every node to be harvested. Used by define_params() to form correct request
    rtoken = None  # also reset to none at first request for each node. Stores resumption tokens as applicable
    record_count = 0
    create_count = 0
    update_count = 0
    last_harvest_time = '1900-01-01T00:00:00Z'
    print('\n\n')
    print(node['nodeID'])
    harvester = OAIPMH_Harvester(
      node['oaipmh_base_url'], node['oaipmh_set'], node['oaipmh_md_prefix'],
      node['sci_md_xml_element'], last_harvest_time)
    mnclient = D1ClientManager(
      node['node_base_url'], node['cert_path'], node['cert_key_path'],
      node['sci_md_formatId'], node['submitter'], node['rightsholder'],
      node['authoritativeMN'], node['originMN']
    )
    while (start == 1) or (start == 0 and rtoken is not None):
      record_list = harvester.get_records(harvester.define_params())
      if record_list is not None:
        rtoken_record = record_list.find('{http://www.openarchives.org/OAI/2.0/}resumptionToken')
        if rtoken_record is None:
          rtoken = None
        else:
          rtoken = rtoken_record.text
          record_list.remove(rtoken_record)  # excludes rtoken from the processing that happens to rest of results
        for metadata_record in record_list:
          record_count += 1
          print('\nRecord #: ' + str(record_count))
          print('-'*30)
          try: # attempt to parse out information from the oai-pmh result
            identifier, record_date, sci_metadata = harvester.process_record(record=metadata_record)
            print('ID: {}'.format(identifier))
            version = re.search(regex, identifier) #identify where in identifier version suffix starts
            if version: # if version suffix found in identifier
              d1_seriesID = identifier[0:version.regs[0][0]] # substring between 1st pos of identifier & version suffix
              d1_current_pid = mnclient.check_exists(d1_seriesID) # check if that seriesID already in GMN
              if d1_current_pid is None: # returns None if seriesID not already in D1, making this a new create()
                if(mnclient.create_new_sci_metadata(
                  sci_metadata_bytes=sci_metadata, pid=identifier, seriesID=d1_seriesID, record_date=record_date)):
                  create_count += 1
              else:
                if(mnclient.update_science_metadata(
                  sci_metadata_bytes=sci_metadata, new_pid=identifier, seriesID=d1_seriesID,
                  record_date=record_date, old_pid=d1_current_pid)):
                  update_count += 1 # if successful update, increment the counter that tracks updates
            else:
              logger.error('No version information found for ID {}. Skipping.'.format(identifier))
          except Exception as e:
            logger.error(e)

      else: # if record_list is None, no records returned for some reason
        pass



# ######################################################################################################
class OAIPMH_Harvester:
  def __init__(self, oaipmh_base_url, oaipmh_set, oaipmh_md_prefix,
               sci_md_xml_element, last_harvest_time, ):
    self.oaipmh_base_url = oaipmh_base_url
    self.oaipmh_set = oaipmh_set
    self.oaipmh_md_prefix = oaipmh_md_prefix
    self.sci_md_xml_element = sci_md_xml_element
    self.last_harvest_time = last_harvest_time


# ----------------------------------------------------------------------------------------------------------------------
  def define_params(self):
    global start
    global rtoken
    if start == 1:
      # It is an option to uncomment this version and comment out harvest based timeslice params
      #params = {'verb': 'ListRecords',
      #          'metadataPrefix': 'iso19139',
      #          'from': '2000-01-01T00:00:00Z',
      #          'until': '2018-01-31T23:59:59Z'}
      params = {'verb': 'ListRecords',
      'metadataPrefix': self.oaipmh_md_prefix,
      'set': self.oaipmh_set,
      'from': self.last_harvest_time}
      start = 0

    else:
      params = {'verb': 'ListRecords',
                'resumptionToken': rtoken}
      rtoken = None
    return params

# ----------------------------------------------------------------------------------------------------------------------
  def get_records(self, parameters):
    headers = {
      'User-Agent': 'DataONE Adapter for OAI-PMH Harvest',
      'From': 'mihli1@utk.edu'}
    try:
      r = requests.get(url=self.oaipmh_base_url, params=parameters, headers=headers)
      if r.status_code == requests.codes.ok:
        root = ET.fromstring(r.content)
        record_list = root.find('{http://www.openarchives.org/OAI/2.0/}ListRecords')
        return record_list # If element not found, returns none (such as if <error code="noRecordsMatch"/>)
      else:
        logging.error('Request failed: {}'.format(r.url))
    except Exception, e:
      logging.error('Request failed: {}'.format(e))


# ----------------------------------------------------------------------------------------------------------------------
  def process_record(self, record):
    identifier = record.find('{http://www.openarchives.org/OAI/2.0/}metadata'). \
      find('{http://www.openarchives.org/OAI/2.0/oai_dc/}dc'). \
      find('{http://purl.org/dc/elements/1.1/}identifier').text
    record_date = record.find('{http://www.openarchives.org/OAI/2.0/}header'). \
      find('{http://www.openarchives.org/OAI/2.0/}datestamp').text
    # convert datetime as string to timezone aware datetime:
    record_date = pytz.utc.localize(datetime.datetime.strptime(record_date, '%Y-%m-%dT%H:%M:%SZ'))
    scimeta = ET.tostring(record.find('{http://www.openarchives.org/OAI/2.0/}metadata'). \
                          find(self.sci_md_xml_element))
    return (identifier, record_date, scimeta)

######################################################################################################

class D1ClientManager:
  def __init__(self, node_base_url, cert_path, cert_key_path, sci_md_formatId,
               submitter, rightsholder, authoritativeMN, originMN):
    self.client = d1_client.mnclient_2_0.MemberNodeClient_2_0(
      node_base_url,
      cert_pem_path=cert_path,
      cert_key_path=cert_key_path,
      timeout=120.0,
      # uncomment verify_tls=False if using a self-signed SSL certificate or comment if not.
      # verify_tls=False
    )
    self.sci_md_formatId = sci_md_formatId
    self.submitter = submitter
    self.rightsholder = rightsholder
    self.authoritativeMN = authoritativeMN
    self.originMN = originMN

  def check_exists(self, seriesID):
    try:
      sys_meta = self.client.getSystemMetadata(seriesID)  # returns head of chain if found
    except d1_common.types.exceptions.NotFound:
      return None
    else:
      return sys_meta.identifier.value() # return current version pid

  def create_new_sci_metadata(self, sci_metadata_bytes, pid, seriesID, record_date):
    try:
      system_metadata = self._generate_system_metadata(sci_metadata_bytes, pid, seriesID, record_date)
      self.client.create(system_metadata.identifier.value(), StringIO.StringIO(sci_metadata_bytes), system_metadata)
      return True
    except d1_common.types.exceptions.IdentifierNotUnique as e:
      logger.error(e)
    except Exception, e:
      logging.error('Failed to create object with PID {} / SID {}.'.format(pid,seriesID) )
      logging.error(e)
      return False

  def update_science_metadata(self, sci_metadata_bytes, new_pid, seriesID, record_date, old_pid):
    try:
      new_version_system_metadata = self._generate_system_metadata(sci_metadata_bytes, new_pid, seriesID, record_date)
      self.client.update(old_pid,
                         StringIO.StringIO(sci_metadata_bytes),
                         new_version_system_metadata.identifier.value(),
                         new_version_system_metadata)
      return True
    except d1_common.types.exceptions.IdentifierNotUnique as e:
      logger.error(e)
    except Exception, e:
      logging.error('Failed to UPDATE object with PID {} /  SID {}.'.format(new_pid, seriesID))
      logging.error(e)
      return False

  def _generate_system_metadata(self, sci_metadata_bytes, pid, seriesID, record_date):
    sys_meta = v2.systemMetadata()
    sys_meta.seriesId = seriesID
    sys_meta.formatId = self.sci_md_formatId
    sys_meta.size = len(sci_metadata_bytes)
    sys_meta.checksum = dataoneTypes.checksum(hashlib.md5(sci_metadata_bytes).hexdigest())
    sys_meta.checksum.algorithm = 'MD5'
    sys_meta.identifier = pid
    # sys_meta.dateUploaded = datetime.datetime.strptime(record_date, "%Y-%m-%dT%H:%M:%SZ")
    sys_meta.dateUploaded = record_date
    sys_meta.dateSysMetadataModified = datetime.datetime.now()
    sys_meta.rightsHolder = self.rightsholder
    sys_meta.submitter = self.submitter
    sys_meta.authoritativeMemberNode = self.authoritativeMN
    sys_meta.originMemberNode = self.originMN
    # access policies for SlenderNode design pattern default to public read only
    accessPolicy = v2.AccessPolicy()
    accessRule = v2.AccessRule()
    accessRule.subject.append(d1_common.const.SUBJECT_PUBLIC)
    permission = v2.Permission('read')
    accessRule.permission.append(permission)
    accessPolicy.append(accessRule)
    sys_meta.accessPolicy = accessPolicy
    return sys_meta

if __name__ == '__main__':
  main()