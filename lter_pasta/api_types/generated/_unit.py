# ./generated/_unit.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:54cf9a010bbda444e584759c31f6ca85f37a73a7
# Generated 2014-03-16 22:56:49.634320 by PyXB version 1.2.3
# Namespace eml://ecoinformatics.org/units-2.1.0 [xmlns:unit]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:8bdde10a-ad90-11e3-bf48-000c294230b4')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'eml://ecoinformatics.org/units-2.1.0', create_if_missing=True)
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
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
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

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LengthUnitType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-unitTypeDefinitions.xsd', 87, 2)
    _Documentation = ''
LengthUnitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LengthUnitType, enum_prefix=None)
LengthUnitType.meter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'meter', tag=u'meter')
LengthUnitType.nanometer = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'nanometer', tag=u'nanometer')
LengthUnitType.micrometer = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'micrometer', tag=u'micrometer')
LengthUnitType.micron = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'micron', tag=u'micron')
LengthUnitType.millimeter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'millimeter', tag=u'millimeter')
LengthUnitType.centimeter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'centimeter', tag=u'centimeter')
LengthUnitType.decimeter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'decimeter', tag=u'decimeter')
LengthUnitType.dekameter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'dekameter', tag=u'dekameter')
LengthUnitType.hectometer = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'hectometer', tag=u'hectometer')
LengthUnitType.kilometer = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'kilometer', tag=u'kilometer')
LengthUnitType.megameter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'megameter', tag=u'megameter')
LengthUnitType.angstrom = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'angstrom', tag=u'angstrom')
LengthUnitType.inch = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'inch', tag=u'inch')
LengthUnitType.Foot_US = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'Foot_US', tag=u'Foot_US')
LengthUnitType.foot = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'foot', tag=u'foot')
LengthUnitType.Foot_Gold_Coast = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'Foot_Gold_Coast', tag=u'Foot_Gold_Coast')
LengthUnitType.fathom = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'fathom', tag=u'fathom')
LengthUnitType.nauticalMile = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'nauticalMile', tag=u'nauticalMile')
LengthUnitType.yard = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'yard', tag=u'yard')
LengthUnitType.Yard_Indian = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'Yard_Indian', tag=u'Yard_Indian')
LengthUnitType.Link_Clarke = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'Link_Clarke', tag=u'Link_Clarke')
LengthUnitType.Yard_Sears = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'Yard_Sears', tag=u'Yard_Sears')
LengthUnitType.mile = LengthUnitType._CF_enumeration.addEnumeration(unicode_value=u'mile', tag=u'mile')
LengthUnitType._InitializeFacetMap(LengthUnitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LengthUnitType', LengthUnitType)

# Atomic simple type: {eml://ecoinformatics.org/units-2.1.0}MassUnitType
class MassUnitType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MassUnitType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-unitTypeDefinitions.xsd', 134, 2)
    _Documentation = ''
MassUnitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MassUnitType, enum_prefix=None)
MassUnitType.kilogram = MassUnitType._CF_enumeration.addEnumeration(unicode_value=u'kilogram', tag=u'kilogram')
MassUnitType.nanogram = MassUnitType._CF_enumeration.addEnumeration(unicode_value=u'nanogram', tag=u'nanogram')
MassUnitType.microgram = MassUnitType._CF_enumeration.addEnumeration(unicode_value=u'microgram', tag=u'microgram')
MassUnitType.milligram = MassUnitType._CF_enumeration.addEnumeration(unicode_value=u'milligram', tag=u'milligram')
MassUnitType.centigram = MassUnitType._CF_enumeration.addEnumeration(unicode_value=u'centigram', tag=u'centigram')
MassUnitType.decigram = MassUnitType._CF_enumeration.addEnumeration(unicode_value=u'decigram', tag=u'decigram')
MassUnitType.gram = MassUnitType._CF_enumeration.addEnumeration(unicode_value=u'gram', tag=u'gram')
MassUnitType.dekagram = MassUnitType._CF_enumeration.addEnumeration(unicode_value=u'dekagram', tag=u'dekagram')
MassUnitType.hectogram = MassUnitType._CF_enumeration.addEnumeration(unicode_value=u'hectogram', tag=u'hectogram')
MassUnitType.megagram = MassUnitType._CF_enumeration.addEnumeration(unicode_value=u'megagram', tag=u'megagram')
MassUnitType.tonne = MassUnitType._CF_enumeration.addEnumeration(unicode_value=u'tonne', tag=u'tonne')
MassUnitType.pound = MassUnitType._CF_enumeration.addEnumeration(unicode_value=u'pound', tag=u'pound')
MassUnitType.ton = MassUnitType._CF_enumeration.addEnumeration(unicode_value=u'ton', tag=u'ton')
MassUnitType._InitializeFacetMap(MassUnitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MassUnitType', MassUnitType)

# Atomic simple type: {eml://ecoinformatics.org/units-2.1.0}otherUnitType
class otherUnitType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'otherUnitType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-unitTypeDefinitions.xsd', 172, 2)
    _Documentation = ''
otherUnitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=otherUnitType, enum_prefix=None)
otherUnitType.dimensionless = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'dimensionless', tag=u'dimensionless')
otherUnitType.second = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'second', tag=u'second')
otherUnitType.kelvin = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'kelvin', tag=u'kelvin')
otherUnitType.coulomb = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'coulomb', tag=u'coulomb')
otherUnitType.ampere = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'ampere', tag=u'ampere')
otherUnitType.mole = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'mole', tag=u'mole')
otherUnitType.candela = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'candela', tag=u'candela')
otherUnitType.number = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'number', tag=u'number')
otherUnitType.radian = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'radian', tag=u'radian')
otherUnitType.degree = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'degree', tag=u'degree')
otherUnitType.grad = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'grad', tag=u'grad')
otherUnitType.cubicMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'cubicMeter', tag=u'cubicMeter')
otherUnitType.nominalMinute = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'nominalMinute', tag=u'nominalMinute')
otherUnitType.nominalHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'nominalHour', tag=u'nominalHour')
otherUnitType.nominalDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'nominalDay', tag=u'nominalDay')
otherUnitType.nominalWeek = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'nominalWeek', tag=u'nominalWeek')
otherUnitType.nominalYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'nominalYear', tag=u'nominalYear')
otherUnitType.nominalLeapYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'nominalLeapYear', tag=u'nominalLeapYear')
otherUnitType.celsius = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'celsius', tag=u'celsius')
otherUnitType.fahrenheit = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'fahrenheit', tag=u'fahrenheit')
otherUnitType.nanosecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'nanosecond', tag=u'nanosecond')
otherUnitType.microsecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'microsecond', tag=u'microsecond')
otherUnitType.millisecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'millisecond', tag=u'millisecond')
otherUnitType.centisecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'centisecond', tag=u'centisecond')
otherUnitType.decisecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'decisecond', tag=u'decisecond')
otherUnitType.dekasecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'dekasecond', tag=u'dekasecond')
otherUnitType.hectosecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'hectosecond', tag=u'hectosecond')
otherUnitType.kilosecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'kilosecond', tag=u'kilosecond')
otherUnitType.megasecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'megasecond', tag=u'megasecond')
otherUnitType.minute = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'minute', tag=u'minute')
otherUnitType.hour = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'hour', tag=u'hour')
otherUnitType.kiloliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'kiloliter', tag=u'kiloliter')
otherUnitType.microliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'microliter', tag=u'microliter')
otherUnitType.milliliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'milliliter', tag=u'milliliter')
otherUnitType.liter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'liter', tag=u'liter')
otherUnitType.gallon = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'gallon', tag=u'gallon')
otherUnitType.quart = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'quart', tag=u'quart')
otherUnitType.bushel = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'bushel', tag=u'bushel')
otherUnitType.cubicInch = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'cubicInch', tag=u'cubicInch')
otherUnitType.pint = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'pint', tag=u'pint')
otherUnitType.megahertz = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'megahertz', tag=u'megahertz')
otherUnitType.kilohertz = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'kilohertz', tag=u'kilohertz')
otherUnitType.hertz = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'hertz', tag=u'hertz')
otherUnitType.millihertz = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'millihertz', tag=u'millihertz')
otherUnitType.newton = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'newton', tag=u'newton')
otherUnitType.joule = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'joule', tag=u'joule')
otherUnitType.calorie = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'calorie', tag=u'calorie')
otherUnitType.britishThermalUnit = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'britishThermalUnit', tag=u'britishThermalUnit')
otherUnitType.footPound = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'footPound', tag=u'footPound')
otherUnitType.lumen = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'lumen', tag=u'lumen')
otherUnitType.lux = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'lux', tag=u'lux')
otherUnitType.becquerel = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'becquerel', tag=u'becquerel')
otherUnitType.gray = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'gray', tag=u'gray')
otherUnitType.sievert = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'sievert', tag=u'sievert')
otherUnitType.katal = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'katal', tag=u'katal')
otherUnitType.henry = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'henry', tag=u'henry')
otherUnitType.megawatt = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'megawatt', tag=u'megawatt')
otherUnitType.kilowatt = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'kilowatt', tag=u'kilowatt')
otherUnitType.watt = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'watt', tag=u'watt')
otherUnitType.milliwatt = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'milliwatt', tag=u'milliwatt')
otherUnitType.megavolt = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'megavolt', tag=u'megavolt')
otherUnitType.kilovolt = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'kilovolt', tag=u'kilovolt')
otherUnitType.volt = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'volt', tag=u'volt')
otherUnitType.millivolt = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'millivolt', tag=u'millivolt')
otherUnitType.farad = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'farad', tag=u'farad')
otherUnitType.ohm = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'ohm', tag=u'ohm')
otherUnitType.ohmMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'ohmMeter', tag=u'ohmMeter')
otherUnitType.siemen = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'siemen', tag=u'siemen')
otherUnitType.weber = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'weber', tag=u'weber')
otherUnitType.tesla = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'tesla', tag=u'tesla')
otherUnitType.pascal = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'pascal', tag=u'pascal')
otherUnitType.megapascal = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'megapascal', tag=u'megapascal')
otherUnitType.kilopascal = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'kilopascal', tag=u'kilopascal')
otherUnitType.atmosphere = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'atmosphere', tag=u'atmosphere')
otherUnitType.bar = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'bar', tag=u'bar')
otherUnitType.millibar = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'millibar', tag=u'millibar')
otherUnitType.kilogramsPerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'kilogramsPerSquareMeter', tag=u'kilogramsPerSquareMeter')
otherUnitType.gramsPerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'gramsPerSquareMeter', tag=u'gramsPerSquareMeter')
otherUnitType.milligramsPerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'milligramsPerSquareMeter', tag=u'milligramsPerSquareMeter')
otherUnitType.kilogramsPerHectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'kilogramsPerHectare', tag=u'kilogramsPerHectare')
otherUnitType.tonnePerHectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'tonnePerHectare', tag=u'tonnePerHectare')
otherUnitType.poundsPerSquareInch = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'poundsPerSquareInch', tag=u'poundsPerSquareInch')
otherUnitType.kilogramPerCubicMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'kilogramPerCubicMeter', tag=u'kilogramPerCubicMeter')
otherUnitType.milliGramsPerMilliLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'milliGramsPerMilliLiter', tag=u'milliGramsPerMilliLiter')
otherUnitType.gramsPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'gramsPerLiter', tag=u'gramsPerLiter')
otherUnitType.milligramsPerCubicMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'milligramsPerCubicMeter', tag=u'milligramsPerCubicMeter')
otherUnitType.microgramsPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'microgramsPerLiter', tag=u'microgramsPerLiter')
otherUnitType.milligramsPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'milligramsPerLiter', tag=u'milligramsPerLiter')
otherUnitType.gramsPerCubicCentimeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'gramsPerCubicCentimeter', tag=u'gramsPerCubicCentimeter')
otherUnitType.gramsPerMilliliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'gramsPerMilliliter', tag=u'gramsPerMilliliter')
otherUnitType.gramsPerLiterPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'gramsPerLiterPerDay', tag=u'gramsPerLiterPerDay')
otherUnitType.litersPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'litersPerSecond', tag=u'litersPerSecond')
otherUnitType.cubicMetersPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'cubicMetersPerSecond', tag=u'cubicMetersPerSecond')
otherUnitType.cubicFeetPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'cubicFeetPerSecond', tag=u'cubicFeetPerSecond')
otherUnitType.squareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'squareMeter', tag=u'squareMeter')
otherUnitType.are = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'are', tag=u'are')
otherUnitType.hectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'hectare', tag=u'hectare')
otherUnitType.squareKilometers = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'squareKilometers', tag=u'squareKilometers')
otherUnitType.squareMillimeters = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'squareMillimeters', tag=u'squareMillimeters')
otherUnitType.squareCentimeters = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'squareCentimeters', tag=u'squareCentimeters')
otherUnitType.acre = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'acre', tag=u'acre')
otherUnitType.squareFoot = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'squareFoot', tag=u'squareFoot')
otherUnitType.squareYard = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'squareYard', tag=u'squareYard')
otherUnitType.squareMile = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'squareMile', tag=u'squareMile')
otherUnitType.litersPerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'litersPerSquareMeter', tag=u'litersPerSquareMeter')
otherUnitType.bushelsPerAcre = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'bushelsPerAcre', tag=u'bushelsPerAcre')
otherUnitType.litersPerHectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'litersPerHectare', tag=u'litersPerHectare')
otherUnitType.squareMeterPerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'squareMeterPerKilogram', tag=u'squareMeterPerKilogram')
otherUnitType.metersPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'metersPerSecond', tag=u'metersPerSecond')
otherUnitType.metersPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'metersPerDay', tag=u'metersPerDay')
otherUnitType.feetPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'feetPerDay', tag=u'feetPerDay')
otherUnitType.feetPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'feetPerSecond', tag=u'feetPerSecond')
otherUnitType.feetPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'feetPerHour', tag=u'feetPerHour')
otherUnitType.yardsPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'yardsPerSecond', tag=u'yardsPerSecond')
otherUnitType.milesPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'milesPerHour', tag=u'milesPerHour')
otherUnitType.milesPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'milesPerSecond', tag=u'milesPerSecond')
otherUnitType.milesPerMinute = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'milesPerMinute', tag=u'milesPerMinute')
otherUnitType.centimetersPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'centimetersPerSecond', tag=u'centimetersPerSecond')
otherUnitType.millimetersPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'millimetersPerSecond', tag=u'millimetersPerSecond')
otherUnitType.centimeterPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'centimeterPerYear', tag=u'centimeterPerYear')
otherUnitType.knots = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'knots', tag=u'knots')
otherUnitType.kilometersPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'kilometersPerHour', tag=u'kilometersPerHour')
otherUnitType.metersPerSecondSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'metersPerSecondSquared', tag=u'metersPerSecondSquared')
otherUnitType.waveNumber = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'waveNumber', tag=u'waveNumber')
otherUnitType.cubicMeterPerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'cubicMeterPerKilogram', tag=u'cubicMeterPerKilogram')
otherUnitType.cubicMicrometersPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'cubicMicrometersPerGram', tag=u'cubicMicrometersPerGram')
otherUnitType.amperePerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'amperePerSquareMeter', tag=u'amperePerSquareMeter')
otherUnitType.amperePerMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'amperePerMeter', tag=u'amperePerMeter')
otherUnitType.molePerCubicMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'molePerCubicMeter', tag=u'molePerCubicMeter')
otherUnitType.molarity = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'molarity', tag=u'molarity')
otherUnitType.molality = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'molality', tag=u'molality')
otherUnitType.candelaPerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'candelaPerSquareMeter', tag=u'candelaPerSquareMeter')
otherUnitType.metersSquaredPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'metersSquaredPerSecond', tag=u'metersSquaredPerSecond')
otherUnitType.metersSquaredPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'metersSquaredPerDay', tag=u'metersSquaredPerDay')
otherUnitType.feetSquaredPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'feetSquaredPerDay', tag=u'feetSquaredPerDay')
otherUnitType.kilogramsPerMeterSquaredPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'kilogramsPerMeterSquaredPerSecond', tag=u'kilogramsPerMeterSquaredPerSecond')
otherUnitType.gramsPerCentimeterSquaredPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'gramsPerCentimeterSquaredPerSecond', tag=u'gramsPerCentimeterSquaredPerSecond')
otherUnitType.gramsPerMeterSquaredPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'gramsPerMeterSquaredPerYear', tag=u'gramsPerMeterSquaredPerYear')
otherUnitType.gramsPerHectarePerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'gramsPerHectarePerDay', tag=u'gramsPerHectarePerDay')
otherUnitType.kilogramsPerHectarePerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'kilogramsPerHectarePerYear', tag=u'kilogramsPerHectarePerYear')
otherUnitType.kilogramsPerMeterSquaredPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'kilogramsPerMeterSquaredPerYear', tag=u'kilogramsPerMeterSquaredPerYear')
otherUnitType.molesPerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'molesPerKilogram', tag=u'molesPerKilogram')
otherUnitType.molesPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'molesPerGram', tag=u'molesPerGram')
otherUnitType.millimolesPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'millimolesPerGram', tag=u'millimolesPerGram')
otherUnitType.molesPerKilogramPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'molesPerKilogramPerSecond', tag=u'molesPerKilogramPerSecond')
otherUnitType.nanomolesPerGramPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'nanomolesPerGramPerSecond', tag=u'nanomolesPerGramPerSecond')
otherUnitType.kilogramsPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'kilogramsPerSecond', tag=u'kilogramsPerSecond')
otherUnitType.tonnesPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'tonnesPerYear', tag=u'tonnesPerYear')
otherUnitType.gramsPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'gramsPerYear', tag=u'gramsPerYear')
otherUnitType.numberPerMeterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'numberPerMeterSquared', tag=u'numberPerMeterSquared')
otherUnitType.numberPerKilometerSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'numberPerKilometerSquared', tag=u'numberPerKilometerSquared')
otherUnitType.numberPerMeterCubed = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'numberPerMeterCubed', tag=u'numberPerMeterCubed')
otherUnitType.numberPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'numberPerLiter', tag=u'numberPerLiter')
otherUnitType.numberPerMilliliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'numberPerMilliliter', tag=u'numberPerMilliliter')
otherUnitType.metersPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'metersPerGram', tag=u'metersPerGram')
otherUnitType.numberPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'numberPerGram', tag=u'numberPerGram')
otherUnitType.gramsPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'gramsPerGram', tag=u'gramsPerGram')
otherUnitType.microgramsPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'microgramsPerGram', tag=u'microgramsPerGram')
otherUnitType.cubicCentimetersPerCubicCentimeters = otherUnitType._CF_enumeration.addEnumeration(unicode_value=u'cubicCentimetersPerCubicCentimeters', tag=u'cubicCentimetersPerCubicCentimeters')
otherUnitType._InitializeFacetMap(otherUnitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'otherUnitType', otherUnitType)

# Atomic simple type: {eml://ecoinformatics.org/units-2.1.0}angleUnitType
class angleUnitType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'angleUnitType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-unitTypeDefinitions.xsd', 361, 2)
    _Documentation = ''
angleUnitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=angleUnitType, enum_prefix=None)
angleUnitType.radian = angleUnitType._CF_enumeration.addEnumeration(unicode_value=u'radian', tag=u'radian')
angleUnitType.degree = angleUnitType._CF_enumeration.addEnumeration(unicode_value=u'degree', tag=u'degree')
angleUnitType.grad = angleUnitType._CF_enumeration.addEnumeration(unicode_value=u'grad', tag=u'grad')
angleUnitType._InitializeFacetMap(angleUnitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'angleUnitType', angleUnitType)

# Union simple type: {eml://ecoinformatics.org/units-2.1.0}StandardUnitDictionary
# superclasses pyxb.binding.datatypes.anySimpleType
class StandardUnitDictionary (pyxb.binding.basis.STD_union):

    """Simple type that is a union of LengthUnitType, MassUnitType, otherUnitType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StandardUnitDictionary')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-unitTypeDefinitions.xsd', 64, 2)
    _Documentation = ''

    _MemberTypes = ( LengthUnitType, MassUnitType, otherUnitType, )
StandardUnitDictionary.meter = u'meter'           # originally LengthUnitType.meter
StandardUnitDictionary.nanometer = u'nanometer'   # originally LengthUnitType.nanometer
StandardUnitDictionary.micrometer = u'micrometer' # originally LengthUnitType.micrometer
StandardUnitDictionary.micron = u'micron'         # originally LengthUnitType.micron
StandardUnitDictionary.millimeter = u'millimeter' # originally LengthUnitType.millimeter
StandardUnitDictionary.centimeter = u'centimeter' # originally LengthUnitType.centimeter
StandardUnitDictionary.decimeter = u'decimeter'   # originally LengthUnitType.decimeter
StandardUnitDictionary.dekameter = u'dekameter'   # originally LengthUnitType.dekameter
StandardUnitDictionary.hectometer = u'hectometer' # originally LengthUnitType.hectometer
StandardUnitDictionary.kilometer = u'kilometer'   # originally LengthUnitType.kilometer
StandardUnitDictionary.megameter = u'megameter'   # originally LengthUnitType.megameter
StandardUnitDictionary.angstrom = u'angstrom'     # originally LengthUnitType.angstrom
StandardUnitDictionary.inch = u'inch'             # originally LengthUnitType.inch
StandardUnitDictionary.Foot_US = u'Foot_US'       # originally LengthUnitType.Foot_US
StandardUnitDictionary.foot = u'foot'             # originally LengthUnitType.foot
StandardUnitDictionary.Foot_Gold_Coast = u'Foot_Gold_Coast'# originally LengthUnitType.Foot_Gold_Coast
StandardUnitDictionary.fathom = u'fathom'         # originally LengthUnitType.fathom
StandardUnitDictionary.nauticalMile = u'nauticalMile'# originally LengthUnitType.nauticalMile
StandardUnitDictionary.yard = u'yard'             # originally LengthUnitType.yard
StandardUnitDictionary.Yard_Indian = u'Yard_Indian'# originally LengthUnitType.Yard_Indian
StandardUnitDictionary.Link_Clarke = u'Link_Clarke'# originally LengthUnitType.Link_Clarke
StandardUnitDictionary.Yard_Sears = u'Yard_Sears' # originally LengthUnitType.Yard_Sears
StandardUnitDictionary.mile = u'mile'             # originally LengthUnitType.mile
StandardUnitDictionary.kilogram = u'kilogram'     # originally MassUnitType.kilogram
StandardUnitDictionary.nanogram = u'nanogram'     # originally MassUnitType.nanogram
StandardUnitDictionary.microgram = u'microgram'   # originally MassUnitType.microgram
StandardUnitDictionary.milligram = u'milligram'   # originally MassUnitType.milligram
StandardUnitDictionary.centigram = u'centigram'   # originally MassUnitType.centigram
StandardUnitDictionary.decigram = u'decigram'     # originally MassUnitType.decigram
StandardUnitDictionary.gram = u'gram'             # originally MassUnitType.gram
StandardUnitDictionary.dekagram = u'dekagram'     # originally MassUnitType.dekagram
StandardUnitDictionary.hectogram = u'hectogram'   # originally MassUnitType.hectogram
StandardUnitDictionary.megagram = u'megagram'     # originally MassUnitType.megagram
StandardUnitDictionary.tonne = u'tonne'           # originally MassUnitType.tonne
StandardUnitDictionary.pound = u'pound'           # originally MassUnitType.pound
StandardUnitDictionary.ton = u'ton'               # originally MassUnitType.ton
StandardUnitDictionary.dimensionless = u'dimensionless'# originally otherUnitType.dimensionless
StandardUnitDictionary.second = u'second'         # originally otherUnitType.second
StandardUnitDictionary.kelvin = u'kelvin'         # originally otherUnitType.kelvin
StandardUnitDictionary.coulomb = u'coulomb'       # originally otherUnitType.coulomb
StandardUnitDictionary.ampere = u'ampere'         # originally otherUnitType.ampere
StandardUnitDictionary.mole = u'mole'             # originally otherUnitType.mole
StandardUnitDictionary.candela = u'candela'       # originally otherUnitType.candela
StandardUnitDictionary.number = u'number'         # originally otherUnitType.number
StandardUnitDictionary.radian = u'radian'         # originally otherUnitType.radian
StandardUnitDictionary.degree = u'degree'         # originally otherUnitType.degree
StandardUnitDictionary.grad = u'grad'             # originally otherUnitType.grad
StandardUnitDictionary.cubicMeter = u'cubicMeter' # originally otherUnitType.cubicMeter
StandardUnitDictionary.nominalMinute = u'nominalMinute'# originally otherUnitType.nominalMinute
StandardUnitDictionary.nominalHour = u'nominalHour'# originally otherUnitType.nominalHour
StandardUnitDictionary.nominalDay = u'nominalDay' # originally otherUnitType.nominalDay
StandardUnitDictionary.nominalWeek = u'nominalWeek'# originally otherUnitType.nominalWeek
StandardUnitDictionary.nominalYear = u'nominalYear'# originally otherUnitType.nominalYear
StandardUnitDictionary.nominalLeapYear = u'nominalLeapYear'# originally otherUnitType.nominalLeapYear
StandardUnitDictionary.celsius = u'celsius'       # originally otherUnitType.celsius
StandardUnitDictionary.fahrenheit = u'fahrenheit' # originally otherUnitType.fahrenheit
StandardUnitDictionary.nanosecond = u'nanosecond' # originally otherUnitType.nanosecond
StandardUnitDictionary.microsecond = u'microsecond'# originally otherUnitType.microsecond
StandardUnitDictionary.millisecond = u'millisecond'# originally otherUnitType.millisecond
StandardUnitDictionary.centisecond = u'centisecond'# originally otherUnitType.centisecond
StandardUnitDictionary.decisecond = u'decisecond' # originally otherUnitType.decisecond
StandardUnitDictionary.dekasecond = u'dekasecond' # originally otherUnitType.dekasecond
StandardUnitDictionary.hectosecond = u'hectosecond'# originally otherUnitType.hectosecond
StandardUnitDictionary.kilosecond = u'kilosecond' # originally otherUnitType.kilosecond
StandardUnitDictionary.megasecond = u'megasecond' # originally otherUnitType.megasecond
StandardUnitDictionary.minute = u'minute'         # originally otherUnitType.minute
StandardUnitDictionary.hour = u'hour'             # originally otherUnitType.hour
StandardUnitDictionary.kiloliter = u'kiloliter'   # originally otherUnitType.kiloliter
StandardUnitDictionary.microliter = u'microliter' # originally otherUnitType.microliter
StandardUnitDictionary.milliliter = u'milliliter' # originally otherUnitType.milliliter
StandardUnitDictionary.liter = u'liter'           # originally otherUnitType.liter
StandardUnitDictionary.gallon = u'gallon'         # originally otherUnitType.gallon
StandardUnitDictionary.quart = u'quart'           # originally otherUnitType.quart
StandardUnitDictionary.bushel = u'bushel'         # originally otherUnitType.bushel
StandardUnitDictionary.cubicInch = u'cubicInch'   # originally otherUnitType.cubicInch
StandardUnitDictionary.pint = u'pint'             # originally otherUnitType.pint
StandardUnitDictionary.megahertz = u'megahertz'   # originally otherUnitType.megahertz
StandardUnitDictionary.kilohertz = u'kilohertz'   # originally otherUnitType.kilohertz
StandardUnitDictionary.hertz = u'hertz'           # originally otherUnitType.hertz
StandardUnitDictionary.millihertz = u'millihertz' # originally otherUnitType.millihertz
StandardUnitDictionary.newton = u'newton'         # originally otherUnitType.newton
StandardUnitDictionary.joule = u'joule'           # originally otherUnitType.joule
StandardUnitDictionary.calorie = u'calorie'       # originally otherUnitType.calorie
StandardUnitDictionary.britishThermalUnit = u'britishThermalUnit'# originally otherUnitType.britishThermalUnit
StandardUnitDictionary.footPound = u'footPound'   # originally otherUnitType.footPound
StandardUnitDictionary.lumen = u'lumen'           # originally otherUnitType.lumen
StandardUnitDictionary.lux = u'lux'               # originally otherUnitType.lux
StandardUnitDictionary.becquerel = u'becquerel'   # originally otherUnitType.becquerel
StandardUnitDictionary.gray = u'gray'             # originally otherUnitType.gray
StandardUnitDictionary.sievert = u'sievert'       # originally otherUnitType.sievert
StandardUnitDictionary.katal = u'katal'           # originally otherUnitType.katal
StandardUnitDictionary.henry = u'henry'           # originally otherUnitType.henry
StandardUnitDictionary.megawatt = u'megawatt'     # originally otherUnitType.megawatt
StandardUnitDictionary.kilowatt = u'kilowatt'     # originally otherUnitType.kilowatt
StandardUnitDictionary.watt = u'watt'             # originally otherUnitType.watt
StandardUnitDictionary.milliwatt = u'milliwatt'   # originally otherUnitType.milliwatt
StandardUnitDictionary.megavolt = u'megavolt'     # originally otherUnitType.megavolt
StandardUnitDictionary.kilovolt = u'kilovolt'     # originally otherUnitType.kilovolt
StandardUnitDictionary.volt = u'volt'             # originally otherUnitType.volt
StandardUnitDictionary.millivolt = u'millivolt'   # originally otherUnitType.millivolt
StandardUnitDictionary.farad = u'farad'           # originally otherUnitType.farad
StandardUnitDictionary.ohm = u'ohm'               # originally otherUnitType.ohm
StandardUnitDictionary.ohmMeter = u'ohmMeter'     # originally otherUnitType.ohmMeter
StandardUnitDictionary.siemen = u'siemen'         # originally otherUnitType.siemen
StandardUnitDictionary.weber = u'weber'           # originally otherUnitType.weber
StandardUnitDictionary.tesla = u'tesla'           # originally otherUnitType.tesla
StandardUnitDictionary.pascal = u'pascal'         # originally otherUnitType.pascal
StandardUnitDictionary.megapascal = u'megapascal' # originally otherUnitType.megapascal
StandardUnitDictionary.kilopascal = u'kilopascal' # originally otherUnitType.kilopascal
StandardUnitDictionary.atmosphere = u'atmosphere' # originally otherUnitType.atmosphere
StandardUnitDictionary.bar = u'bar'               # originally otherUnitType.bar
StandardUnitDictionary.millibar = u'millibar'     # originally otherUnitType.millibar
StandardUnitDictionary.kilogramsPerSquareMeter = u'kilogramsPerSquareMeter'# originally otherUnitType.kilogramsPerSquareMeter
StandardUnitDictionary.gramsPerSquareMeter = u'gramsPerSquareMeter'# originally otherUnitType.gramsPerSquareMeter
StandardUnitDictionary.milligramsPerSquareMeter = u'milligramsPerSquareMeter'# originally otherUnitType.milligramsPerSquareMeter
StandardUnitDictionary.kilogramsPerHectare = u'kilogramsPerHectare'# originally otherUnitType.kilogramsPerHectare
StandardUnitDictionary.tonnePerHectare = u'tonnePerHectare'# originally otherUnitType.tonnePerHectare
StandardUnitDictionary.poundsPerSquareInch = u'poundsPerSquareInch'# originally otherUnitType.poundsPerSquareInch
StandardUnitDictionary.kilogramPerCubicMeter = u'kilogramPerCubicMeter'# originally otherUnitType.kilogramPerCubicMeter
StandardUnitDictionary.milliGramsPerMilliLiter = u'milliGramsPerMilliLiter'# originally otherUnitType.milliGramsPerMilliLiter
StandardUnitDictionary.gramsPerLiter = u'gramsPerLiter'# originally otherUnitType.gramsPerLiter
StandardUnitDictionary.milligramsPerCubicMeter = u'milligramsPerCubicMeter'# originally otherUnitType.milligramsPerCubicMeter
StandardUnitDictionary.microgramsPerLiter = u'microgramsPerLiter'# originally otherUnitType.microgramsPerLiter
StandardUnitDictionary.milligramsPerLiter = u'milligramsPerLiter'# originally otherUnitType.milligramsPerLiter
StandardUnitDictionary.gramsPerCubicCentimeter = u'gramsPerCubicCentimeter'# originally otherUnitType.gramsPerCubicCentimeter
StandardUnitDictionary.gramsPerMilliliter = u'gramsPerMilliliter'# originally otherUnitType.gramsPerMilliliter
StandardUnitDictionary.gramsPerLiterPerDay = u'gramsPerLiterPerDay'# originally otherUnitType.gramsPerLiterPerDay
StandardUnitDictionary.litersPerSecond = u'litersPerSecond'# originally otherUnitType.litersPerSecond
StandardUnitDictionary.cubicMetersPerSecond = u'cubicMetersPerSecond'# originally otherUnitType.cubicMetersPerSecond
StandardUnitDictionary.cubicFeetPerSecond = u'cubicFeetPerSecond'# originally otherUnitType.cubicFeetPerSecond
StandardUnitDictionary.squareMeter = u'squareMeter'# originally otherUnitType.squareMeter
StandardUnitDictionary.are = u'are'               # originally otherUnitType.are
StandardUnitDictionary.hectare = u'hectare'       # originally otherUnitType.hectare
StandardUnitDictionary.squareKilometers = u'squareKilometers'# originally otherUnitType.squareKilometers
StandardUnitDictionary.squareMillimeters = u'squareMillimeters'# originally otherUnitType.squareMillimeters
StandardUnitDictionary.squareCentimeters = u'squareCentimeters'# originally otherUnitType.squareCentimeters
StandardUnitDictionary.acre = u'acre'             # originally otherUnitType.acre
StandardUnitDictionary.squareFoot = u'squareFoot' # originally otherUnitType.squareFoot
StandardUnitDictionary.squareYard = u'squareYard' # originally otherUnitType.squareYard
StandardUnitDictionary.squareMile = u'squareMile' # originally otherUnitType.squareMile
StandardUnitDictionary.litersPerSquareMeter = u'litersPerSquareMeter'# originally otherUnitType.litersPerSquareMeter
StandardUnitDictionary.bushelsPerAcre = u'bushelsPerAcre'# originally otherUnitType.bushelsPerAcre
StandardUnitDictionary.litersPerHectare = u'litersPerHectare'# originally otherUnitType.litersPerHectare
StandardUnitDictionary.squareMeterPerKilogram = u'squareMeterPerKilogram'# originally otherUnitType.squareMeterPerKilogram
StandardUnitDictionary.metersPerSecond = u'metersPerSecond'# originally otherUnitType.metersPerSecond
StandardUnitDictionary.metersPerDay = u'metersPerDay'# originally otherUnitType.metersPerDay
StandardUnitDictionary.feetPerDay = u'feetPerDay' # originally otherUnitType.feetPerDay
StandardUnitDictionary.feetPerSecond = u'feetPerSecond'# originally otherUnitType.feetPerSecond
StandardUnitDictionary.feetPerHour = u'feetPerHour'# originally otherUnitType.feetPerHour
StandardUnitDictionary.yardsPerSecond = u'yardsPerSecond'# originally otherUnitType.yardsPerSecond
StandardUnitDictionary.milesPerHour = u'milesPerHour'# originally otherUnitType.milesPerHour
StandardUnitDictionary.milesPerSecond = u'milesPerSecond'# originally otherUnitType.milesPerSecond
StandardUnitDictionary.milesPerMinute = u'milesPerMinute'# originally otherUnitType.milesPerMinute
StandardUnitDictionary.centimetersPerSecond = u'centimetersPerSecond'# originally otherUnitType.centimetersPerSecond
StandardUnitDictionary.millimetersPerSecond = u'millimetersPerSecond'# originally otherUnitType.millimetersPerSecond
StandardUnitDictionary.centimeterPerYear = u'centimeterPerYear'# originally otherUnitType.centimeterPerYear
StandardUnitDictionary.knots = u'knots'           # originally otherUnitType.knots
StandardUnitDictionary.kilometersPerHour = u'kilometersPerHour'# originally otherUnitType.kilometersPerHour
StandardUnitDictionary.metersPerSecondSquared = u'metersPerSecondSquared'# originally otherUnitType.metersPerSecondSquared
StandardUnitDictionary.waveNumber = u'waveNumber' # originally otherUnitType.waveNumber
StandardUnitDictionary.cubicMeterPerKilogram = u'cubicMeterPerKilogram'# originally otherUnitType.cubicMeterPerKilogram
StandardUnitDictionary.cubicMicrometersPerGram = u'cubicMicrometersPerGram'# originally otherUnitType.cubicMicrometersPerGram
StandardUnitDictionary.amperePerSquareMeter = u'amperePerSquareMeter'# originally otherUnitType.amperePerSquareMeter
StandardUnitDictionary.amperePerMeter = u'amperePerMeter'# originally otherUnitType.amperePerMeter
StandardUnitDictionary.molePerCubicMeter = u'molePerCubicMeter'# originally otherUnitType.molePerCubicMeter
StandardUnitDictionary.molarity = u'molarity'     # originally otherUnitType.molarity
StandardUnitDictionary.molality = u'molality'     # originally otherUnitType.molality
StandardUnitDictionary.candelaPerSquareMeter = u'candelaPerSquareMeter'# originally otherUnitType.candelaPerSquareMeter
StandardUnitDictionary.metersSquaredPerSecond = u'metersSquaredPerSecond'# originally otherUnitType.metersSquaredPerSecond
StandardUnitDictionary.metersSquaredPerDay = u'metersSquaredPerDay'# originally otherUnitType.metersSquaredPerDay
StandardUnitDictionary.feetSquaredPerDay = u'feetSquaredPerDay'# originally otherUnitType.feetSquaredPerDay
StandardUnitDictionary.kilogramsPerMeterSquaredPerSecond = u'kilogramsPerMeterSquaredPerSecond'# originally otherUnitType.kilogramsPerMeterSquaredPerSecond
StandardUnitDictionary.gramsPerCentimeterSquaredPerSecond = u'gramsPerCentimeterSquaredPerSecond'# originally otherUnitType.gramsPerCentimeterSquaredPerSecond
StandardUnitDictionary.gramsPerMeterSquaredPerYear = u'gramsPerMeterSquaredPerYear'# originally otherUnitType.gramsPerMeterSquaredPerYear
StandardUnitDictionary.gramsPerHectarePerDay = u'gramsPerHectarePerDay'# originally otherUnitType.gramsPerHectarePerDay
StandardUnitDictionary.kilogramsPerHectarePerYear = u'kilogramsPerHectarePerYear'# originally otherUnitType.kilogramsPerHectarePerYear
StandardUnitDictionary.kilogramsPerMeterSquaredPerYear = u'kilogramsPerMeterSquaredPerYear'# originally otherUnitType.kilogramsPerMeterSquaredPerYear
StandardUnitDictionary.molesPerKilogram = u'molesPerKilogram'# originally otherUnitType.molesPerKilogram
StandardUnitDictionary.molesPerGram = u'molesPerGram'# originally otherUnitType.molesPerGram
StandardUnitDictionary.millimolesPerGram = u'millimolesPerGram'# originally otherUnitType.millimolesPerGram
StandardUnitDictionary.molesPerKilogramPerSecond = u'molesPerKilogramPerSecond'# originally otherUnitType.molesPerKilogramPerSecond
StandardUnitDictionary.nanomolesPerGramPerSecond = u'nanomolesPerGramPerSecond'# originally otherUnitType.nanomolesPerGramPerSecond
StandardUnitDictionary.kilogramsPerSecond = u'kilogramsPerSecond'# originally otherUnitType.kilogramsPerSecond
StandardUnitDictionary.tonnesPerYear = u'tonnesPerYear'# originally otherUnitType.tonnesPerYear
StandardUnitDictionary.gramsPerYear = u'gramsPerYear'# originally otherUnitType.gramsPerYear
StandardUnitDictionary.numberPerMeterSquared = u'numberPerMeterSquared'# originally otherUnitType.numberPerMeterSquared
StandardUnitDictionary.numberPerKilometerSquared = u'numberPerKilometerSquared'# originally otherUnitType.numberPerKilometerSquared
StandardUnitDictionary.numberPerMeterCubed = u'numberPerMeterCubed'# originally otherUnitType.numberPerMeterCubed
StandardUnitDictionary.numberPerLiter = u'numberPerLiter'# originally otherUnitType.numberPerLiter
StandardUnitDictionary.numberPerMilliliter = u'numberPerMilliliter'# originally otherUnitType.numberPerMilliliter
StandardUnitDictionary.metersPerGram = u'metersPerGram'# originally otherUnitType.metersPerGram
StandardUnitDictionary.numberPerGram = u'numberPerGram'# originally otherUnitType.numberPerGram
StandardUnitDictionary.gramsPerGram = u'gramsPerGram'# originally otherUnitType.gramsPerGram
StandardUnitDictionary.microgramsPerGram = u'microgramsPerGram'# originally otherUnitType.microgramsPerGram
StandardUnitDictionary.cubicCentimetersPerCubicCentimeters = u'cubicCentimetersPerCubicCentimeters'# originally otherUnitType.cubicCentimetersPerCubicCentimeters
StandardUnitDictionary._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'StandardUnitDictionary', StandardUnitDictionary)
