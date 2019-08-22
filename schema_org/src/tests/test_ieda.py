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
from schema_org.core import SITEMAP_RETRIEVAL_FAILURE_MESSAGE
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

    def test_identifier_parsing_error__space(self):
        """
        SCENARIO:  The @id field from the JSON-LD must be parsed, there is a
        space in the @id entry.

        EXPECTED RESULT:  RuntimeError
        """
        harvester = IEDAHarvester()
        jsonld = {'@id': " doi:10.15784/601015"}
        with self.assertRaises(RuntimeError):
            harvester.extract_identifier(jsonld)

    @patch('schema_org.core.logging.getLogger')
    def test_identifier_parsing_error(self, mock_logger):
        """
        SCENARIO:  The JSON-LD @id field has an invalid identifier.

        EXPECTED RESULT:  A RuntimeError is raised.
        """
        harvester = IEDAHarvester()

        with self.assertRaises(RuntimeError):
            harvester.extract_identifier({'@id': 'djlfsdljfasl;'})
            "urn:usap-dc:metadata:609582",

    @patch('schema_org.core.logging.getLogger')
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

    @patch('schema_org.core.logging.getLogger')
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

        content = ir.read_binary('tests.data.ieda', '600121iso.xml')
        with self.assertLogs(logger=harvester.logger, level='DEBUG') as cm:
            with aioresponses() as m:
                m.get(self.regex, body=content)
                doc1 = asyncio.run(harvester.retrieve_metadata_document(url))

            self.assertLogLevelCallCount(cm.output, level='ERROR', n=0)
            self.assertLogLevelCallCount(cm.output, level='WARNING', n=0)

        doc2 = lxml.etree.parse(io.BytesIO(content))
        self.assertEqual(lxml.etree.tostring(doc1), lxml.etree.tostring(doc2))

    @patch('schema_org.core.logging.getLogger')
    def test_metadata_document_retrieval_httperror(self, log_mocker):
        """
        SCENARIO:  an IEDA metadata document URL retrieval results in a
        requests.HTTPError exception being raised.

        EXPECTED RESULT:  An HTTPError is raised.
        """
        harvester = IEDAHarvester()

        url = 'http://get.iedadata.org/600121iso.xml'

        with self.assertRaises(aiohttp.client_exceptions.ClientResponseError):
            with aioresponses() as m:
                m.get(url, status=400)
                asyncio.run(harvester.retrieve_metadata_document(url))

    def test_ieda_600165_unescaped_double_quotes(self):
        """
        SCENARIO:  The HTML file has invalid JSONLD embedded in its SCRIPT.
        Two description fields have unescaped double-quotes.

        EXPECTED RESULT:  An exception is issued.
        """
        harvester = IEDAHarvester()

        text = ir.read_text('tests.data.ieda', '600165.fixed.html')
        doc = lxml.etree.HTML(text)

        with self.assertRaises(json.decoder.JSONDecodeError):
            harvester.extract_jsonld(doc)

    @patch('schema_org.core.logging.getLogger')
    def test_truncated(self, mock_logger):
        """
        SCENARIO:  The HTML file has invalid JSONLD embedded in its SCRIPT.
        The JSON is truncated, which cannot be fixed.

        EXPECTED RESULT:  An exception is raised.
        """
        harvester = IEDAHarvester()
        text = ir.read_text('tests.data.ieda', '601015-truncated.html')
        doc = lxml.etree.HTML(text)

        with self.assertRaises(json.decoder.JSONDecodeError):
            harvester.extract_jsonld(doc)

    def test_ieda_601015_over_escaped_double_quotes(self):
        """
        SCENARIO:  The HTML file has invalid JSONLD embedded in its SCRIPT.
        Two different description field have over-escaped double quotes.

        EXPECTED RESULT:  An exception is issued.
        """
        harvester = IEDAHarvester()
        text = ir.read_text('tests.data.ieda', '601015.fixed.html')
        doc = lxml.etree.HTML(text)

        with self.assertRaises(json.decoder.JSONDecodeError):
            harvester.extract_jsonld(doc)

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
            asyncio.run(harvester.run())

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
                asyncio.run(harvester.harvest_document(doi, doc, record_date))

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
                asyncio.run(harvester.harvest_document(doi, doc, record_date))

            # Did we see a warning?
            self.assertLogLevelCallCount(cm.output, level='WARNING', n=1)

            # Did we increase the failure count?
            self.assertEqual(harvester.failed_count, initial_failed_count + 1)

    @patch('schema_org.d1_client_manager.D1ClientManager.update_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.core.logging.getLogger')
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
            asyncio.run(harvester.harvest_document(doi, doc, record_date))

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
                asyncio.run(harvester.harvest_document(doi, doc, record_date))

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
            asyncio.run(harvester.harvest_document(doi, doc, record_date))

            # Did we see a warning?
            self.assertLogLevelCallCount(cm.output, level='INFO', n=1)

        self.assertEqual(harvester.skipped_exists_count, skipped_count + 1)

    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.core.logging.getLogger')
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

        asyncio.run(harvester.harvest_document('doi.10000/abcde',
                                               doc, record_date))

        harvester.logger.warning.assert_called_once()

    @patch('schema_org.d1_client_manager.D1ClientManager.load_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.core.logging.getLogger')
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

        asyncio.run(harvester.harvest_document('doi.10000/abcde',
                                               doc,
                                               dt.datetime.now()))

        self.assertEqual(harvester.created_count, 1)
        harvester.logger.info.assert_called_once()

    @patch('schema_org.d1_client_manager.D1ClientManager.load_science_metadata')  # noqa: E501
    @patch('schema_org.d1_client_manager.D1ClientManager.check_if_identifier_exists')  # noqa: E501
    @patch('schema_org.core.logging.getLogger')
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

        asyncio.run(harvester.harvest_document('doi.10000/abcde',
                                               doc,
                                               dt.datetime.now()))

        harvester.logger.error.assert_called_once()
