"""
Test suite for command line tools.
"""

# Standard library imports
import sys
from unittest.mock import patch

# Local imports
from schema_org import commandline
from .test_common import TestCommon


class TestSuite(TestCommon):

    @patch.object(sys, 'argv', [''])
    @patch('schema_org.commandline.IEDAHarvester.run')
    @patch('schema_org.commandline.asyncio')
    def test_ieda(self, mock_asyncio, mock_ieda):
        """
        SCENARIO:  Run with no command line arguments.

        EXPECTED RESULT:  The run method was called.
        """
        commandline.ieda()

        self.assertEqual(mock_ieda.call_count, 1)

    @patch.object(sys, 'argv', [''])
    @patch('schema_org.commandline.ARMHarvester.run')
    @patch('schema_org.commandline.asyncio')
    def test_arm(self, mock_asyncio, mock_arm):
        """
        SCENARIO:  Run with no command line arguments.

        EXPECTED RESULT:  The run method was called.
        """
        commandline.arm()

        self.assertEqual(mock_arm.call_count, 1)

    @patch.object(sys, 'argv', [
        '', 'https://www.archive.arm.gov/metadata/adc/sitemap.xml'
    ])
    @patch('schema_org.commandline.D1TestToolAsync.run')
    @patch('schema_org.commandline.asyncio')
    def test_sitemap_validator(self, mock_asyncio, mock_validator):
        """
        SCENARIO:  Run the sitemap validator with a single URL for a positional
        argument.

        EXPECTED RESULT:  The validator method was called.
        """
        commandline.d1_check_site()

        self.assertEqual(mock_validator.call_count, 1)

    @patch.object(sys, 'argv', ['', 'tests/data/ieda/600121iso.xml'])
    @patch('schema_org.commandline.XMLValidator.validate')
    @patch('schema_org.commandline.asyncio')
    def test_xml_validator(self, mock_asyncio, mock_validator):
        """
        SCENARIO:  Run the XML Validator with a single file for a positional
        argument.

        EXPECTED RESULT:  The validator method was called.
        """
        commandline.validate()

        self.assertEqual(mock_validator.call_count, 1)

    @patch('schema_org.html.logging.getLogger')
    @patch.object(sys, 'argv', [
        '', 'tests/data/arm/nsanimfraod1michC2.c1.html'
    ])
    def test_local_html_validator(self, mock_logger):
        """
        SCENARIO:  Run the local HTML validator with a single file for a
        positional argument.  That HTML file has an incorrect @type key in the
        JSON-LD.

        EXPECTED RESULT:  A RuntimeError is issued.
        """
        with self.assertRaises(RuntimeError):
            commandline.d1_check_html()
