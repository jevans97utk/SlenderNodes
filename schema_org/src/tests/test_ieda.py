# standard library imports
import importlib.resources as ir

# 3rd party library imports
import lxml.etree

# local imports
from schema_org.jsonld_validator import JsonLdError
from schema_org.ieda import IEDAHarvester
from .test_common import TestCommon


class TestSuite(TestCommon):

    def test_extract_identifier__doi_style__extra_space(self):
        """
        SCENARIO:  We have JSON-LD from an IEDA landing page.  There is a
        leading space in the JSON-LD field that must be stripped.

        EXPECTED RESULT:  The identifier is verified.
        """

        contents = ir.read_binary('tests.data.ieda', 'ieda600048.html')
        doc = lxml.etree.HTML(contents)

        harvester = IEDAHarvester()

        j = harvester.extract_jsonld(doc)
        identifier = harvester.extract_identifier(j)
        self.assertEqual(identifier, '10.15784/600048')

    def test_extract_identifier__other_style(self):
        """
        SCENARIO:  We have JSON-LD from an IEDA landing page.

        EXPECTED RESULT:  The identifier is verified.
        """

        contents = ir.read_binary('tests.data.ieda', 'ieda609246.html')
        doc = lxml.etree.HTML(contents)

        harvester = IEDAHarvester()

        j = harvester.extract_jsonld(doc)
        identifier = harvester.extract_identifier(j)
        self.assertEqual(identifier, 'urn:usap-dc:metadata:609246')

    def test_extract_identifier__unparseable_id(self):
        """
        SCENARIO:  We have JSON-LD from an IEDA landing page.  The '@id' field
        isn't of the right form.

        EXPECTED RESULT:  A JsonLDError is raised.
        """
        j = {'@id':  'ftp://oid:10.15784/600048'}

        harvester = IEDAHarvester()

        with self.assertRaises(JsonLdError):
            harvester.extract_identifier(j)
