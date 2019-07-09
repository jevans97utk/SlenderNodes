"""
DATAONE adapter for IEDA
"""
# Standard library imports
import re

# Local imports
from .common import CommonHarvester


class IEDAHarvester(CommonHarvester):

    def __init__(self, **kwargs):
        super().__init__(id='ieda', **kwargs)

        self.site_map = 'http://get.iedadata.org/sitemaps/usap_sitemap.xml'

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
