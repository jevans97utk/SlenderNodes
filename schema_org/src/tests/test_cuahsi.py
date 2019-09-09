# standard library imports
import importlib.resources as ir
import re

# 3rd party library imports
from aioresponses import aioresponses
import lxml.etree

# local imports
from schema_org.core import SkipError
from schema_org.cuahsi import CUAHSIHarvester
from .test_common import TestCommon


class TestSuite(TestCommon):

    def setUp(self):
        # Every URL request for ARM will match this pattern, so we set
        # aioresponses to intercept all of them.
        self.pattern = re.compile(r'https://www.hydroshare.org/')

    @aioresponses()
    def test_landing_page_is_missing_jsonld(self, aioresp_mocker):
        """
        SCENARIO:  A landing page does not have a JSON-LD <SCRIPT> element.

        EXPECTED RESULT:  A SkipError is raised.  Many CUAHSI documents
        don't have JSON-LD, and we don't want that counting against the
        failure count.
        """

        contents = ir.read_text('tests.data.cuahsi', 'index.html')
        doc = lxml.etree.HTML(contents)

        obj = CUAHSIHarvester()

        with self.assertLogs(logger=obj.logger, level='DEBUG'):
            with self.assertRaises(SkipError):
                obj.extract_jsonld(doc)
