"""
DATAONE SO core for multiple adaptors.
"""

# Standard library imports
import json
import re

# 3rd party library imports
import lxml.etree

# Local imports
from .core import CoreHarvester, NO_JSON_LD_SCRIPT_ELEMENTS
from .jsonld_validator import JSONLD_Validator, JsonLdError


class SchemaDotOrgHarvester(CoreHarvester):
    """
    Harvester object with schema.org support.

    Attributes
    ----------
    jsonld_validator : obj
        Run conformance checks on the JSON-LD extracted from a site page.
    sitemap : str
        URL for XML site map.  This must be overridden for each custom client.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.jsonld_validator = JSONLD_Validator(logger=self.logger)

        self.sitemap = ''

    def extract_jsonld(self, doc):
        """
        Extract JSON-LD from HTML document.

        Parameters
        ----------
        doc : ElementTree
            The parsed HTML.  The JSON-LD should be embedded within a
            <SCRIPT> element embedded in the <HEAD> element.
        """
        self.logger.debug('extract_jsonld:')
        path = './/script[@type="application/ld+json"]'
        scripts = doc.xpath(path)
        if len(scripts) == 0:
            raise JsonLdError(NO_JSON_LD_SCRIPT_ELEMENTS)

        jsonld = None
        for script in scripts:

            j = json.loads(script.text)
            if '@type' in j and j['@type'] == 'Dataset':
                jsonld = j

        if jsonld is None:
            msg = (
                "Could not locate a JSON-LD <SCRIPT> element with @type "
                "\"Dataset\"."
            )
            raise JsonLdError(msg)

        return jsonld

    def extract_identifier(self, jsonld):
        """
        Parse the DOI from the json['@id'] value.  The identifiers should
        look something like

            'https://dx.doi.org/10.5439/1025173

        The DOI in this case would be '10.5439/1025173'.  This will be used as
        the series identifier.

        Parameters
        ----------
        JSON-LD obj

        Returns
        -------
        The identifier substring.
        """
        pattern = r'''
                  # DOI:prefix/suffix - ARM style
                  (https?://dx.doi.org/(?P<doi>10\.\w+/\w+))
                  '''
        regex = re.compile(pattern, re.VERBOSE)
        m = regex.search(jsonld['@id'])
        if m is None:
            msg = (
                f"DOI ID parsing error, could not parse an ID out of "
                f"JSON-LD '@id' element \"{jsonld['@id']}\""
            )
            raise JsonLdError(msg)

        return m.group('doi')

    async def retrieve_record(self, landing_page_url):
        """
        Read the remote document, extract the JSON-LD, and load it into the
        system.

        Parameters
        ----------
        landing_page_url : str
            URL for remote landing page HTML
        """
        self.logger.debug(f'retrieve_record')
        self.logger.info(f"Requesting {landing_page_url}...")
        content = await self.retrieve_url(landing_page_url)
        doc = lxml.etree.HTML(content)

        self.preprocess_landing_page(doc)

        jsonld = self.extract_jsonld(doc)
        self.jsonld_validator.check(jsonld)

        identifier = self.extract_identifier(jsonld)
        self.logger.debug(f"Have extracted the identifier {identifier}...")

        metadata_url = jsonld['encoding']['contentUrl']

        doc = await self.retrieve_metadata_document(metadata_url)
        return identifier, doc
