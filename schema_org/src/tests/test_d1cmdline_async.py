# standard library imports
import asyncio
import importlib.resources as ir
import io
import re

# 3rd party library imports
import lxml.etree
from aioresponses import aioresponses

# local imports
import schema_org
from schema_org import D1TestToolAsync
from schema_org.common import (
    SITEMAP_RETRIEVAL_FAILURE_MESSAGE
)
from .test_common import TestCommon


class TestSuite(TestCommon):

    def setUp(self):
        self.pattern = re.compile(r'https://www.archive.arm.gov/metadata/adc')

    async def run_test_tool(self, obj):
        await obj._init()
        await obj.run()
        await obj._close()

    @aioresponses()
    def test_no_site_map(self, aioresp_mocker):
        """
        SCENARIO:  The given URL for the sitemap does not seem to exist.

        EXPECTED RESULT:  A requests.HTTPError is raised.
        """
        aioresp_mocker.get(self.pattern, status=400)

        sitemap = 'https://www.archive.arm.gov/metadata/adc/sitemap.txt'
        obj = D1TestToolAsync(sitemap_url=sitemap, verbosity='DEBUG')
        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            asyncio.run(self.run_test_tool(obj))

            msgs = [msg for msg in cm.output if msg.startswith('ERROR')]
            self.assertIn(SITEMAP_RETRIEVAL_FAILURE_MESSAGE, msgs[0])
            self.assertIn('ClientResponseError', msgs[1])

    @aioresponses()
    def test_landing_page_is_not_present(self, aioresp_mocker):
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
            ir.read_text('tests.data.arm', 'sitemap2.xml'),
            b'',
            ir.read_text('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_text('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),
        ]
        aioresp_mocker.get(self.pattern, body=contents[0])
        aioresp_mocker.get(self.pattern, status=400)
        aioresp_mocker.get(self.pattern, body=contents[2])
        aioresp_mocker.get(self.pattern, body=contents[3])

        sitemap = 'https://www.archive.arm.gov/metadata/adc/sitemap_not.xml'
        obj = D1TestToolAsync(sitemap_url=sitemap)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            asyncio.run(self.run_test_tool(obj))

            self.assertErrorCount(cm.output, 1)
            self.assertSuccessfulIngest(cm.output)

    @aioresponses()
    def test_landing_page_is_missing_jsonld(self, aioresp_mocker):
        """
        SCENARIO:  The sitemap references two documents.  The first landing
        page document does not have JSON-LD.  The 2nd one does have it.

        EXPECTED RESULT:  The log records the JSON-LD failure, but also the
        successful ingest of the 2nd document.
        """

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1 (no XML document can be accessed)
        #   3) HTML document for record 2
        #   4) XML document for record 2
        #
        contents = [
            ir.read_text('tests.data.arm', 'sitemap2.xml'),
            ir.read_text('tests.data.arm', 'nsaqcrad1longC2.c2.no_jsonld.html'),  # noqa: E501
            ir.read_text('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_text('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),
        ]
        aioresp_mocker.get(self.pattern, body=contents[0])
        aioresp_mocker.get(self.pattern, body=contents[1])
        aioresp_mocker.get(self.pattern, body=contents[2])
        aioresp_mocker.get(self.pattern, body=contents[3])

        sitemap = 'https://www.archive.arm.gov/metadata/adc/sitemap_not.xml'
        obj = D1TestToolAsync(sitemap_url=sitemap)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            asyncio.run(self.run_test_tool(obj))

            # Verify the single error message.
            error_msgs = [msg for msg in cm.output if msg.startswith('ERROR')]
            self.assertEqual(len(error_msgs), 1)
            self.assertIn(schema_org.common.NO_JSON_LD_SCRIPT_ELEMENTS,
                          error_msgs[0])

            self.assertSuccessfulIngest(cm.output)

    @aioresponses()
    def test_jsonld_script_elemement_is_not_valid_json(self, aioresp_mocker):
        """
        SCENARIO:  The sitemap references two documents.  The first landing
        page document has a JSON-LD script element that is not valid JSON-LD.
        The 2nd document is good.

        EXPECTED RESULT:  The log records the JSON-LD failure, but also the
        successful ingest of the 2nd document.
        """

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1 (no XML document can be accessed)
        #   3) HTML document for record 2
        #   4) XML document for record 2
        #
        contents = [
            ir.read_text('tests.data.arm', 'sitemap2.xml'),
            ir.read_text('tests.data.arm', 'nsaqcrad1longC2.c2.invalid_jsonld.html'),  # noqa: E501
            ir.read_text('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_text('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),
        ]
        for content in contents:
            aioresp_mocker.get(self.pattern, body=content)

        sitemap = 'https://www.archive.arm.gov/metadata/adc/sitemap.xml'
        obj = D1TestToolAsync(sitemap_url=sitemap)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            asyncio.run(self.run_test_tool(obj))

            # Verify the error message.
            error_msgs = [msg for msg in cm.output if msg.startswith('ERROR')]
            self.assertEqual(len(error_msgs), 1)
            self.assertIn(schema_org.common.INVALID_JSONLD_MESSAGE,
                          error_msgs[0])

            self.assertSuccessfulIngest(cm.output)

    @aioresponses()
    def test_jsonld_script_elemement_is_missing_the_id(self, aioresp_mocker):
        """
        SCENARIO:  The sitemap references two documents.  The first landing
        page document has a JSON-LD script element that is missing the ID.
        The 2nd document is good.

        EXPECTED RESULT:  The log records the JSON-LD failure, but also the
        successful ingest of the 2nd document.
        """

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1 (no XML document will be accessed)
        #   3) HTML document for record 2
        #   4) XML document for record 2
        #
        contents = [
            ir.read_text('tests.data.arm', 'sitemap2.xml'),
            ir.read_text('tests.data.arm', 'nsaqcrad1longC2.c2.missing_id.html'),  # noqa: E501
            ir.read_text('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_text('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),
        ]
        for content in contents:
            aioresp_mocker.get(self.pattern, body=content)

        url = 'https://www.archive.arm.gov/metadata/adc/sitemap.xml'
        obj = D1TestToolAsync(sitemap_url=url)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            asyncio.run(self.run_test_tool(obj))

            # Verify the single error message.
            self.assertErrorCount(cm.output, 1)

            error_msgs = [msg for msg in cm.output if msg.startswith('ERROR')]
            self.assertEqual(len(error_msgs), 1)
            self.assertIn('KeyError', error_msgs[0])

            self.assertSuccessfulIngest(cm.output)

    @aioresponses()
    def test_xml_metadata_document_is_missing(self, aioresp_mocker):
        """
        SCENARIO:  The sitemap references two documents.  The first landing
        page document references an XML document that is not present.  The 2nd
        document is good.

        EXPECTED RESULT:  The log records the XML retrieval failure,
        but also the successful ingest of the 2nd document.
        """

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1
        #   3) XML document for record 1 (fails)
        #   3) HTML document for record 2
        #   4) XML document for record 2
        #
        contents = [
            ir.read_text('tests.data.arm', 'sitemap2.xml'),
            ir.read_text('tests.data.arm', 'nsaqcrad1longC2.c2.html'),
            b'',
            ir.read_text('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_text('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),
        ]
        aioresp_mocker.get(self.pattern, body=contents[0])
        aioresp_mocker.get(self.pattern, body=contents[1])
        aioresp_mocker.get(self.pattern, status=400)
        aioresp_mocker.get(self.pattern, body=contents[3])
        aioresp_mocker.get(self.pattern, body=contents[4])

        url = 'https://www.archive.arm.gov/metadata/adc/sitemap.xml'
        obj = D1TestToolAsync(sitemap_url=url)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            asyncio.run(self.run_test_tool(obj))

            # Verify the error message.
            error_msgs = [msg for msg in cm.output if msg.startswith('ERROR')]
            self.assertEqual(len(error_msgs), 1)
            self.assertIn('ClientResponseError', error_msgs[0])

            self.assertSuccessfulIngest(cm.output)

    @aioresponses()
    def test_metadata_document_is_invalid_xml(self, aioresp_mocker):
        """
        SCENARIO:  The sitemap references two documents.  The first landing
        page document references an XML document that is not valid XML.  The
        2nd document is good.

        EXPECTED RESULT:  The log records the invalid XML for the first
        document, but also the successful ingest of the 2nd document.
        """

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1
        #   3) XML document for record 1
        #   3) HTML document for record 2
        #   4) XML document for record 2
        #
        contents = [
            ir.read_text('tests.data.arm', 'sitemap2.xml'),
            ir.read_text('tests.data.arm', 'nsaqcrad1longC2.c2.html'),
            ir.read_text('tests.data.arm', 'nsaqcrad1longC2.c2.invalid.xml'),
            ir.read_text('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_text('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),  # noqa: E501
        ]
        for content in contents:
            aioresp_mocker.get(self.pattern, body=content)

        url = 'https://www.archive.arm.gov/metadata/adc/sitemap.xml'
        obj = D1TestToolAsync(sitemap_url=url)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            asyncio.run(self.run_test_tool(obj))

            # Verify the error message, which is referenced twice.
            error_msgs = [msg for msg in cm.output if msg.startswith('ERROR')]
            self.assertEqual(len(error_msgs), 1)
            self.assertIn('XMLSyntaxError', error_msgs[0])

            self.assertSuccessfulIngest(cm.output)

    @aioresponses()
    def test_metadata_document_does_not_validate(self, aioresp_mocker):
        """
        SCENARIO:  The sitemap references two documents.  The first landing
        page document references an XML document that does not validate.  The
        2nd document is good.

        EXPECTED RESULT:  The successful ingest of the 2nd document is
        reflected in the log.  The validation failure is also reflected,
        specifically the identity of the CI_Responsibility element.
        """

        # External calls to read the:
        #
        #   1) sitemap
        #   2) HTML document for record 1
        #   3) XML document for record 1
        #   3) HTML document for record 2
        #   4) XML document for record 2
        #
        contents = [
            ir.read_text('tests.data.arm', 'sitemap2.xml'),
            ir.read_text('tests.data.arm', 'nsaqcrad1longC2.c2.html'),
            ir.read_text('tests.data.arm', 'nsaqcrad1longC2.c2.xml'),
            ir.read_text('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_text('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),
        ]
        for content in contents:
            aioresp_mocker.get(self.pattern, body=content)

        url = 'https://www.archive.arm.gov/metadata/adc/sitemap.xml'
        obj = D1TestToolAsync(sitemap_url=url)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            asyncio.run(self.run_test_tool(obj))

            # Verify the error message, which is referenced twice.
            error_msgs = [msg for msg in cm.output if msg.startswith('ERROR')]
            self.assertEqual(len(error_msgs), 1)
            self.assertIn('XML document does not validate', error_msgs[0])
            self.assertIn('CI_ResponsibleParty', error_msgs[0])

            self.assertSuccessfulIngest(cm.output)

    @aioresponses()
    def test_sitemap_is_gzipped(self, aioresp_mocker):
        """
        SCENARIO:  The sitemap references two documents, both of which are
        good.  The sitemap is gzipped.

        EXPECTED RESULT:  The successful ingest of both documents is logged.
        """

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
            ir.read_text('tests.data.arm', 'nsaqcrad1longC2.c2.html'),
            ir.read_text('tests.data.arm', 'nsaqcrad1longC2.c2.fixed.xml'),
            ir.read_text('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_text('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),
        ]
        for content in contents:
            aioresp_mocker.get(self.pattern, body=content)

        url = 'https://www.archive.arm.gov/metadata/adc/sitemap.xml'
        obj = D1TestToolAsync(sitemap_url=url)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            asyncio.run(self.run_test_tool(obj))

            self.assertSuccessfulIngest(cm.output, n=2)

    @aioresponses()
    def test_sitemap_url_is_sitemap_index_file(self, aioresp_mocker):
        """
        SCENARIO:  The URL given is actually a sitemap index that references
        two sitemaps.  Both sitemaps have two documents that are both good.

        EXPECTED RESULT:  The successful ingest of all four documents is
        logged.
        """

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
            ir.read_text('tests.data.arm', 'sitemap_index_file.xml'),

            ir.read_binary('tests.data.arm', 'sitemap2.xml.gz'),
            ir.read_text('tests.data.arm', 'nsaqcrad1longC2.c2.html'),
            ir.read_text('tests.data.arm', 'nsaqcrad1longC2.c2.fixed.xml'),
            ir.read_text('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_text('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),  # noqa: E501

            ir.read_binary('tests.data.arm', 'sitemap2.xml.gz'),
            ir.read_text('tests.data.arm', 'nsaqcrad1longC2.c2.html'),
            ir.read_text('tests.data.arm', 'nsaqcrad1longC2.c2.fixed.xml'),
            ir.read_text('tests.data.arm', 'nsasondewnpnS01.b1.html'),
            ir.read_text('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),  # noqa: E501
        ]
        for content in contents:
            aioresp_mocker.get(self.pattern, body=content)

        url = 'https://www.archive.arm.gov/metadata/adc/sitemap_index_file.xml'
        obj = D1TestToolAsync(sitemap_url=url)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            asyncio.run(self.run_test_tool(obj))

            self.assertSuccessfulIngest(cm.output, n=4)

    @aioresponses()
    def test_site_map_is_not_xml(self, aioresp_mocker):
        """
        SCENARIO:  The sitemap document is not XML.

        EXPECTED RESULT:  There is a warning stating that the URL may not be
        XML, plus an XMLSyntaxError is raised.
        """
        content = ir.read_text('tests.data.arm', 'sitemap.txt')
        headers = {'Content-Type': 'text/plain'}
        aioresp_mocker.get(self.pattern, body=content, headers=headers)

        url = 'https://www.archive.arm.gov/metadata/adc/sitemap.txt'
        obj = D1TestToolAsync(sitemap_url=url)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            asyncio.run(self.run_test_tool(obj))

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

    @aioresponses()
    def test_limit_number_of_documents(self, aioresp_mocker):
        """
        SCENARIO:  We do not wish to go through the entire list of documents,
        so a limit is specified.

        EXPECTED RESULT:  There is a warning stating that the URL may not be
        XML, plus an XMLSyntaxError is raised.
        """
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
        for content in contents:
            aioresp_mocker.get(self.pattern, body=content)

        url = 'https://www.archive.arm.gov/metadata/adc/sitemap.xml'
        obj = D1TestToolAsync(sitemap_url=url, num_documents=2)

        with self.assertLogs(logger=obj.logger, level='INFO') as cm:
            asyncio.run(self.run_test_tool(obj))

            self.assertSuccessfulIngest(cm.output, n=2)

        # And just to show, there are 3 URLs in the sitemap.
        doc = lxml.etree.parse(io.BytesIO(contents[0]))
        urls = doc.xpath('.//sm:loc/text()',
                         namespaces=schema_org.common.SITEMAP_NS)
        self.assertEqual(len(urls), 3)
