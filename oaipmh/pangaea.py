# IN PROGRESS
# Last modified date: 5/9/2017

import d1oaipmh

import requests
import xml.etree.ElementTree as ET

#CONSTANTS
BASE_URL = 'https://ws.pangaea.de/oai/provider'

INIT_PARAMS = {'verb': 'ListRecords',
               'metadataPrefix': 'iso19139',
               'from': '2017-01-01T00:00:00Z',
               'until': '2017-01-10T00:00:00Z'}

demo = d1oaipmh.OAIPMH_Harvester(BASE_URL)
demo.startHarvest(INIT_PARAMS)

