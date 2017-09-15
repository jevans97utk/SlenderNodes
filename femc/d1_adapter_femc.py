"""
________________________________________________________________________________________________________________________

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


Author: mihli1@utk.edu
Last Modified Date: 9/15/2017
Last GMN Version tested with: 2.3.7

Important configurations:
 - REST endpoint
 - REST API Key
 - Member Node software endpoint
 - Certificate paths
________________________________________________________________________________________________________________________
"""

import logging

# This is an error tracking log
logging.basicConfig(filename='adapter-errors.log',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.ERROR)
logger = logging.getLogger(__name__)
# logger.setLevel(logging.ERROR)

import os
import d1_client_manager
import requests
import xml.etree.ElementTree as ET
from xml.dom import minidom
import datetime
import time
import calendar


file_name = 'femc_harvest.log' # a file tracking the number of creates, updates, archives executed in a given run.
if os.path.exists(file_name):
  file_action = 'a'  # append to current tracking file if already exists
else:
  file_action = 'w'  # or make a new tracking file if not

# ********************************************** CONFIGURATIONS ********************************************************


# Constants for harvesting
REST_BASE_URL = 'https://www.uvm.edu/femc/dataone'
REST_API_KEY = 'api_key_goes_here'

# Constants for D1_Client_Manager found in d1_client_manager.py, including client and system metadata constants
MN_BASE_URL = 'https://ubuntugmn.kitty.ninja/mn'
CERT = \
  '/home/monica/PycharmProjects/dataone-libclient_2-3-7/certs/kitty/urn_node_mnTestKITTY.crt'
KEY = \
  '/home/monica/PycharmProjects/dataone-libclient_2-3-7/certs/kitty/urn_node_mnTestKITTY.key'

# This is System information that is part of the information we use internally to describe your science metadata
SYSMETA_DICT = \
  {'submitter': 'CN=Monica Ihli A139616,O=Google,C=US,DC=cilogon,DC=org',  # Populate with your CILogon identity
   'rightsholder': 'CN=Monica Ihli A139616,O=Google,C=US,DC=cilogon,DC=org',  # Populate with your CILogon identity
   'authoritativeMN': 'urn:node:mnTestFEMC',  # Use your node's DataONE URI
   'originMN': 'urn:node:mnTestFEMC',  # Use your node's DataONE URI
   'formatId': 'eml://ecoinformatics.org/eml-2.1.1'  # the DataONE supported formatID.
   }

created_count = 0  # global incrementer for metadata records harvested.
updated_count = 0  # incrementer for records updated each time program is run

# ********************************************** MAIN PROGRAM **********************************************************

def main():
  requests.packages.urllib3.disable_warnings()
  client_mgr = d1_client_manager.D1ClientManager(
    MN_BASE_URL, CERT, KEY, SYSMETA_DICT) # This client manager handles all the DataONE api stuff.
  harvester = FEMC_Harvester(REST_BASE_URL, REST_API_KEY) # This harvester handles functionality specific to FEMC.
  last_harvest_time = client_mgr.get_last_harvest_time()  # Latest record date in GMN becomes start time for new query
  last_harvest_epoch_time = calendar.timegm(
    time.strptime(last_harvest_time, "%Y-%m-%d %H:%M:%S.%f")) # FEMC endpoint needs dates in epoch time, so convert
  recordlist = harvester.getRecordsList(
    last_harvest_epoch_time)  # start of by asking the FEMC endpoint for any newly modified /created records

  if recordlist is not None:  # So long as the query returned any items,
    for item in recordlist:  # then for each of those records:
      projectID = item.find('fkProjectID').text # get the project/dataset identifiers
      datasetID = item.find('fkDatasetID').text
      science_metadata = harvester.getScienceMetadata(projectID, datasetID) # and pass to function to get the EML record
      harvester.process_record(client_mgr,projectID, datasetID, science_metadata) #figure out if an update or new record
    # print 'No records found.'
    pass

  tracking_log = open(file_name, file_action) # make a note of how many records added to GMN or updated this round
  tracking_log.write(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") +
                     ', New Records Loaded: {}, Records Updated: {}\n'.format(created_count,
                                                                                                    updated_count))
  tracking_log.close()


# *****************************************************************************************
class FEMC_Harvester:
  def __init__(self, baseURL, apiKEY):
    """
    :param baseURL: The FEMC rest service base URL, not to be confused with the base URL configured for GMN.
    """
    self.baseURL = baseURL
    self.apiKEY = apiKEY

  def getRecordsList(self, last_harvest_time):
    """
    Makes the request query against rest service using the api key & rest base URL passed as an argument.
    :param last_harvest_time: date sysmeta modified of last object created in GMN
    :return: Returns a list of items returned as a result from the rest query if any records returned by query
     found. Otherwise, returns None
    """
    headers = {'User-Agent': 'DataONE Adapter','From': 'mihli1@utk.edu'}

    # just for testing, we can overwrite last harvest time to some particular point if desired:
    #last_harvest_time = '1502668800'
    request_url = self.baseURL + '/changedDatasets/changedSince/' + str(last_harvest_time) + \
                  '/X-API-KEY/' + self.apiKEY
    try:
      r = requests.get(request_url, headers=headers)
      # print 'Status code is {} for request: {}\n\n'.format(r.status_code, r.url)
      if r.status_code == requests.codes.ok:
        root = ET.fromstring(r.content)
        recordList = root.findall('item')
        return recordList
      else:
        logging.error('Request failed: {}'.format(r.url))
        # log failed request
    except Exception, e:
      logging.error('Request failed: {}'.format(e))


  def getScienceMetadata(self, projectID, datasetID):
    """
    After the program gets a list of project/dataset ids, it calls this function for each record. in order to
    retrieve the contents of the science metadata record using the second FEMC rest endpoint
    :param projectID: the project identifier from the FEMC system
    :param datasetID: dataset ID from FEMC system. Combined with project id, they form a unique key for each record
    :return: Returns a list of items returned as a result from the rest query if any records returned by query
     found. Otherwise, returns None
    """
    # form the python request here
    headers = {'User-Agent': 'DataONE Adapter', 'From': 'mihli1@utk.edu'}
    request_url = self.baseURL + '/datasetEML/projectID/' + projectID + '/datasetID/' + datasetID + \
                  '/X-API-KEY/' + self.apiKEY
    try: # try to execute the request here. If it doesn't work out, then log an  error
      r = requests.get(request_url, headers=headers)
      # print 'Status code is {} for request: {}\n\n'.format(r.status_code, r.url)
      if r.status_code == requests.codes.ok:
        science_metadata = ET.fromstring(r.content)
        return science_metadata
      else:
        logging.error('Metadata request failed: Response {} for {}'.format(r.status_code, r.url))
        # log failed request
    except Exception, e:
      logging.error('Metadata request failed: {}'.format(e))


  def process_record(self, client_mgr, projectID, datasetID, eml_record):
    """This function is called for each item in a list which was returned from a rest query. It
    also expects an instance of d1_client_manager.D1ClientManager to be passed as an argument, which will handle making
    the appropriate API method calls.
    The possible outcomes for items passed as an argument:

        (1) A new item is loaded to GMN:
        An item which does not exist in GMN in any form will result in the creation of an object with a
        new seriesId. This happens when D1ClientManager.check_if_identifier_exists() has confirmed that a metadata
        record item is a new or existing object in GMN. D1ClientManager.load_science_metadata() is used to create the
        new object on GMN.

        (2) An existing record on GMN is updated by a newer version:
        This occurs when D1ClientManager.check_if_item_exists() confirms that at least one version of this item already
        exists in GMN. It is interpreted to mean that the science metadata record was already loaded by GMN in the
        past, but the record has since been modified. D1ClientManager.update_science_metadata()
        is called to perform the update. See this function's documentation for more information about the update process
        """
    global created_count
    global updated_count

    identifier = 'p' + projectID + 'ds' + datasetID # First combine project/dataset ID into a single identifier
    scimeta = ET.tostring(eml_record) # convert the elementtree XML object to a string
    checkExistsDict = client_mgr.check_if_identifier_exists(identifier) #

    # if identifier exists already call update method.
    if (checkExistsDict['outcome'] == 'yes'):
      if client_mgr.update_science_metadata(
          minidom.parseString(scimeta).toprettyxml(encoding='utf-8'), identifier):
        updated_count += 1  # function returns 1 if successful; track the number of updated objects
        print 'Identifier {} UPDATED'.format(identifier)

    # if check failed for some reason, it have logged that an issue occurred and skip over the record.
    elif checkExistsDict['outcome'] == 'failed':
      pass

    # If this identifer is not already found in GMN in any way, so create a new object in GMN
    elif checkExistsDict['outcome'] == 'no':
      if client_mgr.load_science_metadata(minidom.parseString(scimeta).toprettyxml(encoding='utf-8'),
                                          identifier,
                                          datetime.datetime.now()
                                          ):
        created_count += 1  # track number of successfully created new objects
        # print 'Identifier {} CREATED'.format(identifier)

    else:
      pass
      # print 'Identifier {} create failed.'.format(identifier)


if __name__ == '__main__':
  main()
