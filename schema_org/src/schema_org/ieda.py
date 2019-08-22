"""
DATAONE adapter for IEDA
"""
# Standard library imports
import re

# Local imports
from .core import CommonHarvester


class IEDAHarvester(CommonHarvester):

    site_map = 'http://get.iedadata.org/sitemaps/usap_sitemap.xml'

    def __init__(self, **kwargs):
        super().__init__(id='ieda', **kwargs)

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
            # DOI:prefix/suffix - IEDA style
            (https?://dx.doi.org/(?P<expected_doi>10\.\w+/\w+))
                |
            # other ARM-style
            (?P<other_doi>urn:usap-dc:metadata:\w+)
            # possible trailing white space (not supposed to be there)
            \s*
        '''
        regex = re.compile(pattern, re.VERBOSE)
        m = regex.search(jsonld['@id'])
        if m is None:
            msg = (
                f"DOI ID parsing error, could not parse an ID out of "
                f"JSON-LD '@id' element \"{jsonld['@id']}\""
            )
            raise RuntimeError(msg)

        if m.group('expected_doi') is not None:
            return m.group('expected_doi')
        else:
            return m.group('other_doi')
