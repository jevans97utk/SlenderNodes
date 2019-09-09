"""
DATAONE adapter for CUAHSI
"""

# Standard library imports
import asyncio
import importlib.resources as ir
import io
import json
import urllib.parse
import zipfile

# 3rd party library imports
import aiohttp
import lxml.etree

# Local imports
from .so_core import SchemaDotOrgHarvester, NO_JSON_LD_SCRIPT_ELEMENTS
from .core import SkipError, SUCCESSFUL_INGEST_MESSAGE


class CUAHSIHarvester(SchemaDotOrgHarvester):

    def __init__(self, **kwargs):
        super().__init__(id='cuahsi', **kwargs)

        # Create the XSLT stylesheet for transforming the CUAHSI documents
        # from their native format to something we can use (simplified DC).
        content = ir.read_binary('schema_org.data', 'simple_d1_dublincore.xsl')
        xslt_tree = lxml.etree.XML(content)
        self.transform_to_dataone_simple_dc = lxml.etree.XSLT(xslt_tree)

        self.site_map = 'https://www.hydroshare.org/sitemap.xml'

        self.asyncio_timeout_error_count = 0
        self.aiohttp_client_payload_error_count = 0
        self.aiohttp_client_response_error_count = 0
        self.zipfile_error_count = 0

    async def consume_sitemap(self, idx, sitemap_queue):
        """
        In a producer/consumer paradigm, here we are consuming work items
        from the sitemap.

        Parameters
        ----------
        idx:  int
            The only purpose for this is to identify the consumer in the logs.
        sitemap_queue : asyncio.Queue
            Holds URLs and modification times retrieved from the sitemap.
        """
        while True:
            try:
                url, lastmod_time = await sitemap_queue.get()
                msg = f'sitemap_consumer[{idx}] ==>  {url}, {lastmod_time}'
                self.logger.debug(msg)

                await self.process_record(url, lastmod_time)

            except aiohttp.ClientPayloadError as e:
                msg = (
                    f"aiohttp.ClientPayloadError:  "
                    f"Unable to process {url} due to \"{e}\"."
                )
                self.logger.warning(msg)
                self.aiohttp_client_payload_error_count += 1

            except aiohttp.ClientResponseError as e:
                msg = (
                    f"aiohttp.ClientResponseError:  "
                    f"Unable to process {url} due to \"{e}\"."
                )
                self.logger.warning(msg)
                self.aiohttp_client_response_error_count += 1

            except asyncio.CancelledError:
                self.logger.debug('CancelledError')
                break

            except asyncio.TimeoutError as e:
                msg = f"asyncio.TimeoutError:  Unable to process {url}:  {e}."
                self.logger.warning(msg)
                self.asyncio_timeout_error_count += 1

            except zipfile.BadZipFile as e:
                msg = (
                    f"zipfile.BadZipFile:  Unable to process {url} due to {e}."
                )
                self.logger.warning(msg)
                self.zipfile_error_count += 1

            except SkipError as e:
                msg = f"Unable to process {url}:  {e}."
                self.logger.warning(msg)
                self.skipped_count += 1

            except RuntimeError as e:
                self.failed_count += 1
                msg = f"RuntimeError:  Unable to process {url} due to \"{e}\"."
                self.logger.error(msg)

                if self.failed_count == self.max_num_errors:
                    self.logger.warning("Error threshold reached.")
                    await self.shutdown()

            except Exception as e:
                self.failed_count += 1
                msg = f"Unable to process {url} due to \"{repr(e)}\"."
                self.logger.error(msg)

                if self.failed_count == self.max_num_errors:
                    self.logger.warning("Error threshold reached.")
                    await self.shutdown()

            else:
                # Use the last part of the URL to identify the record that was
                # successfully processed.
                p = urllib.parse.urlparse(url)
                basename = p.path.split('/')[-1]
                msg = (
                    f"sitemap_consumer[{idx}]:  "
                    f"{SUCCESSFUL_INGEST_MESSAGE}: {basename}"
                )
                self.logger.debug(msg)

                msg = f"{SUCCESSFUL_INGEST_MESSAGE}: {basename}"
                self.logger.info(msg)
                self.processed_count += 1

            sitemap_queue.task_done()

    def preprocess_landing_page(self, landing_page_doc):
        """
        Check the landing page for any information we may need OTHER than
        JSON-LD.

        Parameters
        ----------
        landing_page_doc : lxml element tree
            Document corresponding to the HTML landing page.
        """
        path = './/td[@id="hl-sharing-status"]/text()'
        elts = landing_page_doc.xpath(path)
        if len(elts) == 0:
            msg = "No sharing status element found."
            self.logger.debug(msg)
            raise SkipError(msg)

        sharing_status = elts[0].strip().upper()

        self.logger.debug(f"Sharing status is {sharing_status}.")
        if sharing_status != 'PUBLISHED':
            msg = (
                f"CUAHSI landing page sharing status is {sharing_status} "
                f"instead of PUBLISHED."
            )
            raise SkipError(msg)

    def extract_jsonld(self, doc):
        """
        Extract JSON-LD from HTML document.

        Parameters
        ----------
        doc : ElementTree
            The parsed HTML.  The JSON-LD should be embedded within a
            <SCRIPT> element embedded in the <HEAD> element.
        """
        self.logger.debug('extract_jsonld:')
        path = './/script[@type="application/ld+json"]'
        scripts = doc.xpath(path)
        if len(scripts) == 0:
            raise SkipError(NO_JSON_LD_SCRIPT_ELEMENTS)

        jsonld = json.loads(scripts[0].text)
        return jsonld

    async def retrieve_record(self, landing_page_url):
        """
        Read the remote document, extract the JSON-LD, and load it into the
        system.

        Parameters
        ----------
        landing_page_url : str
            URL for remote landing page HTML
        """
        self.logger.debug(f'retrieve_record')
        self.logger.info(f"Requesting {landing_page_url}...")
        content = await self.retrieve_url(landing_page_url)
        self.logger.debug(f'got the landing page')
        doc = lxml.etree.HTML(content)
        self.logger.debug(f'got the doc')

        self.preprocess_landing_page(doc)
        self.logger.debug(f'pre-processed the landing page')

        jsonld = self.extract_jsonld(doc)
        self.logger.debug(f'got the JSON-LD')

        # Don't bother validating, we know it fails.
        # self.jsonld_validator.check(jsonld)

        identifier = self.extract_identifier(jsonld)
        self.logger.debug(f"Have extracted the identifier {identifier}...")

        # Construct the URL for the bagit zip archive.
        path = './/a[@id="btn-download-all"]'
        elt = doc.xpath(path)[0]
        if 'href' not in elt.attrib:
            msg = (
                f"The landing page at {landing_page_url} likely has a dialog "
                f"pop-up that is fouling our attempts to download the zip "
                f"archive.  This needs to be addressed."
            )
            raise SkipError(msg)

        url = 'https://www.hydroshare.org/' + elt.attrib['href']

        doc = await self.retrieve_metadata_document(url)

        # Must transform the document.
        doc = self.transform_to_dataone_simple_dc(doc)

        return identifier, doc

    def extract_identifier(self, jsonld):
        """
        Parse the DOI from the json['@id'] value.  The identifiers should
        look something like

            'https://dx.doi.org/10.5439/1025173

        The DOI in this case would be '10.5439/1025173'.  This will be used as
        the series identifier.

        Parameters
        ----------
        JSON-LD obj

        Returns
        -------
        The identifier substring.
        """
        identifier = jsonld['identifier']['value']
        return identifier

    async def retrieve_metadata_document(self, url):
        """
        Retrieve the remote metadata document and make any necessary
        transformations on it.

        Parameters
        ----------
        url : str
            URL of remote bagit zip archive

        Returns
        -------
        The ElementTree document.
        """

        self.logger.debug(f'Requesting bagit zip archive: {url}')

        # Retrieve the metadata document.
        zip_content = await self.retrieve_url(url)
        self.logger.debug(f'zip archive length: {len(zip_content)}')

        b = io.BytesIO(zip_content)
        zf = zipfile.ZipFile(b)

        for name in zf.namelist():
            if 'resourcemetadata' in name:
                with zf.open(name, mode='r') as f:
                    content = f.read()

        try:
            doc = lxml.etree.parse(io.BytesIO(content))
        except Exception as e:
            msg = f"Unable to parse the metadata document at {url}:  {e}."
            raise RuntimeError(msg)

        self.logger.debug('Got the metadata document')
        return doc

    def summarize(self):

        super().summarize()
        msg = (
            f'Skipped {self.asyncio_timeout_error_count} records due to '
            f'asyncio timeouts.'
        )
        self.logger.info(msg)

        msg = (
            f'Skipped {self.aiohttp_payload_error_count} records due to '
            f'aiohttp payload errors.'
        )
        self.logger.info(msg)

        msg = (
            f'Skipped {self.aiohttp_payload_error_count} records due to '
            f'aiohttp response errors.'
        )
        self.logger.info(msg)

        msg = (
            f'Skipped {self.zipfile_error_count} records due to '
            f'zipfile errors.'
        )
        self.logger.info(msg)
