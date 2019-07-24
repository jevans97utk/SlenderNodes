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
import unittest

# 3rd party library imports
# Standard library imports

# 3rd party library imports
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

        SCENARIO:  Validates to regular gmd.
        """
        validator = XMLValidator()

        path = pathlib.Path('tests/data/ieda/600121iso.xml')

        actual = validator.validate(path)
        expected = (
            'http://www.isotc211.org/2005/gmd, '
            'http://www.isotc211.org/2005/gmd-noaa'
        )
        self.assertEqual(actual, expected)

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

        actual = validator.validate(file)
        self.assertIn('XMLSyntaxError', actual)

    def test_local_eml_v200(self):
        """
        SCENARIO:   Run the validator against a local EML v2.0.0 file.  The
        DOI is doi:10.5063/AA/knb.165.2.

        EXPECTED RESULT:  Validates to "eml://ecoinformatics.org/eml-2.0.0.
        """
        content = ir.read_binary('tests.data.eml.v2p0p0', 'example.xml')
        file = io.BytesIO(content)

        validator = XMLValidator()
        actual = validator.validate(file)
        expected = "eml://ecoinformatics.org/eml-2.0.0"
        self.assertEqual(actual, expected)

    def test_local_eml_file(self):
        """
        SCENARIO:   Run the validator against a local EML v2.1.1 file

        EXPECTED RESULT:  no errors
        """
        content = ir.read_binary('tests.data.eml.v211', 'example.xml')
        file = io.BytesIO(content)

        validator = XMLValidator()
        actual = validator.validate(file)
        expected = "eml://ecoinformatics.org/eml-2.1.1"
        self.assertEqual(actual, expected)

    def test_local_pangaea_file(self):
        """
        SCENARIO:   Run the validator against a local Pangaea XML file.

        EXPECTED RESULT:  no errors
        """
        content = ir.read_binary('tests.data.pangaea',
                                 '10p1594_pangaea.729391.xml')
        file = io.BytesIO(content)

        validator = XMLValidator()
        actual = validator.validate(file)
        expected = "http://www.isotc211.org/2005/gmd-pangaea"
        self.assertEqual(actual, expected)

    def test_local_dryad_v3p1(self):
        """
        SCENARIO:   Run the validator against a local dryad file.

        EXPECTED RESULT: The format ID is http://datadryad.org/profile/v3.1
        """
        content = ir.read_binary('tests.data.dryad.v3p1', 'example.xml')
        file = io.BytesIO(content)

        validator = XMLValidator()
        actual = validator.validate(file)
        expected = (
            'http://datadryad.org/profile/v3.1, '
            'http://purl.org/dryad/terms/'
        )
        self.assertEqual(actual, expected)

    def test_local_gmd_noaa(self):
        """
        SCENARIO:   Run the validator against a local GMD NOAA file.

        EXPECTED RESULT: It validates to regular gmd, but will also validate to
        gmd-noaa.
        """
        content = ir.read_binary('tests.data.gmd_noaa', 'example.xml')
        file = io.BytesIO(content)

        validator = XMLValidator()
        actual = validator.validate(file)
        expected = (
            'http://www.isotc211.org/2005/gmd, '
            'http://www.isotc211.org/2005/gmd-noaa'
        )
        self.assertEqual(actual, expected)

    @unittest.skip('Does not validate')
    def test_local_fgdc_std_001_1998(self):
        """
        SCENARIO:   Run the validator against a local FGDC STD 001 1998 file.
        The UUID is 173e8d55-947d-4f73-8552-9eebc32020f2

        EXPECTED RESULT: The format ID is FGDC-STD-001-1998.
        """
        content = ir.read_binary('tests.data.fgdc_std_001_1998', 'example.xml')
        file = io.BytesIO(content)

        validator = XMLValidator()
        actual = validator.validate(file)
        expected = 'FGDC-STD-001-1998'
        self.assertEqual(actual, expected)

    def test_local_eml_v2p1p0(self):
        """
        SCENARIO:   Run the validator against a local EML v2.0.1 file.

        EXPECTED RESULT: The format ID is eml://ecoinformatics.org/eml-2.0.1
        """
        content = ir.read_binary('tests.data.eml.v2p0p1', 'example.xml')
        file = io.BytesIO(content)

        validator = XMLValidator()
        actual = validator.validate(file)
        expected = 'eml://ecoinformatics.org/eml-2.0.1'
        self.assertEqual(actual, expected)

    def test_local_onedcx_v1p0(self):
        """
        SCENARIO:   Run the validator against a local DataONE Dublin Core
        Extended v1.0 file.

        EXPECTED RESULT: The format ID is
        http://ns.dataone.org/metadata/schema/onedcx/v1.0
        """
        content = ir.read_binary('tests.data.onedcx.v1p0', 'example.xml')
        file = io.BytesIO(content)

        validator = XMLValidator()
        actual = validator.validate(file)
        expected = 'http://ns.dataone.org/metadata/schema/onedcx/v1.0'
        self.assertEqual(actual, expected)

    @unittest.skip('Does not work, file was not retrieved from dataone')
    def test_local_ncml_v2p2(self):
        """
        SCENARIO:   Run the validator against a local NCML v2.2 file.

        EXPECTED RESULT: The format ID is
        http://www.unidata.ucar.edu/namespaces/netcdf/ncml-2.2
        """
        content = ir.read_binary('tests.data.netcdf.ncmlv2p2', 'example.xml')
        file = io.BytesIO(content)

        validator = XMLValidator()
        actual = validator.validate(file)
        expected = 'http://www.unidata.ucar.edu/namespaces/netcdf/ncml-2.2'
        self.assertEqual(actual, expected)

    @unittest.skip('Does not work, file was not retrieved from dataone')
    def test_local_esriprof80_dtd(self):
        """
        SCENARIO:   Run the validator against a local file with ESRI
        Profile of the Content Standard for Digital Geospatial Metadata,
        March 2003.

        EXPECTED RESULT: The format ID is
        http://www.esri.com/metadata/esriprof80.dtd
        """
        content = ir.read_binary('tests.data.esriprof80_dtd', 'example.xml')
        file = io.BytesIO(content)

        validator = XMLValidator()
        actual = validator.validate(file)
        expected = 'http://www.esri.com/metadata/esriprof80.dtd'
        self.assertEqual(actual, expected)

    @unittest.skip('Could not acquire such a document')
    def test_local_fgdc_std_001_1_1999(self):
        """
        SCENARIO:   Run the validator against a local file with Content
        Standard for Digital Geospatial Metadata, Biological Data Profile,
        version 001.1-1999

        Could not acquire such a document.  There are such files listed in
        dataone, but no system metadata can be found for the IDs.

        EXPECTED RESULT: The format ID is
        FGDC-STD-001.1-1999
        """
        pass

    @unittest.skip('Could not find such a document')
    def test_local_fgdc_std_001_2_1999(self):
        """
        SCENARIO:   Run the validator against a local file with Content
        Standard for Digital Geospatial Metadata, Biological Data Profile,
        version 001.2-1999

        Could not find such a document.  None are listed in dataone.

        EXPECTED RESULT: The format ID is
        FGDC-STD-001.2-1999
        """
        pass

    @unittest.skip('Could not find such a document')
    def test_local_fgdc_std_001_1_1998(self):
        """
        SCENARIO:   Run the validator against a local file with Content
        Standard for Digital Geospatial Metadata, version 001.1-1998

        Could not find such a document.  None are listed in dataone.

        EXPECTED RESULT: The format ID is
        FGDC-STD-001.1-1998
        """
        pass

    @unittest.skip('Could not find such a document')
    def test_local_incits_453_2009(self):
        """
        SCENARIO:   Run the validator against a local file with North
        American Profile of ISO 19115: 2003 Geographic Information.

        Could not find such a document.  None are listed in dataone.

        EXPECTED RESULT: The format ID is
        INCITS-453-2009
        """
        pass

    def test_local_oai_2p0_oai_dc(self):
        """
        SCENARIO:   Run the validator against a local OAI-PMH Dublin
        Core v2.0, with online related resource file.

        EXPECTED RESULT: The format ID is
        http://www.openarchives.org/OAI/2.0/oai_dc/
        """
        content = ir.read_binary('tests.data.oai.2p0.oai_dc', 'example.xml')
        file = io.BytesIO(content)

        validator = XMLValidator()
        actual = validator.validate(file)
        expected = 'http://www.openarchives.org/OAI/2.0/oai_dc/'
        self.assertEqual(actual, expected)

    @unittest.skip('Does not work, file was not retrieved from dataone')
    def test_local_waterml_v1p1(self):
        """
        SCENARIO:   Run the validator against a local file with Water
        Markup Language, version 1.0.

        EXPECTED RESULT: The format ID is
        http://www.cuahsi.org/waterML/1.1/
        """
        content = ir.read_binary('tests.data.waterML.v1p1', 'example.xml')
        file = io.BytesIO(content)

        validator = XMLValidator()
        actual = validator.validate(file)
        expected = 'http://www.cuahsi.org/waterML/1.1/'
        self.assertEqual(actual, expected)
