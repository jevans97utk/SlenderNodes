"""
Test suite for IEDA
"""

# Standard library imports
import datetime as dt
try:
    import importlib.resources as ir
except ImportError:
    import importlib_resources as ir
import json
from unittest.mock import patch

# local imports
from schema_org.ieda import IEDAHarvester
from schema_org.common import (
    UNESCAPED_DOUBLE_QUOTES_MSG, OVER_ESCAPED_DOUBLE_QUOTES_MSG,
    SITE_MAP_RETRIEVAL_FAILURE_MESSAGE
)
from .test_common import TestCommon


class TestSuite(TestCommon):

    def test_identifier_parsing(self):
        """
        SCENARIO:  The @id field from the JSON-LD must be parsed, we are
        presented with various forms out in the wild.

        EXPECTED RESULT:  the 2nd column
        """
        test_cases = [
            ("doi:10.15784/601015", "10.15784/601015"),
            (" doi:10.15784/601015", "10.15784/601015"),
            ("doi:10.15784/601015 ", "10.15784/601015"),
            ("doi:10.7265/N55D8PS0", "10.7265/N55D8PS0"),
            ("urn:usap-dc:metadata:609582", "urn:usap-dc:metadata:609582"),
        ]

        harvester = IEDAHarvester()
        for str_input, expected in test_cases:
            with self.subTest(name=expected):
                jsonld = {'@id': str_input}
                identifier = harvester.extract_identifier(jsonld)
                self.assertEqual(identifier, expected)

    def test_identifier_parsing_error(self):
        """
        SCENARIO:  The JSON-LD @id field has an unexpected identifier.

        EXPECTED RESULT:  RuntimeError
        """
        harvester = IEDAHarvester()
        with self.assertRaises(RuntimeError):
            harvester.extract_identifier({'@id': 'djlfsdljfasl;'})

    @patch('schema_org.common.logging.getLogger')
    def test_metadata_document_retrieval(self, mock_logger):
        """
        SCENARIO:  an IEDA metadata document URL is retrieved and properly
        transformed.

        EXPECTED RESULT:  A byte-stream of a valid metadata document.  The
        logger should have registered the retrieval at the INFO level.
        """
        content = ir.read_binary('tests.data.ieda', '600121iso.xml')
        self.setup_requests_session_patcher(contents=[content])

        harvester = IEDAHarvester()

        harvester.retrieve_metadata_document('http://somewhere/iso.xml')
        harvester.logger.info.assert_called_once()

    @patch('schema_org.common.logging.getLogger')
    def test_metadata_document_retrieval_httperror(self, mock_logger):
        """
        SCENARIO:  an IEDA metadata document URL retrieval results in a
        requests.HTTPError exception being raised.

        EXPECTED RESULT:  A RuntimeError is raised.
        """
        self.setup_requests_session_patcher(status_codes=[400])

        harvester = IEDAHarvester()

        with self.assertRaises(RuntimeError):
            harvester.retrieve_metadata_document('https://abc/600121iso.xml')

        self.assertEqual(harvester.logger.error.call_count, 1)

    @patch('schema_org.d1_client_manager.D1ClientManager.load_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.get_last_harvest_time')  # noqa: E501
    @patch('schema_org.common.logging.getLogger')
    def test_default_run(self, mock_logger, mock_harvest_time,
                         mock_check_if_identifier_exists,
                         mock_load_science_metadata):
        """
        SCENARIO:  Process the sitemap where all the records are newer than
        the last time that the harvester was run.

        EXPECTED RESULT:  The log record reflects the successful calls at the
        INFO level.
        """

        mock_harvest_time.return_value = '1900-01-01T00:00:00Z'
        mock_check_if_identifier_exists.return_value = {'outcome': 'no'}
        mock_load_science_metadata.return_value = True

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1
        #   3) XML document for record 1
        #   4) HTML document for record 2
        #   5) XML document for record 2
        #
        contents = [
            ir.read_binary('tests.data.ieda', 'usap_sitemap.xml'),
            ir.read_binary('tests.data.ieda', 'ieda600048.html'),
            ir.read_binary('tests.data.ieda', '600048iso.xml'),
            ir.read_binary('tests.data.ieda', 'ieda609246.html'),
            ir.read_binary('tests.data.ieda', '609246iso.xml'),
        ]
        status_codes = [200 for item in contents]
        self.setup_requests_session_patcher(contents=contents,
                                            status_codes=status_codes)

        harvester = IEDAHarvester()
        harvester.run()

        # The INFO logger is invoked with:
        #
        #   1) the last harvest time
        #   2-9) 4 calls per record (there are two records)
        #     i)  request for an HTML document
        #     ii) exposing the identifier
        #     iii) request for the XML document
        #     iv) harvesting the object
        #   10) final "updated" count
        #   11) final "skipped" count
        #   12) final "created" count
        #   13) final "unprocessed" count
        self.assertEqual(harvester.logger.info.call_count, 13)

    @patch('schema_org.d1_client_manager.D1ClientManager.load_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.get_last_harvest_time')  # noqa: E501
    @patch('schema_org.common.logging.getLogger')
    def test_default_run_with_one_retrieval_error(
        self,
        mock_logger, mock_harvest_time,
        mock_check_if_identifier_exists,
        mock_load_science_metadata
    ):
        """
        SCENARIO:  Process the sitemap where all the records are newer than
        the last time that the harvester was run.  The last ISO document
        cannot be retrieved, though.

        EXPECTED RESULT:  The log record reflects the successful calls, but
        also the XML failure.
        """

        mock_harvest_time.return_value = '1900-01-01T00:00:00Z'
        mock_check_if_identifier_exists.return_value = {'outcome': 'no'}
        mock_load_science_metadata.return_value = True

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1
        #   3) XML document for record 1
        #   4) HTML document for record 2
        #   5) XML document for record 2
        #
        contents = [
            ir.read_binary('tests.data.ieda', 'usap_sitemap.xml'),
            ir.read_binary('tests.data.ieda', 'ieda600048.html'),
            ir.read_binary('tests.data.ieda', '600048iso.xml'),
            ir.read_binary('tests.data.ieda', 'ieda609246.html'),
            None,
        ]
        status_codes = [200, 200, 200, 200, 400]
        self.setup_requests_session_patcher(contents=contents,
                                            status_codes=status_codes)

        harvester = IEDAHarvester()
        harvester.run()

        # The INFO logger is invoked with:
        #
        #   1) the last harvest time
        #   2-5) 4 calls per record (there are two records)
        #     i)  request for an HTML document
        #     ii) exposing the identifier
        #     iii) request for the XML document
        #     iv) harvesting the object
        #   6-8) 3 calls for the 2nd document items
        #     i)  request for an HTML document
        #     ii) exposing the identifier
        #     iii) request for the XML document
        #   9) final "updated" count
        #   10) final "skipped" count
        #   11) final "created" count
        #   12) final "unprocessed" count
        #
        # But there is one error call for the unretrieved XML document.
        self.assertEqual(harvester.logger.info.call_count, 12)
        self.assertEqual(harvester.logger.error.call_count, 1)

    @patch('schema_org.common.logging.getLogger')
    def test_ieda_600165_unescaped_double_quotes(self, mock_logger):
        """
        SCENARIO:  The HTML file has invalid JSONLD embedded in its SCRIPT.
        Two description fields have unescaped double-quotes.

        EXPECTED RESULT:  A valid JSON document is returned, but the original
        json.decoder.JSONDecodeError is logged at the error level.  The JSONLD
        fix is logged at the warning level.
        """
        harvester = IEDAHarvester()
        text = ir.read_text('tests.data.ieda', '600165.html')

        doc = harvester.extract_jsonld(text)

        harvester.logger.error.assert_called_once()
        harvester.logger.warning.assert_called_with(UNESCAPED_DOUBLE_QUOTES_MSG)  # noqa: E501
        self.assertEqual(harvester.logger.warning.call_count, 2)

        # The document is only None if there was an exception.
        self.assertIsNotNone(doc)
        json.dumps(doc)

    @patch('schema_org.common.logging.getLogger')
    def test_truncated(self, mock_logger):
        """
        SCENARIO:  The HTML file has invalid JSONLD embedded in its SCRIPT.
        The JSON is truncated, which cannot be fixed.

        EXPECTED RESULT:  The unrecoverable error is recorded via the error
        interface.  An exception is raised.
        """
        harvester = IEDAHarvester()
        text = ir.read_text('tests.data.ieda', '601015-truncated.html')

        with self.assertRaises(RuntimeError):
            harvester.extract_jsonld(text)
        harvester.logger.error.assert_called()

    @patch('schema_org.common.logging.getLogger')
    def test_ieda_601015_over_escaped_double_quotes(self, mock_logger):
        """
        SCENARIO:  The HTML file has invalid JSONLD embedded in its SCRIPT.
        Two different description field have over-escaped double quotes.

        EXPECTED RESULT:  A valid JSON document is returned, but the
        original json.decoder.JSONDecodeError is logged at the error
        level, as well as the fix that is logged at the warning level.
        """
        harvester = IEDAHarvester()
        text = ir.read_text('tests.data.ieda', '601015.html')

        doc = harvester.extract_jsonld(text)

        self.assertEqual(harvester.logger.error.call_count, 1)
        harvester.logger.warning.assert_called_with(OVER_ESCAPED_DOUBLE_QUOTES_MSG)  # noqa: E501

        # The document is valid JSON
        self.assertIsNotNone(doc)
        json.dumps(doc)

    @patch('schema_org.common.logging.getLogger')
    def test_site_map_retrieval_failure(self, mock_logger):
        """
        SCENARIO:  a non-200 status code is returned by the site map retrieval.

        EXPECTED RESULT:  the exception is logged.
        """
        self.setup_requests_session_patcher(status_codes=[500])
        harvester = IEDAHarvester()
        harvester.get_site_map()
        harvester.logger.error.assert_any_call(SITE_MAP_RETRIEVAL_FAILURE_MESSAGE)  # noqa: E501

    @patch('schema_org.d1_client_manager.D1ClientManager.update_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.common.logging.getLogger')
    def test_document_already_harvested_but_can_be_successfully_updated(
        self,
        mock_logger,
        mock_check_if_identifier_exists,
        mock_update_science_metadata
    ):
        """
        SCENARIO:  The GMN existance check shows that the document has already
        been harvested.  It has been updated since the last harvest time, and
        the update succeeds.

        EXPECTED RESULT:  The event is logged at the info level.  The update
        count increases by one.
        """
        record_date = dt.datetime.now()
        mock_check_if_identifier_exists.return_value = {
            'outcome': 'yes',
            'record_date': record_date - dt.timedelta(days=1),
            'current_version_id': 1,
        }
        mock_update_science_metadata.return_value = True

        harvester = IEDAHarvester()
        update_count = harvester.updated_count

        doc = ir.read_binary('tests.data.ieda', '600121iso.xml')

        identifier = 'doi.10000/abcde'
        harvester.harvest_document(identifier, doc, record_date)

        harvester.logger.info.assert_called_once()
        self.assertEqual(harvester.updated_count, update_count + 1)

    @patch('schema_org.d1_client_manager.D1ClientManager.update_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.common.logging.getLogger')
    def test_document_already_harvested_but_cannot_be_updated(
        self,
        mock_logger,
        mock_check_if_identifier_exists,
        mock_update_science_metadata
    ):
        """
        SCENARIO:  The GMN existance check shows that the document has already
        been harvested.  It has been updated since the last harvest time, but
        the update failed.

        EXPECTED RESULT:  The event is logged at the warning level.
        """
        record_date = dt.datetime.now()
        mock_check_if_identifier_exists.return_value = {
            'outcome': 'yes',
            'record_date': record_date - dt.timedelta(days=1),
            'current_version_id': 1,
        }
        mock_update_science_metadata.return_value = False

        harvester = IEDAHarvester()
        doc = ir.read_binary('tests.data.ieda', '600121iso.xml')

        identifier = 'doi.10000/abcde'
        harvester.harvest_document(identifier, doc, record_date)

        harvester.logger.warning.assert_called_once()

    @patch('schema_org.d1_client_manager.D1ClientManager.update_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.common.logging.getLogger')
    def test_document_already_harvested_at_same_date(
        self,
        mock_logger,
        mock_check_if_identifier_exists,
        mock_update_science_metadata
    ):
        """
        SCENARIO:  The GMN existance check shows that the document has already
        been harvested and has not changed since the last time.

        EXPECTED RESULT:  The event is logged at the info level.  The skipped
        count goes up by one.
        """
        record_date = dt.datetime.now()
        mock_check_if_identifier_exists.return_value = {
            'outcome': 'yes',
            'record_date': record_date,
        }
        mock_update_science_metadata.return_value = False

        harvester = IEDAHarvester()
        skipped_count = harvester.skipped_exists_count
        doc = ir.read_binary('tests.data.ieda', '600121iso.xml')

        identifier = 'doi.10000/abcde'
        harvester.harvest_document(identifier, doc, record_date)

        harvester.logger.info.assert_called_once()
        self.assertEqual(harvester.skipped_exists_count, skipped_count + 1)

    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.common.logging.getLogger')
    def test_document_check_fails(
        self,
        mock_logger,
        mock_check_if_identifier_exists
    ):
        """
        SCENARIO:  The GMN existance check fails for some reason.

        EXPECTED RESULT:  The event is logged at the warning level.
        """
        mock_check_if_identifier_exists.return_value = {
            'outcome': 'failed',
        }

        harvester = IEDAHarvester()
        doc = ir.read_binary('tests.data.ieda', '600121iso.xml')
        record_date = dt.datetime.now()

        identifier = 'doi.10000/abcde'
        harvester.harvest_document(identifier, doc, record_date)

        harvester.logger.warning.assert_called_once()

    @patch('schema_org.d1_client_manager.D1ClientManager.load_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.common.logging.getLogger')
    def test_document_is_unrecognized_but_successfully_harvested(
        self,
        mock_logger,
        mock_check_if_identifier_exists,
        mock_load_science_metadata
    ):
        """
        SCENARIO:  The GMN has not seen the document before and is successfully
        harvested.

        EXPECTED RESULT:  The event is logged at the info level.  The
        "created_count" goes up by one.
        """
        mock_check_if_identifier_exists.return_value = {'outcome': 'no'}
        mock_load_science_metadata.return_value = True

        harvester = IEDAHarvester()
        doc = ir.read_binary('tests.data.ieda', '600121iso.xml')

        harvester.harvest_document('doi.10000/abcde', doc, dt.datetime.now())

        self.assertEqual(harvester.created_count, 1)
        harvester.logger.info.assert_called_once()

    @patch('schema_org.d1_client_manager.D1ClientManager.load_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.common.logging.getLogger')
    def test_document_is_unrecognized_but_cannot_be_harvested(
        self,
        mock_logger,
        mock_check_if_identifier_exists,
        mock_load_science_metadata
    ):
        """
        SCENARIO:  The GMN has not seen the document before, but still cannot
        harvest the document for some reason.

        EXPECTED RESULT:  The issue is logged at the error level.
        """
        mock_check_if_identifier_exists.return_value = {'outcome': 'no'}
        mock_load_science_metadata.return_value = False

        harvester = IEDAHarvester()
        doc = ir.read_binary('tests.data.ieda', '600121iso.xml')

        harvester.harvest_document('doi.10000/abcde', doc, dt.datetime.now())

        harvester.logger.error.assert_called_once()
