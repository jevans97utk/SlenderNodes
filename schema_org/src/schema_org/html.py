# Standard library imports
import json
import logging
import sys

# 3rd party library imports
import lxml.etree

# Local imports
from .jsonld_validator import JSONLD_Validator


class D1CheckHtmlFile(object):
    """
    This class is useful only for local debugging.
    """
    def __init__(self, html_file, verbosity=None):
        self.html_file = html_file
        self.setup_logging(verbosity)

        self.validator = JSONLD_Validator(self.logger)

    def run(self):
        """
        Open the file, retrieve the JSON-LD and validate it.
        """

        self.logger.info('Running...')
        with open(self.html_file, mode='rt') as f:
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
