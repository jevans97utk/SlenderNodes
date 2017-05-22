#   Tested on dataone.libclient version 2.0.0
#   Last modified date: 5/22/2015
#

import d1oaipmh
import d1_client_manager

import requests
import xml.etree.ElementTree as ET
from xml.dom import minidom
import logging

# Constants for this adapter
SCIMETA_ELEMENT = '{http://www.isotc211.org/2005/gmd}MD_Metadata' # Element containing metadata for this OAI-PMH harvest
# Example for DC would be:
# scimeta_element = '{http://www.openarchives.org/OAI/2.0/oai_dc/}oai_dc'

# Constants for OAIPMH_Harvester found in d1oaipmh.py
OAIPMH_BASE_URL = 'https://ws.pangaea.de/oai/provider'
INIT_PARAMS = {'verb': 'ListRecords',
               'metadataPrefix': 'iso19139',
               'from': '2017-01-01T00:00:00Z',
               'until': '2017-01-15T00:00:00Z'}

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


def main():
    requests.packages.urllib3.disable_warnings()
    logging.basicConfig()
    # change level below to .setLevel(logging.DEBUG) if troubleshooting a problem
    logging.getLogger('').setLevel(logging.ERROR)
    client_mgr = zd1_client_manager.D1ClientManager(MN_BASE_URL, CERT, KEY, SYSMETA_DICT)
    harvester = zd1oaipmh3.OAIPMH_Harvester(OAIPMH_BASE_URL)
    recordList = harvester.startHarvest(INIT_PARAMS)    # get initial batch of records
    count = 0
    # initial records request
    if recordList is not None:  # So long as the query returned any items,
        for record in recordList:  # then for each of those records:
            if record.tag == '{http://www.openarchives.org/OAI/2.0/}resumptionToken':  # if end of batch w/ more records
                resumptionToken = record.text
                while resumptionToken is not None:
                    resumptionToken = get_more_records(client_mgr, resumptionToken) # then get next batch of records
            else:
                process_record(client_mgr, record)
                count += 1
                print count

    else:
        print 'No records found.'



def process_record(client_mgr, record):
    # If this is a deleted record
    if 'status' in record.find('{http://www.openarchives.org/OAI/2.0/}header').attrib:
        if record.find('{http://www.openarchives.org/OAI/2.0/}header').attrib['status'] == 'deleted':
            identifier = record.find('{http://www.openarchives.org/OAI/2.0/}header'). \
                find('{http://www.openarchives.org/OAI/2.0/}identifier')
            print 'Record {} has been DELETED'.format(identifier.text)
            # TO DO: deleted records should have .archive() called on them
            # if this is a science metadata record
    else:
        identifier = record.find('{http://www.openarchives.org/OAI/2.0/}header'). \
            find('{http://www.openarchives.org/OAI/2.0/}identifier')
        scimeta = ET.tostring(record.find('{http://www.openarchives.org/OAI/2.0/}metadata'). \
                              find(SCIMETA_ELEMENT))
        # If identifier already exists on GMN, then perform an update
        if client_mgr.check_if_identifier_exists(identifier.text):
            client_mgr.update_science_metadata(minidom.parseString(scimeta).toprettyxml(encoding='utf-8'),
                                               identifier.text)
            print 'Identifier {} UPDATED'.format(identifier.text)
        else:  # This is an entirely new metadata record
            client_mgr.ingest_science_metadata(minidom.parseString(scimeta).toprettyxml(encoding='utf-8'),
                                               identifier.text,
                                               )
            print 'Identifier {} CREATED'.format(identifier.text)
        # raw_input('Press ENTER to continue: ')

def get_more_records(client_mgr, resumptionToken):
    RESUMPTION_PARAMS = {'verb': 'ListRecords',
                         'resumptionToken': resumptionToken}
    r = requests.get(OAIPMH_BASE_URL, RESUMPTION_PARAMS)
    root = ET.fromstring(r.content)
    recordList = root.find('{http://www.openarchives.org/OAI/2.0/}ListRecords')
    if recordList is not None:  # So long as the query returned any items,
        for record in recordList:
            if record.tag == '{http://www.openarchives.org/OAI/2.0/}resumptionToken':
                resumptionToken = record.text
                print '\nfinished get_more_records batch'
                print 'Next Resumption Token: {}\n'.format(resumptionToken)
                return resumptionToken

            else:
                process_record(client_mgr, record)


if __name__ == '__main__':
    main()