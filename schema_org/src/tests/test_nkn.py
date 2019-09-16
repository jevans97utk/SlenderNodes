# Standard library imports
import asyncio
try:
    import importlib.resources as ir
except ImportError:  # pragma:  nocover
    import importlib_resources as ir
import io
import re
from unittest.mock import patch

# 3rd party library imports
import aiohttp
from aioresponses import aioresponses
import lxml.etree

# local imports
from schema_org.core import SkipError, XMLValidationError
from schema_org.nkn import NKNHarvester, MissingMetadataFileIdentifierError
from .test_common import TestCommon


class TestSuite(TestCommon):

    def setUp(self):
        # aioresponses can use a regex as a way of catching any URL request
        # with this base.
        self.regex = re.compile("https://www.northwestknowledge.net/data/")

    @patch('schema_org.core.logging.getLogger')
    def test_identifier(self, mock_logger):
        """
        SCENARIO:  The NKN identifier is a UUID that must be retrieved from
        the metadata XML document.

        EXPECTED RESULT:  nkn:0a42d2bc-700a-4cf2-a7ac-ad6b892da7f0
        """
        package = 'tests.data.nkn.0a42d2bc-700a-4cf2-a7ac-ad6b892da7f0'
        content = ir.read_binary(package, 'metadata.xml')
        doc = lxml.etree.parse(io.BytesIO(content))

        harvester = NKNHarvester()
        identifier = harvester.extract_identifier(doc)

        self.assertEqual(identifier,
                         'nkn:0a42d2bc-700a-4cf2-a7ac-ad6b892da7f0')

    def test_sitemap_header__text_html_charset_utf8(self):
        """
        SCENARIO:  The sitemap retrieve header includes 'Content-Type' as
        'text/html;charset=UTF-8'.

        EXPECTED RESULT: No warning is logged.
        """
        content = ir.read_binary('tests.data.nkn', 'index.html')
        headers = {'Content-Type': 'text/html;charset=UTF-8'}

        harvester = NKNHarvester()

        with aioresponses() as m:
            m.get(self.regex, body=content, status=200, headers=headers)

            with self.assertLogs(logger=harvester.logger, level='DEBUG') as cm:
                url = "https://www.northwestknowledge.net/data/"
                asyncio.run(harvester.get_sitemap_document(url))

                self.assertLogLevelCallCount(cm.output, level='WARNING', n=0)

    def test_retrieve_record(self):
        """
        SCENARIO:  We have a URL for a landing page.

        EXPECTED RESULT:  The identifier is retrieved.
        """
        url = (
            "https://www.northwestknowledge.net"
            "/data/0a42d2bc-700a-4cf2-a7ac-ad6b892da7f0/"
        )

        # External I/O
        #
        # 1st:  landing page
        # 2nd:  XML metadata document
        package = 'tests.data.nkn.0a42d2bc-700a-4cf2-a7ac-ad6b892da7f0'
        contents = [
            ir.read_binary(package, 'index.html'),
            ir.read_binary(package, 'metadata.xml')
        ]

        harvester = NKNHarvester()

        with self.assertLogs(logger=harvester.logger, level='INFO'):
            with aioresponses() as m:
                m.get(self.regex, body=contents[0])
                m.get(self.regex, body=contents[1])

                identifier, doc = asyncio.run(harvester.retrieve_record(url))

        expected = 'nkn:0a42d2bc-700a-4cf2-a7ac-ad6b892da7f0'
        self.assertEqual(identifier, expected)

    def test_retrieve_record__500_error(self):
        """
        SCENARIO:  We have a URL for a landing page.  The response is a server
        error, however.  This is complimentary to the _404_error test below.

        EXPECTED RESULT:  An Exception is raised (but not a SkipError).
        """
        url = (
            "https://www.northwestknowledge.net"
            "/data/94E2D569-200F-44F7-8937-AB4BD0862C91"
        )

        # External I/O
        #
        # 1st:  landing page
        # 2nd:  XML metadata document  (raises 404)
        package = 'tests.data.nkn.0a42d2bc-700a-4cf2-a7ac-ad6b892da7f0'
        contents = [
            ir.read_binary(package, 'index.html'),
        ]

        harvester = NKNHarvester()

        with self.assertLogs(logger=harvester.logger, level='INFO'):
            with aioresponses() as m:
                m.get(self.regex, body=contents[0])
                m.get(self.regex, status=500)

                with self.assertRaises(aiohttp.ClientResponseError):
                    asyncio.run(harvester.retrieve_record(url))

    def test_retrieve_record__404_error(self):
        """
        SCENARIO:  We have a URL for a landing page.  However, the directory
        on the remote end does not have a metadata.xml document.

        EXPECTED RESULT:  A SkipError is raised.  For other clients, this is
        NOT a SkipError.
        """
        url = (
            "https://www.northwestknowledge.net"
            "/data/94E2D569-200F-44F7-8937-AB4BD0862C91"
        )

        # External I/O
        #
        # 1st:  landing page
        # 2nd:  XML metadata document  (raises 404)
        package = 'tests.data.nkn.0a42d2bc-700a-4cf2-a7ac-ad6b892da7f0'
        contents = [
            ir.read_binary(package, 'index.html'),
        ]

        harvester = NKNHarvester()

        with self.assertLogs(logger=harvester.logger, level='INFO'):
            with aioresponses() as m:
                m.get(self.regex, body=contents[0])
                m.get(self.regex, status=404)

                with self.assertRaises(SkipError):
                    asyncio.run(harvester.retrieve_record(url))

    @patch('schema_org.core.logging.getLogger')
    def test_unsupported_xml_format(self, mock_logger):
        """
        SCENARIO:  Sometimes the XML format is not supported.  We have tests
        for this in other places, but NKN is a special case because we have to
        extract the identifier from the XML metadata rather than the JSON-LD.

        This particular file is some sort of ESRI XML file.

        EXPECTED RESULT:  XMLValidationError
        """
        url = (
            "https://www.northwestknowledge.net"
            "/data/A62BEE88-8F92-4649-BC8D-BC56CE96AE2B"
        )

        package = 'tests.data.nkn.A62BEE88-8F92-4649-BC8D-BC56CE96AE2B'
        contents = [
            ir.read_binary(package, 'metadata.xml'),
            ir.read_binary(package, 'index.html'),
        ]

        harvester = NKNHarvester()

        with aioresponses() as m:
            m.get(self.regex, body=contents[0])
            m.get(self.regex, body=contents[1])

            with self.assertRaises(XMLValidationError):
                asyncio.run(harvester.retrieve_record(url))

    def test_missing_file_identifier(self):
        """
        SCENARIO:  The XML metadata file has an empty file identifier field.

        EXPECTED RESULT:  MissingMetadataFileIdentifierError is raised.
        """
        package = 'tests.data.nkn.60795440-42b0-4fb2-a2d4-7e7c00c66aa1'
        content = ir.read_binary(package, 'metadata.xml')
        doc = lxml.etree.parse(io.BytesIO(content))

        harvester = NKNHarvester()

        with self.assertRaises(MissingMetadataFileIdentifierError):
            harvester.extract_identifier(doc)
