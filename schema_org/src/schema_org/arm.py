"""
DATAONE adapter for ARM
"""

# Standard library imports
import datetime as dt
import re
import urllib.parse

# Local imports
from .common import CommonHarvester


class ARMHarvester(CommonHarvester):

    def __init__(self, host='localhost', port=443,
                 certificate=None, private_key=None,
                 verbosity='INFO'):
        super().__init__(host, port, certificate, private_key,
                         id='arm', verbosity=verbosity)

        self.site_map = 'https://www.archive.arm.gov/metadata/html/site_map.txt'  # noqa: E501

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
            msg = f"DOI ID parsing error:  \"{jsonld['@id']}\""
            raise RuntimeError(msg)

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

    def get_records(self, last_harvest_time):
        """
        Returns
        -------
        list
            List of tuples (URL, LASTMOD) where URL is the URL of the HTML
            document and LASTMOD is the last modification time (for ARM this
            is None because ARM does not provide this in the sitemap.
        """
        r = self.get_site_map()

        # Get a list of URL/modification time pairs.
        # Content type is text/plain, not text/xml
        urls = r.text.splitlines()

        # since there is no modification time, assume that it is now.
        lastmods = [dt.datetime.now() for url in urls]

        z = zip(urls, lastmods)

        records = [(url, lastmod) for url, lastmod in z]

        return records
