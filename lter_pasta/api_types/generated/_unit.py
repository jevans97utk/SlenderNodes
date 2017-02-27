# ./generated/_unit.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:54cf9a010bbda444e584759c31f6ca85f37a73a7
# Generated 2017-01-12 00:01:43.088073 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace eml://ecoinformatics.org/units-2.1.0 [xmlns:unit]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f8e73c56-d894-11e6-9911-000c292ff10e')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('eml://ecoinformatics.org/units-2.1.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {eml://ecoinformatics.org/units-2.1.0}LengthUnitType
class LengthUnitType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LengthUnitType')
    _XSDLocation = pyxb.utils.utility.Location('/home/dahl/d1-git/SlenderNodes/lter_pasta/api_types/schemas/eml-unitTypeDefinitions.xsd', 87, 2)
    _Documentation = ''
LengthUnitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LengthUnitType, enum_prefix=None)
LengthUnitType.meter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='meter', tag='meter')
LengthUnitType.nanometer = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='nanometer', tag='nanometer')
LengthUnitType.micrometer = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='micrometer', tag='micrometer')
LengthUnitType.micron = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='micron', tag='micron')
LengthUnitType.millimeter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='millimeter', tag='millimeter')
LengthUnitType.centimeter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='centimeter', tag='centimeter')
LengthUnitType.decimeter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='decimeter', tag='decimeter')
LengthUnitType.dekameter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='dekameter', tag='dekameter')
LengthUnitType.hectometer = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='hectometer', tag='hectometer')
LengthUnitType.kilometer = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='kilometer', tag='kilometer')
LengthUnitType.megameter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='megameter', tag='megameter')
LengthUnitType.angstrom = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='angstrom', tag='angstrom')
LengthUnitType.inch = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='inch', tag='inch')
LengthUnitType.Foot_US = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='Foot_US', tag='Foot_US')
LengthUnitType.foot = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='foot', tag='foot')
LengthUnitType.Foot_Gold_Coast = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='Foot_Gold_Coast', tag='Foot_Gold_Coast')
LengthUnitType.fathom = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='fathom', tag='fathom')
LengthUnitType.nauticalMile = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='nauticalMile', tag='nauticalMile')
LengthUnitType.yard = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='yard', tag='yard')
LengthUnitType.Yard_Indian = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='Yard_Indian', tag='Yard_Indian')
LengthUnitType.Link_Clarke = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='Link_Clarke', tag='Link_Clarke')
LengthUnitType.Yard_Sears = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='Yard_Sears', tag='Yard_Sears')
LengthUnitType.mile = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='mile', tag='mile')
LengthUnitType._InitializeFacetMap(LengthUnitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LengthUnitType', LengthUnitType)
_module_typeBindings.LengthUnitType = LengthUnitType

# Atomic simple type: {eml://ecoinformatics.org/units-2.1.0}MassUnitType
class MassUnitType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MassUnitType')
    _XSDLocation = pyxb.utils.utility.Location('/home/dahl/d1-git/SlenderNodes/lter_pasta/api_types/schemas/eml-unitTypeDefinitions.xsd', 134, 2)
    _Documentation = ''
MassUnitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MassUnitType, enum_prefix=None)
MassUnitType.kilogram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='kilogram', tag='kilogram')
MassUnitType.nanogram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='nanogram', tag='nanogram')
MassUnitType.microgram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='microgram', tag='microgram')
MassUnitType.milligram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='milligram', tag='milligram')
MassUnitType.centigram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='centigram', tag='centigram')
MassUnitType.decigram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='decigram', tag='decigram')
MassUnitType.gram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='gram', tag='gram')
MassUnitType.dekagram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='dekagram', tag='dekagram')
MassUnitType.hectogram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='hectogram', tag='hectogram')
MassUnitType.megagram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='megagram', tag='megagram')
MassUnitType.tonne = MassUnitType._CF_enumeration.addEnumeration(unicode_value='tonne', tag='tonne')
MassUnitType.pound = MassUnitType._CF_enumeration.addEnumeration(unicode_value='pound', tag='pound')
MassUnitType.ton = MassUnitType._CF_enumeration.addEnumeration(unicode_value='ton', tag='ton')
MassUnitType._InitializeFacetMap(MassUnitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MassUnitType', MassUnitType)
_module_typeBindings.MassUnitType = MassUnitType

# Atomic simple type: {eml://ecoinformatics.org/units-2.1.0}otherUnitType
class otherUnitType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'otherUnitType')
    _XSDLocation = pyxb.utils.utility.Location('/home/dahl/d1-git/SlenderNodes/lter_pasta/api_types/schemas/eml-unitTypeDefinitions.xsd', 172, 2)
    _Documentation = ''
otherUnitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=otherUnitType, enum_prefix=None)
otherUnitType.dimensionless = otherUnitType._CF_enumeration.addEnumeration(unicode_value='dimensionless', tag='dimensionless')
otherUnitType.second = otherUnitType._CF_enumeration.addEnumeration(unicode_value='second', tag='second')
otherUnitType.kelvin = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kelvin', tag='kelvin')
otherUnitType.coulomb = otherUnitType._CF_enumeration.addEnumeration(unicode_value='coulomb', tag='coulomb')
otherUnitType.ampere = otherUnitType._CF_enumeration.addEnumeration(unicode_value='ampere', tag='ampere')
otherUnitType.mole = otherUnitType._CF_enumeration.addEnumeration(unicode_value='mole', tag='mole')
otherUnitType.candela = otherUnitType._CF_enumeration.addEnumeration(unicode_value='candela', tag='candela')
otherUnitType.number = otherUnitType._CF_enumeration.addEnumeration(unicode_value='number', tag='number')
otherUnitType.radian = otherUnitType._CF_enumeration.addEnumeration(unicode_value='radian', tag='radian')
otherUnitType.degree = otherUnitType._CF_enumeration.addEnumeration(unicode_value='degree', tag='degree')
otherUnitType.grad = otherUnitType._CF_enumeration.addEnumeration(unicode_value='grad', tag='grad')
otherUnitType.cubicMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='cubicMeter', tag='cubicMeter')
otherUnitType.nominalMinute = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nominalMinute', tag='nominalMinute')
otherUnitType.nominalHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nominalHour', tag='nominalHour')
otherUnitType.nominalDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nominalDay', tag='nominalDay')
otherUnitType.nominalWeek = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nominalWeek', tag='nominalWeek')
otherUnitType.nominalYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nominalYear', tag='nominalYear')
otherUnitType.nominalLeapYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nominalLeapYear', tag='nominalLeapYear')
otherUnitType.celsius = otherUnitType._CF_enumeration.addEnumeration(unicode_value='celsius', tag='celsius')
otherUnitType.fahrenheit = otherUnitType._CF_enumeration.addEnumeration(unicode_value='fahrenheit', tag='fahrenheit')
otherUnitType.nanosecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nanosecond', tag='nanosecond')
otherUnitType.microsecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microsecond', tag='microsecond')
otherUnitType.millisecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millisecond', tag='millisecond')
otherUnitType.centisecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='centisecond', tag='centisecond')
otherUnitType.decisecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='decisecond', tag='decisecond')
otherUnitType.dekasecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='dekasecond', tag='dekasecond')
otherUnitType.hectosecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='hectosecond', tag='hectosecond')
otherUnitType.kilosecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilosecond', tag='kilosecond')
otherUnitType.megasecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='megasecond', tag='megasecond')
otherUnitType.minute = otherUnitType._CF_enumeration.addEnumeration(unicode_value='minute', tag='minute')
otherUnitType.hour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='hour', tag='hour')
otherUnitType.kiloliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kiloliter', tag='kiloliter')
otherUnitType.microliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microliter', tag='microliter')
otherUnitType.milliliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milliliter', tag='milliliter')
otherUnitType.liter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='liter', tag='liter')
otherUnitType.gallon = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gallon', tag='gallon')
otherUnitType.quart = otherUnitType._CF_enumeration.addEnumeration(unicode_value='quart', tag='quart')
otherUnitType.bushel = otherUnitType._CF_enumeration.addEnumeration(unicode_value='bushel', tag='bushel')
otherUnitType.cubicInch = otherUnitType._CF_enumeration.addEnumeration(unicode_value='cubicInch', tag='cubicInch')
otherUnitType.pint = otherUnitType._CF_enumeration.addEnumeration(unicode_value='pint', tag='pint')
otherUnitType.megahertz = otherUnitType._CF_enumeration.addEnumeration(unicode_value='megahertz', tag='megahertz')
otherUnitType.kilohertz = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilohertz', tag='kilohertz')
otherUnitType.hertz = otherUnitType._CF_enumeration.addEnumeration(unicode_value='hertz', tag='hertz')
otherUnitType.millihertz = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millihertz', tag='millihertz')
otherUnitType.newton = otherUnitType._CF_enumeration.addEnumeration(unicode_value='newton', tag='newton')
otherUnitType.joule = otherUnitType._CF_enumeration.addEnumeration(unicode_value='joule', tag='joule')
otherUnitType.calorie = otherUnitType._CF_enumeration.addEnumeration(unicode_value='calorie', tag='calorie')
otherUnitType.britishThermalUnit = otherUnitType._CF_enumeration.addEnumeration(unicode_value='britishThermalUnit', tag='britishThermalUnit')
otherUnitType.footPound = otherUnitType._CF_enumeration.addEnumeration(unicode_value='footPound', tag='footPound')
otherUnitType.lumen = otherUnitType._CF_enumeration.addEnumeration(unicode_value='lumen', tag='lumen')
otherUnitType.lux = otherUnitType._CF_enumeration.addEnumeration(unicode_value='lux', tag='lux')
otherUnitType.becquerel = otherUnitType._CF_enumeration.addEnumeration(unicode_value='becquerel', tag='becquerel')
otherUnitType.gray = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gray', tag='gray')
otherUnitType.sievert = otherUnitType._CF_enumeration.addEnumeration(unicode_value='sievert', tag='sievert')
otherUnitType.katal = otherUnitType._CF_enumeration.addEnumeration(unicode_value='katal', tag='katal')
otherUnitType.henry = otherUnitType._CF_enumeration.addEnumeration(unicode_value='henry', tag='henry')
otherUnitType.megawatt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='megawatt', tag='megawatt')
otherUnitType.kilowatt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilowatt', tag='kilowatt')
otherUnitType.watt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='watt', tag='watt')
otherUnitType.milliwatt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milliwatt', tag='milliwatt')
otherUnitType.megavolt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='megavolt', tag='megavolt')
otherUnitType.kilovolt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilovolt', tag='kilovolt')
otherUnitType.volt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='volt', tag='volt')
otherUnitType.millivolt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millivolt', tag='millivolt')
otherUnitType.farad = otherUnitType._CF_enumeration.addEnumeration(unicode_value='farad', tag='farad')
otherUnitType.ohm = otherUnitType._CF_enumeration.addEnumeration(unicode_value='ohm', tag='ohm')
otherUnitType.ohmMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='ohmMeter', tag='ohmMeter')
otherUnitType.siemen = otherUnitType._CF_enumeration.addEnumeration(unicode_value='siemen', tag='siemen')
otherUnitType.weber = otherUnitType._CF_enumeration.addEnumeration(unicode_value='weber', tag='weber')
otherUnitType.tesla = otherUnitType._CF_enumeration.addEnumeration(unicode_value='tesla', tag='tesla')
otherUnitType.pascal = otherUnitType._CF_enumeration.addEnumeration(unicode_value='pascal', tag='pascal')
otherUnitType.megapascal = otherUnitType._CF_enumeration.addEnumeration(unicode_value='megapascal', tag='megapascal')
otherUnitType.kilopascal = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilopascal', tag='kilopascal')
otherUnitType.atmosphere = otherUnitType._CF_enumeration.addEnumeration(unicode_value='atmosphere', tag='atmosphere')
otherUnitType.bar = otherUnitType._CF_enumeration.addEnumeration(unicode_value='bar', tag='bar')
otherUnitType.millibar = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millibar', tag='millibar')
otherUnitType.kilogramsPerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramsPerSquareMeter', tag='kilogramsPerSquareMeter')
otherUnitType.gramsPerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerSquareMeter', tag='gramsPerSquareMeter')
otherUnitType.milligramsPerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milligramsPerSquareMeter', tag='milligramsPerSquareMeter')
otherUnitType.kilogramsPerHectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramsPerHectare', tag='kilogramsPerHectare')
otherUnitType.tonnePerHectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value='tonnePerHectare', tag='tonnePerHectare')
otherUnitType.poundsPerSquareInch = otherUnitType._CF_enumeration.addEnumeration(unicode_value='poundsPerSquareInch', tag='poundsPerSquareInch')
otherUnitType.kilogramPerCubicMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramPerCubicMeter', tag='kilogramPerCubicMeter')
otherUnitType.milliGramsPerMilliLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milliGramsPerMilliLiter', tag='milliGramsPerMilliLiter')
otherUnitType.gramsPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerLiter', tag='gramsPerLiter')
otherUnitType.milligramsPerCubicMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milligramsPerCubicMeter', tag='milligramsPerCubicMeter')
otherUnitType.microgramsPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microgramsPerLiter', tag='microgramsPerLiter')
otherUnitType.milligramsPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milligramsPerLiter', tag='milligramsPerLiter')
otherUnitType.gramsPerCubicCentimeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerCubicCentimeter', tag='gramsPerCubicCentimeter')
otherUnitType.gramsPerMilliliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerMilliliter', tag='gramsPerMilliliter')
otherUnitType.gramsPerLiterPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerLiterPerDay', tag='gramsPerLiterPerDay')
otherUnitType.litersPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='litersPerSecond', tag='litersPerSecond')
otherUnitType.cubicMetersPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='cubicMetersPerSecond', tag='cubicMetersPerSecond')
otherUnitType.cubicFeetPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='cubicFeetPerSecond', tag='cubicFeetPerSecond')
otherUnitType.squareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareMeter', tag='squareMeter')
otherUnitType.are = otherUnitType._CF_enumeration.addEnumeration(unicode_value='are', tag='are')
otherUnitType.hectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value='hectare', tag='hectare')
otherUnitType.squareKilometers = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareKilometers', tag='squareKilometers')
otherUnitType.squareMillimeters = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareMillimeters', tag='squareMillimeters')
otherUnitType.squareCentimeters = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareCentimeters', tag='squareCentimeters')
otherUnitType.acre = otherUnitType._CF_enumeration.addEnumeration(unicode_value='acre', tag='acre')
otherUnitType.squareFoot = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareFoot', tag='squareFoot')
otherUnitType.squareYard = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareYard', tag='squareYard')
otherUnitType.squareMile = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareMile', tag='squareMile')
otherUnitType.litersPerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='litersPerSquareMeter', tag='litersPerSquareMeter')
otherUnitType.bushelsPerAcre = otherUnitType._CF_enumeration.addEnumeration(unicode_value='bushelsPerAcre', tag='bushelsPerAcre')
otherUnitType.litersPerHectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value='litersPerHectare', tag='litersPerHectare')
otherUnitType.squareMeterPerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareMeterPerKilogram', tag='squareMeterPerKilogram')
otherUnitType.metersPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='metersPerSecond', tag='metersPerSecond')
otherUnitType.metersPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='metersPerDay', tag='metersPerDay')
otherUnitType.feetPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='feetPerDay', tag='feetPerDay')
otherUnitType.feetPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='feetPerSecond', tag='feetPerSecond')
otherUnitType.feetPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='feetPerHour', tag='feetPerHour')
otherUnitType.yardsPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='yardsPerSecond', tag='yardsPerSecond')
otherUnitType.milesPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milesPerHour', tag='milesPerHour')
otherUnitType.milesPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milesPerSecond', tag='milesPerSecond')
otherUnitType.milesPerMinute = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milesPerMinute', tag='milesPerMinute')
otherUnitType.centimetersPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='centimetersPerSecond', tag='centimetersPerSecond')
otherUnitType.millimetersPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millimetersPerSecond', tag='millimetersPerSecond')
otherUnitType.centimeterPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='centimeterPerYear', tag='centimeterPerYear')
otherUnitType.knots = otherUnitType._CF_enumeration.addEnumeration(unicode_value='knots', tag='knots')
otherUnitType.kilometersPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilometersPerHour', tag='kilometersPerHour')
otherUnitType.metersPerSecondSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='metersPerSecondSquared', tag='metersPerSecondSquared')
otherUnitType.waveNumber = otherUnitType._CF_enumeration.addEnumeration(unicode_value='waveNumber', tag='waveNumber')
otherUnitType.cubicMeterPerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='cubicMeterPerKilogram', tag='cubicMeterPerKilogram')
otherUnitType.cubicMicrometersPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='cubicMicrometersPerGram', tag='cubicMicrometersPerGram')
otherUnitType.amperePerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='amperePerSquareMeter', tag='amperePerSquareMeter')
otherUnitType.amperePerMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='amperePerMeter', tag='amperePerMeter')
otherUnitType.molePerCubicMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molePerCubicMeter', tag='molePerCubicMeter')
otherUnitType.molarity = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molarity', tag='molarity')
otherUnitType.molality = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molality', tag='molality')
otherUnitType.candelaPerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='candelaPerSquareMeter', tag='candelaPerSquareMeter')
otherUnitType.metersSquaredPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='metersSquaredPerSecond', tag='metersSquaredPerSecond')
otherUnitType.metersSquaredPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='metersSquaredPerDay', tag='metersSquaredPerDay')
otherUnitType.feetSquaredPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='feetSquaredPerDay', tag='feetSquaredPerDay')
otherUnitType.kilogramsPerMeterSquaredPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramsPerMeterSquaredPerSecond', tag='kilogramsPerMeterSquaredPerSecond')
otherUnitType.gramsPerCentimeterSquaredPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerCentimeterSquaredPerSecond', tag='gramsPerCentimeterSquaredPerSecond')
otherUnitType.gramsPerMeterSquaredPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerMeterSquaredPerYear', tag='gramsPerMeterSquaredPerYear')
otherUnitType.gramsPerHectarePerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerHectarePerDay', tag='gramsPerHectarePerDay')
otherUnitType.kilogramsPerHectarePerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramsPerHectarePerYear', tag='kilogramsPerHectarePerYear')
otherUnitType.kilogramsPerMeterSquaredPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramsPerMeterSquaredPerYear', tag='kilogramsPerMeterSquaredPerYear')
otherUnitType.molesPerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molesPerKilogram', tag='molesPerKilogram')
otherUnitType.molesPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molesPerGram', tag='molesPerGram')
otherUnitType.millimolesPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millimolesPerGram', tag='millimolesPerGram')
otherUnitType.molesPerKilogramPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molesPerKilogramPerSecond', tag='molesPerKilogramPerSecond')
otherUnitType.nanomolesPerGramPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nanomolesPerGramPerSecond', tag='nanomolesPerGramPerSecond')
otherUnitType.kilogramsPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramsPerSecond', tag='kilogramsPerSecond')
otherUnitType.tonnesPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='tonnesPerYear', tag='tonnesPerYear')
otherUnitType.gramsPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerYear', tag='gramsPerYear')
otherUnitType.numberPerMeterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='numberPerMeterSquared', tag='numberPerMeterSquared')
otherUnitType.numberPerKilometerSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='numberPerKilometerSquared', tag='numberPerKilometerSquared')
otherUnitType.numberPerMeterCubed = otherUnitType._CF_enumeration.addEnumeration(unicode_value='numberPerMeterCubed', tag='numberPerMeterCubed')
otherUnitType.numberPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='numberPerLiter', tag='numberPerLiter')
otherUnitType.numberPerMilliliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='numberPerMilliliter', tag='numberPerMilliliter')
otherUnitType.metersPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='metersPerGram', tag='metersPerGram')
otherUnitType.numberPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='numberPerGram', tag='numberPerGram')
otherUnitType.gramsPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerGram', tag='gramsPerGram')
otherUnitType.microgramsPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microgramsPerGram', tag='microgramsPerGram')
otherUnitType.cubicCentimetersPerCubicCentimeters = otherUnitType._CF_enumeration.addEnumeration(unicode_value='cubicCentimetersPerCubicCentimeters', tag='cubicCentimetersPerCubicCentimeters')
otherUnitType._InitializeFacetMap(otherUnitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'otherUnitType', otherUnitType)
_module_typeBindings.otherUnitType = otherUnitType

# Atomic simple type: {eml://ecoinformatics.org/units-2.1.0}angleUnitType
class angleUnitType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'angleUnitType')
    _XSDLocation = pyxb.utils.utility.Location('/home/dahl/d1-git/SlenderNodes/lter_pasta/api_types/schemas/eml-unitTypeDefinitions.xsd', 361, 2)
    _Documentation = ''
angleUnitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=angleUnitType, enum_prefix=None)
angleUnitType.radian = angleUnitType._CF_enumeration.addEnumeration(unicode_value='radian', tag='radian')
angleUnitType.degree = angleUnitType._CF_enumeration.addEnumeration(unicode_value='degree', tag='degree')
angleUnitType.grad = angleUnitType._CF_enumeration.addEnumeration(unicode_value='grad', tag='grad')
angleUnitType._InitializeFacetMap(angleUnitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'angleUnitType', angleUnitType)
_module_typeBindings.angleUnitType = angleUnitType

# Union simple type: {eml://ecoinformatics.org/units-2.1.0}StandardUnitDictionary
# superclasses pyxb.binding.datatypes.anySimpleType
class StandardUnitDictionary (pyxb.binding.basis.STD_union):

    """Simple type that is a union of LengthUnitType, MassUnitType, otherUnitType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StandardUnitDictionary')
    _XSDLocation = pyxb.utils.utility.Location('/home/dahl/d1-git/SlenderNodes/lter_pasta/api_types/schemas/eml-unitTypeDefinitions.xsd', 64, 2)
    _Documentation = ''

    _MemberTypes = ( LengthUnitType, MassUnitType, otherUnitType, )
StandardUnitDictionary.meter = 'meter'            # originally LengthUnitType.meter
StandardUnitDictionary.nanometer = 'nanometer'    # originally LengthUnitType.nanometer
StandardUnitDictionary.micrometer = 'micrometer'  # originally LengthUnitType.micrometer
StandardUnitDictionary.micron = 'micron'          # originally LengthUnitType.micron
StandardUnitDictionary.millimeter = 'millimeter'  # originally LengthUnitType.millimeter
StandardUnitDictionary.centimeter = 'centimeter'  # originally LengthUnitType.centimeter
StandardUnitDictionary.decimeter = 'decimeter'    # originally LengthUnitType.decimeter
StandardUnitDictionary.dekameter = 'dekameter'    # originally LengthUnitType.dekameter
StandardUnitDictionary.hectometer = 'hectometer'  # originally LengthUnitType.hectometer
StandardUnitDictionary.kilometer = 'kilometer'    # originally LengthUnitType.kilometer
StandardUnitDictionary.megameter = 'megameter'    # originally LengthUnitType.megameter
StandardUnitDictionary.angstrom = 'angstrom'      # originally LengthUnitType.angstrom
StandardUnitDictionary.inch = 'inch'              # originally LengthUnitType.inch
StandardUnitDictionary.Foot_US = 'Foot_US'        # originally LengthUnitType.Foot_US
StandardUnitDictionary.foot = 'foot'              # originally LengthUnitType.foot
StandardUnitDictionary.Foot_Gold_Coast = 'Foot_Gold_Coast'# originally LengthUnitType.Foot_Gold_Coast
StandardUnitDictionary.fathom = 'fathom'          # originally LengthUnitType.fathom
StandardUnitDictionary.nauticalMile = 'nauticalMile'# originally LengthUnitType.nauticalMile
StandardUnitDictionary.yard = 'yard'              # originally LengthUnitType.yard
StandardUnitDictionary.Yard_Indian = 'Yard_Indian'# originally LengthUnitType.Yard_Indian
StandardUnitDictionary.Link_Clarke = 'Link_Clarke'# originally LengthUnitType.Link_Clarke
StandardUnitDictionary.Yard_Sears = 'Yard_Sears'  # originally LengthUnitType.Yard_Sears
StandardUnitDictionary.mile = 'mile'              # originally LengthUnitType.mile
StandardUnitDictionary.kilogram = 'kilogram'      # originally MassUnitType.kilogram
StandardUnitDictionary.nanogram = 'nanogram'      # originally MassUnitType.nanogram
StandardUnitDictionary.microgram = 'microgram'    # originally MassUnitType.microgram
StandardUnitDictionary.milligram = 'milligram'    # originally MassUnitType.milligram
StandardUnitDictionary.centigram = 'centigram'    # originally MassUnitType.centigram
StandardUnitDictionary.decigram = 'decigram'      # originally MassUnitType.decigram
StandardUnitDictionary.gram = 'gram'              # originally MassUnitType.gram
StandardUnitDictionary.dekagram = 'dekagram'      # originally MassUnitType.dekagram
StandardUnitDictionary.hectogram = 'hectogram'    # originally MassUnitType.hectogram
StandardUnitDictionary.megagram = 'megagram'      # originally MassUnitType.megagram
StandardUnitDictionary.tonne = 'tonne'            # originally MassUnitType.tonne
StandardUnitDictionary.pound = 'pound'            # originally MassUnitType.pound
StandardUnitDictionary.ton = 'ton'                # originally MassUnitType.ton
StandardUnitDictionary.dimensionless = 'dimensionless'# originally otherUnitType.dimensionless
StandardUnitDictionary.second = 'second'          # originally otherUnitType.second
StandardUnitDictionary.kelvin = 'kelvin'          # originally otherUnitType.kelvin
StandardUnitDictionary.coulomb = 'coulomb'        # originally otherUnitType.coulomb
StandardUnitDictionary.ampere = 'ampere'          # originally otherUnitType.ampere
StandardUnitDictionary.mole = 'mole'              # originally otherUnitType.mole
StandardUnitDictionary.candela = 'candela'        # originally otherUnitType.candela
StandardUnitDictionary.number = 'number'          # originally otherUnitType.number
StandardUnitDictionary.radian = 'radian'          # originally otherUnitType.radian
StandardUnitDictionary.degree = 'degree'          # originally otherUnitType.degree
StandardUnitDictionary.grad = 'grad'              # originally otherUnitType.grad
StandardUnitDictionary.cubicMeter = 'cubicMeter'  # originally otherUnitType.cubicMeter
StandardUnitDictionary.nominalMinute = 'nominalMinute'# originally otherUnitType.nominalMinute
StandardUnitDictionary.nominalHour = 'nominalHour'# originally otherUnitType.nominalHour
StandardUnitDictionary.nominalDay = 'nominalDay'  # originally otherUnitType.nominalDay
StandardUnitDictionary.nominalWeek = 'nominalWeek'# originally otherUnitType.nominalWeek
StandardUnitDictionary.nominalYear = 'nominalYear'# originally otherUnitType.nominalYear
StandardUnitDictionary.nominalLeapYear = 'nominalLeapYear'# originally otherUnitType.nominalLeapYear
StandardUnitDictionary.celsius = 'celsius'        # originally otherUnitType.celsius
StandardUnitDictionary.fahrenheit = 'fahrenheit'  # originally otherUnitType.fahrenheit
StandardUnitDictionary.nanosecond = 'nanosecond'  # originally otherUnitType.nanosecond
StandardUnitDictionary.microsecond = 'microsecond'# originally otherUnitType.microsecond
StandardUnitDictionary.millisecond = 'millisecond'# originally otherUnitType.millisecond
StandardUnitDictionary.centisecond = 'centisecond'# originally otherUnitType.centisecond
StandardUnitDictionary.decisecond = 'decisecond'  # originally otherUnitType.decisecond
StandardUnitDictionary.dekasecond = 'dekasecond'  # originally otherUnitType.dekasecond
StandardUnitDictionary.hectosecond = 'hectosecond'# originally otherUnitType.hectosecond
StandardUnitDictionary.kilosecond = 'kilosecond'  # originally otherUnitType.kilosecond
StandardUnitDictionary.megasecond = 'megasecond'  # originally otherUnitType.megasecond
StandardUnitDictionary.minute = 'minute'          # originally otherUnitType.minute
StandardUnitDictionary.hour = 'hour'              # originally otherUnitType.hour
StandardUnitDictionary.kiloliter = 'kiloliter'    # originally otherUnitType.kiloliter
StandardUnitDictionary.microliter = 'microliter'  # originally otherUnitType.microliter
StandardUnitDictionary.milliliter = 'milliliter'  # originally otherUnitType.milliliter
StandardUnitDictionary.liter = 'liter'            # originally otherUnitType.liter
StandardUnitDictionary.gallon = 'gallon'          # originally otherUnitType.gallon
StandardUnitDictionary.quart = 'quart'            # originally otherUnitType.quart
StandardUnitDictionary.bushel = 'bushel'          # originally otherUnitType.bushel
StandardUnitDictionary.cubicInch = 'cubicInch'    # originally otherUnitType.cubicInch
StandardUnitDictionary.pint = 'pint'              # originally otherUnitType.pint
StandardUnitDictionary.megahertz = 'megahertz'    # originally otherUnitType.megahertz
StandardUnitDictionary.kilohertz = 'kilohertz'    # originally otherUnitType.kilohertz
StandardUnitDictionary.hertz = 'hertz'            # originally otherUnitType.hertz
StandardUnitDictionary.millihertz = 'millihertz'  # originally otherUnitType.millihertz
StandardUnitDictionary.newton = 'newton'          # originally otherUnitType.newton
StandardUnitDictionary.joule = 'joule'            # originally otherUnitType.joule
StandardUnitDictionary.calorie = 'calorie'        # originally otherUnitType.calorie
StandardUnitDictionary.britishThermalUnit = 'britishThermalUnit'# originally otherUnitType.britishThermalUnit
StandardUnitDictionary.footPound = 'footPound'    # originally otherUnitType.footPound
StandardUnitDictionary.lumen = 'lumen'            # originally otherUnitType.lumen
StandardUnitDictionary.lux = 'lux'                # originally otherUnitType.lux
StandardUnitDictionary.becquerel = 'becquerel'    # originally otherUnitType.becquerel
StandardUnitDictionary.gray = 'gray'              # originally otherUnitType.gray
StandardUnitDictionary.sievert = 'sievert'        # originally otherUnitType.sievert
StandardUnitDictionary.katal = 'katal'            # originally otherUnitType.katal
StandardUnitDictionary.henry = 'henry'            # originally otherUnitType.henry
StandardUnitDictionary.megawatt = 'megawatt'      # originally otherUnitType.megawatt
StandardUnitDictionary.kilowatt = 'kilowatt'      # originally otherUnitType.kilowatt
StandardUnitDictionary.watt = 'watt'              # originally otherUnitType.watt
StandardUnitDictionary.milliwatt = 'milliwatt'    # originally otherUnitType.milliwatt
StandardUnitDictionary.megavolt = 'megavolt'      # originally otherUnitType.megavolt
StandardUnitDictionary.kilovolt = 'kilovolt'      # originally otherUnitType.kilovolt
StandardUnitDictionary.volt = 'volt'              # originally otherUnitType.volt
StandardUnitDictionary.millivolt = 'millivolt'    # originally otherUnitType.millivolt
StandardUnitDictionary.farad = 'farad'            # originally otherUnitType.farad
StandardUnitDictionary.ohm = 'ohm'                # originally otherUnitType.ohm
StandardUnitDictionary.ohmMeter = 'ohmMeter'      # originally otherUnitType.ohmMeter
StandardUnitDictionary.siemen = 'siemen'          # originally otherUnitType.siemen
StandardUnitDictionary.weber = 'weber'            # originally otherUnitType.weber
StandardUnitDictionary.tesla = 'tesla'            # originally otherUnitType.tesla
StandardUnitDictionary.pascal = 'pascal'          # originally otherUnitType.pascal
StandardUnitDictionary.megapascal = 'megapascal'  # originally otherUnitType.megapascal
StandardUnitDictionary.kilopascal = 'kilopascal'  # originally otherUnitType.kilopascal
StandardUnitDictionary.atmosphere = 'atmosphere'  # originally otherUnitType.atmosphere
StandardUnitDictionary.bar = 'bar'                # originally otherUnitType.bar
StandardUnitDictionary.millibar = 'millibar'      # originally otherUnitType.millibar
StandardUnitDictionary.kilogramsPerSquareMeter = 'kilogramsPerSquareMeter'# originally otherUnitType.kilogramsPerSquareMeter
StandardUnitDictionary.gramsPerSquareMeter = 'gramsPerSquareMeter'# originally otherUnitType.gramsPerSquareMeter
StandardUnitDictionary.milligramsPerSquareMeter = 'milligramsPerSquareMeter'# originally otherUnitType.milligramsPerSquareMeter
StandardUnitDictionary.kilogramsPerHectare = 'kilogramsPerHectare'# originally otherUnitType.kilogramsPerHectare
StandardUnitDictionary.tonnePerHectare = 'tonnePerHectare'# originally otherUnitType.tonnePerHectare
StandardUnitDictionary.poundsPerSquareInch = 'poundsPerSquareInch'# originally otherUnitType.poundsPerSquareInch
StandardUnitDictionary.kilogramPerCubicMeter = 'kilogramPerCubicMeter'# originally otherUnitType.kilogramPerCubicMeter
StandardUnitDictionary.milliGramsPerMilliLiter = 'milliGramsPerMilliLiter'# originally otherUnitType.milliGramsPerMilliLiter
StandardUnitDictionary.gramsPerLiter = 'gramsPerLiter'# originally otherUnitType.gramsPerLiter
StandardUnitDictionary.milligramsPerCubicMeter = 'milligramsPerCubicMeter'# originally otherUnitType.milligramsPerCubicMeter
StandardUnitDictionary.microgramsPerLiter = 'microgramsPerLiter'# originally otherUnitType.microgramsPerLiter
StandardUnitDictionary.milligramsPerLiter = 'milligramsPerLiter'# originally otherUnitType.milligramsPerLiter
StandardUnitDictionary.gramsPerCubicCentimeter = 'gramsPerCubicCentimeter'# originally otherUnitType.gramsPerCubicCentimeter
StandardUnitDictionary.gramsPerMilliliter = 'gramsPerMilliliter'# originally otherUnitType.gramsPerMilliliter
StandardUnitDictionary.gramsPerLiterPerDay = 'gramsPerLiterPerDay'# originally otherUnitType.gramsPerLiterPerDay
StandardUnitDictionary.litersPerSecond = 'litersPerSecond'# originally otherUnitType.litersPerSecond
StandardUnitDictionary.cubicMetersPerSecond = 'cubicMetersPerSecond'# originally otherUnitType.cubicMetersPerSecond
StandardUnitDictionary.cubicFeetPerSecond = 'cubicFeetPerSecond'# originally otherUnitType.cubicFeetPerSecond
StandardUnitDictionary.squareMeter = 'squareMeter'# originally otherUnitType.squareMeter
StandardUnitDictionary.are = 'are'                # originally otherUnitType.are
StandardUnitDictionary.hectare = 'hectare'        # originally otherUnitType.hectare
StandardUnitDictionary.squareKilometers = 'squareKilometers'# originally otherUnitType.squareKilometers
StandardUnitDictionary.squareMillimeters = 'squareMillimeters'# originally otherUnitType.squareMillimeters
StandardUnitDictionary.squareCentimeters = 'squareCentimeters'# originally otherUnitType.squareCentimeters
StandardUnitDictionary.acre = 'acre'              # originally otherUnitType.acre
StandardUnitDictionary.squareFoot = 'squareFoot'  # originally otherUnitType.squareFoot
StandardUnitDictionary.squareYard = 'squareYard'  # originally otherUnitType.squareYard
StandardUnitDictionary.squareMile = 'squareMile'  # originally otherUnitType.squareMile
StandardUnitDictionary.litersPerSquareMeter = 'litersPerSquareMeter'# originally otherUnitType.litersPerSquareMeter
StandardUnitDictionary.bushelsPerAcre = 'bushelsPerAcre'# originally otherUnitType.bushelsPerAcre
StandardUnitDictionary.litersPerHectare = 'litersPerHectare'# originally otherUnitType.litersPerHectare
StandardUnitDictionary.squareMeterPerKilogram = 'squareMeterPerKilogram'# originally otherUnitType.squareMeterPerKilogram
StandardUnitDictionary.metersPerSecond = 'metersPerSecond'# originally otherUnitType.metersPerSecond
StandardUnitDictionary.metersPerDay = 'metersPerDay'# originally otherUnitType.metersPerDay
StandardUnitDictionary.feetPerDay = 'feetPerDay'  # originally otherUnitType.feetPerDay
StandardUnitDictionary.feetPerSecond = 'feetPerSecond'# originally otherUnitType.feetPerSecond
StandardUnitDictionary.feetPerHour = 'feetPerHour'# originally otherUnitType.feetPerHour
StandardUnitDictionary.yardsPerSecond = 'yardsPerSecond'# originally otherUnitType.yardsPerSecond
StandardUnitDictionary.milesPerHour = 'milesPerHour'# originally otherUnitType.milesPerHour
StandardUnitDictionary.milesPerSecond = 'milesPerSecond'# originally otherUnitType.milesPerSecond
StandardUnitDictionary.milesPerMinute = 'milesPerMinute'# originally otherUnitType.milesPerMinute
StandardUnitDictionary.centimetersPerSecond = 'centimetersPerSecond'# originally otherUnitType.centimetersPerSecond
StandardUnitDictionary.millimetersPerSecond = 'millimetersPerSecond'# originally otherUnitType.millimetersPerSecond
StandardUnitDictionary.centimeterPerYear = 'centimeterPerYear'# originally otherUnitType.centimeterPerYear
StandardUnitDictionary.knots = 'knots'            # originally otherUnitType.knots
StandardUnitDictionary.kilometersPerHour = 'kilometersPerHour'# originally otherUnitType.kilometersPerHour
StandardUnitDictionary.metersPerSecondSquared = 'metersPerSecondSquared'# originally otherUnitType.metersPerSecondSquared
StandardUnitDictionary.waveNumber = 'waveNumber'  # originally otherUnitType.waveNumber
StandardUnitDictionary.cubicMeterPerKilogram = 'cubicMeterPerKilogram'# originally otherUnitType.cubicMeterPerKilogram
StandardUnitDictionary.cubicMicrometersPerGram = 'cubicMicrometersPerGram'# originally otherUnitType.cubicMicrometersPerGram
StandardUnitDictionary.amperePerSquareMeter = 'amperePerSquareMeter'# originally otherUnitType.amperePerSquareMeter
StandardUnitDictionary.amperePerMeter = 'amperePerMeter'# originally otherUnitType.amperePerMeter
StandardUnitDictionary.molePerCubicMeter = 'molePerCubicMeter'# originally otherUnitType.molePerCubicMeter
StandardUnitDictionary.molarity = 'molarity'      # originally otherUnitType.molarity
StandardUnitDictionary.molality = 'molality'      # originally otherUnitType.molality
StandardUnitDictionary.candelaPerSquareMeter = 'candelaPerSquareMeter'# originally otherUnitType.candelaPerSquareMeter
StandardUnitDictionary.metersSquaredPerSecond = 'metersSquaredPerSecond'# originally otherUnitType.metersSquaredPerSecond
StandardUnitDictionary.metersSquaredPerDay = 'metersSquaredPerDay'# originally otherUnitType.metersSquaredPerDay
StandardUnitDictionary.feetSquaredPerDay = 'feetSquaredPerDay'# originally otherUnitType.feetSquaredPerDay
StandardUnitDictionary.kilogramsPerMeterSquaredPerSecond = 'kilogramsPerMeterSquaredPerSecond'# originally otherUnitType.kilogramsPerMeterSquaredPerSecond
StandardUnitDictionary.gramsPerCentimeterSquaredPerSecond = 'gramsPerCentimeterSquaredPerSecond'# originally otherUnitType.gramsPerCentimeterSquaredPerSecond
StandardUnitDictionary.gramsPerMeterSquaredPerYear = 'gramsPerMeterSquaredPerYear'# originally otherUnitType.gramsPerMeterSquaredPerYear
StandardUnitDictionary.gramsPerHectarePerDay = 'gramsPerHectarePerDay'# originally otherUnitType.gramsPerHectarePerDay
StandardUnitDictionary.kilogramsPerHectarePerYear = 'kilogramsPerHectarePerYear'# originally otherUnitType.kilogramsPerHectarePerYear
StandardUnitDictionary.kilogramsPerMeterSquaredPerYear = 'kilogramsPerMeterSquaredPerYear'# originally otherUnitType.kilogramsPerMeterSquaredPerYear
StandardUnitDictionary.molesPerKilogram = 'molesPerKilogram'# originally otherUnitType.molesPerKilogram
StandardUnitDictionary.molesPerGram = 'molesPerGram'# originally otherUnitType.molesPerGram
StandardUnitDictionary.millimolesPerGram = 'millimolesPerGram'# originally otherUnitType.millimolesPerGram
StandardUnitDictionary.molesPerKilogramPerSecond = 'molesPerKilogramPerSecond'# originally otherUnitType.molesPerKilogramPerSecond
StandardUnitDictionary.nanomolesPerGramPerSecond = 'nanomolesPerGramPerSecond'# originally otherUnitType.nanomolesPerGramPerSecond
StandardUnitDictionary.kilogramsPerSecond = 'kilogramsPerSecond'# originally otherUnitType.kilogramsPerSecond
StandardUnitDictionary.tonnesPerYear = 'tonnesPerYear'# originally otherUnitType.tonnesPerYear
StandardUnitDictionary.gramsPerYear = 'gramsPerYear'# originally otherUnitType.gramsPerYear
StandardUnitDictionary.numberPerMeterSquared = 'numberPerMeterSquared'# originally otherUnitType.numberPerMeterSquared
StandardUnitDictionary.numberPerKilometerSquared = 'numberPerKilometerSquared'# originally otherUnitType.numberPerKilometerSquared
StandardUnitDictionary.numberPerMeterCubed = 'numberPerMeterCubed'# originally otherUnitType.numberPerMeterCubed
StandardUnitDictionary.numberPerLiter = 'numberPerLiter'# originally otherUnitType.numberPerLiter
StandardUnitDictionary.numberPerMilliliter = 'numberPerMilliliter'# originally otherUnitType.numberPerMilliliter
StandardUnitDictionary.metersPerGram = 'metersPerGram'# originally otherUnitType.metersPerGram
StandardUnitDictionary.numberPerGram = 'numberPerGram'# originally otherUnitType.numberPerGram
StandardUnitDictionary.gramsPerGram = 'gramsPerGram'# originally otherUnitType.gramsPerGram
StandardUnitDictionary.microgramsPerGram = 'microgramsPerGram'# originally otherUnitType.microgramsPerGram
StandardUnitDictionary.cubicCentimetersPerCubicCentimeters = 'cubicCentimetersPerCubicCentimeters'# originally otherUnitType.cubicCentimetersPerCubicCentimeters
StandardUnitDictionary._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'StandardUnitDictionary', StandardUnitDictionary)
_module_typeBindings.StandardUnitDictionary = StandardUnitDictionary
