"""
DATAONE adapter for ABDS IPT.

See http://geo.abds.is/ipt/
"""

# Standard library imports
import importlib.resources as ir
import io
import json
import urllib.parse
import zipfile

# 3rd party library imports
import dateutil.parser
import lxml.etree

# Local imports
from .core import CoreHarvester, SkipError, SUCCESSFUL_INGEST_MESSAGE

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

        self.site_map = 'http://geo.abds.is/ipt/rss.do'

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
        """
        self.logger.debug(f'retrieve_record')
        self.logger.info(f"Requesting {metadata_url}...")
        content = await self.retrieve_url(metadata_url)
        doc = lxml.etree.parse(io.BytesIO(content))

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
        The identifier
        """
        path = '/eml:eml/dataset/alternateIdentifier[1]/text()'
        elts = doc.xpath(path, namespaces=EML_211_NSMAP)
        identifier = elts[0]
        return identifier


