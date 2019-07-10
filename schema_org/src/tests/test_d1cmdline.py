# standard library imports
import importlib.resources as ir
import io
import sys
import unittest
from unittest.mock import patch

# 3rd party library imports
import lxml.etree
import requests

# local imports
import schema_org
import schema_org.commandline as commandline
from schema_org import D1TestTool
from .test_common import TestCommon


class TestSuite(TestCommon):

    @unittest.skip('rethink how we test the command line')
    @patch.object(sys, 'argv', ['', 'http://www.acme.org/nositemap.xml'])
    def test_no_site_map(self, mock_logger):
        """
        SCENARIO:  The given URL for the sitemap does not seem to exist.

        EXPECTED RESULT:  A requests.HTTPError is raised.
        """
        self.setup_requests_session_patcher(status_codes=[400])

        with self.assertRaises(requests.HTTPError):
            commandline.d1_check_site()


class TestSuite2(TestCommon):

    def setUp(self):
        self.protocol = 'https'

    def test_no_site_map(self):
        """
        SCENARIO:  The given URL for the sitemap does not seem to exist.

        EXPECTED RESULT:  A requests.HTTPError is raised.
        """
        obj = D1TestTool(sitemap_url='https://www.somewhere.com/sitemap.txt')

        self.setUpRequestsMocking(obj, status_codes=[400])

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            obj.run()

            msgs = [msg for msg in cm.output if msg.startswith('ERROR')]
            self.assertIn(schema_org.common.SITEMAP_RETRIEVAL_FAILURE_MESSAGE,
                          msgs[0])
            self.assertIn('HTTPError', msgs[1])

    def test_landing_page_is_not_present(self):
        """
        SCENARIO:  The sitemap references two documents.  The first landing
        page document that is not present, but the next one is fine.

        EXPECTED RESULT:  The log record reflects the successful calls, but
        also the XML failure.
        """

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1 (fails)
        #   3) HTML document for record 2
        #   4) XML document for record 2
        #
        contents = [
            ir.read_binary('tests.data.arm', 'sitemap2.xml'),
            b'',
            ir.read_binary('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_binary('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),  # noqa: E501
        ]
        status_codes = [200, 400, 200, 200]
        obj = D1TestTool(sitemap_url='https://www.somewhere.com/sitemap.txt')

        self.setUpRequestsMocking(obj,
                                  contents=contents, status_codes=status_codes)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            obj.run()

            self.assertErrorCount(cm.output, 1)

            self.assertSuccessfulIngest(cm.output)

    def test_landing_page_is_missing_jsonld(self):
        """
        SCENARIO:  The sitemap references two documents.  The first landing
        page document does not have JSON-LD.  The 2nd one does have it.

        EXPECTED RESULT:  The log records the JSON-LD failure, but also the
        successful ingest of the 2nd document.
        """

        url = 'https://www.somewhere.com/this_does_not_matter.xml'
        obj = D1TestTool(sitemap_url=url)

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1 (no XML document can be accessed)
        #   3) HTML document for record 2
        #   4) XML document for record 2
        #
        contents = [
            ir.read_binary('tests.data.arm', 'sitemap2.xml'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.no_jsonld.html'),  # noqa: E501
            ir.read_binary('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_binary('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),  # noqa: E501
        ]
        status_codes = [200, 200, 200, 200]
        self.setUpRequestsMocking(obj, contents=contents,
                                  status_codes=status_codes)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            obj.run()

            # Verify the single error message.
            error_msgs = [msg for msg in cm.output if msg.startswith('ERROR')]
            self.assertEqual(len(error_msgs), 1)
            self.assertIn(schema_org.common.NO_JSON_LD_SCRIPT_ELEMENTS,
                          error_msgs[0])

            self.assertSuccessfulIngest(cm.output)

    def test_jsonld_script_elemement_is_not_valid_json(self):
        """
        SCENARIO:  The sitemap references two documents.  The first landing
        page document has a JSON-LD script element that is not valid JSON-LD.
        The 2nd document is good.

        EXPECTED RESULT:  The log records the JSON-LD failure, but also the
        successful ingest of the 2nd document.
        """

        url = 'https://www.somewhere.com/this_does_not_matter.xml'
        obj = D1TestTool(sitemap_url=url)

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1 (no XML document can be accessed)
        #   3) HTML document for record 2
        #   4) XML document for record 2
        #
        contents = [
            ir.read_binary('tests.data.arm', 'sitemap2.xml'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.invalid_jsonld.html'),  # noqa: E501
            ir.read_binary('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_binary('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),  # noqa: E501
        ]
        self.setUpRequestsMocking(obj, contents=contents)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            obj.run()

            # Verify the error message.
            error_msgs = [msg for msg in cm.output if msg.startswith('ERROR')]
            self.assertEqual(len(error_msgs), 1)
            self.assertIn(schema_org.common.INVALID_JSONLD_MESSAGE,
                          error_msgs[0])

            self.assertSuccessfulIngest(cm.output)

    def test_jsonld_script_elemement_is_missing_the_id(self):
        """
        SCENARIO:  The sitemap references two documents.  The first landing
        page document has a JSON-LD script element that is missing the ID.
        The 2nd document is good.

        EXPECTED RESULT:  The log records the JSON-LD failure, but also the
        successful ingest of the 2nd document.
        """

        url = 'https://www.somewhere.com/this_does_not_matter.xml'
        obj = D1TestTool(sitemap_url=url)

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1 (no XML document will be accessed)
        #   3) HTML document for record 2
        #   4) XML document for record 2
        #
        contents = [
            ir.read_binary('tests.data.arm', 'sitemap2.xml'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.missing_id.html'),  # noqa: E501
            ir.read_binary('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_binary('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),  # noqa: E501
        ]
        self.setUpRequestsMocking(obj, contents=contents)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            obj.run()

            # Verify the single error message.
            self.assertErrorCount(cm.output, 1)

            error_msgs = [msg for msg in cm.output if msg.startswith('ERROR')]
            self.assertEqual(len(error_msgs), 1)
            self.assertIn('KeyError', error_msgs[0])

            self.assertSuccessfulIngest(cm.output)

    def test_xml_metadata_document_is_missing(self):
        """
        SCENARIO:  The sitemap references two documents.  The first landing
        page document references an XML document that is not present.  The 2nd
        document is good.

        EXPECTED RESULT:  The log records the XML retrieval failure,
        but also the successful ingest of the 2nd document.
        """

        url = 'https://www.somewhere.com/this_does_not_matter.xml'
        obj = D1TestTool(sitemap_url=url)

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1
        #   3) XML document for record 1 (fails)
        #   3) HTML document for record 2
        #   4) XML document for record 2
        #
        contents = [
            ir.read_binary('tests.data.arm', 'sitemap2.xml'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.html'),
            b'',
            ir.read_binary('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_binary('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),  # noqa: E501
        ]
        status_codes = [200, 200, 400, 200, 200]
        self.setUpRequestsMocking(obj, contents=contents,
                                  status_codes=status_codes)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            obj.run()

            # Verify the error message.
            error_msgs = [msg for msg in cm.output if msg.startswith('ERROR')]
            self.assertEqual(len(error_msgs), 1)
            self.assertIn('HTTPError', error_msgs[0])

            self.assertSuccessfulIngest(cm.output)

    def test_metadata_document_is_invalid_xml(self):
        """
        SCENARIO:  The sitemap references two documents.  The first landing
        page document references an XML document that is not valid XML.  The
        2nd document is good.

        EXPECTED RESULT:  The log records the invalid XML for the first
        document, but also the successful ingest of the 2nd document.
        """

        url = 'https://www.somewhere.com/this_does_not_matter.xml'
        obj = D1TestTool(sitemap_url=url)

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1
        #   3) XML document for record 1
        #   3) HTML document for record 2
        #   4) XML document for record 2
        #
        contents = [
            ir.read_binary('tests.data.arm', 'sitemap2.xml'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.html'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.invalid.xml'),
            ir.read_binary('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_binary('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),  # noqa: E501
        ]
        self.setUpRequestsMocking(obj, contents=contents)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            obj.run()

            # Verify the error message, which is referenced twice.
            error_msgs = [msg for msg in cm.output if msg.startswith('ERROR')]
            self.assertEqual(len(error_msgs), 1)
            self.assertIn('XMLSyntaxError', error_msgs[0])

            self.assertSuccessfulIngest(cm.output)

    def test_metadata_document_does_not_validate(self):
        """
        SCENARIO:  The sitemap references two documents.  The first landing
        page document references an XML document that does not validate.  The
        2nd document is good.

        EXPECTED RESULT:  The successful ingest of the 2nd document is
        reflected in the log.  The validation failure is also reflected,
        specifically the identity of the CI_Responsibility element.
        """

        url = 'https://www.somewhere.com/this_does_not_matter.xml'
        obj = D1TestTool(sitemap_url=url)

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1
        #   3) XML document for record 1
        #   3) HTML document for record 2
        #   4) XML document for record 2
        #
        contents = [
            ir.read_binary('tests.data.arm', 'sitemap2.xml'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.html'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.xml'),
            ir.read_binary('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_binary('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),  # noqa: E501
        ]
        self.setUpRequestsMocking(obj, contents=contents)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            obj.run()

            # Verify the error message, which is referenced twice.
            error_msgs = [msg for msg in cm.output if msg.startswith('ERROR')]
            self.assertEqual(len(error_msgs), 1)
            self.assertIn('XML document does not validate', error_msgs[0])
            self.assertIn('CI_ResponsibleParty', error_msgs[0])

            self.assertSuccessfulIngest(cm.output)

    def test_sitemap_is_gzipped(self):
        """
        SCENARIO:  The sitemap references two documents, both of which are
        good.  The sitemap is gzipped.

        EXPECTED RESULT:  The successful ingest of both documents is logged.
        """

        url = 'https://www.somewhere.com/this_does_not_matter.xml.gz'
        obj = D1TestTool(sitemap_url=url)

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1
        #   3) XML document for record 1
        #   3) HTML document for record 2
        #   4) XML document for record 2
        #
        contents = [
            ir.read_binary('tests.data.arm', 'sitemap2.xml.gz'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.html'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.fixed.xml'),
            ir.read_binary('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_binary('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),  # noqa: E501
        ]
        self.setUpRequestsMocking(obj, contents=contents)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            obj.run()

            self.assertSuccessfulIngest(cm.output, n=2)

    def test_sitemap_url_is_sitemap_index_file(self):
        """
        SCENARIO:  The URL given is actually a sitemap index that references
        two sitemaps.  Both sitemaps have two documents that are both good.

        EXPECTED RESULT:  The successful ingest of all four documents is
        logged.
        """

        url = 'https://www.somewhere.com/this_does_not_matter.xml.gz'
        obj = D1TestTool(sitemap_url=url)

        # External calls to read the:
        #
        #   1) sitemap index file
        #   2) sitemap 1
        #   3) HTML document for record 1
        #   4) XML document for record 1
        #   5) HTML document for record 2
        #   6) XML document for record 2
        #   7) sitemap 2
        #   8) HTML document for record 1
        #   9) XML document for record 1
        #   10) HTML document for record 2
        #   11) XML document for record 2
        #
        contents = [
            ir.read_binary('tests.data.arm', 'sitemap_index_file.xml'),

            ir.read_binary('tests.data.arm', 'sitemap2.xml.gz'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.html'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.fixed.xml'),
            ir.read_binary('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_binary('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),  # noqa: E501

            ir.read_binary('tests.data.arm', 'sitemap2.xml.gz'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.html'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.fixed.xml'),
            ir.read_binary('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_binary('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),  # noqa: E501
        ]
        self.setUpRequestsMocking(obj, contents=contents)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            obj.run()

            self.assertSuccessfulIngest(cm.output, n=4)

    def test_site_map_is_not_xml(self):
        """
        SCENARIO:  The sitemap document is not XML.

        EXPECTED RESULT:  There is a warning stating that the URL may not be
        XML, plus an XMLSyntaxError is raised.
        """
        contents = [ir.read_binary('tests.data.arm', 'sitemap.txt')]
        headers = [{'Content-Type': 'text/plain'}]

        obj = D1TestTool(sitemap_url='https://www.somewhere.com/sitemap.txt')

        self.setUpRequestsMocking(obj, contents=contents, headers=headers)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            obj.run()

            # Verify the warning about the sitemap possibly not being XML.
            warning_msgs = [
                msg for msg in cm.output if msg.startswith('WARNING')
            ]
            self.assertEqual(len(warning_msgs), 1)
            self.assertIn(schema_org.common.SITEMAP_NOT_XML_MESSAGE,
                          warning_msgs[0])

            # Verify the two exceptions that are caught when trying to parse
            # the sitemap.
            error_msgs = [msg for msg in cm.output if msg.startswith('ERROR')]
            self.assertEqual(len(error_msgs), 3)
            self.assertIn('XMLSyntaxError', error_msgs[0])
            self.assertIn('OSError', error_msgs[1])

    def test_limit_number_of_documents(self):
        """
        SCENARIO:  We do not wish to go through the entire list of documents,
        so a limit is specified.

        EXPECTED RESULT:  There is a warning stating that the URL may not be
        XML, plus an XMLSyntaxError is raised.
        """
        url = 'https://www.somewhere.com/this_does_not_matter.xml'
        obj = D1TestTool(sitemap_url=url, num_documents=2)

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1
        #   3) XML document for record 1
        #   3) HTML document for record 2
        #   4) XML document for record 2
        #
        contents = [
            ir.read_binary('tests.data.arm', 'sitemap3.xml'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.html'),
            ir.read_binary('tests.data.arm', 'nsaqcrad1longC2.c2.fixed.xml'),
            ir.read_binary('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_binary('tests.data.arm', 'nsasondewnpnS01.b1.fixed.xml'),
        ]
        self.setUpRequestsMocking(obj, contents=contents)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            obj.run()

            self.assertSuccessfulIngest(cm.output, n=2)

        # And just to show, there are 3 URLs in the sitemap.
        doc = lxml.etree.parse(io.BytesIO(contents[0]))
        urls = doc.xpath('.//sm:loc/text()',
                         namespaces=schema_org.common.SITEMAP_NS)
        self.assertEqual(len(urls), 3)
