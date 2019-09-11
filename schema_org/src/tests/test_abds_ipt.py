"""
Test suite for the Arctic Biodiversity Data Service.
"""

# standard library imports
import importlib.resources as ir
import io
import re

# 3rd party library imports
import lxml.etree

# local imports
from schema_org.abds import AbdsIptHarvester
from .test_common import TestCommon


class TestSuite(TestCommon):

    def setUp(self):
        # Every URL request for ARM will match this pattern, so we set
        # aioresponses to intercept all of them.
        self.pattern = re.compile(r'https://www.hydroshare.org/')

    def test_sitemap(self):
        """
        SCENARIO:  ABDS IPT has an RSS feed to use as a sitemap.

        EXPECTED RESULT:  70 documents.
        """
        contents = ir.read_binary('tests.data.abds', 'abds_ipt_rss.xml')
        doc = lxml.etree.parse(io.BytesIO(contents))

        harvester = AbdsIptHarvester()
        with self.assertLogs(logger=harvester.logger, level='INFO'):
            records = harvester.extract_records_from_sitemap(doc)

        expected = 70
        self.assertEqual(len(records), expected)

    def test_sitemap_is_index_file(self):
        """
        SCENARIO:  ABDS IPT has an RSS feed to use as a sitemap.

        EXPECTED RESULT:  False, it is not an index file.
        """
        contents = ir.read_binary('tests.data.abds', 'abds_ipt_rss.xml')
        doc = lxml.etree.parse(io.BytesIO(contents))

        harvester = AbdsIptHarvester()
        self.assertFalse(harvester.is_sitemap_index_file(doc))

    def test_identifier(self):
        """
        SCENARIO:  We have an EML 2.1.1 ABDS IPT XML document.

        EXPECTED RESULT:  The identifier is
        59876921-fda6-4fd5-af5d-cba2a7152527
        """
        contents = ir.read_binary('tests.data.abds.ipt', 'arcod_2007p6.xml')
        doc = lxml.etree.parse(io.BytesIO(contents))

        harvester = AbdsIptHarvester()
        actual = harvester.extract_identifier(doc)
        expected = '59876921-fda6-4fd5-af5d-cba2a7152527'

        self.assertEqual(actual, expected)
