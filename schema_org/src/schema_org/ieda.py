"""
DATAONE adapter for IEDA
"""
# Standard library imports

# Local imports
from .core import CommonHarvester


class IEDAHarvester(CommonHarvester):

    site_map = 'http://get.iedadata.org/sitemaps/usap_sitemap.xml'

    def __init__(self, **kwargs):
        super().__init__(id='ieda', **kwargs)
