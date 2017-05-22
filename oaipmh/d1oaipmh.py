# IN PROGRESS
# Last modified date: 5/9/2017

import requests
import xml.etree.ElementTree as ET

class OAIPMH_Harvester:
    def __init__(self, baseURL):
        self.baseURL = baseURL

    def startHarvest(self, INIT_PARAMS):
        r = self.initial_records_request(self.baseURL, INIT_PARAMS)
        if r.status_code == requests.codes.ok:
            root = ET.fromstring(r.content)
            recordList = root.find('{http://www.openarchives.org/OAI/2.0/}ListRecords')
            if recordList is not None: #if no records were returned as matching the query
                for record in recordList:
                    if record.tag == '{http://www.openarchives.org/OAI/2.0/}resumptionToken':
                        resumptionToken = record.text
                        while resumptionToken is not None:
                            resumptionToken = get_more_records(self.baseURL, resumptionToken)
                    else:

                        ident = record.find('{http://www.openarchives.org/OAI/2.0/}header').\
                            find('{http://www.openarchives.org/OAI/2.0/}identifier')
                        print 'Record Id: {}'.format(ident.text)
            else:
                print 'No records found.'
        else:
            print 'Bad Status Code'


    def initial_records_request(self, baseURL, INIT_PARAMS):
        # requests accepts the base URL and parameters that will be passed as part of the request.
        try:
            r = requests.get(baseURL, INIT_PARAMS)
            print 'Status code is {} for request: {}\n\n'.format(r.status_code, r.url)
            return r
        except Exception, e:
            print e


def get_more_records(baseURL, resumptionToken):
    RESUMPTION_PARAMS = {'verb': 'ListRecords',
                         'resumptionToken' : resumptionToken}
    r = requests.get(baseURL, RESUMPTION_PARAMS)
    root = ET.fromstring(r.content)
    recordList = root.find('{http://www.openarchives.org/OAI/2.0/}ListRecords')
    for record in recordList:
        if record.tag == '{http://www.openarchives.org/OAI/2.0/}resumptionToken':
            resumptionToken = record.text
            print '\nfinished get_more_records batch'
            print 'Next Resumption Token: {}\n'.format(resumptionToken)
            return resumptionToken

        else:
            ident = record.find('{http://www.openarchives.org/OAI/2.0/}header'). \
                find('{http://www.openarchives.org/OAI/2.0/}identifier')
            print 'Record ID: {}'.format(ident.text)

