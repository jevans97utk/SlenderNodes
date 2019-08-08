# Standard library imports
import importlib.resources as ir
import json

# 3rd party library imports
from pyshacl import Validator
import pyshacl.rdfutil
import pyshacl.monkey


class InvalidContextError(RuntimeError):
    """
    Raise this exception if the @context key is invalid.
    """
    pass


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

        if j['@context'] == "https://schema.org":
            msg = (
                "The context cannot be \"https://schema.org\", as that URL "
                "does not point to a context document.  A minimally valid "
                "@context entry might be '\"@context\": {\"@vocab\": "
                "\"https://schema.org\"}'."
            )
            raise InvalidContextError(msg)

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

        # Process each report stanza.  If there was only one error, there
        # should only be one report stanza.
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
