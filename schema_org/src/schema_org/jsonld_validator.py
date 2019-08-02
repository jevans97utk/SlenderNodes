# Standard library imports
import contextlib
import io
import json
import logging

# 3rd party library imports
from pyshacl import Validator
import pyshacl.rdfutil
import pyshacl.monkey


shacl_graph_src = """
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

schema:MediaObjectShape
    a sh:NodeShape ;
    sh:property [
        sh:path schema:contentUrl ;
        sh:minCount 1 ;
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
        shacl_logger : logging.logger
            We will recover pyshacl log messages from this logger and pass
            some of them (only some) back to our own logger.
        stream : io.StreamIO
            Recover pyshacl messages from this.
        """
        self.logger = logger

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
            return

        if j['@type'] != 'Dataset':
            msg = f"@type key expected to be 'Dataset', not '{j['@type']}'."
            self.logger.error(msg)
            return

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

        shacl_graph = pyshacl.rdfutil.load_from_source(shacl_graph_src,
                                                       rdf_format='turtle',             
                                                       do_owl_imports=False)


        try:                                                                            
            options = dict(inference='rdfs', logger=self.pyshacl_logger)
            validator = Validator(data_graph,
                                  shacl_graph=shacl_graph,                              
                                  options=options)
            with contextlib.redirect_stdout(io.StringIO()):
                # Why do I need to redirect stdio here?
                conforms, report_graph, report_text = validator.run()                       
        except Exception as e:                                                  
            conforms = False                                                            
            report_graph = e                                                            
            report_text = f"Validation Failure - {repr(e)}"
            raise RuntimeError(report_text)
        else:                                                                           
            report_graph = report_graph.serialize(None, encoding='utf-8',               
                                                  format='xml')
                                                                                
        if not conforms:
            self.stream.seek(0)
            report_text = self.stream.getvalue()

            # doc = lxml.etree.parse(io.BytesIO(v_graph))
            self.logger.error(report_text)
