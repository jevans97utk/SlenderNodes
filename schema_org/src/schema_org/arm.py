"""
DATAONE adapter for ARM
"""

# Standard library imports
import re
import urllib.parse

# Local imports
from .common import CommonHarvester

SITE_NSMAP = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}


class ARMHarvester(CommonHarvester):

    def __init__(self, host='localhost', port=443,
                 certificate=None, private_key=None,
                 verbosity='INFO'):
        super().__init__(host, port, certificate, private_key,
                         id='arm', verbosity=verbosity)

        self.site_map = 'https://www.archive.arm.gov/metadata/adc/sitemap.xml'  # noqa: E501

    def extract_identifier(self, jsonld):
        """
        Parse the DOI from the json['@id'] value.  ARM identifiers
        look something like

            'http://dx.doi.org/10.5439/1027257'

        The DOI in this case would be '10.5439/102757'.  This will be used as
        the series identifier.

        Parameters
        ----------
        JSON-LD obj

        Returns
        -------
        The identifier substring.
        """
        pattern = r'''
            https?://dx.doi.org/(?P<id>10\.\w+/\w+)
        '''
        regex = re.compile(pattern, re.VERBOSE)
        m = regex.search(jsonld['@id'])
        if m is None:
            msg = (
                f"DOI ID parsing error, could not parse an ID out of "
                f"JSON-LD '@id' element \"{jsonld['@id']}\""
            )
            self.logger.warning(msg)
            raise RuntimeError(msg)
        else:
            return m.group('id')

    def extract_metadata_url(self, jsonld_doc, landing_page_url):
        """
        Returns
        -------
        The URL for the metadata document.
        """
        p = urllib.parse.urlparse(landing_page_url)

        # Seems a bit dangerous.
        path = p.path.replace('html', 'xml')

        metadata_url = f"{p.scheme}://{p.netloc}{path}"
        return metadata_url
