"""
Test suite for the XML validation
"""
# Standard library imports
try:
    import importlib.resources as ir
except ImportError:  # pragma:  nocover
    import importlib_resources as ir
import io
import pathlib

# 3rd party library imports
import d1_scimeta
import requests_mock

# Local imports
from schema_org.xml_validator import XMLValidator
from .test_common import TestCommon


class TestSuite(TestCommon):

    def test_file_like_object(self):
        """
        SCENARIO:   A file on the local file system is passed into the
        validator.  The file contains valid ISO 19115 metadata.

        SCENARIO:  no errors
        """
        validator = XMLValidator()

        content = ir.read_binary('tests.data.ieda', '600121iso.xml')
        file = io.BytesIO(content)

        validator.validate(file)

    def test_path(self):
        """
        SCENARIO:   A valid pathlib.Path object is passed into the
        validator.  The file contains valid ISO 19115 metadata.

        SCENARIO:  no errors
        """
        validator = XMLValidator()

        path = pathlib.Path('tests/data/ieda/600121iso.xml')

        validator.validate(path)

    def test_url(self):
        """
        SCENARIO:   A valid URL of a valid XML document is provided.

        EXPECTED RESULT:  no errors
        """
        content = ir.read_binary('tests.data.ieda', '600121iso.xml')
        url = 'http://www.acme.org/600121iso.xml'

        with requests_mock.Mocker() as m:
            m.get(url, content=content)

            validator = XMLValidator()
            validator.validate(url)

    def test_file_like_object_but_invalid_xml(self):
        """
        SCENARIO:   A file on the local file system is passed into the
        validator.  The file contains invalid ISO 19115 metadata.

        EXPECTED RESULT:  A TypeError exception is raised.
        """
        validator = XMLValidator()

        content = ir.read_binary('tests.data.arm', 'nsanimfraod1michC2.c1.xml')
        file = io.BytesIO(content)

        with self.assertRaises(d1_scimeta.util.SciMetaError):
            validator.validate(file)

    def test_local_eml_file(self):
        """
        SCENARIO:   Run the validator against a local EML v2.1.1 file

        EXPECTED RESULT:  no errors
        """
        validator = XMLValidator()

        content = ir.read_binary('tests.data.eml', 'doi_10_5063_f1w957h4.xml')
        file = io.BytesIO(content)

        format_id = "eml://ecoinformatics.org/eml-2.1.1"
        validator = XMLValidator()
        validator.validate(file, format_id=format_id)

    def test_local_pangaea_file(self):
        """
        SCENARIO:   Run the validator against a local Pangaea XML file.

        EXPECTED RESULT:  no errors
        """
        validator = XMLValidator()

        content = ir.read_binary('tests.data.pangaea',
                                 '10p1594_pangaea.729391.xml')
        file = io.BytesIO(content)

        format_id = "http://www.isotc211.org/2005/gmd-pangaea"
        validator = XMLValidator()
        validator.validate(file, format_id=format_id)

    def test_local_pangaea_file__wrong_format_id(self):
        """
        SCENARIO:   Run the validator against a local Pangaea XML file, but
        give a wrong format ID.

        EXPECTED RESULT:  no errors
        """
        validator = XMLValidator()

        content = ir.read_binary('tests.data.pangaea',
                                 '10p1594_pangaea.729391.xml')
        file = io.BytesIO(content)

        format_id = "eml://ecoinformatics.org/eml-2.1.1"
        validator = XMLValidator()
        with self.assertRaises(d1_scimeta.util.SciMetaError):
            validator.validate(file, format_id=format_id)
