"""
DATAONE adapter for CUAHSI
"""

# Standard library imports

# Local imports
from .core import CommonHarvester, SkipError

SITE_NSMAP = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}


class CUAHSIHarvester(CommonHarvester):

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
