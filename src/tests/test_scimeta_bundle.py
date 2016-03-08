#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: test_scimeta_bundle

:Synopsis:

:Author:
    servilla
  
:Created:
    3/6/16
"""


import unittest
import logging

import scimeta_bundle

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y%m%d-%H:%M:%S')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('test_scimeta_bundle')

__author__ = "servilla"


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.iso_url = 'http://data.nodc.noaa.gov/geoportal/csw?getxml=%7BCA46801B-FFC0-4DE1-BBAF-0C0100199DD8%7D'
        self.sysmeta_xml = '<?xml version="1.0" ?> <ns1:systemMetadata xmlns:ns1="http://ns.dataone.org/service/types/v1"> <identifier>{CA46801B-FFC0-4DE1-BBAF-0C0100199DD8}</identifier> <formatId>http://www.isotc211.org/2005/gmd</formatId> <size>55695</size> <checksum algorithm="SHA-1">e1b347dbe983d11dd3827292e23df65cdfa63f69</checksum> <submitter>NCEI</submitter> <rightsHolder>NCEI</rightsHolder> <accessPolicy> <allow> <subject>public</subject> <permission>read</permission> </allow> </accessPolicy> <replicationPolicy numberReplicas="0" replicationAllowed="false"/> </ns1:systemMetadata>'
        self.smb = scimeta_bundle.Scimeta_Bundle(self.iso_url, self.sysmeta_xml)

    def tearDown(self):
        pass

    def test_sysmeta(self):
        sysmeta = self.smb.get_sysmeta()
        self.assertTrue(sysmeta, 'System metadata is None')

    def test_iso_size(self):
        iso_size = 55695
        iso_xml = self.smb.get_scimeta()
        self.assertTrue(iso_size == len(iso_xml), 'ISO metadata size failure: expected {0}, but got {1}.'.format(iso_size, len(iso_xml)))

    def test_gmn_create(self):
        self.assertIsNone(self.smb.gmn_create())

if __name__ == '__main__':
    unittest.main()
