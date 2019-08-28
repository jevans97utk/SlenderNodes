"""
DATAONE adapter for CUAHSI
"""

# Standard library imports

# Local imports
from .core import CommonHarvester

SITE_NSMAP = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}


class CUAHSIHarvester(CommonHarvester):

    def __init__(self, **kwargs):
        super().__init__(id='cuahsi', **kwargs)

        self.site_map = 'https://www.hydroshare.org/sitemap.xml'

