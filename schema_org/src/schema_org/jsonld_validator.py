# Standard library imports
import importlib.resources as ir
import json
import urllib.parse

# 3rd party library imports
from pyshacl import Validator
import pyshacl.rdfutil
import pyshacl.monkey

# Local imports


class JsonLdError(RuntimeError):
    """
    Raise this exception if there is a problem with JSON-LD
    """
    pass


class JSONLD_Validator(object):
    """
    Attributes
    ----------
    logger : logging.Logger
        Same logger as 'dataone'.
    """

    def __init__(self, *, id='', logger=None):
        """
        Parameters
        ----------
        id : str
            Identifies the client, i.e. 'ieda', 'arm', etc.
        logger : logging.Logger
            Same logger as 'dataone'.
        """
        self.id = id
        self.logger = logger

        primary_txt = ir.read_text('schema_org.data', 'shacl.ttl')

        txt = ir.read_text('schema_org.data', 'namespace.ttl')
        if self.id == 'arm':
            # Grandfather ARM in here.  They technically get the namespace
            # bad, but we didn't catch that at first.
            namespace_txt = txt.format(namespace_severity='sh:Warning')
        else:
            namespace_txt = txt.format(namespace_severity='sh:Violation')

        # Join them together.  If we were to use the format method on the text
        # from a single file, the "primary" text would have to be altered as
        # well.
        self.shacl_graph_src = '\n'.join([primary_txt, namespace_txt])

    def pre_shacl_checks(self, j):
        """
        Run JSON-LD compliance checks that do not include SHACL.

        Parameters
        ----------
        j : dict
            JSON extracted from a landing page <SCRIPT> element.
        """
        self.logger.debug(f'{__name__}:pre_shacl_checks')
        if '@context' not in j:
            msg = 'JSON-LD missing top-level "@context" key.'
            raise JsonLdError(msg)

        # Inline contexts are currently problematic with regards to
        # certain date keys such as "dateModified".  Suppress this by
        # swapping out the inline context with something else.
        bad_contexts = ["http://schema.org", "http://schema.org/",
                        "https://schema.org", "https://schema.org/"]
        if j['@context'] in bad_contexts:
            j['@context'] = {
                'identifier': 'https://schema.org/identifier',
                'encoding': 'https://schema.org/encoding',
                'contentUrl': 'https://schema.org/contentUrl',
                'description': 'https://schema.org/description',
                'dateModified': 'https://schema.org/dateModified',
                'encodingFormat': 'https://schema.org/encodingFormat',
            }

        if '@type' not in j:
            msg = 'JSON-LD missing top-level "@type" key.'
            raise JsonLdError(msg)

        if j['@type'] != 'Dataset':
            msg = (
                f"JSON-LD @type key expected to be 'Dataset', not "
                f"'{j['@type']}'."
            )
            raise JsonLdError(msg)

        if '@id' not in j:
            msg = 'JSON-LD missing top-level "@id" key.'
            raise JsonLdError(msg)

        p = urllib.parse.urlparse(j['@id'])
        if (
            len(p.scheme) == 0
            or len(p.netloc) == 0
            or len(p.path) == 0
        ):
            msg = (
                f"JSON-LD top-level '@id' key \"{j['@id']}\" does not look "
                f"like an IRI/URI/URL."
            )
            raise JsonLdError(msg)

    def check(self, j):
        """
        Run JSON-LD compliance checks, both DATAONE and SHACL.

        Parameters
        ----------
        j : dict
            JSON extracted from a landing page <SCRIPT> element.
        """
        if self.id in ['ieda']:
            # IEDA JSON-LD does not validate, we know that.
            self.logger.warning(f"Skipping SHACL checks on {self.id.upper()}.")
            return

        self.logger.debug(f'{__name__}:check')
        self.pre_shacl_checks(j)
        self.check_shacl(j)

    def check_shacl(self, j):
        """
        Run SHACL JSON-LD compliance checks.

        Parameters
        ----------
        j : dict
            JSON extracted from a landing page <SCRIPT> element.
        """
        breakpoint()
        self.logger.debug(f'{__name__}:check_shacl')
        pyshacl.monkey.apply_patches()

        data_file = json.dumps(j, indent=4)
        data_graph = pyshacl.rdfutil.load_from_source(data_file,
                                                      rdf_format='json-ld',
                                                      do_owl_imports=False)

        shacl_graph = pyshacl.rdfutil.load_from_source(self.shacl_graph_src,
                                                       rdf_format='turtle',
                                                       do_owl_imports=False)

        try:
            options = {
                'inference': 'rdfs',
                'abort_on_error': False
            }
            validator = Validator(data_graph,
                                  shacl_graph=shacl_graph,
                                  options=options)
            conforms, report_graph, report_text = validator.run()

        except Exception as e:
            conforms = False
            report_text = f"Unexpected validation failure - {repr(e)}"
            self.logger.warning(report_text)
            raise JsonLdError("JSON-LD does not conform.")

        if conforms:
            self.logger.debug("JSON-LD conforms.")
            return

        # So the JSON-LD did not conform.  Parse the report text and log
        # human-readable messages.
        reports = self.parse_reports(report_text)

        error_count = 0
        for report in reports:

            if 'sh:Warning' in report['Severity']:
                self.logger.warning(report['Message'])
            else:
                self.logger.error(report['Message'])
                error_count += 1

                # Sometimes this can provide useful information.
                if report['Value Node'] is not None:
                    self.logger.error(report['Value Node'])

        if error_count > 0:
            raise JsonLdError("JSON-LD does not conform.")

    def parse_reports(self, report_text):
        """
        Parameters
        ----------
        report_text : str
            A part of the report text provided by pyshacl.

            Constraint Violation in MinCountConstraintComponent ... :
                Severity: sh:Violation
                Source Shape: [ ... ]
                Value Node: ...
                Result Path: ...
                Message: ...

        Return Value
        ------------
        dictionary of the individual items
        """
        reports = []

        items = report_text.split('Constraint Violation')
        for item in items:

            if 'Source Shape' not in item:
                # We don't have an actualy constraint violation text stanza
                # here.  Likely it is something that looks like
                #
                # Validation Report
                # Conforms: False
                # Results (2):
                #
                # which is the leading text.
                continue

            d = {}

            d['Value Node'] = self._parse_value_node(item)
            d['Message'] = self._parse_message(item)
            d['Severity'] = self._parse_severity(item)
            d['Result Path'] = self._parse_result_path(item)

            reports.append(d)

        return reports

    def _parse_severity(self, text):
        """
        If possible, parse the Severity item from the report text

        Parameters
        ----------
        text : str
            text describing the violation raised by SHACL
    
        Returns
        -------
        the severity text
        """
        severity = [
            line.strip() for line in text.splitlines()
            if 'Severity:' in line
        ]
        severity = ' '.join(severity[0].split(' ')[1:])
        return severity

    def _parse_message(self, text):
        """
        If possible, parse the Message item from the report text

        Parameters
        ----------
        text : str
            text describing the violation raised by SHACL
        """
        message = [
            line.strip() for line in text.splitlines()
            if 'Message:' in line
        ][0]
        message = ' '.join(message.split(' ')[1:])

        return message

    def _parse_value_node(self, text):
        """
        If possible, parse the Value Node item from the report text

        Parameters
        ----------
        text : str
            text describing the violation raised by SHACL

        Returns
        -------
        the value node text
        """
        try:
            value_node = [
                line.strip() for line in text.splitlines()
                if 'Value Node:' in line
            ][0]
            value_node = ' '.join(value_node.split(' ')[2:])
        except IndexError:
            value_node = None

        return value_node

    def _parse_result_path(self, text):
        """
        If possible, parse the path of the node that triggered the error.

        Parameters
        ----------
        text : str
            text describing the violation raised by SHACL

        Returns
        -------
        the text describing the Result Path
        """
        result_path = [
            line.strip() for line in text.splitlines()
            if 'Result Path:' in line
        ]
        try:
            result_path = ' '.join(result_path[0].split(' ')[2:])
        except IndexError:
            # "Result Path" was not in the text.
            result_path = ''
        
        return result_path

