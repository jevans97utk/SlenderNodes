# Standard library imports
import json

# 3rd party library imports
import pyshacl


shacl_graph = """
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <http://schema.org/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

schema:DatasetShape
    a sh:NodeShape ;
    sh:targetClass schema:Dataset ;
    sh:property [
        sh:path schema:encoding ;
        sh:node schema:MediaObjectShape ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] .

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

    def check(self, j):
        """
        Run JSON-LD compliance checks.

        Parameters
        ----------
        j : dict
            JSON extracted from a landing page <SCRIPT> element.
        """
        if '@type' not in j:
            msg = 'JSON-LD missing top-level "@type" key.'
            self.logger.error(msg)
            return

        if j['@type'] != 'Dataset':
            msg = f"@type key expected to be 'Dataset', not '{j['@type']}'."
            self.logger.error(msg)
            return

        # from this point forward, we rely upon shacl
        kwargs = {
            'shacl_graph': shacl_graph,
            'data_graph_format': 'json-ld',
            'shacl_graph_format': 'turtle',
            'inference': 'rdfs',
            'debug': False,
            'serialize_report_graph': 'xml'
        }
        conforms, v_graph, v_text = pyshacl.validate(json.dumps(j, indent=4),
                                                     **kwargs)

        if not conforms:
            # doc = lxml.etree.parse(io.BytesIO(v_graph))
            self.logger.error(v_text)
