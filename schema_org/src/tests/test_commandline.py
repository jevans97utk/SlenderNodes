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

    @patch.object(sys, 'argv', ['', 'tests/ieda/600121iso.xml'])
    @patch('schema_org.commandline.XMLValidator.validate')
    @patch('schema_org.commandline.asyncio')
    def test_validator(self, mock_asyncio, mock_validator):
        """
        SCENARIO:  Run with no command line arguments.

        EXPECTED RESULT:  The run method was called.
        """
        commandline.validate()

        self.assertEqual(mock_validator.call_count, 1)
