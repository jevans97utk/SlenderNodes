"""
DATAONE adapter for ARM
"""

# Standard library imports

# Local imports
from .so_core import SchemaDotOrgHarvester


class ARMHarvester(SchemaDotOrgHarvester):

    def __init__(self, **kwargs):
        super().__init__(id='arm', **kwargs)

        self.sitemap = 'https://www.archive.arm.gov/metadata/adc/sitemap.xml'  # noqa: E501
