"""
Test suite for the Arctic Biodiversity Data Service.
"""

# standard library imports
import asyncio
import importlib.resources as ir
import io
import re

# 3rd party library imports
from aioresponses import aioresponses
import lxml.etree

# local imports
from schema_org.abds import AbdsIptHarvester
from .test_common import TestCommon


class TestSuite(TestCommon):

    def setUp(self):
        # Every URL request for ABDS IPT will match this pattern, so we set
        # aioresponses to intercept all of them.
        self.regex = re.compile(r'http://geo.abds.is/ipt')

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
        SCENARIO:  We retrieve an EML 2.1.1 ABDS IPT XML document.

        EXPECTED RESULT:  The identifier is verified.
        """
        content = ir.read_binary('tests.data.abds.ipt', 'arcod_2007p6.xml')

        harvester = AbdsIptHarvester()

        with self.assertLogs(logger=harvester.logger, level='INFO'):
            with aioresponses() as m:
                m.get(self.regex, body=content)

                url = 'http://geo.abds.is/ipt/eml.do?r=arcod_2007p6'
                identifier, _ = asyncio.run(harvester.retrieve_record(url))

        self.assertEqual(identifier, '59876921-fda6-4fd5-af5d-cba2a7152527')

    def test_check_if_can_be_updated__document_has_not_changed(self):
        """
        SCENARIO:  The GMN existance check shows that the document has already
        been harvested.  The new document, is the same.  For GMD documents,
        this will raise an exception.  In this case, though, we let it pass
        because the check doesn't support EML 2.1.1

        EXPECTED RESULT:  No exception is raised.
        """
        host, port = 'abds.mn.org', 443
        harvester = AbdsIptHarvester(host=host, port=port)

        # This is the existing document in the MN.  It is marked as complete.
        existing_content = ir.read_binary('tests.data.abds.ipt',
                                          'arcod_2007p6.xml')

        # Verify the document.  This has the effect of setting the format ID,
        # which is EML 2.1.1, not the default GMD.
        doc = lxml.etree.parse(io.BytesIO(existing_content))
        with self.assertLogs(logger=harvester.logger, level='INFO'):
            harvester.validate_document(doc)

        # This is the "update" document, same as the existing document.  Change
        # the progress code.
        doc_bytes = ir.read_binary('tests.data.abds.ipt', 'arcod_2007p6.xml')

        current_sid = 1
        doi = 'doi.10000/abcde'

        regex = re.compile(f'https://{host}:{port}/')
        with aioresponses() as m:
            m.get(regex, body=existing_content)
            asyncio.run(harvester.check_if_can_be_updated(doc_bytes, doi,
                                                          current_sid))
