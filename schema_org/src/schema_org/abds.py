"""
DATAONE adapter for Arctic Biodiversity Data Service, IPT (Integrated
Publishing Toolkit).

See http://geo.abds.is/ipt/
"""

# Standard library imports
import io

# 3rd party library imports
import dateutil.parser
import lxml.etree

# Local imports
from .core import CoreHarvester

# Namespaces used in the ABDS RSS feed.
SITEMAP_NS = {
    'ipt': 'http://ipt.gbif.org/',
    'atom': 'http://www.w3.org/2005/Atom',
    'geo':  'http://www.w3.org/2003/01/geo/wgs84_pos#'
}

EML_211_NSMAP = {
    'eml': 'eml://ecoinformatics.org/eml-2.1.1',
    'dc': 'http://purl.org/dc/terms/',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
}


class AbdsIptHarvester(CoreHarvester):

    def __init__(self, **kwargs):
        super().__init__(id='abds_ipt', **kwargs)

        self.sitemap = 'http://geo.abds.is/ipt/rss.do'

    def is_sitemap_index_file(self, doc):
        """
        Answer the question as to whether the document found at the other end
        of the sitemap URL is a sitemap index file - i.e. it references other
        sitemaps - or if it is a sitemap leaf.

        In the case of an RSS fead, no, it is not and index file, it is its own
        leaf.
        """
        return False

    def extract_records_from_sitemap(self, doc):
        """
        Extract all the URLs and lastmod times from the RSS feed.

        Parameters
        ----------
        doc : ElementTree
            XML document constructed out of RSS feed

        Returns
        -------
        List of records (URLs of metadata documents and publishing dates).
        """
        path = 'channel/item/ipt:eml/text()'
        urls = doc.xpath(path, namespaces=SITEMAP_NS)

        path = 'channel/item/pubDate/text()'
        lastmods = doc.xpath(path, namespaces=SITEMAP_NS)
        lastmods = [dateutil.parser.parse(item) for item in lastmods]

        records = [(url, lastmod) for url, lastmod in zip(urls, lastmods)]

        msg = f"Extracted {len(urls)} from the sitemap document."
        self.logger.info(msg)

        return records

    async def retrieve_record(self, metadata_url):
        """
        Retrieve the metadata record

        Parameters
        ----------
        metadata_url : str
            URL for remote XML metadata file

        Returns
        -------
        identifier : str
            Ideally this is a DOI, but here it is a UUID.
        doc : ElementTree
            Metadata document
        """
        self.logger.debug(f'retrieve_record')
        self.logger.info(f"Requesting {metadata_url}...")
        content = await self.retrieve_url(metadata_url)
        doc = lxml.etree.parse(io.BytesIO(content))

        # Normally it would make sense to factor this out, but the schema.org,
        # it gets a lot more complicated.
        identifier = self.extract_identifier(doc)
        self.logger.debug(f"Have extracted the identifier {identifier}...")

        return identifier, doc

    def extract_identifier(self, doc):
        """
        Parse the identifier from the XML.

        Parameters
        ----------
        XML document

        Returns
        -------
        Ideally this is a DOI, but here it is a UUID.
        """
        path = '/eml:eml/dataset/alternateIdentifier[1]/text()'
        elts = doc.xpath(path, namespaces=EML_211_NSMAP)
        identifier = elts[0]
        return identifier
