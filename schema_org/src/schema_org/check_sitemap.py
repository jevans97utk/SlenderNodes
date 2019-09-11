# Standard library imports

# 3rd party library imports

# local imports
from .so_core import SchemaDotOrgHarvester


class D1CheckSitemap(SchemaDotOrgHarvester):
    """
    Front end to validate a remote sitemap.
    """

    def __init__(self, sitemap_url=None, **kwargs):
        super().__init__(id='d1checksite', **kwargs)

        self.site_map = sitemap_url

    async def harvest_document(self, doi, doc, record_date):
        """
        We don't actually harvest.
        """
        pass
