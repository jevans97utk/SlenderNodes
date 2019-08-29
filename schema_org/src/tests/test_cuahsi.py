# standard library imports
import asyncio
import importlib.resources as ir
import re

# 3rd party library imports
from aioresponses import aioresponses

# local imports
from schema_org import D1CheckSitemap
from schema_org.core import NO_JSON_LD_SCRIPT_ELEMENTS
from .test_common import TestCommon


class TestSuite(TestCommon):

    def setUp(self):
        # Every URL request for ARM will match this pattern, so we set
        # aioresponses to intercept all of them.
        self.pattern = re.compile(r'https://www.archive.arm.gov/metadata/adc')

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
            ir.read_text('tests.data.arm', 'nsasondewnpnS01.b1.fixed.html'),
            ir.read_text('tests.data.arm', 'nsanimfraod1michC2.c1.fixed.xml'),
        ]
        aioresp_mocker.get(self.pattern, body=contents[0])
        aioresp_mocker.get(self.pattern, body=contents[1])
        aioresp_mocker.get(self.pattern, body=contents[2])
        aioresp_mocker.get(self.pattern, body=contents[3])

        sitemap = 'https://www.archive.arm.gov/metadata/adc/sitemap_not.xml'
        obj = D1CheckSitemap(sitemap_url=sitemap)

        with self.assertLogs(logger=obj.logger, level='DEBUG') as cm:
            asyncio.run(obj.run())

            self.assertWarningLogMessage(cm.output, NO_JSON_LD_SCRIPT_ELEMENTS)
            self.assertSuccessfulDebugIngest(cm.output)
