"""
DATAONE adapter for ARM
"""

# Standard library imports
import asyncio
import gzip
import io
import json
import logging
import re
import sys
import urllib.parse

# 3rd party library imports
import aiohttp
import dateutil.parser
import lxml.etree
import requests
import d1_scimeta.validate

# Local imports
from .d1_client_manager import D1ClientManager
from .jsonld_validator import JSONLD_Validator

UNESCAPED_DOUBLE_QUOTES_MSG = 'Unescaped double-quotes have been corrected.'
OVER_ESCAPED_DOUBLE_QUOTES_MSG = (
    'Over-escaped double quotes have been corrected.'
)
SITEMAP_RETRIEVAL_FAILURE_MESSAGE = 'Failed to retrieve the site map.'
NO_JSON_LD_SCRIPT_ELEMENTS = "No JSON-LD <SCRIPT> elements were located."
DOI_IDENTIFIER_MSG = "Have extracted the identifier:  "
SITEMAP_NOT_XML_MESSAGE = "The sitemap may not be XML."
SUCCESSFUL_INGEST_MESSAGE = "Successfully processed record"

ISO_NSMAP = {
    'gmd': 'http://www.isotc211.org/2005/gmd',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'gco': 'http://www.isotc211.org/2005/gco',
    'gml': 'http://www.opengis.net/gml/3.2',
    'xlink': 'http://www.w3.org/1999/xlink',
    'xs': 'http://www.w3.org/2001/XMLSchema'
}

SITEMAP_NS = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}


class CommonHarvester(object):
    """
    Attributes
    ----------
    mn_host : str
        name of the gmn member node host
    client_mgs : object
        Handles direct communication with dataone host.
    {created,failed,rejected_skipped_exists,updated}_count t: int
        Counters for the different ways that records are handled.  "failed" is
        different from "rejected" in the sense that this code knows why a
        rejection occurs.
    jsonld_validator : obj
        Run conformance checks on the JSON-LD extracted from a site page.
    logger : logging.Logger
        All events are recorded by this object.
    max_num_errors : int
        Abort if this threshold is reached.
    mn_base_url : str
        URL for contacting the dataONE host.
    num_documents : int
        Limit the number of documents to this number.  Less than zero
        means retrieve them all.
    num_records_processed : int
        Running total of number of records processed so far.
    num_workers : int
        Limit number of workers operating asynchronously to this number.  If
        1, then it is essentially synchronous.
    session : requests.sessions.Session
        Makes all URL requests.
    """

    def __init__(self, host=None, port=None, certificate=None,
                 private_key=None, verbosity='INFO', id='none',
                 num_documents=-1, num_workers=1, max_num_errors=3):
        """
        Parameters
        ----------
        host, port : str, int
            This fully identifies the DataONE host and port number where we
            will be sending metadata records.
        certificate, key : str or path or None
            Paths to client side certificates.  None if no verification is
            desired.
        max_num_errors : int
            Abort if this threshold is reached.
        num_documents : int
            Limit the number of documents to this number.  Less than zero
            means retrieve them all.
        """
        self.mn_host = host

        self.setup_session(certificate, private_key)

        self.setup_logging(id, verbosity)

        self.mn_base_url = f'https://{host}:{port}/mn'
        sys_meta_dict = {
            'submitter': f'urn:node:{id.upper()}',
            'rightsholder': f'urn:node:{id.upper()}',

            # Use your node's DataONE URI
            'authoritativeMN': f'urn:node:mnTest{id.upper()}',

            # Use your node's DataONE URI
            'originMN': f'urn:node:{id.upper()}',

            # should be consistent w/ scimeta_element format
            'formatId_custom': 'http://www.isotc211.org/2005/gmd'
        }

        self.client_mgr = D1ClientManager(self.mn_base_url,
                                          certificate, private_key,
                                          sys_meta_dict,
                                          self.logger)
        self.format_id = 'http://www.isotc211.org/2005/gmd'

        self.jsonld_validator = JSONLD_Validator(logger=self.logger)

        # Count the different ways that we update/create/skip records.  This
        # will be logged when we are finished.
        self.created_count = 0
        self.failed_count = 0
        self.rejected_count = 0
        self.skipped_exists_count = 0
        self.updated_count = 0
        self.processed_count = 0

        self.num_documents = num_documents
        self.num_records_processed = 0

        self.num_workers = num_workers

        self.max_num_errors = max_num_errors

        requests.packages.urllib3.disable_warnings()

    def setup_session(self, certificate, private_key):
        """
        Instantiate a requests session to help persist certain parameters
        across requests.

        See https://2.python-requests.org/en/master/user/advanced/ for further
        information.
        """

        self.session = requests.Session()

        # Setup the client side certificates if that makes sense.
        if certificate is None and private_key is None:
            self.session.verify = False
        else:
            self.session.cert = (certificate, private_key)

        # Always send these headers.
        self.session.headers = {
            'User-Agent': 'DataONE adapter for schema.org harvest',
            'From': 'jevans97@utk.edu'
        }

    def setup_logging(self, logid, verbosity):
        """
        Parameters
        ----------
        verbosity : str
            Level of logging verbosity.
        """
        level = getattr(logging, verbosity)

        self.logger = logging.getLogger('datatone')
        self.logger.setLevel(level)

        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(format)

        # Log to file
        #
        # I admit that the use of "delay" is only to prevent warnings being
        # issued during testing.
        fh = logging.FileHandler(f'{logid}.log', delay=True)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        # Also log to stdout.
        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(formatter)
        self.logger.addHandler(sh)

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

    def get_last_harvest_time(self):

        if self.mn_host is not None:
            last_harvest_time_str = self.client_mgr.get_last_harvest_time()
            last_harvest_time = dateutil.parser.parse(last_harvest_time_str)
            self.logger.info(f'Last harvest time:  {last_harvest_time}')
        else:
            last_harvest_time_str = '1900-01-01T00:00:00Z'
            last_harvest_time = dateutil.parser.parse(last_harvest_time_str)

        return last_harvest_time

    def summarize(self):

        self.logger.info(f'Created {self.created_count} new records.')
        self.logger.info(f'Updated {self.updated_count} records.')
        self.logger.info(f'Skipped {self.skipped_exists_count} records.')
        self.logger.info(f'Rejected {self.rejected_count} records.')
        self.logger.info(f'Failed to update/create {self.failed_count} records.')  # noqa: E501

    async def shutdown(self):
        """
        Clean up tasks tied to the service's shutdown.
        """
        msg = 'Shutting down...'
        self.logger.info(msg)

        tasks = [
            t for t in asyncio.all_tasks() if t is not asyncio.current_task()
        ]
        msg = f"Cancelling {len(tasks)} outstanding tasks."
        self.logger.info(msg)
        [task.cancel() for task in tasks]
        await asyncio.gather(*tasks, return_exceptions=True)

    async def harvest_document(self, doi, doc, record_date):
        """
        Check if the member node has seen the document before and decide how to
        harvest it (or not) accordingly.

        Parameters
        ----------
        doi : str
            Handle used to identify objects uniquely.
        doc : bytes
            serialized version of XML metadata document
        record_date : datetime obj
            Last document modification time according to the site map.
        """
        self.logger.debug(f'harvest_document:  {doi}')

        # Re-seriealize to bytes.
        docbytes = lxml.etree.tostring(doc, pretty_print=True,
                                       encoding='utf-8', standalone=True)

        exists_dict = self.client_mgr.check_if_identifier_exists(doi)

        if (
            exists_dict['outcome'] == 'yes'
            and exists_dict['record_date'] != record_date
        ):
            current_sid = exists_dict['current_version_id']
            if not await self.can_be_updated(docbytes, doi, current_sid):
                self.rejected_count += 1
                self.logger.warning(f'Refused to update {doi}.')

            # the outcome of exists_dict determines how to
            # handle the record.  if identifier exists in GMN but
            # record date is different, this truly is an update so
            # call update method.
            elif self.client_mgr.update_science_metadata(
                docbytes,
                doi,
                record_date,
                exists_dict['current_version_id']
            ):
                self.updated_count += 1
                self.logger.info(f'Updated {doi}.')
            else:
                self.failed_count += 1
                self.logger.warning(f'Unable to update {doi}.')

        elif (
            exists_dict['outcome'] == 'yes'
            and exists_dict['record_date'] == record_date
        ):
            # if identifier exists but record date is the same, it's not really
            # an update. So skip it and move on.
            #
            # identifier exists but there are no updates to apply because
            # record date is the same
            self.skipped_exists_count += 1

            msg = (
                f'Skipped {doi}, '
                f'it already exists and has the same record date'
            )
            self.logger.info(msg)

        elif exists_dict['outcome'] == 'failed':
            # if check failed for some reason, d1_client_manager would have
            # logged the error so just skip.
            msg = (
                f'The existance check for {doi} failed.  Is this '
                f'logged anywhere?'
            )
            self.logger.warning(msg)

        elif exists_dict['outcome'] == 'no':
            # If this identifer is not already found in GMN in any way, then
            # create a new object in GMN
            if self.client_mgr.load_science_metadata(docbytes, doi, record_date):  # noqa: E501
                # track number of successfully created new objects
                self.created_count += 1

                msg = f'Created a new object identified as {doi}'
                self.logger.info(msg)

            else:
                msg = (
                    f'Unable to create new object identified as {doi}.'
                )
                self.logger.error(msg)
                self.failed_count += 1

    async def can_be_updated(self, new_doc_bytes, doi, existing_sid):
        """
        We have an existing document in the system and have been give a
        proposed update document.  We need to decide if an update is warranted.

        The tie-breakers are:

            i)  the value of the MD_ProgressCode.
            ii) the value of the dateStamp.

        This code MAY break in production.
        """
        new_doc = lxml.etree.parse(io.BytesIO(new_doc_bytes))

        url = f"{self.mn_base_url}/v2/object/{existing_sid}"

        # Get the existing document.
        content = await self.retrieve_url(url, headers={'Accept': 'text/xml'})

        old_doc = lxml.etree.parse(io.BytesIO(content))

        # Get the progress code
        parts = [
            'gmd:identificationInfo',
            'gmd:MD_DataIdentification',
            'gmd:status',
            'gmd:MD_ProgressCode',
            'text()'
        ]
        path = '/'.join(parts)
        new_progress_code = new_doc.xpath(path, namespaces=ISO_NSMAP)[0]
        old_progress_code = old_doc.xpath(path, namespaces=ISO_NSMAP)[0]  # noqa:  F841

        # Get the metadata timestamp.  There are two possible paths.
        path = (
            'gmd:dateStamp/gco:Date/text()'
            '|'
            'gmd:dateStamp/gco:DateTime/text()'
        )
        s = new_doc.xpath(path, namespaces=ISO_NSMAP)[0]
        new_timestamp = dateutil.parser.parse(s)
        s = old_doc.xpath(path, namespaces=ISO_NSMAP)[0]
        old_timestamp = dateutil.parser.parse(s)

        if (
            new_progress_code.lower() in ['complete', 'completed']
            and old_progress_code.lower() not in ['complete', 'completed']
        ):
            # Yes, we should update.  The new document is finished while the
            # old document is not.
            return True
        elif (
            new_progress_code.lower() in ['complete', 'completed']
            and old_progress_code.lower() in ['complete', 'completed']
            and new_timestamp > old_timestamp
        ):
            # We have a tie between the progress codes, but the proposed
            # update document has a newer timestamp.
            return True
        else:
            msg = (
                f"The existing document identified by {doi} with SID "
                f"{existing_sid} has an MD_ProgressCode of "
                f"\"{old_progress_code}\" and a metadata timestamp of "
                f"{old_timestamp} while the proposed updating "
                f"document has MD_ProgressCode \"{new_progress_code}\" and a "
                f"metadata timestamp of {new_timestamp}."
            )
            self.logger.warning(msg)
            return False

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

    async def retrieve_url(self, url, headers=None, check_xml_headers=False):
        """
        Parameters
        ----------
        url : str
            URL of either an HTML document or an XML metadata document
        headers : dict
            Optional headers to supply with the retrieval.
        """
        self.logger.debug(f'retrieve_url: {url}')

        headers = {
            'User-Agent': 'DataONE adapter for schema.org harvest',
            'From': 'jevans97@utk.edu'
        }
        connector = aiohttp.TCPConnector(ssl=False)

        async with aiohttp.ClientSession(headers=headers,
                                         connector=connector) as session:

            async with session.get(url) as response:

                response.raise_for_status()

                if check_xml_headers:
                    exp_headers = [
                        'text/xml',
                        'application/x-gzip',
                        'application/xml'
                    ]
                    if response.headers['Content-Type'] not in exp_headers:
                        msg = (
                            f"get_sitemap_document: headers are "
                            f"{response.headers}"
                        )
                        self.logger.debug(msg)
                        self.logger.warning(SITEMAP_NOT_XML_MESSAGE)

                return await response.read()

    async def run(self):

        self.logger.debug(f'run:  num_workers = {self.num_workers}')
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
        msg = f'requesting {metadata_url}'
        self.logger.info(msg)
        # Retrieve the metadata document.
        content = await self.retrieve_url(metadata_url)

        try:
            doc = lxml.etree.parse(io.BytesIO(content))
        except Exception as e:
            msg = (
                f"Unable to parse the metadata document at {metadata_url} "
                f"due to {repr(e)}."
            )
            raise RuntimeError(msg)

        self.logger.debug('Got the metadata document')
        return doc

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
        self.logger.debug(f'sitemap_consumer[{idx}]:')
        while True:
            url, lastmod_time = await sitemap_queue.get()
            msg = f'sitemap_consumer[{idx}] ==>  {url}, {lastmod_time}'
            self.logger.debug(msg)
            try:
                identifier, doc = await self.retrieve_record(url)
                await self.process_record(identifier, doc, lastmod_time)

            except asyncio.CancelledError:
                self.logger.debug('CancelledError')
                break

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

        # Sometimes there is a space in the @id field.  Can't be having any of
        # that...
        identifier = self.extract_identifier(jsonld)
        self.logger.debug(f"{DOI_IDENTIFIER_MSG}  {identifier}...")

        # The SHACL checks should have verified that this is present and ok.
        metadata_url = jsonld['encoding']['contentUrl']

        doc = await self.retrieve_metadata_document(metadata_url)
        return identifier, doc

    async def process_record(self, identifier, doc, last_mod_time):
        """
        Now that we have the record, validate and harvest it.

        Parameters
        ----------
        identifier : str
            Handle used to identify objects uniquely.
        doc : bytes
            serialized version of XML metadata document
        last_mod_time : datetime.datetime
            Last document modification time according to the site map.
        """
        self.logger.debug(f'process_record:  starting')

        # Validate the document.  We do NOT want this to be subsumed into
        # the harvest operation.
        d1_scimeta.validate.assert_valid(self.format_id, doc)

        await self.harvest_document(identifier, doc, last_mod_time)

        self.logger.debug(f'process_record:  finished')

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
