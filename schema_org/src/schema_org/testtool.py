# Standard library imports
import asyncio
import gzip
import io
import urllib.parse

# 3rd party library imports
import aiohttp
import lxml.etree
import d1_scimeta.validate

# local imports
from .common import (
    CommonHarvester, SITEMAP_RETRIEVAL_FAILURE_MESSAGE,
    SITEMAP_NOT_XML_MESSAGE, DOI_IDENTIFIER_MSG, SUCCESSFUL_INGEST_MESSAGE,
    SITEMAP_NS
)


class D1TestTool(CommonHarvester):

    def __init__(self, sitemap_url=None, **kwargs):
        super().__init__(id='d1checksite', **kwargs)

        self.site_map = sitemap_url

    def harvest_document(self, doi, doc, record_date):
        """
        We don't actually harvest.
        """
        pass

    def summarize(self):
        """
        We don't harvest, so we don't need to summarize it.
        """
        pass


class D1TestToolAsync(D1TestTool):

    def __init__(self, num_workers=1, **kwargs):
        super().__init__(**kwargs)

        self.num_workers = num_workers

    async def _init(self):
        """
        Setup any asyncio resources that really do belong in __init__ if that
        were actually possible.

        Attributes
        ----------
        session : aiohttp session
            Somewhat similar to a requests session

        q : asyncio queue
            URLs for landing page documents go here, to be processed by a set
            number of workers.
        """
        await self._setup_session(None, None)

        self.q = asyncio.Queue()

    async def _setup_session(self, certificate, private_key):
        """
        Instantiate a aiohttp session to help persist certain parameters
        across requests.
        """

        # Setup the client side certificates if that makes sense.
        if certificate is not None or private_key is not None:
            msg = "SSL support not yet implemented."
            raise NotImplementedError(msg)

        # Always send these headers.
        headers = {
            'User-Agent': 'DataONE adapter for schema.org harvest',
            'From': 'jevans97@utk.edu'
        }
        self.session = aiohttp.ClientSession(headers=headers)

    async def _close(self):
        """
        Cannot do this from __del__.
        """
        await self.session.close()

    async def retrieve_url(self, url, headers=None):
        """
        Parameters
        ----------
        url : str
            URL of either an HTML document or an XML metadata document
        headers : dict
            Optional headers to supply with the retrieval.
        """
        self.logger.debug(f'retrieve_url: {url}')
        r = await self.session.get(url, headers=headers)
        r.raise_for_status()
        return r

    async def run(self):

        self.logger.debug(f'run')
        last_harvest_time = self.get_last_harvest_time()

        try:
            await self.process_sitemap(self.site_map, last_harvest_time)
        except Exception as e:
            self.logger.error(repr(e))

        self.summarize()

    async def retrieve_metadata_document(self, metadata_url):
        """
        Retrieve the remote metadata document and make any necessary
        transformations on it.

        Parameters
        ----------
        metadata_url : str
            URL of remote metadata document
        identifier : str
            ID from JSON-LD description

        Returns
        -------
        The ElementTree document.
        """
        self.logger.debug(f'retrieve_metadata_document')
        # Retrieve the metadata document.
        self.logger.info(f"Requesting {metadata_url}...")
        r = await self.retrieve_url(metadata_url)
        try:
            doc = lxml.etree.parse(io.BytesIO(await r.read()))
        except Exception as e:
            msg = (
                f"Unable to parse the metadata document at {metadata_url} "
                f"due to {repr(e)}."
            )
            raise RuntimeError(msg)

        return doc

    async def consume(self, idx, q):
        """
        This corresponse to a worker drone.  Process records while we can.
        """
        self.logger.debug(f'consume({idx}):')
        while True:
            url, lastmod_time = await q.get()
            self.logger.debug(f'consume({idx}) ==>  {url}, {lastmod_time}')
            try:
                await self.process_record(url, lastmod_time)
            except Exception as e:
                self.failed_count += 1
                msg = (
                    f"consume({idx}):  Unable to process {url} due to "
                    f"{repr(e)}."
                )
                self.logger.error(msg)
            else:
                p = urllib.parse.urlparse(url)
                basename = p.path.split('/')[-1]
                msg = (
                    f"consume({idx}):  {SUCCESSFUL_INGEST_MESSAGE}: {basename}"
                )
                self.logger.info(msg)

            q.task_done()

    async def process_record(self, landing_page_url, record_date):
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
        self.logger.debug(f'process_record')
        self.logger.info(f"Requesting {landing_page_url}...")
        r = await self.retrieve_url(landing_page_url)

        try:
            doc = lxml.etree.HTML(await r.text())
        except ValueError:
            doc = lxml.etree.HTML(await r.read())

        jsonld = self.extract_jsonld(doc)

        # Sometimes there is a space in the @id field.  Can't be having any of
        # that...
        identifier = self.extract_identifier(jsonld)
        self.logger.info(f"{DOI_IDENTIFIER_MSG}  {identifier}...")

        metadata_url = self.extract_metadata_url(jsonld)

        doc = await self.retrieve_metadata_document(metadata_url)
        d1_scimeta.validate.assert_valid(self.format_id, doc)

        self.harvest_document(identifier, doc, record_date)

    async def process_sitemap(self, sitemap_url, last_harvest_time):
        """
        Process the sitemap.  This may involve recursive calls.

        Parameters
        ----------
        sitemap_url : str
            URL for a sitemap or sitemap index file
        last_harvest_time : datetime
            According to the MN, this is the last time we, uh, harvested any
            document.
        """
        msg = f"process_sitemap: {sitemap_url}, {last_harvest_time}"
        self.logger.info(msg)

        doc = await self.get_sitemap_document(sitemap_url)
        if self.is_sitemap_index_file(doc):

            sitemap_urls = doc.xpath('sm:sitemap/sm:loc/text()',
                                     namespaces=SITEMAP_NS)

            for sitemap_url in sitemap_urls:
                await self.process_sitemap(sitemap_url, last_harvest_time)

        else:
            await self.process_sitemap_leaf(doc, last_harvest_time)

    async def process_sitemap_leaf(self, doc, last_harvest_time):
        """
        We are at a sitemap leaf, i.e. the sitemap does not reference other
        sitemaps.  This is where we can retrieve landing pages instead of
        other sitemaps.

        Parameters
        ----------
        doc : ElementTree object
            Describes the sitemap leaf.
        last_harvest_time : datetime
            According to the MN, this is the last time we, uh, harvested any
            document.
        """
        self.logger.debug(f'process_sitemap_leaf:')

        records = self.extract_records_from_sitemap(doc, last_harvest_time)
        for url, lastmod_time in records:
            self.q.put_nowait((url, lastmod_time))

        # Create the worker tasks to consume the URLs
        tasks = []
        for j in range(self.num_workers):
            task = asyncio.create_task(self.consume(j, self.q))
            tasks.append(task)
        await self.q.join()

        # Cancel any remaining tasks.
        for task in tasks:
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)

    async def get_sitemap_document(self, sitemap_url):
        """
        Parameters
        ---------
        sitemap_url : str
            URL for a sitemap or sitemap index file.
        """
        self.logger.debug(f'get_sitemap_document: {sitemap_url}')
        try:
            r = await self.retrieve_url(sitemap_url)
        except Exception as e:
            msg = f"{SITEMAP_RETRIEVAL_FAILURE_MESSAGE} due to {repr(e)}"
            self.logger.error(msg)
            raise

        if r.headers['Content-Type'] not in ['text/xml', 'application/x-gzip']:
            self.logger.warning(SITEMAP_NOT_XML_MESSAGE)

        try:
            doc = lxml.etree.parse(io.BytesIO(await r.read()))
        except lxml.etree.XMLSyntaxError as e:
            msg1 = repr(e)

            # was it compressed?
            try:
                content = await r.read()
                doc = lxml.etree.parse(io.BytesIO(gzip.decompress(content)))
            except OSError as e:
                # Must not have been gzipped.
                # TODO:  more exceptions possible here
                self.logger.error(msg1)
                self.logger.error(repr(e))
                msg = f'Unable to process the sitemap {sitemap_url}.'
                raise RuntimeError(msg)

        return doc


async def run_test_tool(sitemap_url, **kwargs):
    """
    See https://stackoverflow.com
        /questions/33128325
        /how-to-set-class-attribute-with-await-in-init/33134213
    for the reason behind this.  asyncio not well adapted to magic methods just
    yet, it would seem.
    """
    obj = D1TestToolAsync(sitemap_url=sitemap_url, **kwargs)
    await obj._init()
    await obj.run()
    await obj._close()
