# Standard library imports
import importlib.resources as ir
import json
import logging
import sys
import urllib.parse

# 3rd party library imports
import lxml.etree
from pyshacl import Validator
import pyshacl.rdfutil
import pyshacl.monkey


class InvalidContextError(RuntimeError):
    """
    Raise this exception if the @context key is invalid.
    """
    pass


class InvalidIRIError(RuntimeError):
    """
    Raise this exception if the top-level @id key is invalid.
    """


class JSONLD_Validator(object):
    """
    Attributes
    ----------
    logger : logging.Logger
        Same logger as 'dataone'.
    """

    def __init__(self, logger):
        """
        Parameters
        ----------
        logger : logging.Logger
            Same logger as 'dataone'.
        """
        self.logger = logger

        self.shacl_graph_src = ir.read_text('schema_org.data', 'shacl.ttl')

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
            raise RuntimeError(msg)

        # Inline contexts are currently problematic with regards to
        # certain date keys such as "dateModified".  Suppress this by
        # swapping out the inline context with something else.
        bad_contexts = ["http://schema.org", "http://schema.org/",
                        "https://schema.org", "https://schema.org/"]
        if j['@context'] in bad_contexts:
            j['@context'] = {"@vocab": "http://schema.org/"}

        if '@type' not in j:
            msg = 'JSON-LD missing top-level "@type" key.'
            raise RuntimeError(msg)

        if j['@type'] != 'Dataset':
            msg = (
                f"JSON-LD @type key expected to be 'Dataset', not "
                f"'{j['@type']}'."
            )
            raise RuntimeError(msg)

        if '@id' not in j:
            msg = 'JSON-LD missing top-level "@id" key.'
            raise RuntimeError(msg)

        p = urllib.parse.urlparse(j['@id'])
        if (
            len(p.scheme) == 0
            or len(p.netloc) == 0
            or len(p.path) == 0
        ):
            msg = (
                f"JSON-LD top-level '@id' key \"{j['@id']}\" does not look "
                f"like an IRI."
            )
            raise InvalidIRIError(msg)

    def check(self, j):
        """
        Run JSON-LD compliance checks, both DATAONE and SHACL.

        Parameters
        ----------
        j : dict
            JSON extracted from a landing page <SCRIPT> element.
        """
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
            report_text = f"Validation Failure - {repr(e)}"
            self.logger.debug(report_text)
            raise RuntimeError("JSON-LD does not conform.")

        if conforms:
            self.logger.info("JSON-LD conforms.")
            return

        # So the JSON-LD did not conform.  Parse the report text and log
        # human-readable messages.
        reports = self.parse_reports(report_text)

        error_count = 0
        for report in reports:

            if 'sh:Warning' in report['Severity']:
                self.logger.warning(report['Message'])
            else:
                error_count += 1
                self.logger.error(report['Message'])

        if error_count > 0:
            raise RuntimeError("JSON-LD does not conform.")

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

            try:
                value_node = [
                    line.strip() for line in item.splitlines()
                    if 'Value Node:' in line
                ][0]
                value_node = ' '.join(value_node.split(' ')[2:])
            except IndexError:
                d['Value Node'] = ''
            else:
                d['Value Node'] = value_node

            message = [
                line.strip() for line in item.splitlines()
                if 'Message:' in line
            ][0]
            message = ' '.join(message.split(' ')[1:])
            d['Message'] = message

            severity = [
                line.strip() for line in item.splitlines()
                if 'Severity:' in line
            ]
            severity = ' '.join(severity[0].split(' ')[1:])
            d['Severity'] = severity

            result_path = [
                line.strip() for line in item.splitlines()
                if 'Result Path:' in line
            ]
            result_path = ' '.join(result_path[0].split(' ')[2:])
            d['Result Path'] = result_path

            # The Message field will be an amalgamation.
            if d['Value Node'] != '':
                d['Message'] += f"  The value found was {d['Value Node']}"

            reports.append(d)

        return reports


class D1CheckHtmlFile(object):
    """
    This is useful only for local debugging.
    """
    def __init__(self, html_file, verbosity=None):
        self.html_file = html_file
        self.setup_logging(verbosity)

        self.validator = JSONLD_Validator(self.logger)

    def run(self):

        self.logger.info('Running...')
        with open(self.html_file) as f:
            text = f.read()
        doc = lxml.etree.HTML(text)
        scripts = doc.xpath('head/script[@type="application/ld+json"]')
        script = scripts[0]

        self.logger.info('Loading...')
        j = json.loads(script.text)

        self.logger.info('Validating...')
        self.validator.check(j)

    def setup_logging(self, verbosity):
        """
        Parameters
        ----------
        verbosity : str
            Level of logging verbosity.
        """
        level = getattr(logging, verbosity)
        self.logger = logging.getLogger(__name__)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(format)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
