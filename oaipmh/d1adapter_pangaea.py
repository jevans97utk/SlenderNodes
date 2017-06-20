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
    TRUST_CLIENT_SUBMITTER = True
    TRUST_CLIENT_ORIGINMEMBERNODE = True
    TRUST_CLIENT_AUTHORITATIVEMEMBERNODE = True
    TRUST_CLIENT_DATESYSMETADATAMODIFIED = False
    TRUST_CLIENT_SERIALVERSION = False
    TRUST_CLIENT_DATEUPLOADED = True

Comment out _pyxb_set_with_override(sysmeta_pyxb, 'dateUploaded', now_datetime) from view_util.py


Last tested on dataone.libclient version 2.0.0

Last modified date: 6/05/2017


Processing will range from 10 - 14 seconds per batch of 50. 
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

# this is just a file tracking the number of creates, updates, archives executed in a given run.
file_name = 'OAI-PMH_harvest.log'
if os.path.exists(file_name):
    file_action = 'a' # append if already exists
else:
    file_action = 'w' # make a new file if not

# ********************************************** CONFIGURATIONS ********************************************************

# Constants for this adapter
SCIMETA_ELEMENT = '{http://www.isotc211.org/2005/gmd}MD_Metadata' # Element containing metadata for this OAI-PMH harvest
# Example for DC would be:
# scimeta_element = '{http://www.openarchives.org/OAI/2.0/oai_dc/}oai_dc'

# Constants for OAIPMH_Harvester
OAIPMH_BASE_URL = 'https://ws.pangaea.de/oai/provider'

# Constants for D1_Client_Manager found in d1_client_manager.py, including client and system metadata constants
MN_BASE_URL = 'https://centos7-3gmn.kitty.ninja/mn'
CERT = '../certs_centos/client_cert.pem'    # Should be either D1 generated cert (Prod) or local CA generated (Test)
KEY = '../certs_centos/client_key_nopassword.pem'  # Either D1 generated cert key (Prod) or local CA generated (Test)
SYSMETA_DICT = \
    {'submitter': 'CN=Monica Ihli A139616,O=Google,C=US,DC=cilogon,DC=org',  # Populate with your CILogon identity
     'rightsholder': 'CN=Monica Ihli A139616,O=Google,C=US,DC=cilogon,DC=org',  # Populate with your CILogon identity
     'authoritativeMN': 'urn:node:mnTestPangaea',  # Use your node's DataONE URI
     'originMN': 'urn:node:mnTestPangaea',  # Use your node's DataONE URI
     'formatId': 'http://www.isotc211.org/2005/gmd'  # must be consistent w/ the scimeta_element format specified above!
      }
created_count = 0  # global incrementer for metadata records harvested.
updated_count = 0  # incrementer for records updated each time program is run
archived_count = 0  # incrementer for records archived in a given run

# ********************************************** MAIN PROGRAM **********************************************************

def main():
    requests.packages.urllib3.disable_warnings()
    client_mgr = d1_client_manager.D1ClientManager(MN_BASE_URL, CERT, KEY, SYSMETA_DICT)
    harvester = OAIPMH_Harvester(OAIPMH_BASE_URL)
    last_harvest_time = client_mgr.get_last_harvest_time()  # get date most recent sysmetamodified as start of timeslice
    init_params = harvester.getInitialParameters(last_harvest_time) # constructs request parameters, incl. last harvest
    recordlist = harvester.getRecords(init_params)  # get initial batch of records using the dict of request params

    # initial records request
    if recordlist is not None:  # So long as the query returned any items,
        for record in recordlist:  # then for each of those records:
            if record.tag == '{http://www.openarchives.org/OAI/2.0/}resumptionToken':  # if end of batch w/ more records
                resumptionToken = record.text
                # print '\n****** First Resumption Token: {} ******\n'.format(resumptionToken)
                while resumptionToken is not None:
                    resumptionToken = harvester.get_more_records(  # then get the next batch
                        client_mgr, harvester, resumptionToken)
            else:
                harvester.process_record(client_mgr, record)
    else:
        # print 'No records found.'
        pass
    tracking_log = open(file_name, file_action)
    tracking_log.write(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") +
                       ', New Records Loaded: {}, Records Updated: {}, Records archived: {}\n'.format(created_count, updated_count, archived_count))
    tracking_log.close()


# ******************************************* OAI-PMH CLASSES & FUNCTIONS **********************************************

class OAIPMH_Harvester:
    def __init__(self, baseURL):
        """
        
        :param baseURL: The OAI-PMH provider's base URL, not to be confused with the base URL configured for GMN.
        """
        self.baseURL = baseURL

    def getInitialParameters(self, last_harvest_time):
        # hard coded timeslice params are an option if the below lines are uncommented and the other dict is commented
        #init_params = {'verb': 'ListRecords',
        #               'metadataPrefix': 'iso19139',
        #               'from': '2017-06-15T00:00:00Z',
        #               'until': '2017-06-15T23:59:59Z'}
        init_params = {'verb': 'ListRecords',
                       'metadataPrefix': 'iso19139',
                       'from': last_harvest_time}
        return init_params

    def getRecords(self, parameters):
        """
        Makes the OAI-PMH query request using the parameters passed as an argument.   
              
        :param parameters: OAI-PMH query parameters. The initial request parameters are defined at the beginning of the
         script. Subsequent calls for remaining batches of records to be retrieved from the query will be called from
         .get_more_records(), and will include the resumption token.
        :return: Returns a list of items returned as a result from an OAI=PMH query if ListRecords subelement can be
         found. Otherwise, returns None
        """

        # to do: move headers to the top
        headers = {
            'User-Agent': 'DataONE Adapter Development Testing',
            'From': 'mihli1@utk.edu'
        }
        try:
            r = requests.get(url=self.baseURL, params=parameters, headers=headers)
            # print 'Status code is {} for request: {}\n\n'.format(r.status_code, r.url)
            if r.status_code == requests.codes.ok:
                root = ET.fromstring(r.content)
                recordList = root.find('{http://www.openarchives.org/OAI/2.0/}ListRecords')
                # if the ListRecords subelement is not found, then recordList is returned as None
                # the main program responds differently if None is returned.
                return recordList
            else:
                logging.error('Request failed: {}'.format(r.url))
                # log failed request
        except Exception, e:
            logging.error('Request failed: {}'.format(e))

    # if root.find ListRecords doesn't find the records list subelement, then it will return an empty recordList
    # This is how it will work in the case of no record matching the timeslice (<error code="noRecordsMatch"/>)

    def get_more_records(self, client_mgr, harvester, resumptionToken):
        """
        This function is called by main part of script and accepts a parsed resumption token as an argument. The token
        is used to construct a new request for additional records to be retrieved from an OAI-PMH query. As long as
        this function continues to return a resumption token, the main program will continue to call it.
        A process_record() function is called within to determine how items other than resumption tokens (science
        metadata records) should be handled. 
        
        :param client_mgr: instance of D1ClientManager
        :param harvester: instance of OAIPMH_Harvester
        :param resumptionToken: resumption token parsed from a previous batch of records returned from  OAI-PMH query.
        :return: resumptionToken, if a resumption token is found.
        """
        resumption_params = {'verb': 'ListRecords',
                             'resumptionToken': resumptionToken}
        recordlist = harvester.getRecords(resumption_params)
        if recordlist is not None:  # So long as the query returned any items,
            for record in recordlist:
                if record.tag == '{http://www.openarchives.org/OAI/2.0/}resumptionToken':
                    resumptionToken = record.text
                    # print '\n****** Next Resumption Token: {} ******\n'.format(resumptionToken)
                    return resumptionToken

                else:
                    harvester.process_record(client_mgr, record)

    def process_record(self, client_mgr, record):
        """This function is called for each non-resumption token item in a list which was returned from an OAI-PMH query. It
        also expects an instance of d1_client_manager.D1ClientManager to be passed as an argument, which will handle making
        the appropriate API method calls.
        There are 4 possible outcomes for items passed as an argument:
            
            (1) A list item with deleted status is archived in GMN: 
            D1ClientManager.check_if_identifier_exists() has queried GMN to determine if the native repository system ID for
            this item already exists as a seriesId in GMN. Having found that this identifier exists in GMN, the most current
            version of the science metadata record in GMN is then archived-- in essence, a 'soft' delete is performed. 
            
            (2) A list item received from OAI-PMH query having deleted status is ignored:
            This is expected to only be encountered in the initial load from the native repository to GMN. Records which
            already have deleted status at the time this adapter goes online will not be acknowledged by GMN.        
            
            (3) A new item is loaded to GMN:
            An item which does not exist in GMN in any form will result in the creation of an object with a
            new seriesId. This happens when D1ClientManager.check_if_identifier_exists() has confirmed that a metadata record item is a new
            or existing object in GMN. D1ClientManager.load_science_metadata() is used to create the new object on GMN.
                
            (4) An existing record on GMN is updated by a newer version:
            This occurs when D1ClientManager.check_if_item_exists() confirms that at least one version of this item already
            exists in GMN. It is interpreted to mean that the science metadata record was already loaded by GMN in the
            past, but the record has since been modified, and so it's new datetimestamp has caused it to show up again in
            the OAI-PMH query results. D1ClientManager.update_science_metadata() is called to perform the update. See this
            function's documentation for more information about the update process.        
            """
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
                if (client_mgr.check_if_identifier_exists(identifier)=='yes' and
                    identifier !="oai:pangaea.de:deleted.dummy"):
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
            checkExistsDict = client_mgr.check_if_identifier_exists(identifier)

            # if identifier exists but record date is different, this truly is an update so call update method.
            if (checkExistsDict['outcome'] == 'yes' and checkExistsDict['record_date'] != datetime.datetime.strptime(
                    record_date, "%Y-%m-%dT%H:%M:%SZ")):
                if client_mgr.update_science_metadata(minidom.parseString(scimeta).toprettyxml(encoding='utf-8'),
                                                      identifier, record_date):
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
                                                    record_date
                                                    ):
                    created_count += 1  # track number of successfully created new objects
                    # print 'Identifier {} CREATED'.format(identifier)
                else:
                    # print 'Identifier {} create failed.'.format(identifier)
                    # error here is logged in d1_client_manager.py
                    pass

if __name__ == '__main__':
    main()