# standard library imports
import asyncio
import importlib.resources as ir
import re

# 3rd party library imports
from aioresponses import aioresponses

# local imports
from schema_org.core import NO_JSON_LD_SCRIPT_ELEMENTS
from schema_org.cuahsi import CUAHSIHarvester
from .test_common import TestCommon


class TestSuite(TestCommon):

    def setUp(self):
        # Every URL request for ARM will match this pattern, so we set
        # aioresponses to intercept all of them.
        self.pattern = re.compile(r'https://www.hydroshare.org/')
