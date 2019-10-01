"""
DATAONE adapter for Arctic Biodiversity Data Service GeoNetwork Catalog
(different from IPT).

See http://geonetwork-opensource.org

There is a JSON resource with metadata about all the metadata.

metadata URL:
    Always given by http://geo.abds.is/geonetwork/srv/eng/xml.metadata.get, but
    with different GET parameters.
lastModified:
    given by the 'changeDate' key for each item
PID (record version):
    given by a UUID in each item
SID (series ID):
    Computed as a checksum
"""

# Standard library imports
import io

# 3rd party library imports
import dateutil.parser
import dateutil.utils
import lxml.etree

# Local imports
from .core import CoreHarvester, SITEMAP_RETRIEVAL_FAILURE_MESSAGE

# Namespaces used in the ABDS GeoNetwork feed.
SITEMAP_NS = {
    'gmd':  'http://www.isotc211.org/2005/gmd',
    'gco':  'http://www.isotc211.org/2005/gco',
    'gts':  'http://www.isotc211.org/2005/gts',
    'srv':  'http://www.isotc211.org/2005/srv',
    'gml':  'http://www.opengis.net/gml',
    'xlink':  'http://www.w3.org/1999/xlink',
    'geonet':  'http://www.fao.org/geonetwork',
}


class AbdsGeonetHarvester(CoreHarvester):

    def __init__(self, **kwargs):
        super().__init__(id='abds_geonet', **kwargs)

        self.sitemap = (
            'http://geo.abds.is/geonetwork/srv/eng/q'
            '?_content_type=json'
            '&facet.q='
            '&fast=index'
            '&from=1'
            '&resultType=details'
            '&sortBy=relevance'
        )

        self.sys_meta_dict['authoritativeMN'] = 'urn:node:mnTestABDSGeonet'
        self.sys_meta_dict['originMN'] = 'urn:node:mnTestABDSGeonet'
        self.sys_meta_dict['rightsholder'] = 'CN=urn:node:mnTestABDSGeonet,DC=dataone,DC=org'  # noqa : E501
        self.sys_meta_dict['submitter'] = 'CN=urn:node:mnTestABDSGeonet,DC=dataone,DC=org'  # noqa : E501

    async def get_sitemap_document(self, sitemap_url):
        """
        Retrieve a remote sitemap document.

        Parameters
        ---------
        sitemap_url : str
            URL for a sitemap or sitemap index file.
        """
        self.logger.info(f'Requesting sitemap document from {sitemap_url}')

        try:
            j = await self.retrieve_url(sitemap_url, return_json=True)
        except Exception as e:
            msg = f"{SITEMAP_RETRIEVAL_FAILURE_MESSAGE} due to {e}"
            self.logger.error(msg)
            raise

        return j

    async def process_sitemap(self, sitemap_url, last_harvest):
        """
        Determine if the sitemap (or RSS feed or whatever) is an index file
        or whether it is a single document.  If an index file, we need to
        descend recursively into it.

        Parameters
        ----------
        sitemap_url : str
            URL for a sitemap or sitemap index file
        last_harvest : datetime
            According to the MN, this is the last time we, uh, harvested any
            document.
        """
        msg = f"process_sitemap: {sitemap_url}, {last_harvest}"
        self.logger.debug(msg)

        j = await self.get_sitemap_document(sitemap_url)

        self.logger.debug("process_sitemap:  This is a sitemap leaf.")
        await self.process_sitemap_leaf(j, last_harvest)

    def extract_records_from_sitemap(self, j):
        """
        Extract all the URLs and lastmod times from the JSON feed.
        """
        record_url = 'http://geo.abds.is/geonetwork/srv/eng/xml.metadata.get'
        items = j['metadata']
        urls = [
            f"{record_url}?id={item['geonet:info']['id']}" for item in items
        ]

        lastmods = [
            dateutil.parser.parse(item['geonet:info']['changeDate'])
            for item in items
        ]

        # Make them timezone-aware.
        UTC = dateutil.tz.gettz("UTC")
        lastmods = [dateutil.utils.default_tzinfo(dt, UTC) for dt in lastmods]

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
        sid : str
            Ideally this is a DOI, but here it is a UUID.
        pid : str
            The version of the document.
        doc : ElementTree
            Metadata document
        """
        self.logger.debug(f'retrieve_record')
        self.logger.info(f"Requesting {metadata_url}...")
        content = await self.retrieve_url(metadata_url)
        doc = lxml.etree.parse(io.BytesIO(content))

        sid = self.extract_series_identifier(doc)
        self.logger.debug(f"Have extracted the identifier {sid}...")

        return sid, None, doc

    def extract_series_identifier(self, doc):
        """
        Parse the identifier from the XML.

        Parameters
        ----------
        XML document

        Returns
        -------
        Ideally this is a DOI, but here it is a UUID.
        """
        path = 'gmd:fileIdentifier/gco:CharacterString/text()'
        elts = doc.xpath(path, namespaces=SITEMAP_NS)
        identifier = elts[0]
        return identifier
