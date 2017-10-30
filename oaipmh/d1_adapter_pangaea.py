"""
________________________________________________________________________________________________________________________

d1oaipmh_adapter_pangea.py acts as both an OAI-PMH harvester client and an adapter bridging harvested content into an
installation of DataONE Generic Member Node (GMN). This is the main script which handles OAI-PMH querying and processing
while an accompanying script, d1_client_manager.py, is required for managing the actual operations upon data into GMN
using the Python library implementation of DataONE GMN. The script is designed to be reusable for any OAI-PMH server with 
very little modification. Server-specific configurations are defined at the top.

NOTES ON RECORD BATCHES AND TERMINATION FOR PANGAEA:
The complete set of all records which match the information retrieval criteria of an OAI-PMH query against Pangaea's
OAI-PMH server is returned in batches of 50 items at a time. A batch of 50 is followed by a resumption token. Complete
query result sets are terminated by a valid resumption token followed by a dummy placeholder deleted record identified
as "oai:pangaea.de:deleted.dummy". This is slightly different than the OAI-PMH specification of terminating result sets
with an empty resumption token. This termination mechanism is employed both if less than 50 are returned for the 
whole query, as well as if less than 50 items remain to be returned from a larger result set. So, for example, a query 
with 43 items meeting that criteria would return a batch of 43 items, followed by a valid resumption token, and then
the dummy deleted record. A query with 217 results would return 4 batches of 50 records each, followed by a batch of
17 records, terminated by a valid resumption token and then an instance of a deleted dummy record.

In this implementation the mechanism of terminating resultsets has no impact on the outcome due to the condition that
records with deleted status but which do not match an existing identifier in the GMN datastore are ignored.
 
NOTES ON IDENTIFIERS:
This adapter script assumes content mutability on behalf of the native repository. It treats the native repository's
system identifier as the DataONE seriesId, while an arbitrarily generated unique identifier is assigned to each
version of a given record loaded into GMN.

REQUIREMENTS FOR GMN CONFIGURATIONS IN SETTINGS_SITE.PY
    TRUST_CLIENT_DATESYSMETADATAMODIFIED = True
    TRUST_CLIENT_DATEUPLOADED = True
___________________________________________________________
"""

import logging
logging.basicConfig(filename='adapter-errors.log',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.ERROR)
logger = logging.getLogger(__name__)

import os
import d1_client_manager_pangaea
import requests
import xml.etree.ElementTree as ET
from xml.dom import minidom
import datetime
import time

file_name = 'OAI-PMH_harvest.log'
if os.path.exists(file_name):
    file_action = 'a' # append if already exists
else:
    file_action = 'w' # make a new file if not

# ----------------------------------------------------------------------------------------------------------------------

OAIPMH_BASE_URL = 'https://ws.pangaea.de/oai/provider'
SCIMETA_ELEMENT = '{http://www.isotc211.org/2005/gmd}MD_Metadata'
#For dc would be something like SCIMETA_ELEMENT = '{http://www.openarchives.org/OAI/2.0/oai_dc/}oai_dc'
MN_BASE_URL = 'https://pangaea-dev-orc-1.test.dataone.org/mn'
CERT = './certs/pangaea-dev/urn_node_mnTestPANGAEA-1.crt'    # Should be either D1 generated cert (Prod) or local CA generated (Test)
KEY = './certs/pangaea-dev/urn_node_mnTestPANGAEA-1.key'  # Either D1 generated cert key (Prod) or local CA generated (Test)
SYSMETA_DICT = \
    {'submitter': 'CN=Monica Ihli A139616,O=Google,C=US,DC=cilogon,DC=org',  # Populate with your CILogon identity
     'rightsholder': 'CN=Monica Ihli A139616,O=Google,C=US,DC=cilogon,DC=org',  # Populate with your CILogon identity
     'authoritativeMN': 'urn:node:mnTestPangaea',  # Use your node's DataONE URI
     'originMN': 'urn:node:mnTestPangaea',  # Use your node's DataONE URI
     'formatId_iso': 'http://www.isotc211.org/2005/gmd',  # must be consistent w/ scimeta_element format specified above!
     'formatId_NOAA': 'http://www.isotc211.org/2005/gmd-noaa'
      }
created_count = 0  # global incrementer for metadata records harvested.
updated_count = 0  # global incrementer for records updated each time program is run
archived_count = 0 # global incrementer for records archived in a given run
start = 1  # is this the initial query request?
rtoken = None
last_harvest_time = ''


# ----------------------------------------------------------------------------------------------------------------------
def main():
  global rtoken
  global last_harvest_time
  requests.packages.urllib3.disable_warnings()
  client_mgr = d1_client_manager_pangaea.D1ClientManager(MN_BASE_URL, CERT, KEY, SYSMETA_DICT)
  harvester = OAIPMH_Harvester(OAIPMH_BASE_URL)
  last_harvest_time = client_mgr.get_last_harvest_time()  # get date most recent sysmetamodified as start of timeslice
  while (start == 1) or (start == 0 and rtoken is not None):
    record_list = harvester.get_records(harvester.define_params())
    if record_list is not None:
      rtoken_record = record_list.find('{http://www.openarchives.org/OAI/2.0/}resumptionToken')
      if rtoken_record is None:
        rtoken = None
      else:
        rtoken = rtoken_record.text
        record_list.remove(rtoken_record)
      for metadata_record in record_list:
        harvester.process_record(record=metadata_record, client_mgr=client_mgr)
    else:
        # print 'No records found.'
        pass


# ----------------------------------------------------------------------------------------------------------------------
class OAIPMH_Harvester:
  def __init__(self, baseURL):
    """
    :param baseURL: The OAI-PMH provider's base URL, not to be confused with the base URL configured for GMN.
    """
    self.baseURL = baseURL

# ----------------------------------------------------------------------------------------------------------------------
  def define_params(self):
    """
    OAI-PMH query format depends on whether this is the initial or a subsequent oai-pmh request. After initial params
    have been defined once, start is reset to false. Next time function is called, rtoken params will be returned.
    """
    global start
    global rtoken
    if start == 1:
      #params = {'verb': 'ListRecords',
      #          'metadataPrefix': 'iso19139',
      #          'from': '2017-08-04T00:00:00Z',
      #          'until': '2017-08-04T12:43:10Z'}
      params = {'verb': 'ListRecords',
                'metadataPrefix': 'iso19139',
                'from': last_harvest_time}
      start = 0
    else:
      params = {'verb': 'ListRecords',
                'resumptionToken': rtoken}
      rtoken = None
    return params

# ----------------------------------------------------------------------------------------------------------------------
  def get_records(self, parameters):
    headers = {
      'User-Agent': 'DataONE Adapter Development Testing',
      'From': 'mihli1@utk.edu'}
    try:
      r = requests.get(url=self.baseURL, params=parameters, headers=headers)
      # print 'Status code is {} for request: {}\n\n'.format(r.status_code, r.url)
      if r.status_code == requests.codes.ok:
        root = ET.fromstring(r.content)
        record_list = root.find('{http://www.openarchives.org/OAI/2.0/}ListRecords')
        return record_list # If element not found, returns none (such as if <error code="noRecordsMatch"/>)
      else:
        logging.error('Request failed: {}'.format(r.url))
    except Exception, e:
      logging.error('Request failed: {}'.format(e))
      # print e


# ----------------------------------------------------------------------------------------------------------------------
  def process_record(self, client_mgr, record):
    global created_count
    global updated_count
    global archived_count
    # If this is a record with deleted status, check if already exists in GMN. If does not exist, then ignore. But
    # if it does already exist in GMN, then it should be archived.
    if 'status' in record.find('{http://www.openarchives.org/OAI/2.0/}header').attrib:
      if record.find('{http://www.openarchives.org/OAI/2.0/}header').attrib['status'] == 'deleted':
        identifier = record.find('{http://www.openarchives.org/OAI/2.0/}header'). \
          find('{http://www.openarchives.org/OAI/2.0/}identifier').text.replace(
          'oai:pangaea.de:', '')
        if (client_mgr.check_if_identifier_exists(identifier) == 'yes' and
                identifier != "oai:pangaea.de:deleted.dummy"):
          if client_mgr.archive_science_metadata(identifier):
            archived_count += 1  # track the number of successfully archived objects

    # Otherwise status is not deleted, so parse record ID, date, and metadata contents.
    # Then check if this identifier already exists in GMN.
    else:
      identifier = record.find('{http://www.openarchives.org/OAI/2.0/}header'). \
        find('{http://www.openarchives.org/OAI/2.0/}identifier').text.replace(
        'oai:pangaea.de:', '')
      record_date = record.find('{http://www.openarchives.org/OAI/2.0/}header'). \
        find('{http://www.openarchives.org/OAI/2.0/}datestamp').text
      scimeta = ET.tostring(record.find('{http://www.openarchives.org/OAI/2.0/}metadata'). \
                            find(SCIMETA_ELEMENT))
      format = self.detect_format(record)

      checkExistsDict = client_mgr.check_if_identifier_exists(identifier)

      # if identifier exists but record date is different, this truly is an update so call update method.
      if (checkExistsDict['outcome'] == 'yes' and checkExistsDict['record_date'] != datetime.datetime.strptime(
        record_date, "%Y-%m-%dT%H:%M:%SZ")):
        if client_mgr.update_science_metadata(minidom.parseString(scimeta).toprettyxml(encoding='utf-8'),
                                              identifier, record_date, format):
          updated_count += 1  # track the number of succesfully updated objects
          # print 'Identifier {} UPDATED'.format(identifier)

      # if identifier exists but record date is the same, it's not really an update. So skip it and move on.
      elif (checkExistsDict['outcome'] == 'yes' and checkExistsDict['record_date'] == datetime.datetime.strptime(
        record_date, "%Y-%m-%dT%H:%M:%SZ")):
        # print 'Skipped over record ' + identifier + ' . Exists in GMN but no updates to apply.'
        pass

      # if check failed for some reason, it will just log that an issue ocurred and skip over the record.
      elif checkExistsDict['outcome'] == 'failed':
        pass

      # If this identifer is not already found in GMN in any way, so create a new object in GMN
      elif checkExistsDict['outcome'] == 'no':
        if client_mgr.load_science_metadata(minidom.parseString(scimeta).toprettyxml(encoding='utf-8'),
                                            identifier,
                                            record_date,
                                            format):
          created_count += 1  # track number of successfully created new objects
          # print 'Identifier {} CREATED'.format(identifier)
        else:
          # print 'Identifier {} create failed.'.format(identifier)
          # error here is logged in d1_client_manager.py
          pass

  def detect_format(self, record):
    gmd = '{http://www.isotc211.org/2005/gmd}'
    checkNOAA = record.find('{http://www.openarchives.org/OAI/2.0/}metadata/'
                            + gmd + 'MD_Metadata/' + gmd + 'identificationInfo/'
                            + gmd + 'MD_DataIdentification/' + gmd + 'extent/'
                            + gmd + 'EX_Extent/' + gmd + 'temporalElement/'
                            + gmd + 'EX_TemporalExtent/'
                            + gmd + 'extent/{http://www.opengis.net/gml}TimePeriod')
    if checkNOAA is None:
      return 'formatId_NOAA'
    else:
      return 'formatId_iso'


# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
  main()
