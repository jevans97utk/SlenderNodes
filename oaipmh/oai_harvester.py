# IN PROGRESS!
#
# Last updated 4/24/2017 @ 12:45 pm
# Next steps:
#   - move response parsing into a function
#   - convert to loop for cycling through each page of new xml docs so long as a resumption token is found:
#           RESUMPTION_PARAMS = {'verb': 'ListRecords', 'resumptionToken' : rtoken}
#           r = requests.get(BASE_URL, RESUMPTION_PARAMS)
#   - Exceptions & handling for status codes, such as wait and try again if 503
#       *BUT* needs to be aware of the expiration date of resumption code when encountered mid list


import requests
import xml.etree.ElementTree as ET



# just writing stuff to a file temporarily while developing
# f = open("output.txt", "w")

BASE_URL = 'https://ws.pangaea.de/oai/provider'

# Build a dictionary of parameters for initial ListRecords request
# For testing purposes, I'm using hardcoded from and until values. Obviously when the adapter
# is in place, from parameter will be populated the most recent harvest point in time
INIT_PARAMS = {'verb': 'ListRecords',
               'metadataPrefix': 'iso19139',
               'from': '2015-01-01T00:00:00Z',
               'until': '2017-01-02T00:00:00Z'}

# requests accepts the base URL and parameters that will be passed as part of the request.
r = requests.get(BASE_URL, INIT_PARAMS)
print 'Status code is {} for request: {}\n\n'.format(r.status_code, r.url)
# print r.url
#doc = xdom.parseString(r.text.encode('utf-8'))
#pretty_xml_as_string = doc.toprettyxml()
#f.write(pretty_xml_as_string.encode('utf-8'))

if r.status_code == requests.codes.ok:
    root = ET.fromstring(r.content)
    recordList = root.find('{http://www.openarchives.org/OAI/2.0/}ListRecords')
    i = 1
    for record in recordList:
        if record.tag == '{http://www.openarchives.org/OAI/2.0/}resumptionToken':
            rtoken = record.text
            print 'Resumption Token: {}'.format(rtoken)
        else:
            print 'Record #: {}'.format(i)
            ident = record.find('{http://www.openarchives.org/OAI/2.0/}header').\
                find('{http://www.openarchives.org/OAI/2.0/}identifier')
            print 'Identifier: {}'.format(ident.text)
            dataseturi = record.find('{http://www.openarchives.org/OAI/2.0/}metadata').\
                find('{http://www.isotc211.org/2005/gmd}MD_Metadata').\
                find('{http://www.isotc211.org/2005/gmd}dataSetURI').\
                find('{http://www.isotc211.org/2005/gco}CharacterString')
            print 'Data located at: {}\n'.format(dataseturi.text)
        i += 1
else:
    print 'Bad Status Code'

