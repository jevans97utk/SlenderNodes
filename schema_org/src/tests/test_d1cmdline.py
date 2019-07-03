# standard library imports
import importlib.resources as ir
import sys
from unittest.mock import patch

# 3rd party library imports
import lxml.etree
import requests

# local imports
import schema_org.commandline as commandline
from schema_org import D1TestTool
from .test_common import TestCommon


@patch('schema_org.common.logging.getLogger')
class TestSuite(TestCommon):

    @patch.object(sys, 'argv', ['', 'http://www.acme.org/nositemap.xml'])
    def test_no_site_map(self, mock_logger):
        """
        SCENARIO:  The given URL for the sitemap does not seem to exist.

        EXPECTED RESULT:  A requests.HTTPError is raised.
        """
        self.setup_requests_session_patcher(status_codes=[400])

        with self.assertRaises(requests.HTTPError):
            commandline.d1_check_site()

    def test_site_map_is_not_xml(self, mock_logger):
        """
        SCENARIO:  The sitemap document is not XML.

        EXPECTED RESULT:  There is a warning stating that the URL may not be
        XML, plus an XMLSyntaxError is raised.
        """
        content = ir.read_binary('tests.data.arm', 'sitemap.txt')

        contents = [content]
        headers = [{'Content-Type': 'text/plain'}]

        self.setup_requests_session_patcher(contents=contents, headers=headers)

        o = D1TestTool(sitemap_url='http://www.archive.arm.org/sitemap.txt')
        with self.assertRaises(lxml.etree.XMLSyntaxError):
            o.run()

        self.assertEqual(o.logger.warning.call_count, 1)
