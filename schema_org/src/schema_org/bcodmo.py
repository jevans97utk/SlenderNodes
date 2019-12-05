"""
DATAONE adapter for BCO-DMO

metadata URL:
    Must be retrieved via another hop from landing page JSON-LD
lastModified:
    Taken from the sitemap.
PID (record version):
    None
SID (series ID):
    DOI taken from the '@id' key in the JSON-LD.
"""

# Standard library imports
import io
import json

# 3rd party library imports
import lxml.etree

# Local imports
from .so_core import SchemaDotOrgHarvester
from . import sotools


class BCODMOHarvester(SchemaDotOrgHarvester):

    def __init__(self, host='localhost', port=443, **kwargs):
        sitemap_url = 'https://www.bco-dmo.org/sitemap.xml'
        kwargs['sitemap_url'] = sitemap_url

        super().__init__(id='bcodmo', host=host, port=port, base_path='/bcodmo',
                         **kwargs)

        authoritative_mn = 'urn:node:mnTestBCODMO'
        self.sys_meta_dict['authoritativeMN'] = authoritative_mn
        self.sys_meta_dict['originMN'] = authoritative_mn

        rightsholder = 'CN=urn:node:mnTestBCODMO,DC=dataone,DC=org'
        self.sys_meta_dict['rightsholder'] = rightsholder
        self.sys_meta_dict['submitter'] = rightsholder

    def post_process_sitemap_records(self, records, last_harvest_time):
        """
        Prune the sitemap records for various reasons.  In addition to the
        superclass reasons, we also prune any URL that does not contain the
        string "dataset".

        Parameters
        ----------
        records : list
            Each item in the list is composed of a URL and a last modification
            date.
        """
        # If we do not wish to ignore the last harvest time, then only those
        # records in the sitemap that are newer than the last harvest time will
        # pass through.
        records = super().post_process_sitemap_records(records,
                                                       last_harvest_time)
        nrecs = len(records)

        records = [
            (url, lastmod) for url, lastmod in records
            if 'dataset' in url
        ]

        num_skipped = nrecs - len(records)
        msg = (
            f"{num_skipped} records skipped due to dataset-in-URL restriction."
        )
        self.logger.info(msg)

        return records

    async def retrieve_record(self, landing_page_url):
        """
        Read the remote document, extract the JSON-LD, and load it into the
        system.

        Parameters
        ----------
        landing_page_url : str
            URL for remote landing page HTML

        Returns
        -------
        sid : str
            Node's system identifier for this object, which becomes the
            series ID.
        pid : str
            Intended to be the GMN unique identifier of the science
            metadata record to be archived.
        last_modified : datetime or None
        doc : ElementTree
        """
        content, _ = await self.retrieve_url(landing_page_url)
        html = content.decode('utf-8')
        doc = lxml.etree.HTML(content)

        # This section of code may be removable.
        # jsonld = self.get_jsonld(doc)
        # self.validate_dataone_so_jsonld(jsonld)

        g = sotools.common.loadSOGraphFromHtml(html, landing_page_url)

        identifiers = sotools.common.getLiteralDatasetIdentifiers(g)
        sid = identifiers[0]['value']
        self.logger.debug(f"Series ID (sid): {sid}")

        # extract the PID
        # This is currently None for ARM.  Will it be the case for all SO
        # documents?  Non-SO docs must provide custom code to get the PID.
        pid = None

        # No dateModified, so we will rely upon the sitemap for this.
        dateModified = None


        # extract the XML metadata URL.  We have to get an intermediate URL
        # first.
        intermediate_url = self.get_bcodmo_json_datapackage_url(g)
        contents, _ = await self.retrieve_url(intermediate_url)
        j = json.load(io.BytesIO(contents))

        metadata_links = [
            x for x in j['resources']
            if x['odo:hasFileType'] == 'odo:Metadata_FileType'
        ]
        metadata_link = metadata_links[0]['path']

        doc = await self.retrieve_metadata_document(metadata_link)

        self.logger.debug(f"Record version (pid): {pid}")

        return sid, pid, dateModified, doc

    def get_bcodmo_json_datapackage_url(self, g):
        """
        """
        SPARQL_PREFIXES = """
            PREFIX rdf:      <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX ODO:      <http://ocean-data.org/schema/>
            PREFIX SO:       <https://schema.org/>
            PREFIX xsd:      <http://www.w3.org/2001/XMLSchema#>
            PREFIX datacite: <http://purl.org/spar/datacite/>
        """

        q = (
            SPARQL_PREFIXES
            + """
        SELECT ?contentUrl
        WHERE {
            ?x rdf:type SO:Dataset .
            ?y rdf:type SO:DataDownload .
            ?y SO:contentUrl ?contentUrl .
            ?y SO:encodingFormat ?encodingFormat .
            FILTER (str(?encodingFormat) = 'application/vnd.datapackage+json') .
        }
        """
        )
        res = []
        qres = g.query(q)
        for v in qres:
            res.append({"value": str(v[0]), "propertyId":"Literal"})
        return res[0]['value']
    
