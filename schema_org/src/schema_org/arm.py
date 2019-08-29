"""
DATAONE adapter for ARM
"""

# Standard library imports

# Local imports
from .so_core import SchemaDotOrgHarvester

SITE_NSMAP = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}


class ARMHarvester(SchemaDotOrgHarvester):

    def __init__(self, **kwargs):
        super().__init__(id='arm', **kwargs)

        self.site_map = 'https://www.archive.arm.gov/metadata/adc/sitemap.xml'  # noqa: E501
