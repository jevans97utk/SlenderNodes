# 3rd party library imports

# local imports
from .common import CommonHarvester


class D1TestTool(CommonHarvester):

    def __init__(self, sitemap_url=None):
        super().__init__(id='d1checksite')

        self.site_map = sitemap_url

    def harvest_document(self, doi, doc, record_date):
        """
        We don't actually harvest.
        """
        pass

    def summarize(self):
        """
        We don't harvest, so we don't need to summarize it.
        """
        pass
