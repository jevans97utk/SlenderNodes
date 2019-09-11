"""
DATAONE SO core for multiple adaptors.
"""

# Standard library imports
import asyncio
import copy
from dataclasses import dataclass
import datetime as dt
import gzip
import io
import logging
import re
import sys

# 3rd party library imports
import aiohttp
import dateutil.parser
import lxml.etree
import pandas as pd
import requests
import d1_scimeta.validate

# Local imports
from .d1_client_manager import D1ClientManager
from .xml_validator import XMLValidator

SITEMAP_RETRIEVAL_FAILURE_MESSAGE = 'Failed to retrieve the site map.'
NO_JSON_LD_SCRIPT_ELEMENTS = "No JSON-LD <SCRIPT> elements were located."
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

# If an exception is one of these, then we may wish to try again.  Sometimes
ERROR_RETRY_CANDIDATES = (
    aiohttp.ClientPayloadError, aiohttp.ClientResponseError,
    asyncio.TimeoutError
)


@dataclass
class SlenderNodeJob(object):
    """
    Represents a job for processing a single document.

    Use dataclasses instead of a named tuple because named tuples are
    immutable and we want to keep track of the number of failures with any
    particular job.

    Attributes
    ----------
    url : str
        URL of either a landing page or metadata document
    identifier : str
        Usually a DOI, sometimes a UUID.  We often do not have this information
        when the job gets created.
    lastmod : datetime
        date when the document was last modified on the remote end
    num_failures : int
        Number of failures for this particular job so far.  If a job fails
        and the number of allowed failures per job is greater than 1, then we
        may want to try again.  Sometimes failures on the remote side may be
        sporadic.
    result : Exception or None
        None if the job succeeded, or the generated exception if the job
        failed.
    """
    url: str
    identifier: str
    lastmod: dt.datetime
    num_failures: int
    result: Exception


class SkipError(RuntimeError):
    """
    Raise this exception when there is reason to not even attempt to harvest
    a document with the GMN software.
    """
    pass


class RefusedToUpdateRecord(RuntimeError):
    """
    Raise this when we have a record whose metadata says we should not update
    it.  One reason seen was that a metadata timestamp regressed to an
    earlier date.
    """
    pass


class UnableToCreateNewGMNObject(RuntimeError):
    """
    Raise this when we have an identifier we have not seen before, but for
    some reason the GMN software cannot harvest it.
    """
    pass


class UnableToUpdateGmnRecord(RuntimeError):
    """
    Raise this when we have an identifier that we HAVE seen before, and the
    reported modification date indicates that we should update it, but for
    some reason the GMN software cannot update it.
    """
    pass


class XMLValidationError(RuntimeError):
    pass


class InvalidSitemapError(RuntimeError):
    pass


class XMLMetadataParsingError(RuntimeError):
    pass


class CoreHarvester(object):
    """
    Attributes
    ----------
    mn_host : str
        name of the gmn member node host
    client_mgs : object
        Handles direct communication with dataone host.
    {created,failed,rejected_updated}_count t: int
        Counters for the different ways that records are handled.  "failed" is
        different from "rejected" in the sense that this code knows why a
        rejection occurs.
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
    regex : str
        If not None, restrict documents to those that match this regular
        expression.
    session : requests.sessions.Session
        Makes all URL requests.
    sys_meta_dict : dict
        A dict containing node-specific system metadata properties that
        will apply to all science metadata documents loaded into GMN.
    """

    def __init__(self, host=None, port=None, certificate=None,
                 private_key=None, verbosity='INFO', id='none',
                 num_documents=-1, num_workers=1, max_num_errors=3,
                 regex=None, retry=0, ignore_harvest_time=False):
        """
        Parameters
        ----------
        host, port : str, int
            This fully identifies the DataONE host and port number where we
            will be sending metadata records.
        certificate, private_key : str or path or None
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
        self.sys_meta_dict = {
            'submitter': f'urn:node:{id.upper()}',
            'rightsholder': f'urn:node:{id.upper()}',

            # Use your node's DataONE URI
            'authoritativeMN': f'urn:node:mnTest{id.upper()}',

            # Use your node's DataONE URI
            'originMN': f'urn:node:{id.upper()}',

            # should be consistent w/ scimeta_element format
            # This starts off as a default.  It will be changed if necessary.
            'formatId_custom': 'http://www.isotc211.org/2005/gmd'
        }

        self.client_mgr = D1ClientManager(self.mn_base_url,
                                          certificate, private_key,
                                          self.sys_meta_dict,
                                          self.logger)

        self.job_records = []

        # Count the different ways that we update/create/skip records.  This
        # will be logged when we are finished.
        self.failed_count = 0
        self.updated_count = 0
        self.created_count = 0

        self.retry = retry

        self.num_documents = num_documents
        self.num_records_processed = 0

        self.num_workers = num_workers

        self.max_num_errors = max_num_errors

        self.regex = re.compile(regex) if regex is not None else None
        self.ignore_harvest_time = ignore_harvest_time

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
        """
        Summarize the harvest results.
        """

        self.logger.info("\n\n")
        self.logger.info("Job Summary")
        self.logger.info("===========")
        self.logger.info(f"There were {self.created_count} new records.")
        self.logger.info(f"There were {self.updated_count} updated records.")

        self.summarize_job_records()

    def summarize_job_records(self):
        """
        Summarize the job records.  Keep this factored out of the summarize
        routine for the purpose of testing.
        """
        # Create a pandas dataframe out of the job results.
        columns = ['URL', 'Identifier', 'NumFailures', 'Result']
        records = [
            (job.url, job.identifier, job.num_failures, job.result)
            for job in self.job_records
        ]
        df = pd.DataFrame.from_records(records, columns=columns)

        # The rows with None in the Results column are successes.  Anything
        # else in there should be an Exception object.
        msg = f"Successfully processed {df.Result.isnull().sum()} records."
        self.logger.info(msg)

        # Restrict to the job failures.
        df = df.dropna()
        if len(df) == 0:
            # If no errors, then nothing more to do.
            return

        # Split the exceptions into two parts, the exception name and the
        # exception message.
        fcn = lambda x: repr(x).split('(')[0]  # noqa:  E371
        df = df.assign(error=lambda df: df.Result.apply(fcn))
        columns = ['URL', 'Identifier', 'NumFailures', 'Result']
        df_error = df.drop(columns, axis='columns')
        df_error['count'] = 1
        summary = df_error.groupby('error').sum()

        self.logger.info("\n\n")
        self.logger.error(f"Error summary:\n\n{summary}\n\n")

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
            await self.check_if_can_be_updated(docbytes, doi, current_sid)

            # the outcome of exists_dict determines how to
            # handle the record.  if identifier exists in GMN but
            # record date is different, this truly is an update so
            # call update method.
            if self.client_mgr.update_science_metadata(
                docbytes,
                doi,
                record_date,
                exists_dict['current_version_id']
            ):
                self.updated_count += 1
                self.logger.info(f'Updated {doi}.')
            else:
                raise UnableToUpdateGmnRecord(f'Unable to update {doi}.')

        elif (
            exists_dict['outcome'] == 'yes'
            and exists_dict['record_date'] == record_date
        ):
            # if identifier exists but record date is the same, it's not really
            # an update. So skip it and move on.
            msg = (
                f'Skipping {doi}, '
                f'it already exists and has the same record date {record_date}'
            )
            raise SkipError(msg)

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
                raise UnableToCreateNewGMNObject(msg)

    async def check_if_can_be_updated(self, new_doc_bytes, doi, existing_sid):
        """
        We have an existing document in the system and have been give a
        proposed update document.  We need to decide if an update is warranted.

        The tie-breakers are:

            i)  the value of the MD_ProgressCode.
            ii) the value of the dateStamp.

        We can currently only do this check when the format ID is the default.
        """
        if self.sys_meta_dict['formatId_custom'] != 'http://www.isotc211.org/2005/gmd':  # noqa:  E501
            return True

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
            return
        elif (
            new_progress_code.lower() in ['complete', 'completed']
            and old_progress_code.lower() in ['complete', 'completed']
            and new_timestamp > old_timestamp
        ):
            # We have a tie between the progress codes, but the proposed
            # update document has a newer timestamp.
            return
        else:
            msg = (
                f"The existing document identified by {doi} with SID "
                f"{existing_sid} has an MD_ProgressCode of "
                f"\"{old_progress_code}\" and a metadata timestamp of "
                f"{old_timestamp} while the proposed updating "
                f"document has MD_ProgressCode \"{new_progress_code}\" and a "
                f"metadata timestamp of {new_timestamp}."
            )
            raise RefusedToUpdateRecord(msg)

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

    def extract_records_from_sitemap(self, doc):
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

        records = [(url, lastmod) for url, lastmod in zip(urls, lastmods)]

        msg = f"Extracted {len(urls)} from the sitemap document."
        self.logger.info(msg)
        return records

    def post_process_sitemap_records(self, records, last_harvest_time):
        """
        Prune the sitemap records for various reasons.

        Parameters
        ----------
        records : list
            Each item in the list is composed of a URL and a last modification
            date.
        """
        # If we do not wish to ignore the last harvest time, then only those
        # records in the sitemap that are newer than the last harvest time will
        # pass through.
        nrecs = len(records)
        if not self.ignore_harvest_time:
            records = [
                (url, lastmod) for url, lastmod in records
                if lastmod > last_harvest_time
            ]

            nskipped = nrecs - len(records)
            msg = f"{nskipped} records skipped due to lastmod time."
            self.logger.info(msg)

        # If a regex was specified, filter out any records that do not match.
        if self.regex is not None:
            nrecs = len(records)
            records = [
                (url, lastmod) for url, lastmod in records
                if self.regex.search(url)
            ]
            num_skipped = nrecs - len(records)
            msg = f"{num_skipped} records skipped due to regex restriction."
            self.logger.info(msg)

        # Check that we do not exceed the maximum number of documents.
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
                        'text/xml;charset=UTF-8',
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
                f"Unable to parse the metadata document at {metadata_url}:  "
                f"{e}."
            )
            raise XMLMetadataParsingError(msg)

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
        while True:
            try:
                job = await sitemap_queue.get()
                msg = (
                    f"sitemap_consumer[{idx}] ==>  {job.url}, "
                    f"{job.lastmod}:  "
                    f"job failure count = {job.num_failures}, "
                    f"queue size = {sitemap_queue.qsize()}"
                )
                self.logger.info(msg)

                await self.process_job(job)

            except asyncio.CancelledError:
                self.logger.debug('CancelledError')
                break

            except SkipError as e:
                job.result = e
                self.job_records.append(copy.copy(job))
                msg = f"Unable to process {job.url}:  {e}"
                self.logger.warning(msg)

            except Exception as e:
                job.result = e

                self.job_records.append(copy.copy(job))

                msg = f"Unable to process {job.url}:  {e}"
                self.logger.error(msg)

                self.failed_count += 1
                if self.failed_count == self.max_num_errors:
                    self.logger.warning("Error threshold reached.")
                    await self.shutdown()

                if job.num_failures < self.retry:
                    if isinstance(e, ERROR_RETRY_CANDIDATES):
                        self.logger.info(f"Throwing {job.url} back on queue")
                        job.num_failures += 1
                        sitemap_queue.put_nowait(job)

            else:
                # The job was successful.
                job.result = None
                self.job_records.append(copy.copy(job))

                msg = (
                        f"sitemap_consumer[{idx}]:  "
                        f"{SUCCESSFUL_INGEST_MESSAGE}: {job.identifier}"
                )
                self.logger.debug(msg)

                msg = f"{SUCCESSFUL_INGEST_MESSAGE}: {job.identifier}"
                self.logger.info(msg)

            sitemap_queue.task_done()

    async def process_job(self, job):
        """
        Now that we have the record, validate and harvest it.

        Parameters
        ----------
        job : SlenderNodeJob
            Record containing at least the following attributes: landing page
            URL, last document modification time according to the site map.
        """
        self.logger.debug(f'process_job:  starting')

        job.identifier, doc = await self.retrieve_record(job.url)
        self.validate_document(doc)
        await self.harvest_document(job.identifier, doc, job.lastmod)

        self.logger.debug(f'process_job:  finished')

    def validate_document(self, doc):
        """
        Verify that the format ID we have for the document is correct.

        Parameters
        ----------
        doc : bytes
            serialized version of XML metadata document
        """
        format_id = self.sys_meta_dict['formatId_custom']
        try:
            d1_scimeta.validate.assert_valid(format_id, doc)
        except Exception:
            # Ok, so it did not validate against the default id.  Try to
            # figure out another format id that works.
            msg = f"Default validation failed with format ID {format_id}."
            self.logger.info(msg)

            validator = XMLValidator(logger=self.logger)
            format_id = validator.validate(doc)
            if format_id is None:
                raise XMLValidationError('XML metadata validation failed.')
            else:
                # Reset the format ID to the one that worked.
                self.sys_meta_dict['formatId_custom'] = format_id

    def preprocess_landing_page(self, landing_page_doc):
        """
        Check the landing page for any information we may need OTHER than
        JSON-LD.

        Parameters
        ----------
        landing_page_doc : lxml element tree
            Document corresponding to the HTML landing page.
        """
        # Nothing to do in the general case.
        pass

    async def retrieve_record(self, document_url):
        """
        Parameters
        ----------
        document_url : str
            URL for a remote document, could be a landing page, could be an
            XML document

        Returns
        -------
        identifier : str
            Ideally this is a DOI, but here it is a UUID.
        doc : ElementTree
            Metadata document
        """
        raise NotImplementedError('must supply in sub class')

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

        doc = await self.get_sitemap_document(sitemap_url)
        if self.is_sitemap_index_file(doc):

            msg = "process_sitemap:  This is a sitemap index file."
            self.logger.debug(msg)

            path = 'sm:sitemap/sm:loc/text()'
            sitemap_urls = doc.xpath(path, namespaces=SITEMAP_NS)
            for sitemap_url in sitemap_urls:
                await self.process_sitemap(sitemap_url, last_harvest)

        else:

            self.logger.debug("process_sitemap:  This is a sitemap leaf.")
            await self.process_sitemap_leaf(doc, last_harvest)

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
            content = await self.retrieve_url(sitemap_url,
                                              check_xml_headers=True)
        except Exception as e:
            msg = f"{SITEMAP_RETRIEVAL_FAILURE_MESSAGE} due to {repr(e)}"
            self.logger.error(msg)
            raise

        try:
            doc = lxml.etree.parse(io.BytesIO(content))
        except lxml.etree.XMLSyntaxError as e:
            msg1 = str(e)

            try:
                # Gzipped XML can cause an XMLSyntaxError, so try again.
                doc = lxml.etree.parse(io.BytesIO(gzip.decompress(content)))
            except OSError:
                # Must not have been gzipped.
                # TODO:  Is there some other possibility here?
                msg = (
                    f"XMLSyntaxError:  sitemap document at {sitemap_url}: "
                    f"{msg1}"
                )
                self.logger.error(msg)

                msg = (
                    f'Unable to process the sitemap retrieved from '
                    f'{sitemap_url}.'
                )
                raise InvalidSitemapError(msg)

        return doc

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

        records = self.extract_records_from_sitemap(doc)
        records = self.post_process_sitemap_records(records, last_harvest)
        for url, lastmod_time in records:
            job = SlenderNodeJob(url, '', lastmod_time, 0, None)
            sitemap_queue.put_nowait(job)

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
