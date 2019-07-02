"""
DATAONE adapter for the web demo
"""
# Standard library imports
import json
import pprint
import re

# 3rd party library imports
import lxml

# Local imports
from .common import CommonHarvester


class WebDemo(CommonHarvester):

    def __init__(self, server_url, dump=None, dumpkeys=None, **kwargs):
        super().__init__(id='demo', log_to_stdout=True, **kwargs)

        self.site_map = server_url
        self.dumparg = dump
        self.dumpkeys = dumpkeys

        # monkey patch the last harvest time.
        self.client_mgr.get_last_harvest_time = lambda: '1900-01-01T00:00:00Z'

    def process_record(self, landing_page_url, record_date):
        """
        Read the remote document, extract the JSON-LD, and load it into the
        system.

        Parameters
        ----------
        jsonld_url : str
            URL for remote IEDA HTML document
        record_date : datetime obj
            Last document modification time according to the site map.
        """
        self.logger.info(f"Requesting {landing_page_url}...")
        r = self.retrieve_url(landing_page_url)

        try:
            doc = lxml.etree.HTML(r.text)
        except ValueError:
            doc = lxml.etree.HTML(r.content)

        jsonld = self.extract_jsonld(doc)

        if self.dumpkeys:
            pprint.pprint(jsonld.keys())

        if self.dumparg is not None:
            if self.dumparg == 'dumpkeys':
                pprint.pprint(jsonld.keys())
            else:
                pprint.pprint(jsonld[self.dumparg])

        # Sometimes there is a space in the @id field.  Can't be having any of
        # that...
        identifier = self.extract_identifier(jsonld)
        self.logger.info(f"Have identified {identifier}...")

        metadata_url = self.extract_metadata_url(jsonld)

        doc = self.retrieve_metadata_document(metadata_url)

        self.harvest_document(identifier, doc, record_date)

        item = {
            'landing_page_url': landing_page_url,
            'last_modification_date': record_date,
            'json_ld': json.dumps(jsonld),
            'metadata_url': metadata_url,
        }
        self.documents.append(item)

    def extract_metadata_url(self, jsonld):
        try:
            return self.extract_metadata_url_ieda(jsonld)
        except:
            return jsonld['encoding']['contentUrl']

    def extract_metadata_url_ieda(self, jsonld):
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
        if m is not None:
            if m.group('doi_id') is not None:
                return m.group('doi_id')
            else:
                return m.group('other_id')

        # Try ARM
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
            self.logger.error(msg)
            raise RuntimeError(msg)
        else:
            return m.group('id')

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
