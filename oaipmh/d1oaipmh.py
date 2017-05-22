# Tested on dataone.libclient version 2.0.0.
# Last modified date: 5/9/2017

import requests
import xml.etree.ElementTree as ET

class OAIPMH_Harvester:
    def __init__(self, baseURL):
        self.baseURL = baseURL

    def startHarvest(self, INIT_PARAMS):
        r = requests.get(self.baseURL, INIT_PARAMS)
        print 'Status code is {} for request: {}\n\n'.format(r.status_code, r.url)
        if r.status_code == requests.codes.ok:
            root = ET.fromstring(r.content)
            recordList = root.find('{http://www.openarchives.org/OAI/2.0/}ListRecords')
            return recordList
        else:
            print 'Bad Status Code'

