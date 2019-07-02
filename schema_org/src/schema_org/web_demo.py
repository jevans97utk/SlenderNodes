"""
DATAONE adapter for the web demo
"""
# Standard library imports
import re

# Local imports
from .common import CommonHarvester


class WebDemo(CommonHarvester):

    def __init__(self, server_url, **kwargs):
        super().__init__(id='demo', **kwargs)

        self.site_map = server_url

        # monkey patch the last harvest time.
        self.client_mgr.get_last_harvest_time = lambda: '1900-01-01T00:00:00Z'

    def extract_metadata_url(self, jsonld):
        """
        In IEDA, the JSON-LD is structured as follows:

        {
            .
            .
            .
            "distribution": [
                {
                    "@type": "DataDownload",
                    "additionalType": "http://www.w3.org/ns/dcat#DataCatalog",
                    "encodingFormat": "text/xml",
                    "name": "ISO Metadata Document",
                    "url": "http://get.iedadata.org/path/to/doc.xml"
                },
                {
                    "@id": "http://www.usap-dc.org/view/dataset/609246",
                    "@type": "DataDownload",
                    "additionalType": "dcat:distribution",
                    "url": "http://www.usap-dc.org/view/dataset/609246",
                    "name": "landing page",
                    .
                    .
                    .
                },
                .
                .
                .
            ],
            .
            .
            .
        }

        Parameters
        ----------
        jsonld : dict
            JSON-LD as retrieved from a <SCRIPT> element in the landing page
            URL.

        Returns
        -------
        The URL for the metadata document.
        """
        items = [
            item for item in jsonld['distribution']
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
            self.logger.error(msg)
            raise RuntimeError(msg)

        if m.group('doi_id') is not None:
            return m.group('doi_id')
        else:
            return m.group('other_id')

    def harvest_document(self, doi, doc, record_date):
        """
        Do nothing.  This is just a demo, after all.

        Parameters
        ----------
        doi : str
            Handle used to identify objects uniquely.
        doc : bytes
            serialized version of XML metadata document
        record_date : datetime obj
            Last document modification time according to the site map.
        """
        pass
