# Standard library imports
import datetime as dt
try:
    import importlib.resources as ir
except ImportError:
    import importlib_resources as ir
from unittest.mock import patch

# 3rd party library imports
import requests

# local imports
from schema_org.arm import ARMHarvester
from schema_org.common import SITE_MAP_RETRIEVAL_FAILURE_MESSAGE
from .test_common import TestCommon


class TestSuite(TestCommon):

    def test_identifier_parsing(self):
        """
        SCENARIO:  The @id field from the JSON-LD must be parsed, we are
        presented with http://dx.doi.org/10.5439/1027257.

        EXPECTED RESULT:  10.5439/1027257
        """
        jsonld = {'@id': 'http://dx.doi.org/10.5439/1027257'}
        harvester = ARMHarvester()
        identifier = harvester.extract_identifier(jsonld)

        self.assertEqual(identifier, '10.5439/1027257')

    def test_identifier_parsing_negative(self):
        """
        SCENARIO:  The @id field from the JSON-LD must be parsed, but the given
        field is bad.

        EXPECTED RESULT:  RuntimeError
        """
        jsonld = {'@id': 'http://dx.doi.orggg/10.5439/1027257'}
        harvester = ARMHarvester()
        with self.assertRaises(RuntimeError):
            harvester.extract_identifier(jsonld)

    def test_records_retrieval(self):
        """
        SCENARIO:  We retrieve and process the sitemap

        EXPECTED RESULT:  4859 tuples of URLs and lastmod times are retrieved
        """
        content = ir.read_binary('tests.data.arm', 'sitemap.xml')
        self.setup_requests_session_patcher(contents=[content])

        harvester = ARMHarvester()
        last_harvest_time = dt.datetime(2019, 1, 1, tzinfo=dt.timezone.utc)
        records = harvester.get_records(last_harvest_time)
        self.assertEqual(len(records), 2)

    @patch('schema_org.common.logging.getLogger')
    def test_site_map_retrieval_failure(self, mock_logger):
        """
        SCENARIO:  a non-200 status code is returned by the site map retrieval.

        EXPECTED RESULT:  A requests HTTPError is raised and the exception is
        logged.
        """
        self.setup_requests_session_patcher(status_codes=[400])

        harvester = ARMHarvester(verbosity='INFO')
        with self.assertRaises(requests.HTTPError):
            harvester.get_site_map()

        harvester.logger.error.assert_any_call(SITE_MAP_RETRIEVAL_FAILURE_MESSAGE)  # noqa: E501

    def test_bad_verbosity(self):
        """
        SCENARIO:  the harvester is called with a bad verbosity value.  This
        should be precluded by the command line entry point, but you never
        know.

        EXPECTED RESULT:  a TypeError is raised
        """

        with self.assertRaises(TypeError):
            ARMHarvester(verbose='WARNING2')
