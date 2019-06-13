"""
DATAONE adapter for ARM
"""

# Standard library imports
import io
import json
import logging
import re

# 3rd party library imports
import dateutil
from lxml import etree
import requests

# Local imports
from .d1_client_manager import D1ClientManager

UNESCAPED_DOUBLE_QUOTES_MSG = 'Unescaped double-quotes have been corrected.'
OVER_ESCAPED_DOUBLE_QUOTES_MSG = (
    'Over-escaped double quotes have been corrected.'
)
SITE_MAP_RETRIEVAL_FAILURE_MESSAGE = 'Failed to retrieve the site map.'

ISO_NSMAP = {
    'gmd': 'http://www.isotc211.org/2005/gmd',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'gco': 'http://www.isotc211.org/2005/gco',
    'gml': 'http://www.opengis.net/gml/3.2',
    'xlink': 'http://www.w3.org/1999/xlink',
    'xs': 'http://www.w3.org/2001/XMLSchema'
}


class CommonHarvester(object):
    """
    Attributes
    ----------
    client_mgs : object
        Handles direct communication with dataone host.
    created_count, skipped_exist_count, updated_count: int
        Counters for the different ways that records are handled.
    logger : logging.Logger
        All events are recorded by this object.
    mn_base_url : str
        URL for contacting the dataONE host.
    session : requests.sessions.Session
        Makes all URL requests.
    """

    def __init__(self, host, port, certificate, private_key, id=None,
                 verbosity='INFO'):
        """
        Parameters
        ----------
        host, port : str, int
            This fully identifies the DataONE host and port number where we
            will be sending metadata records.
        certificate, key : str or path or None
            Paths to client side certificates.  None if no verification is
            desired.
        """
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
            'formatId_custom': f'http://www.isotc211.org/2005/gmd-{id}'
        }

        self.client_mgr = D1ClientManager(self.mn_base_url,
                                          certificate, private_key,
                                          sys_meta_dict,
                                          self.logger)

        # Count the different ways that we update/create/skip records.  This
        # will be logged when we are finished.
        self.updated_count = 0
        self.skipped_exists_count = 0
        self.created_count = 0
        self.unprocessed_count = 0

        requests.packages.urllib3.disable_warnings()

    def get_site_map(self):
        """
        Retrieve the site map.

        See https://www.sitemaps.org for more information.
        """
        # Retrieve all the URLs in the site map.
        r = self.session.get(self.site_map)
        try:
            r.raise_for_status()
        except requests.HTTPError as e:
            self.logger.error(SITE_MAP_RETRIEVAL_FAILURE_MESSAGE)
            self.logger.error(repr(e))
            raise
        return r

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
        self.logger = logging.getLogger(__name__)

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
        text = scripts[0].text

        # May have to make two passes at this.
        count = 0
        while True:
            try:
                jsonld = json.loads(text)
            except json.decoder.JSONDecodeError as e:
                # Log the error, try to fix the JSON string, and try again.
                self.logger.error(repr(e))
                text = self.fix_jsonld_text(text)
                count += 1
            else:
                return jsonld

            if count == 10:
                # We cannot fix this.  We tried with the original string,
                # and we tried to find some common fixable issues.  No luck.
                msg = 'Unable to fix embeded JSON-LD.'
                self.logger.error(msg)
                raise RuntimeError(msg)

    def retrieve_url(self, url):
        """
        Parameters
        ----------
        url : str
            URL of either an HTML document or an XML metadata document
        """
        r = self.session.get(url)
        try:
            r.raise_for_status()
        except requests.HTTPError as e:
            self.logger.error(repr(e))
            raise RuntimeError(repr(e))
        else:
            return r

    def run(self):
        last_harvest_time_str = self.client_mgr.get_last_harvest_time()
        last_harvest_time = dateutil.parser.parse(last_harvest_time_str)
        self.logger.info(f'Last harvest time:  {last_harvest_time}')

        records = self.get_records(last_harvest_time)
        for url, lastmod_time in records:
            try:
                self.process_record(url, lastmod_time)
            except etree.XMLSyntaxError as e:
                self.unprocessed_count += 1
                msg = f"Unable to process {url} due to {repr(e)}."
                self.logger.error(e)
            except RuntimeError:
                self.unprocessed_count += 1

        self.logger.info(f'Updated {self.updated_count} records.')
        self.logger.info(f'Skipped {self.skipped_exists_count} records.')
        self.logger.info(f'Created {self.created_count} new records.')

        msg = f'Could not process {self.unprocessed_count} records.'
        self.logger.info(msg)

    def harvest_document(self, identifier, doc, record_date):
        """
        Check if the member node has seen the document before and decide how to
        harvest it (or not) accordingly.

        Parameters
        ----------
        identifier : str
            Handle used to identify objects uniquely.
        doc : bytes
            serialized version of XML metadata document
        record_date : datetime obj
            Last document modification time according to the site map.
        """
        exists_dict = self.client_mgr.check_if_identifier_exists(identifier)

        if (
            exists_dict['outcome'] == 'yes'
            and exists_dict['record_date'] != record_date
        ):

            # the outcome of exists_dict determines how to
            # handle the record.  if identifier exists in GMN but
            # record date is different, this truly is an update so
            # call update method.
            if self.client_mgr.update_science_metadata(
                doc,
                identifier,
                record_date,
                exists_dict['current_version_id']
            ):
                # track the number of succesfully updated objects
                self.updated_count += 1

                self.logger.info(f'Updated {identifier}.')
            else:
                self.logger.warning(f'Unable to updated {identifier}.')

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
                f'Skipped {identifier}, '
                f'it already exists and has the same record date'
            )
            self.logger.info(msg)

        elif exists_dict['outcome'] == 'failed':
            # if check failed for some reason, d1_client_manager would have
            # logged the error so just skip.
            msg = (
                f'The existance check for {identifier} failed.  Is this '
                f'logged anywhere?'
            )
            self.logger.warning(msg)

        elif exists_dict['outcome'] == 'no':
            # If this identifer is not already found in GMN in any way, then
            # create a new object in GMN
            if self.client_mgr.load_science_metadata(doc, identifier,
                                                     record_date):
                # track number of successfully created new objects
                self.created_count += 1

                msg = f'Created a new object identified as {identifier}'
                self.logger.info(msg)

            else:
                msg = (
                    f'Unable to create new object identified as {identifier}.'
                )
                self.logger.error(msg)

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
        Byte stream corresponding to possibly transformed metadata document.
        """
        # Retrieve the metadata document.
        self.logger.info(f"Requesting {metadata_url}...")
        r = self.retrieve_url(metadata_url)
        doc = etree.parse(io.BytesIO(r.content))

        # Re-seriealize to bytes.
        docbytes = etree.tostring(doc, pretty_print=True,
                                  encoding='utf-8', standalone=True)

        return docbytes

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

        doc = etree.HTML(r.text)
        jsonld = self.extract_jsonld(doc)

        # Sometimes there is a space in the @id field.  Can't be having any of
        # that...
        identifier = self.extract_identifier(doc, jsonld)
        self.logger.info(f"Have identified {identifier}...")

        # The URL for the metadata documents should be the first 'url' field
        # of the field named 'ISO Metadata Document'
        metadata_url = self.extract_metadata_url(jsonld, landing_page_url)

        doc = self.retrieve_metadata_document(metadata_url)

        self.harvest_document(identifier, doc, record_date)
