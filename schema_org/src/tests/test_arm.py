# Standard library imports
import asyncio
try:
    import importlib.resources as ir
except ImportError:  # pragma:  nocover
    import importlib_resources as ir
import re
from unittest.mock import patch

# 3rd party library imports
from aioresponses import aioresponses

# local imports
from schema_org.arm import ARMHarvester
from .test_common import TestCommon


@patch('schema_org.core.logging.getLogger')
class TestSuite(TestCommon):

    def test_identifier_parsing(self, mock_logger):
        """
        SCENARIO:  The @id field from the JSON-LD must be parsed, we are
        presented with http://dx.doi.org/10.5439/1027257.

        EXPECTED RESULT:  The ID "10.5439/1027257" is returned.
        """
        jsonld = {'@id': 'http://dx.doi.org/10.5439/1027257'}
        harvester = ARMHarvester()
        identifier = harvester.extract_identifier(jsonld)

        self.assertEqual(identifier, '10.5439/1027257')

    def test_identifier_parsing_error(self, mock_logger):
        """
        SCENARIO:  The @id field from the JSON-LD must be parsed, but the given
        field is bad.

        EXPECTED RESULT:  RuntimeError and a warning is logged.
        """
        jsonld = {'@id': 'http://dx.doi.orggg/10.5439/1027257'}
        harvester = ARMHarvester()

        with self.assertRaises(RuntimeError):
            harvester.extract_identifier(jsonld)

        self.assertEqual(harvester.logger.error.call_count, 1)

    def test_bad_verbosity(self, mock_logger):
        """
        SCENARIO:  the harvester is called with a bad verbosity value.  This
        should be precluded by the command line entry point, but you never
        know.

        EXPECTED RESULT:  a TypeError is raised
        """

        with self.assertRaises(TypeError):
            ARMHarvester(verbose='WARNING2')


class TestSuite2(TestCommon):

    def setUp(self):
        self.regex = re.compile('https://www.archive.arm.gov/metadata/adc')

    @patch('schema_org.d1_client_manager.D1ClientManager.load_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.get_last_harvest_time')  # noqa: E501
    def test_default_run(self,
                         mock_harvest_time,
                         mock_check_if_identifier_exists,
                         mock_load_science_metadata):
        """
        SCENARIO:  We have a valid sitemap and valid documents.

        EXPECTED RESULT:  No errors are logged.  One record is successfully
        harvested, according to the logs.
        """

        mock_harvest_time.return_value = '1900-01-01T00:00:00Z'
        mock_check_if_identifier_exists.return_value = {'outcome': 'no'}
        mock_load_science_metadata.return_value = True

        harvester = ARMHarvester()

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1
        #   3) XML document for record 1
        #
        contents = [
            ir.read_binary('tests.data.arm', 'sitemap-1.xml'),
            ir.read_binary('tests.data.arm',
                           'nsanimfraod1michC2.c1.fixed.html'),
            ir.read_binary('tests.data.arm',
                           'nsanimfraod1michC2.c1.fixed.xml'),
        ]
        status_codes = [200, 200, 200]

        with aioresponses() as m:
            for content, status_code in zip(contents, status_codes):
                m.get(self.regex, body=content, status=status_code)

            with self.assertLogs(logger=harvester.logger, level='DEBUG') as cm:
                asyncio.run(harvester.run())

                self.assertLogLevelCallCount(cm.output, level='ERROR', n=0)
                self.assertInfoLogMessage(cm.output, 'Created 1 new record')

    @patch('schema_org.d1_client_manager.D1ClientManager.load_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.get_last_harvest_time')  # noqa: E501
    def test__last_harvest_time_gt_lastmod(self,
                                           mock_harvest_time,
                                           mock_check_if_identifier_exists,
                                           mock_load_science_metadata):
        """
        SCENARIO:  We have a valid sitemap and valid documents.  One of the
        documents, though, was harvested since it was last modified.

        EXPECTED RESULT:  No errors are logged.  A message is logged that the
        one record was skipped.
        """

        # Set the harvest time ahead of the lastmod time.  If we're still
        # running this code in the 23rd century, well dang...
        mock_harvest_time.return_value = '2200-01-01T00:00:00Z'
        mock_check_if_identifier_exists.return_value = {'outcome': 'no'}
        mock_load_science_metadata.return_value = True

        harvester = ARMHarvester(host='test.arm.gov')

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1
        #   3) XML document for record 1
        #
        contents = [
            ir.read_binary('tests.data.arm', 'sitemap-1.xml'),
            ir.read_binary('tests.data.arm',
                           'nsanimfraod1michC2.c1.fixed.html'),
            ir.read_binary('tests.data.arm',
                           'nsanimfraod1michC2.c1.fixed.xml'),
        ]
        status_codes = [200, 200, 200]
        headers = [
            {'Content-Type': 'application/xml'},
            {'Content-Type': 'application/html'},
            {'Content-Type': 'application/xml'},
        ]

        z = zip(contents, status_codes, headers)
        with aioresponses() as m:
            for content, status_code, headers in z:
                m.get(self.regex,
                      body=content, status=status_code, headers=headers)

            with self.assertLogs(logger=harvester.logger, level='DEBUG') as cm:
                asyncio.run(harvester.run())

                self.assertLogLevelCallCount(cm.output, level='ERROR', n=0)
                self.assertInfoLogMessage(cm.output, 'Created 0 new record')

                expected = '1 records skipped due to lastmod time'
                self.assertInfoLogMessage(cm.output, expected)

    @patch('schema_org.d1_client_manager.D1ClientManager.get_last_harvest_time')  # noqa: E501
    def test_metadata_document_retrieval_failure(self, mock_harvest_time):
        """
        SCENARIO:  The XML metadata document is invalid.

        EXPECTED RESULT:  The failure count goes up by one.
        """

        mock_harvest_time.return_value = '1900-01-01T00:00:00Z'

        harvester = ARMHarvester()
        failed_count = harvester.failed_count

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1
        #   3) XML document for record 1
        #
        contents = [
            ir.read_binary('tests.data.arm', 'sitemap-1.xml'),
            ir.read_binary('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.html'),  # noqa: E501
            ir.read_binary('tests.data.arm', 'nsanimfraod1michC2.c1.xml'),
        ]
        status_codes = [200, 200, 400]

        with aioresponses() as m:
            for content, status_code in zip(contents, status_codes):
                m.get(self.regex, body=content, status=status_code)

            with self.assertLogs(logger=harvester.logger, level='DEBUG') as cm:
                asyncio.run(harvester.run())

                self.assertDebugLogMessage(cm.output, 'ClientResponseError')
                self.assertErrorLogMessage(cm.output, 'Bad Request')

        self.assertEqual(harvester.failed_count, failed_count + 1)
