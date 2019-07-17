"""
Test suite for IEDA
"""

# Standard library imports
import asyncio
import datetime as dt
try:
    import importlib.resources as ir
except ImportError:  # pragma:  nocover
    import importlib_resources as ir
import io
import json
import re
from unittest.mock import patch

# 3rd party library imports
import aiohttp
from aioresponses import aioresponses
import dateutil.parser
import lxml.etree
import requests_mock

# local imports
from schema_org.ieda import IEDAHarvester
from schema_org.common import (
    UNESCAPED_DOUBLE_QUOTES_MSG, OVER_ESCAPED_DOUBLE_QUOTES_MSG,
    SITEMAP_RETRIEVAL_FAILURE_MESSAGE, run_harvester
)
from .test_common import TestCommon


class TestSuite(TestCommon):
    """
    Attributes
    ----------
    adapter : obj
        This intercepts all the outgoing HTTP requests
    pattern : str
        Match any URLs going to that site, we will catch them with
        aioresponses.
    """

    def setUp(self):
        """
        Attributes
        ----------
        regex : obj
            Any URL that matches this should have its request intercepted
            by the mocking layer.
        xml_hdr, html_hdr : dicts
            Headers that the requests/aiohttp layer should send back.
        """

        self.adapter = requests_mock.Adapter()
        self.protocol = 'http'

        self.regex = re.compile('http://get.iedadata.org/.*')

        self.xml_hdr = {'Content-Type': 'text/xml'}
        self.html_hdr = {'Content-Type': 'text/html'}

    async def run_harvest(self, harvester, identifier, doc, record_date):
        """
        Helper routine to allow us to isolate the harvest_document method.
        """
        await harvester._async_finish_init()
        await harvester.harvest_document(identifier, doc, record_date)
        await harvester._async_close()

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

    @patch('schema_org.common.logging.getLogger')
    def test_identifier_parsing_error(self, mock_logger):
        """
        SCENARIO:  The JSON-LD @id field has an invalid identifier.

        EXPECTED RESULT:  A RuntimeError is raised.
        """
        harvester = IEDAHarvester()

        with self.assertRaises(RuntimeError):
            harvester.extract_identifier({'@id': 'djlfsdljfasl;'})

    @patch('schema_org.common.logging.getLogger')
    def test_restrict_to_2_items_from_sitemap(self, mock_logger):
        """
        SCENARIO:  The sitemap lists 3 documents, but we have specified that
        only 2 are to be processed.

        EXPECTED RESULT:  The list of documents retrieve has length 2.
        """

        harvester = IEDAHarvester(num_documents=2)

        content = ir.read_binary('tests.data.ieda', 'sitemap3.xml')
        doc = lxml.etree.parse(io.BytesIO(content))
        last_harvest = dateutil.parser.parse('1900-01-01T00:00:00Z')

        records = harvester.extract_records_from_sitemap(doc, last_harvest)
        self.assertEqual(len(records), 2)

    @patch('schema_org.common.logging.getLogger')
    def test_sitemap_num_docs_restriction_does_not_apply(self, mock_logger):
        """
        SCENARIO:  The sitemap lists 3 documents, but we have specified that
        4 are to be processed.

        EXPECTED RESULT:  The list of documents retrieve has length 3.  The
        setting of 4 has no effect.
        """

        harvester = IEDAHarvester(num_documents=4)

        content = ir.read_binary('tests.data.ieda', 'sitemap3.xml')
        doc = lxml.etree.parse(io.BytesIO(content))
        last_harvest = dateutil.parser.parse('1900-01-01T00:00:00Z')

        records = harvester.extract_records_from_sitemap(doc, last_harvest)
        self.assertEqual(len(records), 3)

    def test_metadata_document_retrieval(self):
        """
        SCENARIO:  an IEDA metadata document URL is retrieved and properly
        transformed.

        EXPECTED RESULT:  A byte-stream of a valid metadata document.  There
        are no ERROR or WARNING messages logged.
        """

        url = 'http://get.iedadata.org/600121iso.xml'
        harvester = IEDAHarvester()

        async def runme(harvester, url):
            await harvester._async_finish_init()
            resp = await harvester.retrieve_metadata_document(url)
            await harvester._async_close()
            return resp

        content = ir.read_binary('tests.data.ieda', '600121iso.xml')
        with self.assertLogs(logger=harvester.logger, level='DEBUG') as cm:
            with aioresponses() as m:
                m.get(self.regex, body=content)
                doc1 = asyncio.run(runme(harvester, url))

            self.assertLogLevelCallCount(cm.output, level='ERROR', n=0)
            self.assertLogLevelCallCount(cm.output, level='WARNING', n=0)

        doc2 = lxml.etree.parse(io.BytesIO(content))
        self.assertEqual(lxml.etree.tostring(doc1), lxml.etree.tostring(doc2))

    @patch('schema_org.common.logging.getLogger')
    def test_metadata_document_retrieval_httperror(self, log_mocker):
        """
        SCENARIO:  an IEDA metadata document URL retrieval results in a
        requests.HTTPError exception being raised.

        EXPECTED RESULT:  An HTTPError is raised.
        """
        harvester = IEDAHarvester()
        asyncio.run(harvester._async_finish_init())

        url = 'http://get.iedadata.org/600121iso.xml'

        with self.assertRaises(aiohttp.client_exceptions.ClientResponseError):
            with aioresponses() as m:
                m.get(url, status=400)
                asyncio.run(harvester.retrieve_metadata_document(url))

    @patch('schema_org.d1_client_manager.D1ClientManager.load_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.get_last_harvest_time')  # noqa: E501
    def test_default_run(self, mock_harvest_time,
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

        harvester = IEDAHarvester()

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
        headers = [
            {'Content-Type': 'text/xml'},
            {'Content-Type': 'text/html'},
            {'Content-Type': 'text/xml'},
            {'Content-Type': 'text/html'},
            {'Content-Type': 'text/xml'},
        ]
        with aioresponses() as m:
            for content, headers in zip(contents, headers):
                m.get(self.regex, body=content, headers=headers)

            with self.assertLogs(logger=harvester.logger, level='DEBUG') as cm:
                asyncio.run(run_harvester(harvester))

                # There should be lots of log messages at the info level, but
                # none at the warning or error level.
                self.assertLogLevelCallCount(cm.output, level='WARNING', n=0)
                self.assertLogLevelCallCount(cm.output, level='ERROR', n=0)

                log_message = 'Created 2 new records'
                self.assertLogMessage(cm.output, log_message, level='INFO')

    @patch('schema_org.d1_client_manager.D1ClientManager.load_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.get_last_harvest_time')  # noqa: E501
    def test_default_run_with_one_retrieval_error(
        self,
        mock_harvest_time,
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

        harvester = IEDAHarvester(verbosity='DEBUG')

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
            ir.read_binary('tests.data.ieda', 'ieda609246.html'),
            ir.read_binary('tests.data.ieda', '609246iso.xml'),
            ir.read_binary('tests.data.ieda', 'ieda600048.html'),
            b'',
        ]

        with aioresponses() as m:
            m.get(self.regex, body=contents[0], headers=self.xml_hdr)
            m.get(self.regex, body=contents[1], headers=self.html_hdr)
            m.get(self.regex, body=contents[2], headers=self.xml_hdr)
            m.get(self.regex, body=contents[3], headers=self.html_hdr)
            m.get(self.regex, status=400, headers=self.xml_hdr)

            with self.assertLogs(logger=harvester.logger, level='DEBUG') as cm:
                asyncio.run(run_harvester(harvester))

                self.assertSuccessfulIngest(cm.output, n=1)
                self.assertLogLevelCallCount(cm.output, level='ERROR', n=1)
                self.assertLogMessage(cm.output, 'ClientResponseError')

    def test_ieda_600165_unescaped_double_quotes(self):
        """
        SCENARIO:  The HTML file has invalid JSONLD embedded in its SCRIPT.
        Two description fields have unescaped double-quotes.

        EXPECTED RESULT:  A valid JSON document is returned, but the original
        json.decoder.JSONDecodeError is logged at the warning level.  The
        JSONLD fix is also logged at the warning level.
        """
        harvester = IEDAHarvester()

        text = ir.read_text('tests.data.ieda', '600165.html')
        doc = lxml.etree.HTML(text)

        with self.assertLogs(logger=harvester.logger, level='WARNING') as cm:
            j = harvester.extract_jsonld(doc)

            # Two log messages, both of them warnings.
            self.assertEqual(len(cm.output), 3)
            self.assertTrue(cm.output[0].startswith('WARNING'))
            self.assertTrue(cm.output[1].startswith('WARNING'))
            self.assertTrue(cm.output[2].startswith('WARNING'))

            # The first message is the initial failure to decode the JSON.
            self.assertIn('JSONDecodeError', cm.output[0])

            # The second and 3rd messages are notices of the fix.
            self.assertIn(UNESCAPED_DOUBLE_QUOTES_MSG, cm.output[1])
            self.assertIn(UNESCAPED_DOUBLE_QUOTES_MSG, cm.output[2])

        # The document is only None if there was an exception.
        self.assertIsNotNone(j)
        json.dumps(j)

    @patch('schema_org.common.logging.getLogger')
    def test_truncated(self, mock_logger):
        """
        SCENARIO:  The HTML file has invalid JSONLD embedded in its SCRIPT.
        The JSON is truncated, which cannot be fixed.

        EXPECTED RESULT:  An exception is raised.
        """
        harvester = IEDAHarvester()
        text = ir.read_text('tests.data.ieda', '601015-truncated.html')
        doc = lxml.etree.HTML(text)

        with self.assertRaises(RuntimeError):
            harvester.extract_jsonld(doc)

    def test_ieda_601015_over_escaped_double_quotes(self):
        """
        SCENARIO:  The HTML file has invalid JSONLD embedded in its SCRIPT.
        Two different description field have over-escaped double quotes.

        EXPECTED RESULT:  A valid JSON document is returned, but the
        original json.decoder.JSONDecodeError message is logged at the warning
        level, as well as the fix that is also logged at the warning level.
        """
        harvester = IEDAHarvester()
        text = ir.read_text('tests.data.ieda', '601015.html')
        doc = lxml.etree.HTML(text)

        with self.assertLogs(logger=harvester.logger, level='WARNING') as cm:
            j = harvester.extract_jsonld(doc)

            # Two log messages, both of them warnings.
            self.assertEqual(len(cm.output), 2)
            self.assertTrue(cm.output[0].startswith('WARNING'))
            self.assertTrue(cm.output[1].startswith('WARNING'))

            # The first message is the initial failure to decode the JSON.
            self.assertIn('JSONDecodeError', cm.output[0])

            # The second message is notice of the fix.
            self.assertIn(OVER_ESCAPED_DOUBLE_QUOTES_MSG, cm.output[1])

        # The document is valid JSON
        self.assertIsNotNone(j)
        json.dumps(j)

    @aioresponses()
    def test_site_map_retrieval_failure(self, aioresp_mocker):
        """
        SCENARIO:  a non-200 status code is returned by the site map retrieval.

        EXPECTED RESULT:  A requests HTTPError is raised and the exception is
        logged.
        """
        harvester = IEDAHarvester()

        aioresp_mocker.get(self.regex, status=500)

        with self.assertLogs(logger=harvester.logger, level='INFO') as cm:
            asyncio.run(run_harvester(harvester))

            self.assertLogMessage(cm.output, SITEMAP_RETRIEVAL_FAILURE_MESSAGE)

    @patch('schema_org.d1_client_manager.D1ClientManager.update_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    def test_document_already_harvested_but_can_be_successfully_updated(
        self,
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
        host, port = 'ieda.mn.org', 443
        harvester = IEDAHarvester(host=host, port=port)

        # This is the existing document in the MN.  It is marked as complete.
        existing_content = ir.read_binary('tests.data.ieda', '600121iso.xml')

        record_date = dt.datetime.now()
        mock_check_if_identifier_exists.return_value = {
            'outcome': 'yes',
            'record_date': record_date - dt.timedelta(days=1),
            'current_version_id': 1,
        }
        mock_update_science_metadata.return_value = True

        harvester = IEDAHarvester(host=host, port=port)
        update_count = harvester.updated_count

        # This is the "update" document, same as the existing document.  It is
        # already marked as "complete".  Bump the timestamp to just a bit later
        # to make ok to proceed.
        docbytes = ir.read_binary('tests.data.ieda', '600121iso-later.xml')
        doc = lxml.etree.parse(io.BytesIO(docbytes))
        doi = 'doi.10000/abcde'

        regex = re.compile('https://ieda.mn.org:443/')
        with self.assertLogs(logger=harvester.logger, level='DEBUG') as cm:
            with aioresponses() as m:
                m.get(regex, body=existing_content)
                asyncio.run(self.run_harvest(harvester, doi, doc, record_date))

            # Did we see a warning?
            self.assertLogLevelCallCount(cm.output, level='INFO', n=1)

            # Did we increase the update count?
            self.assertEqual(harvester.updated_count, update_count + 1)

    @patch('schema_org.d1_client_manager.D1ClientManager.update_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    def test_document_already_harvested_but_fails_to_update(
        self,
        mock_check_if_identifier_exists,
        mock_update_science_metadata
    ):
        """
        SCENARIO:  The GMN existance check shows that the document has already
        been harvested.  It has been updated since the last harvest time, but
        the update failed.

        EXPECTED RESULT:  The failure count goes up by one and the event is
        logged at the warning level.
        """
        host, port = 'ieda.mn.org', 443
        harvester = IEDAHarvester(host=host, port=port)

        # This is the existing document in the MN.  It is requested by the
        # update check, and it is marked as complete.
        existing_content = ir.read_binary('tests.data.ieda', '600121iso.xml')

        record_date = dt.datetime.now()
        mock_check_if_identifier_exists.return_value = {
            'outcome': 'yes',
            'record_date': record_date - dt.timedelta(days=1),
            'current_version_id': 1,
        }
        mock_update_science_metadata.return_value = False

        harvester = IEDAHarvester(host=host, port=port)
        initial_failed_count = harvester.failed_count

        # Read a document that is the same except it has a later metadata
        # timestamp.  This means that we should update it.
        doc_bytes = ir.read_binary('tests.data.ieda', '600121iso-later.xml')
        doc = lxml.etree.parse(io.BytesIO(doc_bytes))

        doi = 'doi.10000/abcde'

        regex = re.compile('https://ieda.mn.org:443/')
        with self.assertLogs(logger=harvester.logger, level='DEBUG') as cm:
            with aioresponses() as m:
                m.get(regex, body=existing_content)
                asyncio.run(self.run_harvest(harvester, doi, doc, record_date))

            # Did we see a warning?
            self.assertLogLevelCallCount(cm.output, level='WARNING', n=1)

            # Did we increase the failure count?
            self.assertEqual(harvester.failed_count, initial_failed_count + 1)

    @patch('schema_org.d1_client_manager.D1ClientManager.update_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.common.logging.getLogger')
    def test_document_already_harvested__followup_record_is_complete(
        self,
        mock_logger,
        mock_check_if_identifier_exists,
        mock_update_science_metadata
    ):
        """
        SCENARIO:  The GMN existance check shows that the document has already
        been harvested but has been marked as "ongoing".  It has been updated
        since the last harvest time, and the new record is marked as
        "complete".  The update succeeds.

        EXPECTED RESULT:  The updated count goes up by one and the event is
        logged at the info level.
        """
        # This is the existing document in the MN.  It is requested by the
        # update check, and it is marked as ongoing.
        existing_content = ir.read_binary('tests.data.ieda',
                                          '600121iso-ongoing.xml')

        # This is the proposed update document that is the same except it is
        # marked as complete.
        update_doc_bytes = ir.read_binary('tests.data.ieda', '600121iso.xml')
        doc = lxml.etree.parse(io.BytesIO(update_doc_bytes))

        record_date = dt.datetime.now()
        mock_check_if_identifier_exists.return_value = {
            'outcome': 'yes',
            'record_date': record_date - dt.timedelta(days=1),
            'current_version_id': 1,
        }
        mock_update_science_metadata.return_value = True

        host, port = 'ieda.mn.org', 443
        harvester = IEDAHarvester(host=host, port=port)
        initial_updated_count = harvester.updated_count

        doi = 'doi.10000/abcde'

        regex = re.compile('https://ieda.mn.org:443/')
        with aioresponses() as m:
            m.get(regex, body=existing_content)
            asyncio.run(self.run_harvest(harvester, doi, doc, record_date))

        # Did we increase the failure count?
        self.assertEqual(harvester.updated_count, initial_updated_count + 1)

        # Did we see a warning?
        self.assertTrue(harvester.logger.info.call_count > 0)

    @patch('schema_org.d1_client_manager.D1ClientManager.update_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    def test_document_already_harvested__followup_record_is_too_old(
        self,
        mock_check_if_identifier_exists,
        mock_update_science_metadata
    ):
        """
        SCENARIO:  The GMN existance check shows that the document has already
        been harvested.  It has been updated since the last harvest time, but
        the proposed update record is even older than the original.

        EXPECTED RESULT:  The rejected count goes up by one and the event is
        logged at the warning level.
        """
        # This is the existing document in the MN.  It is requested by the
        # update check, and it is marked as complete.
        existing_content = ir.read_binary('tests.data.ieda', '600121iso.xml')

        record_date = dt.datetime.now()
        mock_check_if_identifier_exists.return_value = {
            'outcome': 'yes',
            'record_date': record_date - dt.timedelta(days=1),
            'current_version_id': 1,
        }
        mock_update_science_metadata.return_value = False

        host, port = 'ieda.mn.org', 443
        harvester = IEDAHarvester(host=host, port=port)

        initial_rejected_count = harvester.rejected_count

        # Read a document that is the same except it has an earlier metadata
        # timestamp.  This means that we should NOT update it.
        doc_bytes = ir.read_binary('tests.data.ieda', '600121iso-earlier.xml')
        doc = lxml.etree.parse(io.BytesIO(doc_bytes))

        doi = 'doi.10000/abcde'

        regex = re.compile('https://ieda.mn.org:443/')
        with self.assertLogs(logger=harvester.logger, level='DEBUG') as cm:
            with aioresponses() as m:
                m.get(regex, body=existing_content)
                asyncio.run(self.run_harvest(harvester, doi, doc, record_date))

            # Did we see a warning?
            self.assertLogLevelCallCount(cm.output, level='WARNING', n=2)

        # Did we increase the failure count?
        self.assertEqual(harvester.rejected_count, initial_rejected_count + 1)

    @patch('schema_org.d1_client_manager.D1ClientManager.update_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    def test_document_already_harvested_at_same_date(
        self,
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
        docbytes = ir.read_binary('tests.data.ieda', '600121iso.xml')
        doc = lxml.etree.parse(io.BytesIO(docbytes))

        doi = 'doi.10000/abcde'

        with self.assertLogs(logger=harvester.logger, level='DEBUG') as cm:
            asyncio.run(self.run_harvest(harvester, doi, doc, record_date))

            # Did we see a warning?
            self.assertLogLevelCallCount(cm.output, level='INFO', n=1)

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
        docbytes = ir.read_binary('tests.data.ieda', '600121iso.xml')
        doc = lxml.etree.parse(io.BytesIO(docbytes))

        record_date = dt.datetime.now()

        asyncio.run(self.run_harvest(harvester,
                                     'doi.10000/abcde',
                                     doc,
                                     record_date))

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
        docbytes = ir.read_binary('tests.data.ieda', '600121iso.xml')
        doc = lxml.etree.parse(io.BytesIO(docbytes))

        asyncio.run(self.run_harvest(harvester,
                                     'doi.10000/abcde',
                                     doc,
                                     dt.datetime.now()))

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
        docbytes = ir.read_binary('tests.data.ieda', '600121iso.xml')
        doc = lxml.etree.parse(io.BytesIO(docbytes))

        asyncio.run(self.run_harvest(harvester,
                                     'doi.10000/abcde',
                                     doc,
                                     dt.datetime.now()))

        harvester.logger.error.assert_called_once()
