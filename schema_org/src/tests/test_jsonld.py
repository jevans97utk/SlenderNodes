"""
Tests for validity of schema.org JSON-LD.
"""

# Standard library imports
import importlib.resources as ir
import json
import logging
# 3rd party library imports

# Local imports
from schema_org.jsonld_validator import JSONLD_Validator
from .test_common import TestCommon


class TestSuite(TestCommon):

    def setUp(self):

        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                            level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    def test_missing_top_level_type_key(self):
        """
        SCENARIO:  The JSON-LD does not have the '@type': 'Dataset' keypair.

        EXPECTED RESULT.  An error is logged.
        """

        content = ir.read_text('tests.data.jsonld', 'missing_dataset.json')
        j = json.loads(content)

        v = JSONLD_Validator(logger=self.logger)
        with self.assertLogs(logger=v.logger, level='INFO') as cm:
            with self.assertRaises(RuntimeError):
                v.check(j)
            expected = 'JSON-LD missing top-level "@type" key.'
            self.assertErrorLogMessage(cm.output, expected)

    def test_missing_top_level_type_dataset_keypair(self):
        """
        SCENARIO:  The JSON-LD does not have the '@type': 'Dataset' keypair.

        EXPECTED RESULT.  An error is logged.
        """

        j = {'@type': 'Book'}

        v = JSONLD_Validator(logger=self.logger)
        with self.assertLogs(logger=v.logger, level='INFO') as cm:
            with self.assertRaises(RuntimeError):
                v.check(j)
            expected = (
                "JSON-LD @type key expected to be 'Dataset', not 'Book'."
            )
            self.assertErrorLogMessage(cm.output, expected)

    def test_dataset_type_is_camelcase(self):
        """
        SCENARIO:  The JSON-LD has "DataSet" instead of "Dataset".

        EXPECTED RESULT.  An error is logged.
        """

        j = {'@type': 'DataSet'}

        v = JSONLD_Validator(logger=self.logger)
        with self.assertLogs(logger=v.logger, level='INFO') as cm:
            with self.assertRaises(RuntimeError):
                v.check(j)
            expected = (
                "JSON-LD @type key expected to be 'Dataset', not 'DataSet'."
            )
            self.assertErrorLogMessage(cm.output, expected)

    def test_missing_top_level_encoding_keyword(self):
        """
        SCENARIO:  The JSON-LD does not have the 'encoding' keyword at the
        top level.

        EXPECTED RESULT.  An error is logged.
        """
        s = """
        {
            "@context": { "@vocab": "http://schema.org/" },
            "@type": "Dataset"
        }
        """
        j = json.loads(s)

        v = JSONLD_Validator(logger=self.logger)
        with self.assertLogs(logger=v.logger, level='INFO') as cm:
            with self.assertRaises(RuntimeError):
                v.check(j)

            expected = "JSON-LD is missing a top-level encoding keyword."
            self.assertErrorLogMessage(cm.output, expected)

    def test__encoding__missing_contentUrl_keyword(self):
        """
        SCENARIO:  The JSON-LD does not have the 'contentUrl' keyword in the
        'encoding' block.

        EXPECTED RESULT.  An error is logged.
        """
        s = """
        {
            "@context": { "@vocab": "http://schema.org/" },
            "@type": "Dataset",
            "encoding": {
                "@type": "MediaObject",
                "description": ""
            }
        }
        """
        j = json.loads(s)

        v = JSONLD_Validator(logger=self.logger)
        with self.assertLogs(logger=v.logger, level='INFO') as cm:
            with self.assertRaises(RuntimeError):
                v.check(j)
            expected = (
                "JSON-LD encoding section is missing a contentUrl keyword."
            )
            self.assertErrorLogMessage(cm.output, expected)

    def test__encoding__missing_description_keyword(self):
        """
        SCENARIO:  The JSON-LD does not have the 'description' keyword in the
        'encoding' block.

        EXPECTED RESULT.  An warning is logged.
        """
        s = """
        {
            "@context": { "@vocab": "http://schema.org/" },
            "@type": "Dataset",
            "encoding": {
                "@type": "MediaObject",
                "contentUrl": "https://somewhere.out.there.com/",
                "dateModified": "2004-02-02"
            },
            "identifier": {
                "@type": "PropertyValue",
                "value": "something"
            }
        }
        """
        j = json.loads(s)

        v = JSONLD_Validator(logger=self.logger)
        with self.assertLogs(logger=v.logger, level='INFO') as cm:
            with self.assertRaises(RuntimeError):
                v.check(j)
            expected = (
                "JSON-LD encoding section is missing a description keyword."
            )
            self.assertWarningLogMessage(cm.output, expected)
            self.assertLogLevelCallCount(cm.output, level='ERROR', n=0)

    def test__encoding__missing_dateModified_keyword(self):
        """
        SCENARIO:  The JSON-LD does not have the 'dateModified' keyword in the
        'encoding' block.

        EXPECTED RESULT.  An warning is logged, as dateModified is optional.
        """
        s = """
        {
            "@context": { "@vocab": "http://schema.org/" },
            "@type": "Dataset",
            "encoding": {
                "@type": "MediaObject",
                "contentUrl": "https://somewhere.out.there.com/",
                "description": ""
            }
        }
        """
        j = json.loads(s)

        v = JSONLD_Validator(logger=self.logger)
        with self.assertLogs(logger=v.logger, level='INFO') as cm:
            with self.assertRaises(RuntimeError):
                v.check(j)
            expected = (
                "JSON-LD encoding section is missing a dateModified keyword."
            )
            self.assertWarningLogMessage(cm.output, expected)

    def test__encoding__dateModified_is_date(self):
        """
        SCENARIO:  The JSON-LD has the 'dateModified' keyword in the date
        format.

        EXPECTED RESULT.  No errors or warnings are logged.
        """
        s = """
        {
            "@context": { "@vocab": "http://schema.org/" },
            "@type": "Dataset",
            "encoding": {
                "@type": "MediaObject",
                "contentUrl": "https://somewhere.out.there.com/",
                "description": "",
                "dateModified": "2019-08-02"
            }
        }
        """
        j = json.loads(s)

        v = JSONLD_Validator(logger=self.logger)
        with self.assertLogs(logger=v.logger, level='INFO') as cm:
            v.check(j)
            self.assertLogLevelCallCount(cm.output, level='ERROR', n=0)

    def test__encoding__dateModified_is_invalid_date(self):
        """
        SCENARIO:  The JSON-LD has the 'dateModified' keyword that is not in
        a valid date or datetime format.

        EXPECTED RESULT.  A ValueError is raised and the error is logged.
        """
        s = """
        {
            "@context": { "@vocab": "http://schema.org/" },
            "@type": "Dataset",
            "encoding": {
                "@type": "MediaObject",
                "contentUrl": "https://somewhere.out.there.com/",
                "description": "",
                "dateModified": "2019-08-0A"
            }
        }
        """
        j = json.loads(s)

        v = JSONLD_Validator(logger=self.logger)
        with self.assertLogs(logger=v.logger, level='INFO') as cm:
            with self.assertRaises(ValueError):
                v.check(j)
            expected = ['Invalid dateModified key']
            self.assertErrorLogMessage(cm.output, expected)

    def test__encoding__dateModified_is_invalid_datetime(self):
        """
        SCENARIO:  The JSON-LD has the 'dateModified' keyword that is not in
        a valid date or datetime format.

        EXPECTED RESULT.  A ValueError is raised and the error is logged.
        """
        s = """
        {
            "@context": { "@vocab": "http://schema.org/" },
            "@type": "Dataset",
            "encoding": {
                "@type": "MediaObject",
                "contentUrl": "https://somewhere.out.there.com/",
                "description": "",
                "dateModified": "2019-08-08T23:59:70"
            }
        }
        """
        j = json.loads(s)

        v = JSONLD_Validator(logger=self.logger)
        with self.assertLogs(logger=v.logger, level='INFO') as cm:
            with self.assertRaises(ValueError):
                v.check(j)
            expected = ['Invalid dateModified key']
            self.assertErrorLogMessage(cm.output, expected)

    def test__identifier_block_missing(self):
        """
        SCENARIO:  The JSON-LD is missing the identifier section at the top
        level.

        EXPECTED RESULT.  An error is logged.
        """
        s = """
        {
            "@context": { "@vocab": "http://schema.org/" },
            "@type": "Dataset",
            "encoding": {
                "@type": "MediaObject",
                "contentUrl": "https://somewhere.out.there.com/",
                "description": "",
                "dateModified": "2019-08-08T23:59:59"
            }
        }
        """
        j = json.loads(s)

        v = JSONLD_Validator(logger=self.logger)
        with self.assertLogs(logger=v.logger, level='INFO') as cm:
            with self.assertRaises(RuntimeError):
                v.check(j)
            expected = ['JSON-LD is missing a top-level identifier keyword']
            self.assertErrorLogMessage(cm.output, expected)
