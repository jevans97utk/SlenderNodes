"""
DATAONE SO core for multiple adaptors.
"""

# Standard library imports
import asyncio
import gzip
import io
import json
import re
import urllib.parse
import zipfile

# 3rd party library imports
import aiohttp
import dateutil.parser
import lxml.etree

# Local imports
from .core import CoreHarvester, SkipError
from .jsonld_validator import JSONLD_Validator

SITEMAP_RETRIEVAL_FAILURE_MESSAGE = 'Failed to retrieve the site map.'
NO_JSON_LD_SCRIPT_ELEMENTS = "No JSON-LD <SCRIPT> elements were located."
SITEMAP_NOT_XML_MESSAGE = "The sitemap may not be XML."
SUCCESSFUL_INGEST_MESSAGE = "Successfully processed record"

SITEMAP_NS = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}


class SchemaDotOrgHarvester(CoreHarvester):
    """
    Harvester object with schema.org support.

    Attributes
    ----------
    jsonld_validator : obj
        Run conformance checks on the JSON-LD extracted from a site page.
    site_map : str
        URL for XML site map.  This must be overridden for each custom client.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.jsonld_validator = JSONLD_Validator(logger=self.logger)
        self.site_map = 'https://www.archive.arm.gov/metadata/adc/sitemap.xml'

    def extract_jsonld(self, doc):
        """
        Extract JSON-LD from HTML document.

        What we hope for is that:
            1) jsonld['distribution'][0]['name'] = 'ISO Metadata Document'
            2) jsonld['distribution'][0]['url'] is the XML url
            3) jsonld['distribution'][1]['name'] = 'landing page'

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
            raise RuntimeError(NO_JSON_LD_SCRIPT_ELEMENTS)

        jsonld = None
        for script in scripts:

            j = json.loads(script.text)
            if '@type' in j and j['@type'] == 'Dataset':
                jsonld = j

        if jsonld is None:
            msg = (
                "Could not locate a JSON-LD <SCRIPT> element with @type "
                "\"Dataset\"."
            )
            raise RuntimeError(msg)

        return jsonld

    def is_sitemap_index_file(self, doc):
        """
        Answer the question as to whether the document found at the other end
        of the sitemap URL is a sitemap index file - i.e. it references other
        sitemaps - or if it is a sitemap leaf.
        """

        elts = doc.xpath('sm:sitemap', namespaces=SITEMAP_NS)
        if len(elts) > 0:
            return True
        else:
            return False

    def extract_records_from_sitemap(self, doc, last_harvest_time):
        """
        Extract all the URLs and lastmod times from an XML sitemap.
        """

        urls = doc.xpath('.//sm:loc/text()', namespaces=SITEMAP_NS)

        lastmods = doc.xpath('.//sm:lastmod/text()',
                             namespaces=SITEMAP_NS)
        if len(lastmods) == 0:
            # Sometimes a sitemap has no <lastmod> items at all.  That's ok.
            lastmods = [
                dateutil.parser.parse('1950-01-01T00:00:00Z')
                for url in urls
            ]
        else:
            # Parse the last modification times.  It is possible that the dates
            # have no timezone information in them, so we will assume that it
            # is UTC.
            lastmods = [dateutil.parser.parse(item) for item in lastmods]
            UTC = dateutil.tz.gettz("UTC")
            lastmods = [
                dateitem.replace(tzinfo=dateitem.tzinfo or UTC)
                for dateitem in lastmods
            ]

        z = zip(urls, lastmods)

        msg = f"Extracted {len(urls)} from the sitemap document."
        self.logger.info(msg)

        records = [
            (url, lastmod) for url, lastmod in z if lastmod > last_harvest_time
        ]

        msg = (
            f"{len(urls) - len(records)} records skipped due to lastmod time."
        )
        self.logger.info(msg)

        # Further restrict by regex if so specified.
        if self.regex is not None:
            nrecs = len(records)
            records = [
                (url, lastmod) for url, lastmod in records
                if self.regex.search(url)
            ]
            num_skipped = nrecs - len(records)
            msg = f"{num_skipped} records skipped due to regex restriction."
            self.logger.info(msg)

        self.num_records_processed += len(records)
        if (
            self.num_records_processed > self.num_documents
            and self.num_documents > -1
        ):
            diff = self.num_records_processed - self.num_documents
            records = records[:-diff]

        msg = f"Looking to process {len(records)} records..."
        self.logger.info(msg)
        return records

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
        pattern = r'''
                  # DOI:prefix/suffix - ARM style
                  (https?://dx.doi.org/(?P<doi>10\.\w+/\w+))
                  '''
        regex = re.compile(pattern, re.VERBOSE)
        m = regex.search(jsonld['@id'])
        if m is None:
            msg = (
                f"DOI ID parsing error, could not parse an ID out of "
                f"JSON-LD '@id' element \"{jsonld['@id']}\""
            )
            raise RuntimeError(msg)

        return m.group('doi')

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

            except asyncio.CancelledError:
                self.logger.debug('CancelledError')
                break

            except aiohttp.ClientResponseError as e:
                msg =  (
                    f"aiohttp.ClientResponseError:  "
                    f"Unable to process {url} due to \"{e}\"."
                )
                self.logger.warning(msg)
                self.asyncio_aiohttp_warning_count += 1

            except (asyncio.TimeoutError, aiohttp.ClientPayloadError, zipfile.BadZipFile) as e:
                msg =  f"Unable to process {url} due to \"{e}\"."
                self.logger.warning(msg)
                self.asyncio_aiohttp_warning_count += 1

            except SkipError as e:
                msg =  f"Unable to process {url} due to \"{e}\"."
                self.logger.warning(msg)
                self.skipped_count += 1

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
        doc = lxml.etree.HTML(content)

        jsonld = self.extract_jsonld(doc)
        self.jsonld_validator.check(jsonld)

        identifier = self.extract_identifier(jsonld)
        self.logger.debug(f"Have extracted the identifier {identifier}...")

        metadata_url = jsonld['encoding']['contentUrl']

        doc = await self.retrieve_metadata_document(metadata_url)
        return identifier, doc

    async def process_sitemap(self, sitemap_url, last_harvest):
        """
        Process the sitemap.  This may involve recursive calls.

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

        doc = await self.get_sitemap_document(sitemap_url)
        if self.is_sitemap_index_file(doc):

            self.logger.debug("It is a sitemap index file.")
            path = 'sm:sitemap/sm:loc/text()'
            sitemap_urls = doc.xpath(path, namespaces=SITEMAP_NS)
            for sitemap_url in sitemap_urls:
                await self.process_sitemap(sitemap_url, last_harvest)

        else:

            self.logger.debug("It is a sitemap leaf.")
            await self.process_sitemap_leaf(doc, last_harvest)

    async def process_sitemap_leaf(self, doc, last_harvest):
        """
        We are at a sitemap leaf, i.e. the sitemap does not reference other
        sitemaps.  This is where we can retrieve landing pages instead of
        other sitemaps.

        Parameters
        ----------
        doc : ElementTree object
            Describes the sitemap leaf.
        last_harvest : datetime
            According to the MN, this is the last time we, uh, harvested any
            document.
        """
        self.logger.debug(f'process_sitemap_leaf:')

        sitemap_queue = asyncio.Queue()

        records = self.extract_records_from_sitemap(doc, last_harvest)
        for url, lastmod_time in records:
            sitemap_queue.put_nowait((url, lastmod_time))

        # Create the worker tasks to consume the URLs
        tasks = []
        for j in range(self.num_workers):
            msg = (
                f'process_sitemap_leaf: create task for sitemap_consumer[{j}]'
            )
            self.logger.debug(msg)
            task = asyncio.create_task(self.consume_sitemap(j, sitemap_queue))
            tasks.append(task)
        await sitemap_queue.join()

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
            content = await self.retrieve_url(sitemap_url,
                                              check_xml_headers=True)
        except Exception as e:
            msg = f"{SITEMAP_RETRIEVAL_FAILURE_MESSAGE} due to {repr(e)}"
            self.logger.error(msg)
            raise

        try:
            doc = lxml.etree.parse(io.BytesIO(content))
        except lxml.etree.XMLSyntaxError as e:
            msg1 = repr(e)

            # was it compressed?
            try:
                doc = lxml.etree.parse(io.BytesIO(gzip.decompress(content)))
            except OSError as e:
                # Must not have been gzipped.
                # TODO:  more exceptions possible here
                self.logger.error(msg1)
                self.logger.error(repr(e))
                msg = f'Unable to process the sitemap {sitemap_url}.'
                raise RuntimeError(msg)

        return doc
