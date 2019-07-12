"""
DATAONE adapter for ARM
"""

# Standard library imports
import gzip
import io
import json
import logging
import re
import sys
import urllib.parse

# 3rd party library imports
import dateutil.parser
import lxml.etree
import requests
import d1_scimeta.validate

# Local imports
from .d1_client_manager import D1ClientManager

UNESCAPED_DOUBLE_QUOTES_MSG = 'Unescaped double-quotes have been corrected.'
OVER_ESCAPED_DOUBLE_QUOTES_MSG = (
    'Over-escaped double quotes have been corrected.'
)
SITEMAP_RETRIEVAL_FAILURE_MESSAGE = 'Failed to retrieve the site map.'
NO_JSON_LD_SCRIPT_ELEMENTS = "No JSON-LD <SCRIPT> elements were located."
DOI_IDENTIFIER_MSG = "Have extracted the identifier:  "
INVALID_JSONLD_MESSAGE = "Unable to fix embedded JSON-LD due to"
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
    logger : logging.Logger
        All events are recorded by this object.
    mn_base_url : str
        URL for contacting the dataONE host.
    num_documents : int
        Limit the number of documents to this number.  Less than zero
        means retrieve them all.
    num_records_processed : int
        Running total of number of records processed so far.
    session : requests.sessions.Session
        Makes all URL requests.
    """

    def __init__(self, host=None, port=None, certificate=None,
                 private_key=None, verbosity='INFO', regex=None, id=None,
                 num_documents=-1):
        """
        Parameters
        ----------
        host, port : str, int
            This fully identifies the DataONE host and port number where we
            will be sending metadata records.
        certificate, key : str or path or None
            Paths to client side certificates.  None if no verification is
            desired.
        num_documents : int
            Limit the number of documents to this number.  Less than zero
            means retrieve them all.
        """
        self.mn_host = host

        self.setup_session(certificate, private_key)

        self.setup_logging(id, verbosity)

        self.regex = None if regex is None else re.compile(regex)

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

        # Count the different ways that we update/create/skip records.  This
        # will be logged when we are finished.
        self.created_count = 0
        self.failed_count = 0
        self.rejected_count = 0
        self.skipped_exists_count = 0
        self.updated_count = 0

        self.num_documents = num_documents
        self.num_records_processed = 0

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
        logging.basicConfig(filename=f'{logid}.log',
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            level=level)
        self.logger = logging.getLogger('datatone')

        # Also log to stdout.
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(format)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def fix_jsonld_text(self, text):
        """
        """
        text = self.fix_over_escaped_double_quotes(text)
        text = self.fix_unescaped_double_quotes(text)
        return text

    def fix_over_escaped_double_quotes(self, text):
        """
        The JSON-LD string may have a top-level description field that has
        incorrectly escaped double-quotes, i.e.

            description":
                "Abstract:
                ...
                Antarctic climate, as well as the interhemispheric
                phasing of the \\"bipolar seesaw\\". We present the
                WD2014 chronology for the upper part (0-2850 m; 31.2
                ..."

        We have double quotes preceded by two backslashes, but there really
        should only be a single backslash.  Making this more complicated is
        the unfortunate fact that the python interpreter makes changes to
        strings before we can get at them.  Specifically, any backslash '/'
        must be represented by '//' in a string literal.  So in the example
        given, the substring is seen from Python as

            '\\\\"bipolar seesaw\\\\"'

        When using the raw-string form of string literals, however, the example
        string can be represented as

            r'\\"bipolar seesaw\\"'

        """
        regex = re.compile(r'\\\\"')
        if regex.search(text):
            self.logger.warning(OVER_ESCAPED_DOUBLE_QUOTES_MSG)
            text = regex.sub(r'\\"', text)
        return text

    def fix_unescaped_double_quotes(self, text):
        """
        The JSON-LD string has a field that looks something like

        "contributor": {
            ...
            "description":"stuff with "quoted stuff" inside",
            ...
        }

        The correct representation would be

        "contributor": {
            ...
            "description":"stuff with \"quoted stuff\" inside",
            ...
        }
        """
        pattern = r'''
            "description":
            # possible white space
            \s*
            # the leading double quote of the description key value
            "
            # the description text, which may or may not include an unescaped
            # double quote
            (?P<desc>.*?)
            # look-ahead for either the end of the description field followed
            # by another key-value pair, or the end of the enclosing record.
            (?=( (",\s*") | ("}) ) )
        '''
        regex = re.compile(pattern, re.VERBOSE)

        # Look for a double quote that is NOT preceeded by a backslash.
        unescaped_dbl_quote_regex = re.compile(r'(?<!\\)"')

        for m in regex.finditer(text):

            desc_text = m.group('desc')

            m_unescaped = unescaped_dbl_quote_regex.search(desc_text)
            if m_unescaped is None:
                # No unescaped double quote in this description field.
                continue

            new_desc_text = re.sub(r'"', r'\\"', desc_text)

            # Insert the modified text back into the presumed JSON-LD text.
            self.logger.warning(UNESCAPED_DOUBLE_QUOTES_MSG)

            idx = text.find(desc_text)
            text = text[:idx] + new_desc_text + text[idx + len(desc_text):]

        return text

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
        scripts = doc.xpath('head/script[@type="application/ld+json"]')
        if len(scripts) == 0:
            raise RuntimeError(NO_JSON_LD_SCRIPT_ELEMENTS)

        text = scripts[0].text

        # Is it valid JSON?
        try:
            jsonld = json.loads(text)
        except json.decoder.JSONDecodeError as e:
            # Log the error as a warning because we are going to try to fix it.
            self.logger.warning(repr(e))
        else:
            return jsonld

        # May have to make two passes at this.
        count = 0
        while True:
            text = self.fix_jsonld_text(text)

            # Try again.
            try:
                jsonld = json.loads(text)
            except json.decoder.JSONDecodeError as e:
                msg = repr(e)
                count += 1
            else:
                return jsonld

            if count == 2:
                # We cannot fix this.  We tried with the original string,
                # and we tried to find some common fixable issues.  No luck.
                msg = f"{INVALID_JSONLD_MESSAGE}: \"{msg}\"."
                raise RuntimeError(msg)

    def retrieve_url(self, url, headers=None):
        """
        Parameters
        ----------
        url : str
            URL of either an HTML document or an XML metadata document
        headers : dict
            Optional headers to supply with the retrieval.
        """
        r = self.session.get(url, headers=headers)
        r.raise_for_status()
        return r

    def get_last_harvest_time(self):

        if self.mn_host is not None:
            last_harvest_time_str = self.client_mgr.get_last_harvest_time()
            last_harvest_time = dateutil.parser.parse(last_harvest_time_str)
            self.logger.info(f'Last harvest time:  {last_harvest_time}')
        else:
            last_harvest_time_str = '1900-01-01T00:00:00Z'
            last_harvest_time = dateutil.parser.parse(last_harvest_time_str)

        return last_harvest_time

    def run(self):

        last_harvest_time = self.get_last_harvest_time()

        try:
            self.process_sitemap(self.site_map, last_harvest_time)
        except Exception as e:
            self.logger.error(repr(e))

        self.summarize()

    def summarize(self):

        self.logger.info(f'Created {self.created_count} new records.')
        self.logger.info(f'Updated {self.updated_count} records.')
        self.logger.info(f'Skipped {self.skipped_exists_count} records.')
        self.logger.info(f'Rejected {self.rejected_count} records.')
        self.logger.info(f'Failed to update/create {self.failed_count} records.')  # noqa: E501

    def harvest_document(self, doi, doc, record_date):
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
        # Re-seriealize to bytes.
        docbytes = lxml.etree.tostring(doc, pretty_print=True,
                                       encoding='utf-8', standalone=True)

        exists_dict = self.client_mgr.check_if_identifier_exists(doi)

        if (
            exists_dict['outcome'] == 'yes'
            and exists_dict['record_date'] != record_date
        ):
            current_sid = exists_dict['current_version_id']
            if not self.can_be_updated(docbytes, doi, current_sid):
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

    def can_be_updated(self, new_doc_bytes, doi, existing_sid):
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
        r = self.retrieve_url(url, headers={'Accept': 'text/xml'})

        old_doc = lxml.etree.parse(io.BytesIO(r.content))

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

    def retrieve_metadata_document(self, metadata_url):
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
        # Retrieve the metadata document.
        self.logger.info(f"Requesting {metadata_url}...")
        r = self.retrieve_url(metadata_url)
        try:
            doc = lxml.etree.parse(io.BytesIO(r.content))
        except Exception as e:
            msg = (
                f"Unable to parse the metadata document at {metadata_url} "
                f"due to {repr(e)}."
            )
            raise RuntimeError(msg)

        return doc

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

        # Sometimes there is a space in the @id field.  Can't be having any of
        # that...
        identifier = self.extract_identifier(jsonld)
        self.logger.info(f"{DOI_IDENTIFIER_MSG}  {identifier}...")

        metadata_url = self.extract_metadata_url(jsonld)

        doc = self.retrieve_metadata_document(metadata_url)
        d1_scimeta.validate.assert_valid(self.format_id, doc)

        self.harvest_document(identifier, doc, record_date)

    def url_is_cleared(self, url, lastmod, last_harvest_time):
        """
        If the user supplied a regex, then we want to only attempt those
        landing page URLs that match the regex.  Otherwise, look at the last
        harvest time to determine if the URL is cleared.
        """
        if self.regex is not None:
            if self.regex.search(url):
                return True
            else:
                return False
        else:
            if lastmod >= last_harvest_time:
                return True
            else:
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

    def process_sitemap(self, sitemap_url, last_harvest_time):
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
        msg = f"Processing sitemap at {sitemap_url}."
        self.logger.info(msg)

        doc = self.get_sitemap_document(sitemap_url)
        if self.is_sitemap_index_file(doc):

            sitemap_urls = doc.xpath('sm:sitemap/sm:loc/text()',
                                     namespaces=SITEMAP_NS)

            for sitemap_url in sitemap_urls:
                self.process_sitemap(sitemap_url, last_harvest_time)

        else:
            self.process_sitemap_leaf(doc, last_harvest_time)

    def process_sitemap_leaf(self, doc, last_harvest_time):
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

        records = self.extract_records_from_sitemap(doc, last_harvest_time)
        for url, lastmod_time in records:
            try:
                self.process_record(url, lastmod_time)
            except Exception as e:
                self.failed_count += 1
                msg = f"Unable to process {url} due to {repr(e)}."
                self.logger.error(msg)
            else:
                p = urllib.parse.urlparse(url)
                basename = p.path.split('/')[-1]
                msg = f"{SUCCESSFUL_INGEST_MESSAGE}: {basename}"
                self.logger.info(msg)

    def get_sitemap_document(self, sitemap_url):
        """
        Parameters
        ---------
        sitemap_url : str
            URL for a sitemap or sitemap index file.
        """
        try:
            r = self.retrieve_url(sitemap_url)
        except requests.HTTPError as e:
            msg = f"{SITEMAP_RETRIEVAL_FAILURE_MESSAGE} due to {repr(e)}"
            self.logger.error(msg)
            raise

        if r.headers['Content-Type'] not in ['text/xml', 'application/x-gzip']:
            self.logger.warning(SITEMAP_NOT_XML_MESSAGE)

        try:
            doc = lxml.etree.parse(io.BytesIO(r.content))
        except lxml.etree.XMLSyntaxError as e:
            msg1 = repr(e)

            # was it compressed?
            try:
                doc = lxml.etree.parse(io.BytesIO(gzip.decompress(r.content)))
            except OSError as e:
                # Must not have been gzipped.
                self.logger.error(msg1)
                self.logger.error(repr(e))
                msg = f'Unable to process the sitemap {sitemap_url}.'
                raise RuntimeError(msg)

        return doc

    def extract_records_from_sitemap(self, doc, last_harvest_time):
        """
        Extract all the URLs and lastmod times from an XML sitemap.
        """

        urls = doc.xpath('.//sm:loc/text()', namespaces=SITEMAP_NS)

        lastmods = doc.xpath('.//sm:lastmod/text()',
                             namespaces=SITEMAP_NS)

        # Parse the last modification times.  It is possible that the dates
        # have no timezone information in them, so we will assume that it is
        # UTC.
        lastmods = [dateutil.parser.parse(item) for item in lastmods]
        UTC = dateutil.tz.gettz("UTC")
        lastmods = [
            dateitem.replace(tzinfo=dateitem.tzinfo or UTC)
            for dateitem in lastmods
        ]

        z = zip(urls, lastmods)

        records = [
            (url, lastmod)
            for url, lastmod in z
            if self.url_is_cleared(url, lastmod, last_harvest_time)
        ]

        self.num_records_processed += len(records)
        if (
            self.num_records_processed > self.num_documents
            and self.num_documents > -1
        ):
            diff = self.num_records_processed - self.num_documents
            records = records[:-diff]

        return records

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
            # DOI:prefix/suffix - IEDA style
            (https?://dx.doi.org/(?P<doi_id_ieda>10\.\w+/\w+))
                |
            # ARM-style
            (doi:(?P<doi_id_arm>10.\w+/\w+))
                |
            # other ARM-style
            (?P<other_id>urn:usap-dc:metadata:\w+)
            # possible trailing white space (not supposed to be there)
            \s*
        '''
        regex = re.compile(pattern, re.VERBOSE)
        m = regex.search(jsonld['@id'])
        if m is None:
            msg = (
                f"DOI ID parsing error, could not parse an ID out of "
                f"JSON-LD '@id' element \"{jsonld['@id']}\""
            )
            raise RuntimeError(msg)

        if m.group('doi_id_ieda') is not None:
            return m.group('doi_id_ieda')
        elif m.group('doi_id_arm') is not None:
            return m.group('doi_id_arm')
        else:
            return m.group('other_id')

    def extract_metadata_url(self, jsonld):
        """
        In ARM, the JSON-LD is structured as follows

        {
           .
           .
           .
           "encoding" : {
               "@type": "MediaObject",
               "contentUrl": "https://www.acme.org/path/to/doc.xml",
               "encodingFormat": "http://www.isotc211.org/2005/gmd",
               "description": "ISO TC211 XML rendering of metadata.",
               "dateModified": "2019-06-17T10:34:57.260047"
           }
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
        try:
            return jsonld['encoding']['contentUrl']
        except KeyError as e:
            # If this happens, maybe we have IEDA?
            msg = (
                f"Could not find the metadata URL in "
                f"JSON-LD['encoding']['contentUrl'] "
                f"due to {repr(e)}, so trying to find in "
                f"JSON-LD['distribution'] hierarchy."
            )
            self.logger.warning(msg)
            items = [
                item for item in jsonld['distribution']
                if item['name'] == 'ISO Metadata Document'
            ]
            metadata_url = items[0]['url']
            return metadata_url
