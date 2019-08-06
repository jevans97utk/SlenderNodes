# Standard library imports
import contextlib
import importlib.resources as ir
import io
import json
import logging

# 3rd party library imports
import dateutil.parser
from pyshacl import Validator
import pyshacl.rdfutil
import pyshacl.monkey


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
        pyshacl_logger : logging.logger
            We will recover pyshacl log messages from this logger and pass
            some of them (only some) back to our own logger.
        stream : io.StreamIO
            Recover pyshacl messages from this.
        """
        self.logger = logger

        self.shacl_graph_src = ir.read_text('schema_org.data', 'shacl.ttl')

        self.stream = io.StringIO()
        handler = logging.StreamHandler(self.stream)
        self.pyshacl_logger = logging.getLogger('dataone-shacl')
        self.pyshacl_logger.setLevel(logging.DEBUG)
        self.pyshacl_logger.addHandler(handler)

    def check(self, j):
        """
        Run JSON-LD compliance checks, both DATAONE and SHACL.

        Parameters
        ----------
        j : dict
            JSON extracted from a landing page <SCRIPT> element.
        """
        self.logger.debug(f'{__name__}:check')
        if '@type' not in j:
            msg = 'JSON-LD missing top-level "@type" key.'
            self.logger.error(msg)
            raise RuntimeError(msg)

        if j['@type'] != 'Dataset':
            msg = (
                f"JSON-LD @type key expected to be 'Dataset', not "
                f"'{j['@type']}'."
            )
            self.logger.error(msg)
            raise RuntimeError(msg)

        self.check_shacl(j)

        self.post_shacl_checks(j)

    def post_shacl_checks(self, j):
        """
        Run tests that do not lend themselves well to SHACL.

        Parameters
        ----------
        j : dict
            JSON extracted from a landing page <SCRIPT> element.
        """
        self.logger.debug(f'{__name__}:post_shacl_checks')

        # SHACL seems to have a hard time validating dates.
        #
        # Validate the dateModified key if it is there.
        if 'encoding' in j and 'dateModified' in j['encoding']:
            try:
                dateutil.parser.isoparse(j['encoding']['dateModified'])
            except ValueError as e:
                msg = (
                    f"Invalid dateModified key:  "
                    f"Value \"{j['encoding']['dateModified']}\" "
                    f"produced error message \"{e}\".  "
                    f"Valid examples might be '2002-04-04' or "
                    f"'2019-08-02T23:59:59Z'"
                )
                self.logger.error(msg)
                raise

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
                'logger': self.pyshacl_logger,
                'abort_on_error': False
            }
            validator = Validator(data_graph,
                                  shacl_graph=shacl_graph,
                                  options=options)
            conforms, report_graph, report_text = validator.run()

        except Exception as e:
            conforms = False
            report_graph = e
            report_text = f"Validation Failure - {repr(e)}"
            self.logger.debug(report_text)
            raise RuntimeError("JSON-LD does not conform.")
        else:
            report_graph = report_graph.serialize(None, encoding='utf-8',
                                                  format='xml')
        if conforms:
            self.logger.info("JSON-LD conforms.")
            return

        self.stream.seek(0)
        report_text = self.stream.getvalue()

        items = report_text.strip().split('\n\n')
        error_count = 0
        for item in items:
            message = [
                line.strip() for line in item.splitlines()
                if 'Message:' in line
            ][0]
            message = ' '.join(message.split(' ')[1:])

            severity = [
                line for line in item.splitlines() if 'Severity:' in line
            ]
            severity = ' '.join(severity[0].split(' ')[1:])

            if 'sh:Warning' in severity:
                self.logger.warning(message)
            else:
                error_count += 1
                self.logger.error(message)

        if error_count > 0:
            raise RuntimeError("JSON-LD does not conform.")
