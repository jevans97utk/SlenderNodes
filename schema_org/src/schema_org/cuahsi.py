"""
DATAONE adapter for CUAHSI
"""

# Standard library imports

# Local imports
from .so_core import SchemaDotOrgHarvester
from .core import SkipError

SITE_NSMAP = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}


class CUAHSIHarvester(SchemaDotOrgHarvester):

    def __init__(self, **kwargs):
        super().__init__(id='cuahsi', **kwargs)

        self.site_map = 'https://www.hydroshare.org/sitemap.xml'

    def preprocess_landing_page(self, landing_page_doc):
        """
        Check the landing page for any information we may need OTHER than
        JSON-LD.

        Parameters
        ----------
        landing_page_doc : lxml element tree
            Document corresponding to the HTML landing page.
        """
        path = './/td[@id="hl-sharing-status"]/text()'
        elts = landing_page_doc.xpath(path)
        if len(elts) == 0:
            msg = "No sharing status element found."
            raise SkipError(msg)

        sharing_status = elts[0].strip().upper()

        self.logger.debug(f"Sharing status is {sharing_status}.")
        if sharing_status != 'PUBLISHED':
            msg = (
                f"CUAHSI landing page sharing status is {sharing_status} "
                f"instead of PUBLISHED."
            )
            raise SkipError(msg)

    def extract_jsonld(self, doc):
        """
        Extract JSON-LD from HTML document.

        What we hope for is that:
            1) jsonld['distribution'][0]['name'] = 'ISO Metadata Document'
            2) jsonld['distribution'][0]['url'] is the XML url
            3) jsonld['distribution'][1]['name'] = 'landing page'

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
            raise SkipError(NO_JSON_LD_SCRIPT_ELEMENTS)

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
            raise RuntimeError(msg)

        return jsonld

