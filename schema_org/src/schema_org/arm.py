"""
DATAONE adapter for ARM
"""

# Standard library imports

# Local imports
from .core import CommonHarvester

SITE_NSMAP = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}


class ARMHarvester(CommonHarvester):

    def __init__(self, **kwargs):
        super().__init__(id='arm', **kwargs)

        self.site_map = 'https://www.archive.arm.gov/metadata/adc/sitemap.xml'  # noqa: E501
