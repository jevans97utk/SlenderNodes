"""
DATAONE adapter for IEDA
"""
# Standard library imports
import re

# Local imports
from .common import CommonHarvester


class IEDAHarvester(CommonHarvester):

    def __init__(self, host='localhost', port=443,
                 certificate=None, private_key=None,
                 verbosity='INFO'):
        super().__init__(host, port, certificate, private_key, id='ieda',
                         verbosity=verbosity)

        self.site_map = 'http://get.iedadata.org/sitemaps/usap_sitemap.xml'

    def extract_metadata_url(self, jsonld_doc, landing_page_url):
        """
        Returns
        -------
        The URL for the metadata document.
        """
        items = [
            item for item in jsonld_doc['distribution']
            if item['name'] == 'ISO Metadata Document'
        ]
        metadata_url = items[0]['url']
        return metadata_url

    def extract_identifier(self, jsonld):
        """
        Parse the DOI from the json['@id'] value.  IEDA identifiers
        look something like

            'doi:10.15784/601015'

        The DOI in this case would be '10.15784/601015'.  This will be used as
        the series identifier.

        Parameters
        ----------
        JSON-LD obj

        Returns
        -------
        The identifier substring.
        """
        pattern = r'''
            # possible leading white space (not supposed to be there)
            \s*
            # DOI:prefix/suffix
            (doi:(?P<doi_id>10.\w+/\w+))
                |
            (?P<other_id>urn:usap-dc:metadata:\w+)
            # possible trailing white space (not supposed to be there)
            \s*
        '''
        regex = re.compile(pattern, re.VERBOSE)
        m = regex.search(jsonld['@id'])
        if m is None:
            msg = f"DOI ID parsing error:  \"{jsonld['@id']}\""
            raise RuntimeError(msg)

        if m.group('doi_id') is not None:
            return m.group('doi_id')
        else:
            return m.group('other_id')