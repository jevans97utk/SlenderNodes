# ./generated/_nsgroup.py
# -*- coding: utf-8 -*-
# PyXB bindings for NGM:16d1a475437443b1596a94d74eaf02b5f26b68b8
# Generated 2014-03-16 22:56:49.637589 by PyXB version 1.2.3
# Group contents:
# Namespace eml://ecoinformatics.org/access-2.1.0 [xmlns:acc]
# Namespace eml://ecoinformatics.org/coverage-2.1.0 [xmlns:cov]
# Namespace eml://ecoinformatics.org/literature-2.1.0 [xmlns:cit]
# Namespace eml://ecoinformatics.org/party-2.1.0 [xmlns:rp]
# Namespace eml://ecoinformatics.org/project-2.1.0 [xmlns:proj]
# Namespace eml://ecoinformatics.org/resource-2.1.0 [xmlns:res]


import pyxb
import pyxb.binding
import pyxb.utils.utility

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:8bdde10a-ad90-11e3-bf48-000c294230b4')

# Import bindings for schemas in group
import pyxb.binding.datatypes
import _unit as _ImportedBinding__unit
import _txt as _ImportedBinding__txt

# NOTE: All namespace declarations are reserved within the binding
_Namespace_acc = pyxb.namespace.NamespaceForURI(u'eml://ecoinformatics.org/access-2.1.0', create_if_missing=True)
_Namespace_acc.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_cov = pyxb.namespace.NamespaceForURI(u'eml://ecoinformatics.org/coverage-2.1.0', create_if_missing=True)
_Namespace_cov.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_rp = pyxb.namespace.NamespaceForURI(u'eml://ecoinformatics.org/party-2.1.0', create_if_missing=True)
_Namespace_rp.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_proj = pyxb.namespace.NamespaceForURI(u'eml://ecoinformatics.org/project-2.1.0', create_if_missing=True)
_Namespace_proj.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_res = pyxb.namespace.NamespaceForURI(u'eml://ecoinformatics.org/resource-2.1.0', create_if_missing=True)
_Namespace_res.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_cit = pyxb.namespace.NamespaceForURI(u'eml://ecoinformatics.org/literature-2.1.0', create_if_missing=True)
_Namespace_cit.configureCategories(['typeBinding', 'elementBinding'])

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 275, 6)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.allowFirst = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'allowFirst', tag=u'allowFirst')
STD_ANON.denyFirst = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'denyFirst', tag=u'denyFirst')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 361, 12)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.read = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'read', tag=u'read')
STD_ANON_.write = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'write', tag=u'write')
STD_ANON_.changePermission = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'changePermission', tag=u'changePermission')
STD_ANON_.all = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'all', tag=u'all')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 369, 12)
    _Documentation = None
STD_ANON_2._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 600, 16)
    _Documentation = None
STD_ANON_3._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_3, value=pyxb.binding.datatypes.decimal(180.0))
STD_ANON_3._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_3, value=pyxb.binding.datatypes.decimal(-180.0))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_maxInclusive,
   STD_ANON_3._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 632, 16)
    _Documentation = None
STD_ANON_4._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_4, value=pyxb.binding.datatypes.decimal(180.0))
STD_ANON_4._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_4, value=pyxb.binding.datatypes.decimal(-180.0))
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_maxInclusive,
   STD_ANON_4._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 660, 16)
    _Documentation = None
STD_ANON_5._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_5, value=pyxb.binding.datatypes.decimal(90.0))
STD_ANON_5._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_5, value=pyxb.binding.datatypes.decimal(-90.0))
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_maxInclusive,
   STD_ANON_5._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 688, 16)
    _Documentation = None
STD_ANON_6._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_6, value=pyxb.binding.datatypes.decimal(90.0))
STD_ANON_6._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_6, value=pyxb.binding.datatypes.decimal(-90.0))
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_maxInclusive,
   STD_ANON_6._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 935, 8)
    _Documentation = None
STD_ANON_7._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_7, value=pyxb.binding.datatypes.decimal(90.0))
STD_ANON_7._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_7, value=pyxb.binding.datatypes.decimal(-90.0))
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_maxInclusive,
   STD_ANON_7._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 960, 8)
    _Documentation = None
STD_ANON_8._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_8, value=pyxb.binding.datatypes.decimal(180.0))
STD_ANON_8._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_8, value=pyxb.binding.datatypes.decimal(-180.0))
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_maxInclusive,
   STD_ANON_8._CF_minInclusive)

# Atomic simple type: {eml://ecoinformatics.org/coverage-2.1.0}GRingType
class GRingType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cov, u'GRingType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 969, 2)
    _Documentation = ''
GRingType._InitializeFacetMap()
_Namespace_cov.addCategoryObject('typeBinding', u'GRingType', GRingType)

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 542, 6)
    _Documentation = None
STD_ANON_9._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_9, enum_prefix=None)
STD_ANON_9.contentProvider = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'contentProvider', tag=u'contentProvider')
STD_ANON_9.custodianSteward = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'custodianSteward', tag=u'custodianSteward')
STD_ANON_9.owner = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'owner', tag=u'owner')
STD_ANON_9.user = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'user', tag=u'user')
STD_ANON_9.distributor = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'distributor', tag=u'distributor')
STD_ANON_9.metadataProvider = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'metadataProvider', tag=u'metadataProvider')
STD_ANON_9.originator = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'originator', tag=u'originator')
STD_ANON_9.pointOfContact = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'pointOfContact', tag=u'pointOfContact')
STD_ANON_9.principalInvestigator = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'principalInvestigator', tag=u'principalInvestigator')
STD_ANON_9.processor = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'processor', tag=u'processor')
STD_ANON_9.publisher = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'publisher', tag=u'publisher')
STD_ANON_9.author = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'author', tag=u'author')
STD_ANON_9.editor = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'editor', tag=u'editor')
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 559, 6)
    _Documentation = None
STD_ANON_10._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 441, 6)
    _Documentation = None
STD_ANON_11._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_11, enum_prefix=None)
STD_ANON_11.climate = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'climate', tag=u'climate')
STD_ANON_11.hydrology = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'hydrology', tag=u'hydrology')
STD_ANON_11.soils = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'soils', tag=u'soils')
STD_ANON_11.geology = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'geology', tag=u'geology')
STD_ANON_11.disturbance = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'disturbance', tag=u'disturbance')
STD_ANON_11.bailey = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'bailey', tag=u'bailey')
STD_ANON_11.biome = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'biome', tag=u'biome')
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 452, 6)
    _Documentation = None
STD_ANON_12._InitializeFacetMap()

# Atomic simple type: {eml://ecoinformatics.org/resource-2.1.0}KeyTypeCode
class KeyTypeCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_res, u'KeyTypeCode')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 440, 2)
    _Documentation = ''
KeyTypeCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=KeyTypeCode, enum_prefix=None)
KeyTypeCode.place = KeyTypeCode._CF_enumeration.addEnumeration(unicode_value=u'place', tag=u'place')
KeyTypeCode.stratum = KeyTypeCode._CF_enumeration.addEnumeration(unicode_value=u'stratum', tag=u'stratum')
KeyTypeCode.temporal = KeyTypeCode._CF_enumeration.addEnumeration(unicode_value=u'temporal', tag=u'temporal')
KeyTypeCode.theme = KeyTypeCode._CF_enumeration.addEnumeration(unicode_value=u'theme', tag=u'theme')
KeyTypeCode.taxonomic = KeyTypeCode._CF_enumeration.addEnumeration(unicode_value=u'taxonomic', tag=u'taxonomic')
KeyTypeCode._InitializeFacetMap(KeyTypeCode._CF_enumeration)
_Namespace_res.addCategoryObject('typeBinding', u'KeyTypeCode', KeyTypeCode)

# Union simple type: {eml://ecoinformatics.org/resource-2.1.0}yearDate
# superclasses pyxb.binding.datatypes.anySimpleType
class yearDate (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.gYear, pyxb.binding.datatypes.date."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_res, u'yearDate')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 505, 2)
    _Documentation = ''

    _MemberTypes = ( pyxb.binding.datatypes.gYear, pyxb.binding.datatypes.date, )
yearDate._InitializeFacetMap()
_Namespace_res.addCategoryObject('typeBinding', u'yearDate', yearDate)

# List simple type: {eml://ecoinformatics.org/resource-2.1.0}IDType
# superclasses pyxb.binding.datatypes.anySimpleType
class IDType (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.string."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_res, u'IDType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 517, 2)
    _Documentation = ''

    _ItemType = pyxb.binding.datatypes.string
IDType._InitializeFacetMap()
_Namespace_res.addCategoryObject('typeBinding', u'IDType', IDType)

# List simple type: {eml://ecoinformatics.org/resource-2.1.0}SystemType
# superclasses pyxb.binding.datatypes.anySimpleType
class SystemType (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.string."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_res, u'SystemType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 536, 2)
    _Documentation = ''

    _ItemType = pyxb.binding.datatypes.string
SystemType._InitializeFacetMap()
_Namespace_res.addCategoryObject('typeBinding', u'SystemType', SystemType)

# Atomic simple type: {eml://ecoinformatics.org/resource-2.1.0}ScopeType
class ScopeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_res, u'ScopeType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 556, 2)
    _Documentation = ''
ScopeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ScopeType, enum_prefix=None)
ScopeType.system = ScopeType._CF_enumeration.addEnumeration(unicode_value=u'system', tag=u'system')
ScopeType.document = ScopeType._CF_enumeration.addEnumeration(unicode_value=u'document', tag=u'document')
ScopeType._InitializeFacetMap(ScopeType._CF_enumeration)
_Namespace_res.addCategoryObject('typeBinding', u'ScopeType', ScopeType)

# Atomic simple type: {eml://ecoinformatics.org/resource-2.1.0}FunctionType
class FunctionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_res, u'FunctionType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 576, 2)
    _Documentation = None
FunctionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FunctionType, enum_prefix=None)
FunctionType.download = FunctionType._CF_enumeration.addEnumeration(unicode_value=u'download', tag=u'download')
FunctionType.information = FunctionType._CF_enumeration.addEnumeration(unicode_value=u'information', tag=u'information')
FunctionType._InitializeFacetMap(FunctionType._CF_enumeration)
_Namespace_res.addCategoryObject('typeBinding', u'FunctionType', FunctionType)

# Atomic simple type: {eml://ecoinformatics.org/resource-2.1.0}NonEmptyStringType
class NonEmptyStringType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_res, u'NonEmptyStringType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1161, 2)
    _Documentation = ''
NonEmptyStringType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
NonEmptyStringType._CF_pattern = pyxb.binding.facets.CF_pattern()
NonEmptyStringType._CF_pattern.addPattern(pattern=u'[\\s]*[\\S][\\s\\S]*')
NonEmptyStringType._InitializeFacetMap(NonEmptyStringType._CF_minLength,
   NonEmptyStringType._CF_pattern)
_Namespace_res.addCategoryObject('typeBinding', u'NonEmptyStringType', NonEmptyStringType)

# Union simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_13 (pyxb.binding.basis.STD_union):

    """Simple type that is a union of STD_ANON_, STD_ANON_2."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 359, 8)
    _Documentation = None

    _MemberTypes = ( STD_ANON_, STD_ANON_2, )
STD_ANON_13._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_13._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_13)
STD_ANON_13.read = u'read'                        # originally STD_ANON_.read
STD_ANON_13.write = u'write'                      # originally STD_ANON_.write
STD_ANON_13.changePermission = u'changePermission'# originally STD_ANON_.changePermission
STD_ANON_13.all = u'all'                          # originally STD_ANON_.all
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_pattern,
   STD_ANON_13._CF_enumeration)

# Union simple type: {eml://ecoinformatics.org/party-2.1.0}RoleType
# superclasses pyxb.binding.datatypes.anySimpleType
class RoleType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of STD_ANON_9, STD_ANON_10."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_rp, u'RoleType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 524, 2)
    _Documentation = ''

    _MemberTypes = ( STD_ANON_9, STD_ANON_10, )
RoleType.contentProvider = u'contentProvider'     # originally STD_ANON_9.contentProvider
RoleType.custodianSteward = u'custodianSteward'   # originally STD_ANON_9.custodianSteward
RoleType.owner = u'owner'                         # originally STD_ANON_9.owner
RoleType.user = u'user'                           # originally STD_ANON_9.user
RoleType.distributor = u'distributor'             # originally STD_ANON_9.distributor
RoleType.metadataProvider = u'metadataProvider'   # originally STD_ANON_9.metadataProvider
RoleType.originator = u'originator'               # originally STD_ANON_9.originator
RoleType.pointOfContact = u'pointOfContact'       # originally STD_ANON_9.pointOfContact
RoleType.principalInvestigator = u'principalInvestigator'# originally STD_ANON_9.principalInvestigator
RoleType.processor = u'processor'                 # originally STD_ANON_9.processor
RoleType.publisher = u'publisher'                 # originally STD_ANON_9.publisher
RoleType.author = u'author'                       # originally STD_ANON_9.author
RoleType.editor = u'editor'                       # originally STD_ANON_9.editor
RoleType._InitializeFacetMap()
_Namespace_rp.addCategoryObject('typeBinding', u'RoleType', RoleType)

# Union simple type: {eml://ecoinformatics.org/project-2.1.0}DescriptorType
# superclasses pyxb.binding.datatypes.anySimpleType
class DescriptorType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of STD_ANON_11, STD_ANON_12."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_proj, u'DescriptorType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 421, 2)
    _Documentation = ''

    _MemberTypes = ( STD_ANON_11, STD_ANON_12, )
DescriptorType.climate = u'climate'               # originally STD_ANON_11.climate
DescriptorType.hydrology = u'hydrology'           # originally STD_ANON_11.hydrology
DescriptorType.soils = u'soils'                   # originally STD_ANON_11.soils
DescriptorType.geology = u'geology'               # originally STD_ANON_11.geology
DescriptorType.disturbance = u'disturbance'       # originally STD_ANON_11.disturbance
DescriptorType.bailey = u'bailey'                 # originally STD_ANON_11.bailey
DescriptorType.biome = u'biome'                   # originally STD_ANON_11.biome
DescriptorType._InitializeFacetMap()
_Namespace_proj.addCategoryObject('typeBinding', u'DescriptorType', DescriptorType)

# Complex type {eml://ecoinformatics.org/access-2.1.0}AccessRule with content type ELEMENT_ONLY
class AccessRule (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_acc, u'AccessRule')
    _XSDLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 302, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element principal uses Python identifier principal
    __principal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'principal'), 'principal', '__emlecoinformatics_orgaccess_2_1_0_AccessRule_principal', True, pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 316, 6), )

    
    principal = property(__principal.value, __principal.set, None, u'')

    
    # Element permission uses Python identifier permission
    __permission = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'permission'), 'permission', '__emlecoinformatics_orgaccess_2_1_0_AccessRule_permission', True, pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 334, 6), )

    
    permission = property(__permission.value, __permission.set, None, u'')

    _ElementMap.update({
        __principal.name() : __principal,
        __permission.name() : __permission
    })
    _AttributeMap.update({
        
    })
_Namespace_acc.addCategoryObject('typeBinding', u'AccessRule', AccessRule)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 243, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element beginDate uses Python identifier beginDate
    __beginDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'beginDate'), 'beginDate', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_beginDate', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 245, 14), )

    
    beginDate = property(__beginDate.value, __beginDate.set, None, u'')

    
    # Element endDate uses Python identifier endDate
    __endDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'endDate'), 'endDate', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_endDate', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 260, 14), )

    
    endDate = property(__endDate.value, __endDate.set, None, u'')

    _ElementMap.update({
        __beginDate.name() : __beginDate,
        __endDate.name() : __endDate
    })
    _AttributeMap.update({
        
    })



# Complex type {eml://ecoinformatics.org/coverage-2.1.0}SingleDateTimeType with content type ELEMENT_ONLY
class SingleDateTimeType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cov, u'SingleDateTimeType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 283, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element calendarDate uses Python identifier calendarDate
    __calendarDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'calendarDate'), 'calendarDate', '__emlecoinformatics_orgcoverage_2_1_0_SingleDateTimeType_calendarDate', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 298, 8), )

    
    calendarDate = property(__calendarDate.value, __calendarDate.set, None, u'')

    
    # Element time uses Python identifier time
    __time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'time'), 'time', '__emlecoinformatics_orgcoverage_2_1_0_SingleDateTimeType_time', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 318, 8), )

    
    time = property(__time.value, __time.set, None, u'')

    
    # Element alternativeTimeScale uses Python identifier alternativeTimeScale
    __alternativeTimeScale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'alternativeTimeScale'), 'alternativeTimeScale', '__emlecoinformatics_orgcoverage_2_1_0_SingleDateTimeType_alternativeTimeScale', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 348, 6), )

    
    alternativeTimeScale = property(__alternativeTimeScale.value, __alternativeTimeScale.set, None, u'')

    _ElementMap.update({
        __calendarDate.name() : __calendarDate,
        __time.name() : __time,
        __alternativeTimeScale.name() : __alternativeTimeScale
    })
    _AttributeMap.update({
        
    })
_Namespace_cov.addCategoryObject('typeBinding', u'SingleDateTimeType', SingleDateTimeType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 379, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element timeScaleName uses Python identifier timeScaleName
    __timeScaleName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'timeScaleName'), 'timeScaleName', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON__timeScaleName', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 381, 12), )

    
    timeScaleName = property(__timeScaleName.value, __timeScaleName.set, None, u'')

    
    # Element timeScaleAgeEstimate uses Python identifier timeScaleAgeEstimate
    __timeScaleAgeEstimate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'timeScaleAgeEstimate'), 'timeScaleAgeEstimate', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON__timeScaleAgeEstimate', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 398, 12), )

    
    timeScaleAgeEstimate = property(__timeScaleAgeEstimate.value, __timeScaleAgeEstimate.set, None, u'')

    
    # Element timeScaleAgeUncertainty uses Python identifier timeScaleAgeUncertainty
    __timeScaleAgeUncertainty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'timeScaleAgeUncertainty'), 'timeScaleAgeUncertainty', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON__timeScaleAgeUncertainty', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 423, 12), )

    
    timeScaleAgeUncertainty = property(__timeScaleAgeUncertainty.value, __timeScaleAgeUncertainty.set, None, u'')

    
    # Element timeScaleAgeExplanation uses Python identifier timeScaleAgeExplanation
    __timeScaleAgeExplanation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'timeScaleAgeExplanation'), 'timeScaleAgeExplanation', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON__timeScaleAgeExplanation', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 437, 12), )

    
    timeScaleAgeExplanation = property(__timeScaleAgeExplanation.value, __timeScaleAgeExplanation.set, None, u'')

    
    # Element timeScaleCitation uses Python identifier timeScaleCitation
    __timeScaleCitation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'timeScaleCitation'), 'timeScaleCitation', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON__timeScaleCitation', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 450, 12), )

    
    timeScaleCitation = property(__timeScaleCitation.value, __timeScaleCitation.set, None, u'')

    _ElementMap.update({
        __timeScaleName.name() : __timeScaleName,
        __timeScaleAgeEstimate.name() : __timeScaleAgeEstimate,
        __timeScaleAgeUncertainty.name() : __timeScaleAgeUncertainty,
        __timeScaleAgeExplanation.name() : __timeScaleAgeExplanation,
        __timeScaleCitation.name() : __timeScaleCitation
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 573, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element westBoundingCoordinate uses Python identifier westBoundingCoordinate
    __westBoundingCoordinate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'westBoundingCoordinate'), 'westBoundingCoordinate', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_2_westBoundingCoordinate', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 575, 14), )

    
    westBoundingCoordinate = property(__westBoundingCoordinate.value, __westBoundingCoordinate.set, None, u'')

    
    # Element eastBoundingCoordinate uses Python identifier eastBoundingCoordinate
    __eastBoundingCoordinate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'eastBoundingCoordinate'), 'eastBoundingCoordinate', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_2_eastBoundingCoordinate', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 607, 14), )

    
    eastBoundingCoordinate = property(__eastBoundingCoordinate.value, __eastBoundingCoordinate.set, None, u'')

    
    # Element northBoundingCoordinate uses Python identifier northBoundingCoordinate
    __northBoundingCoordinate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'northBoundingCoordinate'), 'northBoundingCoordinate', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_2_northBoundingCoordinate', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 639, 14), )

    
    northBoundingCoordinate = property(__northBoundingCoordinate.value, __northBoundingCoordinate.set, None, u'')

    
    # Element southBoundingCoordinate uses Python identifier southBoundingCoordinate
    __southBoundingCoordinate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'southBoundingCoordinate'), 'southBoundingCoordinate', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_2_southBoundingCoordinate', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 667, 14), )

    
    southBoundingCoordinate = property(__southBoundingCoordinate.value, __southBoundingCoordinate.set, None, u'')

    
    # Element boundingAltitudes uses Python identifier boundingAltitudes
    __boundingAltitudes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'boundingAltitudes'), 'boundingAltitudes', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_2_boundingAltitudes', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 695, 14), )

    
    boundingAltitudes = property(__boundingAltitudes.value, __boundingAltitudes.set, None, u'')

    _ElementMap.update({
        __westBoundingCoordinate.name() : __westBoundingCoordinate,
        __eastBoundingCoordinate.name() : __eastBoundingCoordinate,
        __northBoundingCoordinate.name() : __northBoundingCoordinate,
        __southBoundingCoordinate.name() : __southBoundingCoordinate,
        __boundingAltitudes.name() : __boundingAltitudes
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 711, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element altitudeMinimum uses Python identifier altitudeMinimum
    __altitudeMinimum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'altitudeMinimum'), 'altitudeMinimum', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_3_altitudeMinimum', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 713, 20), )

    
    altitudeMinimum = property(__altitudeMinimum.value, __altitudeMinimum.set, None, u'')

    
    # Element altitudeMaximum uses Python identifier altitudeMaximum
    __altitudeMaximum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'altitudeMaximum'), 'altitudeMaximum', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_3_altitudeMaximum', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 728, 20), )

    
    altitudeMaximum = property(__altitudeMaximum.value, __altitudeMaximum.set, None, u'')

    
    # Element altitudeUnits uses Python identifier altitudeUnits
    __altitudeUnits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'altitudeUnits'), 'altitudeUnits', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_3_altitudeUnits', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 743, 20), )

    
    altitudeUnits = property(__altitudeUnits.value, __altitudeUnits.set, None, u'')

    _ElementMap.update({
        __altitudeMinimum.name() : __altitudeMinimum,
        __altitudeMaximum.name() : __altitudeMaximum,
        __altitudeUnits.name() : __altitudeUnits
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 775, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element datasetGPolygonOuterGRing uses Python identifier datasetGPolygonOuterGRing
    __datasetGPolygonOuterGRing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'datasetGPolygonOuterGRing'), 'datasetGPolygonOuterGRing', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_4_datasetGPolygonOuterGRing', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 777, 14), )

    
    datasetGPolygonOuterGRing = property(__datasetGPolygonOuterGRing.value, __datasetGPolygonOuterGRing.set, None, u'')

    
    # Element datasetGPolygonExclusionGRing uses Python identifier datasetGPolygonExclusionGRing
    __datasetGPolygonExclusionGRing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'datasetGPolygonExclusionGRing'), 'datasetGPolygonExclusionGRing', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_4_datasetGPolygonExclusionGRing', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 837, 14), )

    
    datasetGPolygonExclusionGRing = property(__datasetGPolygonExclusionGRing.value, __datasetGPolygonExclusionGRing.set, None, u'')

    _ElementMap.update({
        __datasetGPolygonOuterGRing.name() : __datasetGPolygonOuterGRing,
        __datasetGPolygonExclusionGRing.name() : __datasetGPolygonExclusionGRing
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 808, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element gRingPoint uses Python identifier gRingPoint
    __gRingPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'gRingPoint'), 'gRingPoint', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_5_gRingPoint', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 811, 22), )

    
    gRingPoint = property(__gRingPoint.value, __gRingPoint.set, None, u'')

    
    # Element gRing uses Python identifier gRing
    __gRing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'gRing'), 'gRing', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_5_gRing', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 822, 20), )

    
    gRing = property(__gRing.value, __gRing.set, None, u'')

    _ElementMap.update({
        __gRingPoint.name() : __gRingPoint,
        __gRing.name() : __gRing
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 867, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element gRingPoint uses Python identifier gRingPoint
    __gRingPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'gRingPoint'), 'gRingPoint', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_6_gRingPoint', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 869, 20), )

    
    gRingPoint = property(__gRingPoint.value, __gRingPoint.set, None, u'')

    
    # Element gRing uses Python identifier gRing
    __gRing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'gRing'), 'gRing', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_6_gRing', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 881, 20), )

    
    gRing = property(__gRing.value, __gRing.set, None, u'')

    _ElementMap.update({
        __gRingPoint.name() : __gRingPoint,
        __gRing.name() : __gRing
    })
    _AttributeMap.update({
        
    })



# Complex type {eml://ecoinformatics.org/coverage-2.1.0}GRingPointType with content type ELEMENT_ONLY
class GRingPointType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cov, u'GRingPointType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 903, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element gRingLatitude uses Python identifier gRingLatitude
    __gRingLatitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'gRingLatitude'), 'gRingLatitude', '__emlecoinformatics_orgcoverage_2_1_0_GRingPointType_gRingLatitude', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 916, 6), )

    
    gRingLatitude = property(__gRingLatitude.value, __gRingLatitude.set, None, u'')

    
    # Element gRingLongitude uses Python identifier gRingLongitude
    __gRingLongitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'gRingLongitude'), 'gRingLongitude', '__emlecoinformatics_orgcoverage_2_1_0_GRingPointType_gRingLongitude', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 942, 6), )

    
    gRingLongitude = property(__gRingLongitude.value, __gRingLongitude.set, None, u'')

    _ElementMap.update({
        __gRingLatitude.name() : __gRingLatitude,
        __gRingLongitude.name() : __gRingLongitude
    })
    _AttributeMap.update({
        
    })
_Namespace_cov.addCategoryObject('typeBinding', u'GRingPointType', GRingPointType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1039, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element classificationSystem uses Python identifier classificationSystem
    __classificationSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'classificationSystem'), 'classificationSystem', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_7_classificationSystem', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1041, 14), )

    
    classificationSystem = property(__classificationSystem.value, __classificationSystem.set, None, u'')

    
    # Element identificationReference uses Python identifier identificationReference
    __identificationReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'identificationReference'), 'identificationReference', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_7_identificationReference', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1079, 14), )

    
    identificationReference = property(__identificationReference.value, __identificationReference.set, None, u'')

    
    # Element identifierName uses Python identifier identifierName
    __identifierName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'identifierName'), 'identifierName', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_7_identifierName', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1090, 14), )

    
    identifierName = property(__identifierName.value, __identifierName.set, None, u'')

    
    # Element taxonomicProcedures uses Python identifier taxonomicProcedures
    __taxonomicProcedures = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'taxonomicProcedures'), 'taxonomicProcedures', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_7_taxonomicProcedures', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1101, 14), )

    
    taxonomicProcedures = property(__taxonomicProcedures.value, __taxonomicProcedures.set, None, u'')

    
    # Element taxonomicCompleteness uses Python identifier taxonomicCompleteness
    __taxonomicCompleteness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'taxonomicCompleteness'), 'taxonomicCompleteness', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_7_taxonomicCompleteness', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1114, 14), )

    
    taxonomicCompleteness = property(__taxonomicCompleteness.value, __taxonomicCompleteness.set, None, u'')

    
    # Element vouchers uses Python identifier vouchers
    __vouchers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'vouchers'), 'vouchers', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_7_vouchers', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1130, 14), )

    
    vouchers = property(__vouchers.value, __vouchers.set, None, u'')

    _ElementMap.update({
        __classificationSystem.name() : __classificationSystem,
        __identificationReference.name() : __identificationReference,
        __identifierName.name() : __identifierName,
        __taxonomicProcedures.name() : __taxonomicProcedures,
        __taxonomicCompleteness.name() : __taxonomicCompleteness,
        __vouchers.name() : __vouchers
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1052, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element classificationSystemCitation uses Python identifier classificationSystemCitation
    __classificationSystemCitation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'classificationSystemCitation'), 'classificationSystemCitation', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_8_classificationSystemCitation', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1054, 20), )

    
    classificationSystemCitation = property(__classificationSystemCitation.value, __classificationSystemCitation.set, None, u'')

    
    # Element classificationSystemModifications uses Python identifier classificationSystemModifications
    __classificationSystemModifications = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'classificationSystemModifications'), 'classificationSystemModifications', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_8_classificationSystemModifications', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1064, 20), )

    
    classificationSystemModifications = property(__classificationSystemModifications.value, __classificationSystemModifications.set, None, u'')

    _ElementMap.update({
        __classificationSystemCitation.name() : __classificationSystemCitation,
        __classificationSystemModifications.name() : __classificationSystemModifications
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1140, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element specimen uses Python identifier specimen
    __specimen = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'specimen'), 'specimen', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_9_specimen', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1142, 20), )

    
    specimen = property(__specimen.value, __specimen.set, None, u'')

    
    # Element repository uses Python identifier repository
    __repository = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'repository'), 'repository', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_9_repository', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1154, 20), )

    
    repository = property(__repository.value, __repository.set, None, u'')

    _ElementMap.update({
        __specimen.name() : __specimen,
        __repository.name() : __repository
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1165, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element originator uses Python identifier originator
    __originator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'originator'), 'originator', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_10_originator', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1167, 26), )

    
    originator = property(__originator.value, __originator.set, None, u'')

    _ElementMap.update({
        __originator.name() : __originator
    })
    _AttributeMap.update({
        
    })



# Complex type {eml://ecoinformatics.org/coverage-2.1.0}TaxonomicClassificationType with content type ELEMENT_ONLY
class TaxonomicClassificationType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cov, u'TaxonomicClassificationType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1226, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element taxonRankName uses Python identifier taxonRankName
    __taxonRankName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'taxonRankName'), 'taxonRankName', '__emlecoinformatics_orgcoverage_2_1_0_TaxonomicClassificationType_taxonRankName', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1248, 6), )

    
    taxonRankName = property(__taxonRankName.value, __taxonRankName.set, None, u'')

    
    # Element taxonRankValue uses Python identifier taxonRankValue
    __taxonRankValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'taxonRankValue'), 'taxonRankValue', '__emlecoinformatics_orgcoverage_2_1_0_TaxonomicClassificationType_taxonRankValue', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1262, 6), )

    
    taxonRankValue = property(__taxonRankValue.value, __taxonRankValue.set, None, u'')

    
    # Element commonName uses Python identifier commonName
    __commonName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'commonName'), 'commonName', '__emlecoinformatics_orgcoverage_2_1_0_TaxonomicClassificationType_commonName', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1283, 6), )

    
    commonName = property(__commonName.value, __commonName.set, None, u'')

    
    # Element taxonomicClassification uses Python identifier taxonomicClassification
    __taxonomicClassification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'taxonomicClassification'), 'taxonomicClassification', '__emlecoinformatics_orgcoverage_2_1_0_TaxonomicClassificationType_taxonomicClassification', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1297, 6), )

    
    taxonomicClassification = property(__taxonomicClassification.value, __taxonomicClassification.set, None, u'')

    _ElementMap.update({
        __taxonRankName.name() : __taxonRankName,
        __taxonRankValue.name() : __taxonRankValue,
        __commonName.name() : __commonName,
        __taxonomicClassification.name() : __taxonomicClassification
    })
    _AttributeMap.update({
        
    })
_Namespace_cov.addCategoryObject('typeBinding', u'TaxonomicClassificationType', TaxonomicClassificationType)


# Complex type {eml://ecoinformatics.org/literature-2.1.0}Article with content type ELEMENT_ONLY
class Article (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cit, u'Article')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 282, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element journal uses Python identifier journal
    __journal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'journal'), 'journal', '__emlecoinformatics_orgliterature_2_1_0_Article_journal', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 294, 6), )

    
    journal = property(__journal.value, __journal.set, None, u'')

    
    # Element volume uses Python identifier volume
    __volume = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'volume'), 'volume', '__emlecoinformatics_orgliterature_2_1_0_Article_volume', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 308, 6), )

    
    volume = property(__volume.value, __volume.set, None, u'')

    
    # Element issue uses Python identifier issue
    __issue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'issue'), 'issue', '__emlecoinformatics_orgliterature_2_1_0_Article_issue', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 320, 6), )

    
    issue = property(__issue.value, __issue.set, None, u'')

    
    # Element pageRange uses Python identifier pageRange
    __pageRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'pageRange'), 'pageRange', '__emlecoinformatics_orgliterature_2_1_0_Article_pageRange', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 332, 6), )

    
    pageRange = property(__pageRange.value, __pageRange.set, None, u'')

    
    # Element publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'publisher'), 'publisher', '__emlecoinformatics_orgliterature_2_1_0_Article_publisher', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 345, 6), )

    
    publisher = property(__publisher.value, __publisher.set, None, u'')

    
    # Element publicationPlace uses Python identifier publicationPlace
    __publicationPlace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'publicationPlace'), 'publicationPlace', '__emlecoinformatics_orgliterature_2_1_0_Article_publicationPlace', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 358, 6), )

    
    publicationPlace = property(__publicationPlace.value, __publicationPlace.set, None, u'')

    
    # Element ISSN uses Python identifier ISSN
    __ISSN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ISSN'), 'ISSN', '__emlecoinformatics_orgliterature_2_1_0_Article_ISSN', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 372, 6), )

    
    ISSN = property(__ISSN.value, __ISSN.set, None, u'')

    _ElementMap.update({
        __journal.name() : __journal,
        __volume.name() : __volume,
        __issue.name() : __issue,
        __pageRange.name() : __pageRange,
        __publisher.name() : __publisher,
        __publicationPlace.name() : __publicationPlace,
        __ISSN.name() : __ISSN
    })
    _AttributeMap.update({
        
    })
_Namespace_cit.addCategoryObject('typeBinding', u'Article', Article)


# Complex type {eml://ecoinformatics.org/literature-2.1.0}Book with content type ELEMENT_ONLY
class Book (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cit, u'Book')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 387, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'publisher'), 'publisher', '__emlecoinformatics_orgliterature_2_1_0_Book_publisher', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 397, 6), )

    
    publisher = property(__publisher.value, __publisher.set, None, u'')

    
    # Element publicationPlace uses Python identifier publicationPlace
    __publicationPlace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'publicationPlace'), 'publicationPlace', '__emlecoinformatics_orgliterature_2_1_0_Book_publicationPlace', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 410, 6), )

    
    publicationPlace = property(__publicationPlace.value, __publicationPlace.set, None, u'')

    
    # Element edition uses Python identifier edition
    __edition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'edition'), 'edition', '__emlecoinformatics_orgliterature_2_1_0_Book_edition', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 424, 6), )

    
    edition = property(__edition.value, __edition.set, None, u'')

    
    # Element volume uses Python identifier volume
    __volume = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'volume'), 'volume', '__emlecoinformatics_orgliterature_2_1_0_Book_volume', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 435, 6), )

    
    volume = property(__volume.value, __volume.set, None, u'')

    
    # Element numberOfVolumes uses Python identifier numberOfVolumes
    __numberOfVolumes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'numberOfVolumes'), 'numberOfVolumes', '__emlecoinformatics_orgliterature_2_1_0_Book_numberOfVolumes', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 448, 6), )

    
    numberOfVolumes = property(__numberOfVolumes.value, __numberOfVolumes.set, None, u'')

    
    # Element totalPages uses Python identifier totalPages
    __totalPages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'totalPages'), 'totalPages', '__emlecoinformatics_orgliterature_2_1_0_Book_totalPages', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 459, 6), )

    
    totalPages = property(__totalPages.value, __totalPages.set, None, u'')

    
    # Element totalFigures uses Python identifier totalFigures
    __totalFigures = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'totalFigures'), 'totalFigures', '__emlecoinformatics_orgliterature_2_1_0_Book_totalFigures', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 471, 6), )

    
    totalFigures = property(__totalFigures.value, __totalFigures.set, None, u'')

    
    # Element totalTables uses Python identifier totalTables
    __totalTables = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'totalTables'), 'totalTables', '__emlecoinformatics_orgliterature_2_1_0_Book_totalTables', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 483, 6), )

    
    totalTables = property(__totalTables.value, __totalTables.set, None, u'')

    
    # Element ISBN uses Python identifier ISBN
    __ISBN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ISBN'), 'ISBN', '__emlecoinformatics_orgliterature_2_1_0_Book_ISBN', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 495, 6), )

    
    ISBN = property(__ISBN.value, __ISBN.set, None, u'')

    _ElementMap.update({
        __publisher.name() : __publisher,
        __publicationPlace.name() : __publicationPlace,
        __edition.name() : __edition,
        __volume.name() : __volume,
        __numberOfVolumes.name() : __numberOfVolumes,
        __totalPages.name() : __totalPages,
        __totalFigures.name() : __totalFigures,
        __totalTables.name() : __totalTables,
        __ISBN.name() : __ISBN
    })
    _AttributeMap.update({
        
    })
_Namespace_cit.addCategoryObject('typeBinding', u'Book', Book)


# Complex type {eml://ecoinformatics.org/literature-2.1.0}Manuscript with content type ELEMENT_ONLY
class Manuscript (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cit, u'Manuscript')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 632, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element institution uses Python identifier institution
    __institution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'institution'), 'institution', '__emlecoinformatics_orgliterature_2_1_0_Manuscript_institution', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 642, 6), )

    
    institution = property(__institution.value, __institution.set, None, u'')

    
    # Element totalPages uses Python identifier totalPages
    __totalPages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'totalPages'), 'totalPages', '__emlecoinformatics_orgliterature_2_1_0_Manuscript_totalPages', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 656, 6), )

    
    totalPages = property(__totalPages.value, __totalPages.set, None, u'')

    _ElementMap.update({
        __institution.name() : __institution,
        __totalPages.name() : __totalPages
    })
    _AttributeMap.update({
        
    })
_Namespace_cit.addCategoryObject('typeBinding', u'Manuscript', Manuscript)


# Complex type {eml://ecoinformatics.org/literature-2.1.0}Report with content type ELEMENT_ONLY
class Report (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cit, u'Report')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 671, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element reportNumber uses Python identifier reportNumber
    __reportNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reportNumber'), 'reportNumber', '__emlecoinformatics_orgliterature_2_1_0_Report_reportNumber', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 683, 6), )

    
    reportNumber = property(__reportNumber.value, __reportNumber.set, None, u'')

    
    # Element publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'publisher'), 'publisher', '__emlecoinformatics_orgliterature_2_1_0_Report_publisher', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 696, 6), )

    
    publisher = property(__publisher.value, __publisher.set, None, u'')

    
    # Element publicationPlace uses Python identifier publicationPlace
    __publicationPlace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'publicationPlace'), 'publicationPlace', '__emlecoinformatics_orgliterature_2_1_0_Report_publicationPlace', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 709, 6), )

    
    publicationPlace = property(__publicationPlace.value, __publicationPlace.set, None, u'')

    
    # Element totalPages uses Python identifier totalPages
    __totalPages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'totalPages'), 'totalPages', '__emlecoinformatics_orgliterature_2_1_0_Report_totalPages', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 723, 6), )

    
    totalPages = property(__totalPages.value, __totalPages.set, None, u'')

    _ElementMap.update({
        __reportNumber.name() : __reportNumber,
        __publisher.name() : __publisher,
        __publicationPlace.name() : __publicationPlace,
        __totalPages.name() : __totalPages
    })
    _AttributeMap.update({
        
    })
_Namespace_cit.addCategoryObject('typeBinding', u'Report', Report)


# Complex type {eml://ecoinformatics.org/literature-2.1.0}PersonalCommunication with content type ELEMENT_ONLY
class PersonalCommunication (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cit, u'PersonalCommunication')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 737, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'publisher'), 'publisher', '__emlecoinformatics_orgliterature_2_1_0_PersonalCommunication_publisher', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 748, 6), )

    
    publisher = property(__publisher.value, __publisher.set, None, u'')

    
    # Element publicationPlace uses Python identifier publicationPlace
    __publicationPlace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'publicationPlace'), 'publicationPlace', '__emlecoinformatics_orgliterature_2_1_0_PersonalCommunication_publicationPlace', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 761, 6), )

    
    publicationPlace = property(__publicationPlace.value, __publicationPlace.set, None, u'')

    
    # Element communicationType uses Python identifier communicationType
    __communicationType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'communicationType'), 'communicationType', '__emlecoinformatics_orgliterature_2_1_0_PersonalCommunication_communicationType', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 775, 6), )

    
    communicationType = property(__communicationType.value, __communicationType.set, None, u'')

    
    # Element recipient uses Python identifier recipient
    __recipient = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'recipient'), 'recipient', '__emlecoinformatics_orgliterature_2_1_0_PersonalCommunication_recipient', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 789, 6), )

    
    recipient = property(__recipient.value, __recipient.set, None, u'')

    _ElementMap.update({
        __publisher.name() : __publisher,
        __publicationPlace.name() : __publicationPlace,
        __communicationType.name() : __communicationType,
        __recipient.name() : __recipient
    })
    _AttributeMap.update({
        
    })
_Namespace_cit.addCategoryObject('typeBinding', u'PersonalCommunication', PersonalCommunication)


# Complex type {eml://ecoinformatics.org/literature-2.1.0}Map with content type ELEMENT_ONLY
class Map (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cit, u'Map')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 803, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'publisher'), 'publisher', '__emlecoinformatics_orgliterature_2_1_0_Map_publisher', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 815, 6), )

    
    publisher = property(__publisher.value, __publisher.set, None, u'')

    
    # Element edition uses Python identifier edition
    __edition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'edition'), 'edition', '__emlecoinformatics_orgliterature_2_1_0_Map_edition', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 827, 6), )

    
    edition = property(__edition.value, __edition.set, None, u'')

    
    # Element geographicCoverage uses Python identifier geographicCoverage
    __geographicCoverage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'geographicCoverage'), 'geographicCoverage', '__emlecoinformatics_orgliterature_2_1_0_Map_geographicCoverage', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 838, 6), )

    
    geographicCoverage = property(__geographicCoverage.value, __geographicCoverage.set, None, u'')

    
    # Element scale uses Python identifier scale
    __scale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'scale'), 'scale', '__emlecoinformatics_orgliterature_2_1_0_Map_scale', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 850, 6), )

    
    scale = property(__scale.value, __scale.set, None, u'')

    _ElementMap.update({
        __publisher.name() : __publisher,
        __edition.name() : __edition,
        __geographicCoverage.name() : __geographicCoverage,
        __scale.name() : __scale
    })
    _AttributeMap.update({
        
    })
_Namespace_cit.addCategoryObject('typeBinding', u'Map', Map)


# Complex type {eml://ecoinformatics.org/literature-2.1.0}AudioVisual with content type ELEMENT_ONLY
class AudioVisual (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cit, u'AudioVisual')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 862, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'publisher'), 'publisher', '__emlecoinformatics_orgliterature_2_1_0_AudioVisual_publisher', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 874, 6), )

    
    publisher = property(__publisher.value, __publisher.set, None, u'')

    
    # Element publicationPlace uses Python identifier publicationPlace
    __publicationPlace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'publicationPlace'), 'publicationPlace', '__emlecoinformatics_orgliterature_2_1_0_AudioVisual_publicationPlace', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 888, 6), )

    
    publicationPlace = property(__publicationPlace.value, __publicationPlace.set, None, u'')

    
    # Element performer uses Python identifier performer
    __performer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'performer'), 'performer', '__emlecoinformatics_orgliterature_2_1_0_AudioVisual_performer', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 902, 6), )

    
    performer = property(__performer.value, __performer.set, None, u'')

    
    # Element ISBN uses Python identifier ISBN
    __ISBN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ISBN'), 'ISBN', '__emlecoinformatics_orgliterature_2_1_0_AudioVisual_ISBN', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 915, 6), )

    
    ISBN = property(__ISBN.value, __ISBN.set, None, u'')

    _ElementMap.update({
        __publisher.name() : __publisher,
        __publicationPlace.name() : __publicationPlace,
        __performer.name() : __performer,
        __ISBN.name() : __ISBN
    })
    _AttributeMap.update({
        
    })
_Namespace_cit.addCategoryObject('typeBinding', u'AudioVisual', AudioVisual)


# Complex type {eml://ecoinformatics.org/literature-2.1.0}Generic with content type ELEMENT_ONLY
class Generic (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {eml://ecoinformatics.org/literature-2.1.0}Generic with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cit, u'Generic')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 930, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'publisher'), 'publisher', '__emlecoinformatics_orgliterature_2_1_0_Generic_publisher', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 932, 6), )

    
    publisher = property(__publisher.value, __publisher.set, None, u'')

    
    # Element publicationPlace uses Python identifier publicationPlace
    __publicationPlace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'publicationPlace'), 'publicationPlace', '__emlecoinformatics_orgliterature_2_1_0_Generic_publicationPlace', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 945, 6), )

    
    publicationPlace = property(__publicationPlace.value, __publicationPlace.set, None, u'')

    
    # Element referenceType uses Python identifier referenceType
    __referenceType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'referenceType'), 'referenceType', '__emlecoinformatics_orgliterature_2_1_0_Generic_referenceType', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 959, 6), )

    
    referenceType = property(__referenceType.value, __referenceType.set, None, u'')

    
    # Element volume uses Python identifier volume
    __volume = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'volume'), 'volume', '__emlecoinformatics_orgliterature_2_1_0_Generic_volume', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 972, 6), )

    
    volume = property(__volume.value, __volume.set, None, u'')

    
    # Element numberOfVolumes uses Python identifier numberOfVolumes
    __numberOfVolumes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'numberOfVolumes'), 'numberOfVolumes', '__emlecoinformatics_orgliterature_2_1_0_Generic_numberOfVolumes', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 985, 6), )

    
    numberOfVolumes = property(__numberOfVolumes.value, __numberOfVolumes.set, None, u'')

    
    # Element totalPages uses Python identifier totalPages
    __totalPages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'totalPages'), 'totalPages', '__emlecoinformatics_orgliterature_2_1_0_Generic_totalPages', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 996, 6), )

    
    totalPages = property(__totalPages.value, __totalPages.set, None, u'')

    
    # Element totalFigures uses Python identifier totalFigures
    __totalFigures = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'totalFigures'), 'totalFigures', '__emlecoinformatics_orgliterature_2_1_0_Generic_totalFigures', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1009, 6), )

    
    totalFigures = property(__totalFigures.value, __totalFigures.set, None, u'')

    
    # Element totalTables uses Python identifier totalTables
    __totalTables = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'totalTables'), 'totalTables', '__emlecoinformatics_orgliterature_2_1_0_Generic_totalTables', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1022, 6), )

    
    totalTables = property(__totalTables.value, __totalTables.set, None, u'')

    
    # Element edition uses Python identifier edition
    __edition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'edition'), 'edition', '__emlecoinformatics_orgliterature_2_1_0_Generic_edition', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1035, 6), )

    
    edition = property(__edition.value, __edition.set, None, u'')

    
    # Element originalPublication uses Python identifier originalPublication
    __originalPublication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'originalPublication'), 'originalPublication', '__emlecoinformatics_orgliterature_2_1_0_Generic_originalPublication', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1048, 6), )

    
    originalPublication = property(__originalPublication.value, __originalPublication.set, None, u'')

    
    # Element reprintEdition uses Python identifier reprintEdition
    __reprintEdition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reprintEdition'), 'reprintEdition', '__emlecoinformatics_orgliterature_2_1_0_Generic_reprintEdition', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1061, 6), )

    
    reprintEdition = property(__reprintEdition.value, __reprintEdition.set, None, u'')

    
    # Element reviewedItem uses Python identifier reviewedItem
    __reviewedItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reviewedItem'), 'reviewedItem', '__emlecoinformatics_orgliterature_2_1_0_Generic_reviewedItem', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1074, 6), )

    
    reviewedItem = property(__reviewedItem.value, __reviewedItem.set, None, u'')

    
    # Element ISBN uses Python identifier ISBN
    __ISBN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ISBN'), 'ISBN', '__emlecoinformatics_orgliterature_2_1_0_Generic_ISBN', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1090, 8), )

    
    ISBN = property(__ISBN.value, __ISBN.set, None, u'')

    
    # Element ISSN uses Python identifier ISSN
    __ISSN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ISSN'), 'ISSN', '__emlecoinformatics_orgliterature_2_1_0_Generic_ISSN', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1103, 8), )

    
    ISSN = property(__ISSN.value, __ISSN.set, None, u'')

    _ElementMap.update({
        __publisher.name() : __publisher,
        __publicationPlace.name() : __publicationPlace,
        __referenceType.name() : __referenceType,
        __volume.name() : __volume,
        __numberOfVolumes.name() : __numberOfVolumes,
        __totalPages.name() : __totalPages,
        __totalFigures.name() : __totalFigures,
        __totalTables.name() : __totalTables,
        __edition.name() : __edition,
        __originalPublication.name() : __originalPublication,
        __reprintEdition.name() : __reprintEdition,
        __reviewedItem.name() : __reviewedItem,
        __ISBN.name() : __ISBN,
        __ISSN.name() : __ISSN
    })
    _AttributeMap.update({
        
    })
_Namespace_cit.addCategoryObject('typeBinding', u'Generic', Generic)


# Complex type {eml://ecoinformatics.org/literature-2.1.0}Thesis with content type ELEMENT_ONLY
class Thesis (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cit, u'Thesis')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1119, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element degree uses Python identifier degree
    __degree = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'degree'), 'degree', '__emlecoinformatics_orgliterature_2_1_0_Thesis_degree', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1132, 6), )

    
    degree = property(__degree.value, __degree.set, None, u'')

    
    # Element institution uses Python identifier institution
    __institution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'institution'), 'institution', '__emlecoinformatics_orgliterature_2_1_0_Thesis_institution', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1146, 6), )

    
    institution = property(__institution.value, __institution.set, None, u'')

    
    # Element totalPages uses Python identifier totalPages
    __totalPages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'totalPages'), 'totalPages', '__emlecoinformatics_orgliterature_2_1_0_Thesis_totalPages', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1159, 6), )

    
    totalPages = property(__totalPages.value, __totalPages.set, None, u'')

    _ElementMap.update({
        __degree.name() : __degree,
        __institution.name() : __institution,
        __totalPages.name() : __totalPages
    })
    _AttributeMap.update({
        
    })
_Namespace_cit.addCategoryObject('typeBinding', u'Thesis', Thesis)


# Complex type {eml://ecoinformatics.org/literature-2.1.0}Presentation with content type ELEMENT_ONLY
class Presentation (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cit, u'Presentation')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1173, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element conferenceName uses Python identifier conferenceName
    __conferenceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'conferenceName'), 'conferenceName', '__emlecoinformatics_orgliterature_2_1_0_Presentation_conferenceName', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1187, 6), )

    
    conferenceName = property(__conferenceName.value, __conferenceName.set, None, u'')

    
    # Element conferenceDate uses Python identifier conferenceDate
    __conferenceDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'conferenceDate'), 'conferenceDate', '__emlecoinformatics_orgliterature_2_1_0_Presentation_conferenceDate', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1199, 6), )

    
    conferenceDate = property(__conferenceDate.value, __conferenceDate.set, None, u'')

    
    # Element conferenceLocation uses Python identifier conferenceLocation
    __conferenceLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'conferenceLocation'), 'conferenceLocation', '__emlecoinformatics_orgliterature_2_1_0_Presentation_conferenceLocation', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1210, 6), )

    
    conferenceLocation = property(__conferenceLocation.value, __conferenceLocation.set, None, u'')

    _ElementMap.update({
        __conferenceName.name() : __conferenceName,
        __conferenceDate.name() : __conferenceDate,
        __conferenceLocation.name() : __conferenceLocation
    })
    _AttributeMap.update({
        
    })
_Namespace_cit.addCategoryObject('typeBinding', u'Presentation', Presentation)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 236, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute phonetype uses Python identifier phonetype
    __phonetype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'phonetype'), 'phonetype', '__emlecoinformatics_orgparty_2_1_0_CTD_ANON_phonetype', pyxb.binding.datatypes.string, unicode_default=u'voice')
    __phonetype._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 239, 16)
    __phonetype._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 239, 16)
    
    phonetype = property(__phonetype.value, __phonetype.set, None, u'')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __phonetype.name() : __phonetype
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 302, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute directory uses Python identifier directory
    __directory = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'directory'), 'directory', '__emlecoinformatics_orgparty_2_1_0_CTD_ANON__directory', pyxb.binding.datatypes.string, required=True)
    __directory._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 305, 16)
    __directory._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 305, 16)
    
    directory = property(__directory.value, __directory.set, None, u'')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __directory.name() : __directory
    })



# Complex type {eml://ecoinformatics.org/party-2.1.0}Person with content type ELEMENT_ONLY
class Person (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_rp, u'Person')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 334, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element salutation uses Python identifier salutation
    __salutation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'salutation'), 'salutation', '__emlecoinformatics_orgparty_2_1_0_Person_salutation', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 378, 6), )

    
    salutation = property(__salutation.value, __salutation.set, None, u'')

    
    # Element givenName uses Python identifier givenName
    __givenName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'givenName'), 'givenName', '__emlecoinformatics_orgparty_2_1_0_Person_givenName', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 391, 6), )

    
    givenName = property(__givenName.value, __givenName.set, None, u'')

    
    # Element surName uses Python identifier surName
    __surName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'surName'), 'surName', '__emlecoinformatics_orgparty_2_1_0_Person_surName', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 409, 6), )

    
    surName = property(__surName.value, __surName.set, None, u'')

    _ElementMap.update({
        __salutation.name() : __salutation,
        __givenName.name() : __givenName,
        __surName.name() : __surName
    })
    _AttributeMap.update({
        
    })
_Namespace_rp.addCategoryObject('typeBinding', u'Person', Person)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 208, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element descriptor uses Python identifier descriptor
    __descriptor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'descriptor'), 'descriptor', '__emlecoinformatics_orgproject_2_1_0_CTD_ANON_descriptor', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 210, 14), )

    
    descriptor = property(__descriptor.value, __descriptor.set, None, u'')

    
    # Element citation uses Python identifier citation
    __citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'citation'), 'citation', '__emlecoinformatics_orgproject_2_1_0_CTD_ANON_citation', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 329, 14), )

    
    citation = property(__citation.value, __citation.set, None, u'')

    
    # Element coverage uses Python identifier coverage
    __coverage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'coverage'), 'coverage', '__emlecoinformatics_orgproject_2_1_0_CTD_ANON_coverage', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 340, 14), )

    
    coverage = property(__coverage.value, __coverage.set, None, u'')

    _ElementMap.update({
        __descriptor.name() : __descriptor,
        __citation.name() : __citation,
        __coverage.name() : __coverage
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 251, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute name_or_id uses Python identifier name_or_id
    __name_or_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name_or_id'), 'name_or_id', '__emlecoinformatics_orgproject_2_1_0_CTD_ANON__name_or_id', pyxb.binding.datatypes.string)
    __name_or_id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 254, 28)
    __name_or_id._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 254, 28)
    
    name_or_id = property(__name_or_id.value, __name_or_id.set, None, u'')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name_or_id.name() : __name_or_id
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 367, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__emlecoinformatics_orgproject_2_1_0_CTD_ANON_2_description', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 369, 14), )

    
    description = property(__description.value, __description.set, None, u'')

    
    # Element citation uses Python identifier citation
    __citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'citation'), 'citation', '__emlecoinformatics_orgproject_2_1_0_CTD_ANON_2_citation', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 384, 14), )

    
    citation = property(__citation.value, __citation.set, None, u'')

    _ElementMap.update({
        __description.name() : __description,
        __citation.name() : __citation
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 278, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element keyword uses Python identifier keyword
    __keyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'keyword'), 'keyword', '__emlecoinformatics_orgresource_2_1_0_CTD_ANON_keyword', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 280, 12), )

    
    keyword = property(__keyword.value, __keyword.set, None, u'')

    
    # Element keywordThesaurus uses Python identifier keywordThesaurus
    __keywordThesaurus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'keywordThesaurus'), 'keywordThesaurus', '__emlecoinformatics_orgresource_2_1_0_CTD_ANON_keywordThesaurus', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 316, 12), )

    
    keywordThesaurus = property(__keywordThesaurus.value, __keywordThesaurus.set, None, u'')

    _ElementMap.update({
        __keyword.name() : __keyword,
        __keywordThesaurus.name() : __keywordThesaurus
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 754, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__emlecoinformatics_orgresource_2_1_0_CTD_ANON__name', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 756, 14), )

    
    name = property(__name.value, __name.set, None, u'')

    
    # Element definition uses Python identifier definition
    __definition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'definition'), 'definition', '__emlecoinformatics_orgresource_2_1_0_CTD_ANON__definition', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 768, 14), )

    
    definition = property(__definition.value, __definition.set, None, u'')

    
    # Element defaultValue uses Python identifier defaultValue
    __defaultValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'defaultValue'), 'defaultValue', '__emlecoinformatics_orgresource_2_1_0_CTD_ANON__defaultValue', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 784, 14), )

    
    defaultValue = property(__defaultValue.value, __defaultValue.set, None, u'')

    _ElementMap.update({
        __name.name() : __name,
        __definition.name() : __definition,
        __defaultValue.name() : __defaultValue
    })
    _AttributeMap.update({
        
    })



# Complex type {eml://ecoinformatics.org/resource-2.1.0}InlineType with content type MIXED
class InlineType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_res, u'InlineType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 816, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_Namespace_res.addCategoryObject('typeBinding', u'InlineType', InlineType)


# Complex type {eml://ecoinformatics.org/resource-2.1.0}OfflineType with content type ELEMENT_ONLY
class OfflineType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_res, u'OfflineType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 843, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mediumName uses Python identifier mediumName
    __mediumName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'mediumName'), 'mediumName', '__emlecoinformatics_orgresource_2_1_0_OfflineType_mediumName', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 856, 6), )

    
    mediumName = property(__mediumName.value, __mediumName.set, None, u'')

    
    # Element mediumDensity uses Python identifier mediumDensity
    __mediumDensity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'mediumDensity'), 'mediumDensity', '__emlecoinformatics_orgresource_2_1_0_OfflineType_mediumDensity', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 871, 6), )

    
    mediumDensity = property(__mediumDensity.value, __mediumDensity.set, None, u'')

    
    # Element mediumDensityUnits uses Python identifier mediumDensityUnits
    __mediumDensityUnits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'mediumDensityUnits'), 'mediumDensityUnits', '__emlecoinformatics_orgresource_2_1_0_OfflineType_mediumDensityUnits', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 885, 6), )

    
    mediumDensityUnits = property(__mediumDensityUnits.value, __mediumDensityUnits.set, None, u'')

    
    # Element mediumVolume uses Python identifier mediumVolume
    __mediumVolume = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'mediumVolume'), 'mediumVolume', '__emlecoinformatics_orgresource_2_1_0_OfflineType_mediumVolume', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 896, 6), )

    
    mediumVolume = property(__mediumVolume.value, __mediumVolume.set, None, u'')

    
    # Element mediumFormat uses Python identifier mediumFormat
    __mediumFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'mediumFormat'), 'mediumFormat', '__emlecoinformatics_orgresource_2_1_0_OfflineType_mediumFormat', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 908, 6), )

    
    mediumFormat = property(__mediumFormat.value, __mediumFormat.set, None, u'')

    
    # Element mediumNote uses Python identifier mediumNote
    __mediumNote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'mediumNote'), 'mediumNote', '__emlecoinformatics_orgresource_2_1_0_OfflineType_mediumNote', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 920, 6), )

    
    mediumNote = property(__mediumNote.value, __mediumNote.set, None, u'')

    _ElementMap.update({
        __mediumName.name() : __mediumName,
        __mediumDensity.name() : __mediumDensity,
        __mediumDensityUnits.name() : __mediumDensityUnits,
        __mediumVolume.name() : __mediumVolume,
        __mediumFormat.name() : __mediumFormat,
        __mediumNote.name() : __mediumNote
    })
    _AttributeMap.update({
        
    })
_Namespace_res.addCategoryObject('typeBinding', u'OfflineType', OfflineType)


# Complex type {eml://ecoinformatics.org/resource-2.1.0}OnlineType with content type ELEMENT_ONLY
class OnlineType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_res, u'OnlineType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 932, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element onlineDescription uses Python identifier onlineDescription
    __onlineDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'onlineDescription'), 'onlineDescription', '__emlecoinformatics_orgresource_2_1_0_OnlineType_onlineDescription', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 962, 6), )

    
    onlineDescription = property(__onlineDescription.value, __onlineDescription.set, None, u'')

    
    # Element url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'url'), 'url', '__emlecoinformatics_orgresource_2_1_0_OnlineType_url', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 975, 8), )

    
    url = property(__url.value, __url.set, None, u'')

    
    # Element connection uses Python identifier connection
    __connection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'connection'), 'connection', '__emlecoinformatics_orgresource_2_1_0_OnlineType_connection', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 989, 8), )

    
    connection = property(__connection.value, __connection.set, None, u'')

    
    # Element connectionDefinition uses Python identifier connectionDefinition
    __connectionDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'connectionDefinition'), 'connectionDefinition', '__emlecoinformatics_orgresource_2_1_0_OnlineType_connectionDefinition', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1001, 8), )

    
    connectionDefinition = property(__connectionDefinition.value, __connectionDefinition.set, None, u'')

    _ElementMap.update({
        __onlineDescription.name() : __onlineDescription,
        __url.name() : __url,
        __connection.name() : __connection,
        __connectionDefinition.name() : __connectionDefinition
    })
    _AttributeMap.update({
        
    })
_Namespace_res.addCategoryObject('typeBinding', u'OnlineType', OnlineType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1120, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__emlecoinformatics_orgresource_2_1_0_CTD_ANON_2_name', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1122, 14), )

    
    name = property(__name.value, __name.set, None, u'')

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__emlecoinformatics_orgresource_2_1_0_CTD_ANON_2_value', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1135, 14), )

    
    value_ = property(__value.value, __value.set, None, u'')

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })



# Complex type {eml://ecoinformatics.org/access-2.1.0}AccessType with content type ELEMENT_ONLY
class AccessType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_acc, u'AccessType')
    _XSDLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 208, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element allow uses Python identifier allow
    __allow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'allow'), 'allow', '__emlecoinformatics_orgaccess_2_1_0_AccessType_allow', True, pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 228, 8), )

    
    allow = property(__allow.value, __allow.set, None, u'')

    
    # Element deny uses Python identifier deny
    __deny = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'deny'), 'deny', '__emlecoinformatics_orgaccess_2_1_0_AccessType_deny', True, pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 240, 8), )

    
    deny = property(__deny.value, __deny.set, None, u'')

    
    # Element references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'references'), 'references', '__emlecoinformatics_orgaccess_2_1_0_AccessType_references', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6), )

    
    references = property(__references.value, __references.set, None, u'')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__emlecoinformatics_orgaccess_2_1_0_AccessType_id', IDType)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 256, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 256, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgaccess_2_1_0_AccessType_system', SystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 257, 4)
    __system._UseLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 257, 4)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scope'), 'scope', '__emlecoinformatics_orgaccess_2_1_0_AccessType_scope', ScopeType, unicode_default=u'document')
    __scope._DeclarationLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 258, 4)
    __scope._UseLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 258, 4)
    
    scope = property(__scope.value, __scope.set, None, None)

    
    # Attribute order uses Python identifier order
    __order = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'order'), 'order', '__emlecoinformatics_orgaccess_2_1_0_AccessType_order', STD_ANON, unicode_default=u'allowFirst')
    __order._DeclarationLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 259, 4)
    __order._UseLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 259, 4)
    
    order = property(__order.value, __order.set, None, u'')

    
    # Attribute authSystem uses Python identifier authSystem
    __authSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'authSystem'), 'authSystem', '__emlecoinformatics_orgaccess_2_1_0_AccessType_authSystem', pyxb.binding.datatypes.string, required=True)
    __authSystem._DeclarationLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 282, 4)
    __authSystem._UseLocation = pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 282, 4)
    
    authSystem = property(__authSystem.value, __authSystem.set, None, u'')

    _ElementMap.update({
        __allow.name() : __allow,
        __deny.name() : __deny,
        __references.name() : __references
    })
    _AttributeMap.update({
        __id.name() : __id,
        __system.name() : __system,
        __scope.name() : __scope,
        __order.name() : __order,
        __authSystem.name() : __authSystem
    })
_Namespace_acc.addCategoryObject('typeBinding', u'AccessType', AccessType)


# Complex type {eml://ecoinformatics.org/coverage-2.1.0}Coverage with content type ELEMENT_ONLY
class Coverage (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cov, u'Coverage')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 113, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element geographicCoverage uses Python identifier geographicCoverage
    __geographicCoverage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'geographicCoverage'), 'geographicCoverage', '__emlecoinformatics_orgcoverage_2_1_0_Coverage_geographicCoverage', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 131, 8), )

    
    geographicCoverage = property(__geographicCoverage.value, __geographicCoverage.set, None, u'')

    
    # Element temporalCoverage uses Python identifier temporalCoverage
    __temporalCoverage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'temporalCoverage'), 'temporalCoverage', '__emlecoinformatics_orgcoverage_2_1_0_Coverage_temporalCoverage', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 146, 8), )

    
    temporalCoverage = property(__temporalCoverage.value, __temporalCoverage.set, None, u'')

    
    # Element taxonomicCoverage uses Python identifier taxonomicCoverage
    __taxonomicCoverage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'taxonomicCoverage'), 'taxonomicCoverage', '__emlecoinformatics_orgcoverage_2_1_0_Coverage_taxonomicCoverage', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 168, 8), )

    
    taxonomicCoverage = property(__taxonomicCoverage.value, __taxonomicCoverage.set, None, u'')

    
    # Element references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'references'), 'references', '__emlecoinformatics_orgcoverage_2_1_0_Coverage_references', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6), )

    
    references = property(__references.value, __references.set, None, u'')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__emlecoinformatics_orgcoverage_2_1_0_Coverage_id', IDType)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 193, 4)
    __id._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 193, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgcoverage_2_1_0_Coverage_system', SystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 194, 4)
    __system._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 194, 4)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scope'), 'scope', '__emlecoinformatics_orgcoverage_2_1_0_Coverage_scope', ScopeType, unicode_default=u'document')
    __scope._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 195, 4)
    __scope._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 195, 4)
    
    scope = property(__scope.value, __scope.set, None, None)

    _ElementMap.update({
        __geographicCoverage.name() : __geographicCoverage,
        __temporalCoverage.name() : __temporalCoverage,
        __taxonomicCoverage.name() : __taxonomicCoverage,
        __references.name() : __references
    })
    _AttributeMap.update({
        __id.name() : __id,
        __system.name() : __system,
        __scope.name() : __scope
    })
_Namespace_cov.addCategoryObject('typeBinding', u'Coverage', Coverage)


# Complex type {eml://ecoinformatics.org/coverage-2.1.0}TemporalCoverage with content type ELEMENT_ONLY
class TemporalCoverage (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cov, u'TemporalCoverage')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 197, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element singleDateTime uses Python identifier singleDateTime
    __singleDateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'singleDateTime'), 'singleDateTime', '__emlecoinformatics_orgcoverage_2_1_0_TemporalCoverage_singleDateTime', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 212, 8), )

    
    singleDateTime = property(__singleDateTime.value, __singleDateTime.set, None, u'')

    
    # Element rangeOfDates uses Python identifier rangeOfDates
    __rangeOfDates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'rangeOfDates'), 'rangeOfDates', '__emlecoinformatics_orgcoverage_2_1_0_TemporalCoverage_rangeOfDates', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 228, 8), )

    
    rangeOfDates = property(__rangeOfDates.value, __rangeOfDates.set, None, u'')

    
    # Element references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'references'), 'references', '__emlecoinformatics_orgcoverage_2_1_0_TemporalCoverage_references', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6), )

    
    references = property(__references.value, __references.set, None, u'')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__emlecoinformatics_orgcoverage_2_1_0_TemporalCoverage_id', IDType)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 281, 4)
    __id._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 281, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __singleDateTime.name() : __singleDateTime,
        __rangeOfDates.name() : __rangeOfDates,
        __references.name() : __references
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_Namespace_cov.addCategoryObject('typeBinding', u'TemporalCoverage', TemporalCoverage)


# Complex type {eml://ecoinformatics.org/coverage-2.1.0}GeographicCoverage with content type ELEMENT_ONLY
class GeographicCoverage (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cov, u'GeographicCoverage')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 471, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element geographicDescription uses Python identifier geographicDescription
    __geographicDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'geographicDescription'), 'geographicDescription', '__emlecoinformatics_orgcoverage_2_1_0_GeographicCoverage_geographicDescription', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 487, 8), )

    
    geographicDescription = property(__geographicDescription.value, __geographicDescription.set, None, u'')

    
    # Element boundingCoordinates uses Python identifier boundingCoordinates
    __boundingCoordinates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'boundingCoordinates'), 'boundingCoordinates', '__emlecoinformatics_orgcoverage_2_1_0_GeographicCoverage_boundingCoordinates', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 536, 8), )

    
    boundingCoordinates = property(__boundingCoordinates.value, __boundingCoordinates.set, None, u'')

    
    # Element datasetGPolygon uses Python identifier datasetGPolygon
    __datasetGPolygon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'datasetGPolygon'), 'datasetGPolygon', '__emlecoinformatics_orgcoverage_2_1_0_GeographicCoverage_datasetGPolygon', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 758, 8), )

    
    datasetGPolygon = property(__datasetGPolygon.value, __datasetGPolygon.set, None, u'')

    
    # Element references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'references'), 'references', '__emlecoinformatics_orgcoverage_2_1_0_GeographicCoverage_references', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6), )

    
    references = property(__references.value, __references.set, None, u'')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__emlecoinformatics_orgcoverage_2_1_0_GeographicCoverage_id', IDType)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 899, 4)
    __id._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 899, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgcoverage_2_1_0_GeographicCoverage_system', SystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 900, 4)
    __system._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 900, 4)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scope'), 'scope', '__emlecoinformatics_orgcoverage_2_1_0_GeographicCoverage_scope', ScopeType, unicode_default=u'document')
    __scope._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 901, 4)
    __scope._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 901, 4)
    
    scope = property(__scope.value, __scope.set, None, None)

    _ElementMap.update({
        __geographicDescription.name() : __geographicDescription,
        __boundingCoordinates.name() : __boundingCoordinates,
        __datasetGPolygon.name() : __datasetGPolygon,
        __references.name() : __references
    })
    _AttributeMap.update({
        __id.name() : __id,
        __system.name() : __system,
        __scope.name() : __scope
    })
_Namespace_cov.addCategoryObject('typeBinding', u'GeographicCoverage', GeographicCoverage)


# Complex type {eml://ecoinformatics.org/coverage-2.1.0}TaxonomicCoverage with content type ELEMENT_ONLY
class TaxonomicCoverage (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cov, u'TaxonomicCoverage')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1015, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element taxonomicSystem uses Python identifier taxonomicSystem
    __taxonomicSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'taxonomicSystem'), 'taxonomicSystem', '__emlecoinformatics_orgcoverage_2_1_0_TaxonomicCoverage_taxonomicSystem', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1029, 8), )

    
    taxonomicSystem = property(__taxonomicSystem.value, __taxonomicSystem.set, None, u'')

    
    # Element generalTaxonomicCoverage uses Python identifier generalTaxonomicCoverage
    __generalTaxonomicCoverage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'generalTaxonomicCoverage'), 'generalTaxonomicCoverage', '__emlecoinformatics_orgcoverage_2_1_0_TaxonomicCoverage_generalTaxonomicCoverage', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1196, 8), )

    
    generalTaxonomicCoverage = property(__generalTaxonomicCoverage.value, __generalTaxonomicCoverage.set, None, u'')

    
    # Element taxonomicClassification uses Python identifier taxonomicClassification
    __taxonomicClassification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'taxonomicClassification'), 'taxonomicClassification', '__emlecoinformatics_orgcoverage_2_1_0_TaxonomicCoverage_taxonomicClassification', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1210, 8), )

    
    taxonomicClassification = property(__taxonomicClassification.value, __taxonomicClassification.set, None, u'')

    
    # Element references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'references'), 'references', '__emlecoinformatics_orgcoverage_2_1_0_TaxonomicCoverage_references', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6), )

    
    references = property(__references.value, __references.set, None, u'')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__emlecoinformatics_orgcoverage_2_1_0_TaxonomicCoverage_id', IDType)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1224, 4)
    __id._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1224, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __taxonomicSystem.name() : __taxonomicSystem,
        __generalTaxonomicCoverage.name() : __generalTaxonomicCoverage,
        __taxonomicClassification.name() : __taxonomicClassification,
        __references.name() : __references
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_Namespace_cov.addCategoryObject('typeBinding', u'TaxonomicCoverage', TaxonomicCoverage)


# Complex type {eml://ecoinformatics.org/literature-2.1.0}CitationType with content type ELEMENT_ONLY
class CitationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {eml://ecoinformatics.org/literature-2.1.0}CitationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cit, u'CitationType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 97, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'contact'), 'contact', '__emlecoinformatics_orgliterature_2_1_0_CitationType_contact', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 101, 8), )

    
    contact = property(__contact.value, __contact.set, None, u'')

    
    # Element article uses Python identifier article
    __article = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'article'), 'article', '__emlecoinformatics_orgliterature_2_1_0_CitationType_article', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 112, 10), )

    
    article = property(__article.value, __article.set, None, u'')

    
    # Element book uses Python identifier book
    __book = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'book'), 'book', '__emlecoinformatics_orgliterature_2_1_0_CitationType_book', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 124, 10), )

    
    book = property(__book.value, __book.set, None, u'')

    
    # Element chapter uses Python identifier chapter
    __chapter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'chapter'), 'chapter', '__emlecoinformatics_orgliterature_2_1_0_CitationType_chapter', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 135, 10), )

    
    chapter = property(__chapter.value, __chapter.set, None, u'')

    
    # Element editedBook uses Python identifier editedBook
    __editedBook = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'editedBook'), 'editedBook', '__emlecoinformatics_orgliterature_2_1_0_CitationType_editedBook', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 149, 10), )

    
    editedBook = property(__editedBook.value, __editedBook.set, None, u'')

    
    # Element manuscript uses Python identifier manuscript
    __manuscript = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'manuscript'), 'manuscript', '__emlecoinformatics_orgliterature_2_1_0_CitationType_manuscript', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 162, 10), )

    
    manuscript = property(__manuscript.value, __manuscript.set, None, u'')

    
    # Element report uses Python identifier report
    __report = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'report'), 'report', '__emlecoinformatics_orgliterature_2_1_0_CitationType_report', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 173, 10), )

    
    report = property(__report.value, __report.set, None, u'')

    
    # Element thesis uses Python identifier thesis
    __thesis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'thesis'), 'thesis', '__emlecoinformatics_orgliterature_2_1_0_CitationType_thesis', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 186, 10), )

    
    thesis = property(__thesis.value, __thesis.set, None, u'')

    
    # Element conferenceProceedings uses Python identifier conferenceProceedings
    __conferenceProceedings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'conferenceProceedings'), 'conferenceProceedings', '__emlecoinformatics_orgliterature_2_1_0_CitationType_conferenceProceedings', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 200, 10), )

    
    conferenceProceedings = property(__conferenceProceedings.value, __conferenceProceedings.set, None, u'')

    
    # Element personalCommunication uses Python identifier personalCommunication
    __personalCommunication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'personalCommunication'), 'personalCommunication', '__emlecoinformatics_orgliterature_2_1_0_CitationType_personalCommunication', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 211, 10), )

    
    personalCommunication = property(__personalCommunication.value, __personalCommunication.set, None, u'')

    
    # Element map uses Python identifier map
    __map = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'map'), 'map', '__emlecoinformatics_orgliterature_2_1_0_CitationType_map', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 223, 10), )

    
    map = property(__map.value, __map.set, None, u'')

    
    # Element generic uses Python identifier generic
    __generic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'generic'), 'generic', '__emlecoinformatics_orgliterature_2_1_0_CitationType_generic', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 235, 10), )

    
    generic = property(__generic.value, __generic.set, None, u'')

    
    # Element audioVisual uses Python identifier audioVisual
    __audioVisual = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'audioVisual'), 'audioVisual', '__emlecoinformatics_orgliterature_2_1_0_CitationType_audioVisual', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 248, 10), )

    
    audioVisual = property(__audioVisual.value, __audioVisual.set, None, u'')

    
    # Element presentation uses Python identifier presentation
    __presentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'presentation'), 'presentation', '__emlecoinformatics_orgliterature_2_1_0_CitationType_presentation', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 260, 10), )

    
    presentation = property(__presentation.value, __presentation.set, None, u'')

    
    # Element alternateIdentifier uses Python identifier alternateIdentifier
    __alternateIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'alternateIdentifier'), 'alternateIdentifier', '__emlecoinformatics_orgliterature_2_1_0_CitationType_alternateIdentifier', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 91, 6), )

    
    alternateIdentifier = property(__alternateIdentifier.value, __alternateIdentifier.set, None, u'')

    
    # Element shortName uses Python identifier shortName
    __shortName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'shortName'), 'shortName', '__emlecoinformatics_orgliterature_2_1_0_CitationType_shortName', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 112, 6), )

    
    shortName = property(__shortName.value, __shortName.set, None, u'')

    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'title'), 'title', '__emlecoinformatics_orgliterature_2_1_0_CitationType_title', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 126, 6), )

    
    title = property(__title.value, __title.set, None, u'')

    
    # Element creator uses Python identifier creator
    __creator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'creator'), 'creator', '__emlecoinformatics_orgliterature_2_1_0_CitationType_creator', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 144, 6), )

    
    creator = property(__creator.value, __creator.set, None, u'')

    
    # Element metadataProvider uses Python identifier metadataProvider
    __metadataProvider = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'metadataProvider'), 'metadataProvider', '__emlecoinformatics_orgliterature_2_1_0_CitationType_metadataProvider', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 160, 6), )

    
    metadataProvider = property(__metadataProvider.value, __metadataProvider.set, None, u'')

    
    # Element associatedParty uses Python identifier associatedParty
    __associatedParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'associatedParty'), 'associatedParty', '__emlecoinformatics_orgliterature_2_1_0_CitationType_associatedParty', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 174, 6), )

    
    associatedParty = property(__associatedParty.value, __associatedParty.set, None, u'')

    
    # Element pubDate uses Python identifier pubDate
    __pubDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'pubDate'), 'pubDate', '__emlecoinformatics_orgliterature_2_1_0_CitationType_pubDate', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 211, 6), )

    
    pubDate = property(__pubDate.value, __pubDate.set, None, u'')

    
    # Element language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'language'), 'language', '__emlecoinformatics_orgliterature_2_1_0_CitationType_language', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 225, 6), )

    
    language = property(__language.value, __language.set, None, u'')

    
    # Element series uses Python identifier series
    __series = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'series'), 'series', '__emlecoinformatics_orgliterature_2_1_0_CitationType_series', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 238, 6), )

    
    series = property(__series.value, __series.set, None, u'')

    
    # Element abstract uses Python identifier abstract
    __abstract = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'abstract'), 'abstract', '__emlecoinformatics_orgliterature_2_1_0_CitationType_abstract', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 251, 6), )

    
    abstract = property(__abstract.value, __abstract.set, None, u'')

    
    # Element keywordSet uses Python identifier keywordSet
    __keywordSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'keywordSet'), 'keywordSet', '__emlecoinformatics_orgliterature_2_1_0_CitationType_keywordSet', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 262, 6), )

    
    keywordSet = property(__keywordSet.value, __keywordSet.set, None, u'')

    
    # Element additionalInfo uses Python identifier additionalInfo
    __additionalInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'additionalInfo'), 'additionalInfo', '__emlecoinformatics_orgliterature_2_1_0_CitationType_additionalInfo', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 332, 6), )

    
    additionalInfo = property(__additionalInfo.value, __additionalInfo.set, None, u'')

    
    # Element intellectualRights uses Python identifier intellectualRights
    __intellectualRights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'intellectualRights'), 'intellectualRights', '__emlecoinformatics_orgliterature_2_1_0_CitationType_intellectualRights', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 345, 6), )

    
    intellectualRights = property(__intellectualRights.value, __intellectualRights.set, None, u'')

    
    # Element distribution uses Python identifier distribution
    __distribution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'distribution'), 'distribution', '__emlecoinformatics_orgliterature_2_1_0_CitationType_distribution', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 364, 6), )

    
    distribution = property(__distribution.value, __distribution.set, None, u'')

    
    # Element coverage uses Python identifier coverage
    __coverage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'coverage'), 'coverage', '__emlecoinformatics_orgliterature_2_1_0_CitationType_coverage', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 377, 6), )

    
    coverage = property(__coverage.value, __coverage.set, None, u'')

    
    # Element references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'references'), 'references', '__emlecoinformatics_orgliterature_2_1_0_CitationType_references', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6), )

    
    references = property(__references.value, __references.set, None, u'')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__emlecoinformatics_orgliterature_2_1_0_CitationType_id', IDType)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 278, 4)
    __id._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 278, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgliterature_2_1_0_CitationType_system', SystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 279, 4)
    __system._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 279, 4)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scope'), 'scope', '__emlecoinformatics_orgliterature_2_1_0_CitationType_scope', ScopeType, unicode_default=u'document')
    __scope._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 280, 4)
    __scope._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 280, 4)
    
    scope = property(__scope.value, __scope.set, None, None)

    _ElementMap.update({
        __contact.name() : __contact,
        __article.name() : __article,
        __book.name() : __book,
        __chapter.name() : __chapter,
        __editedBook.name() : __editedBook,
        __manuscript.name() : __manuscript,
        __report.name() : __report,
        __thesis.name() : __thesis,
        __conferenceProceedings.name() : __conferenceProceedings,
        __personalCommunication.name() : __personalCommunication,
        __map.name() : __map,
        __generic.name() : __generic,
        __audioVisual.name() : __audioVisual,
        __presentation.name() : __presentation,
        __alternateIdentifier.name() : __alternateIdentifier,
        __shortName.name() : __shortName,
        __title.name() : __title,
        __creator.name() : __creator,
        __metadataProvider.name() : __metadataProvider,
        __associatedParty.name() : __associatedParty,
        __pubDate.name() : __pubDate,
        __language.name() : __language,
        __series.name() : __series,
        __abstract.name() : __abstract,
        __keywordSet.name() : __keywordSet,
        __additionalInfo.name() : __additionalInfo,
        __intellectualRights.name() : __intellectualRights,
        __distribution.name() : __distribution,
        __coverage.name() : __coverage,
        __references.name() : __references
    })
    _AttributeMap.update({
        __id.name() : __id,
        __system.name() : __system,
        __scope.name() : __scope
    })
_Namespace_cit.addCategoryObject('typeBinding', u'CitationType', CitationType)


# Complex type {eml://ecoinformatics.org/literature-2.1.0}Chapter with content type ELEMENT_ONLY
class Chapter (Book):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cit, u'Chapter')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 510, 2)
    _ElementMap = Book._ElementMap.copy()
    _AttributeMap = Book._AttributeMap.copy()
    # Base type is Book
    
    # Element publisher (publisher) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element publicationPlace (publicationPlace) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element edition (edition) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element volume (volume) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element numberOfVolumes (numberOfVolumes) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element totalPages (totalPages) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element totalFigures (totalFigures) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element totalTables (totalTables) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element ISBN (ISBN) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element chapterNumber uses Python identifier chapterNumber
    __chapterNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'chapterNumber'), 'chapterNumber', '__emlecoinformatics_orgliterature_2_1_0_Chapter_chapterNumber', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 526, 10), )

    
    chapterNumber = property(__chapterNumber.value, __chapterNumber.set, None, u'')

    
    # Element editor uses Python identifier editor
    __editor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'editor'), 'editor', '__emlecoinformatics_orgliterature_2_1_0_Chapter_editor', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 538, 10), )

    
    editor = property(__editor.value, __editor.set, None, u'')

    
    # Element bookTitle uses Python identifier bookTitle
    __bookTitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'bookTitle'), 'bookTitle', '__emlecoinformatics_orgliterature_2_1_0_Chapter_bookTitle', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 553, 10), )

    
    bookTitle = property(__bookTitle.value, __bookTitle.set, None, u'')

    
    # Element pageRange uses Python identifier pageRange
    __pageRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'pageRange'), 'pageRange', '__emlecoinformatics_orgliterature_2_1_0_Chapter_pageRange', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 564, 10), )

    
    pageRange = property(__pageRange.value, __pageRange.set, None, u'')

    _ElementMap.update({
        __chapterNumber.name() : __chapterNumber,
        __editor.name() : __editor,
        __bookTitle.name() : __bookTitle,
        __pageRange.name() : __pageRange
    })
    _AttributeMap.update({
        
    })
_Namespace_cit.addCategoryObject('typeBinding', u'Chapter', Chapter)


# Complex type {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty with content type ELEMENT_ONLY
class ResponsibleParty (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_rp, u'ResponsibleParty')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 69, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element individualName uses Python identifier individualName
    __individualName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'individualName'), 'individualName', '__emlecoinformatics_orgparty_2_1_0_ResponsibleParty_individualName', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 107, 10), )

    
    individualName = property(__individualName.value, __individualName.set, None, u'')

    
    # Element organizationName uses Python identifier organizationName
    __organizationName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'organizationName'), 'organizationName', '__emlecoinformatics_orgparty_2_1_0_ResponsibleParty_organizationName', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 141, 10), )

    
    organizationName = property(__organizationName.value, __organizationName.set, None, u'')

    
    # Element positionName uses Python identifier positionName
    __positionName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'positionName'), 'positionName', '__emlecoinformatics_orgparty_2_1_0_ResponsibleParty_positionName', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 176, 10), )

    
    positionName = property(__positionName.value, __positionName.set, None, u'')

    
    # Element address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'address'), 'address', '__emlecoinformatics_orgparty_2_1_0_ResponsibleParty_address', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 210, 8), )

    
    address = property(__address.value, __address.set, None, u'')

    
    # Element phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'phone'), 'phone', '__emlecoinformatics_orgparty_2_1_0_ResponsibleParty_phone', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 223, 8), )

    
    phone = property(__phone.value, __phone.set, None, u'')

    
    # Element electronicMailAddress uses Python identifier electronicMailAddress
    __electronicMailAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'electronicMailAddress'), 'electronicMailAddress', '__emlecoinformatics_orgparty_2_1_0_ResponsibleParty_electronicMailAddress', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 256, 8), )

    
    electronicMailAddress = property(__electronicMailAddress.value, __electronicMailAddress.set, None, u'')

    
    # Element onlineUrl uses Python identifier onlineUrl
    __onlineUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'onlineUrl'), 'onlineUrl', '__emlecoinformatics_orgparty_2_1_0_ResponsibleParty_onlineUrl', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 270, 8), )

    
    onlineUrl = property(__onlineUrl.value, __onlineUrl.set, None, u'')

    
    # Element userId uses Python identifier userId
    __userId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'userId'), 'userId', '__emlecoinformatics_orgparty_2_1_0_ResponsibleParty_userId', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 286, 8), )

    
    userId = property(__userId.value, __userId.set, None, u'')

    
    # Element references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'references'), 'references', '__emlecoinformatics_orgparty_2_1_0_ResponsibleParty_references', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6), )

    
    references = property(__references.value, __references.set, None, u'')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__emlecoinformatics_orgparty_2_1_0_ResponsibleParty_id', IDType)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 330, 4)
    __id._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 330, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgparty_2_1_0_ResponsibleParty_system', SystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 331, 4)
    __system._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 331, 4)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scope'), 'scope', '__emlecoinformatics_orgparty_2_1_0_ResponsibleParty_scope', ScopeType, unicode_default=u'document')
    __scope._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 332, 4)
    __scope._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 332, 4)
    
    scope = property(__scope.value, __scope.set, None, None)

    _ElementMap.update({
        __individualName.name() : __individualName,
        __organizationName.name() : __organizationName,
        __positionName.name() : __positionName,
        __address.name() : __address,
        __phone.name() : __phone,
        __electronicMailAddress.name() : __electronicMailAddress,
        __onlineUrl.name() : __onlineUrl,
        __userId.name() : __userId,
        __references.name() : __references
    })
    _AttributeMap.update({
        __id.name() : __id,
        __system.name() : __system,
        __scope.name() : __scope
    })
_Namespace_rp.addCategoryObject('typeBinding', u'ResponsibleParty', ResponsibleParty)


# Complex type {eml://ecoinformatics.org/party-2.1.0}Address with content type ELEMENT_ONLY
class Address (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_rp, u'Address')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 426, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element deliveryPoint uses Python identifier deliveryPoint
    __deliveryPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'deliveryPoint'), 'deliveryPoint', '__emlecoinformatics_orgparty_2_1_0_Address_deliveryPoint', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 439, 8), )

    
    deliveryPoint = property(__deliveryPoint.value, __deliveryPoint.set, None, u'')

    
    # Element city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'city'), 'city', '__emlecoinformatics_orgparty_2_1_0_Address_city', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 452, 8), )

    
    city = property(__city.value, __city.set, None, u'')

    
    # Element administrativeArea uses Python identifier administrativeArea
    __administrativeArea = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'administrativeArea'), 'administrativeArea', '__emlecoinformatics_orgparty_2_1_0_Address_administrativeArea', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 463, 8), )

    
    administrativeArea = property(__administrativeArea.value, __administrativeArea.set, None, u'')

    
    # Element postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'postalCode'), 'postalCode', '__emlecoinformatics_orgparty_2_1_0_Address_postalCode', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 476, 8), )

    
    postalCode = property(__postalCode.value, __postalCode.set, None, u'')

    
    # Element country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'country'), 'country', '__emlecoinformatics_orgparty_2_1_0_Address_country', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 490, 8), )

    
    country = property(__country.value, __country.set, None, u'')

    
    # Element references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'references'), 'references', '__emlecoinformatics_orgparty_2_1_0_Address_references', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6), )

    
    references = property(__references.value, __references.set, None, u'')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__emlecoinformatics_orgparty_2_1_0_Address_id', IDType)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 505, 4)
    __id._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 505, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgparty_2_1_0_Address_system', SystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 506, 4)
    __system._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 506, 4)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scope'), 'scope', '__emlecoinformatics_orgparty_2_1_0_Address_scope', ScopeType, unicode_default=u'document')
    __scope._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 507, 4)
    __scope._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 507, 4)
    
    scope = property(__scope.value, __scope.set, None, None)

    _ElementMap.update({
        __deliveryPoint.name() : __deliveryPoint,
        __city.name() : __city,
        __administrativeArea.name() : __administrativeArea,
        __postalCode.name() : __postalCode,
        __country.name() : __country,
        __references.name() : __references
    })
    _AttributeMap.update({
        __id.name() : __id,
        __system.name() : __system,
        __scope.name() : __scope
    })
_Namespace_rp.addCategoryObject('typeBinding', u'Address', Address)


# Complex type {eml://ecoinformatics.org/project-2.1.0}ResearchProjectType with content type ELEMENT_ONLY
class ResearchProjectType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_proj, u'ResearchProjectType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 82, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'title'), 'title', '__emlecoinformatics_orgproject_2_1_0_ResearchProjectType_title', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 102, 8), )

    
    title = property(__title.value, __title.set, None, u'')

    
    # Element personnel uses Python identifier personnel
    __personnel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'personnel'), 'personnel', '__emlecoinformatics_orgproject_2_1_0_ResearchProjectType_personnel', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 115, 8), )

    
    personnel = property(__personnel.value, __personnel.set, None, u'')

    
    # Element abstract uses Python identifier abstract
    __abstract = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'abstract'), 'abstract', '__emlecoinformatics_orgproject_2_1_0_ResearchProjectType_abstract', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 168, 8), )

    
    abstract = property(__abstract.value, __abstract.set, None, u'')

    
    # Element funding uses Python identifier funding
    __funding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'funding'), 'funding', '__emlecoinformatics_orgproject_2_1_0_ResearchProjectType_funding', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 178, 8), )

    
    funding = property(__funding.value, __funding.set, None, u'')

    
    # Element studyAreaDescription uses Python identifier studyAreaDescription
    __studyAreaDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'studyAreaDescription'), 'studyAreaDescription', '__emlecoinformatics_orgproject_2_1_0_ResearchProjectType_studyAreaDescription', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 191, 8), )

    
    studyAreaDescription = property(__studyAreaDescription.value, __studyAreaDescription.set, None, u'')

    
    # Element designDescription uses Python identifier designDescription
    __designDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'designDescription'), 'designDescription', '__emlecoinformatics_orgproject_2_1_0_ResearchProjectType_designDescription', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 353, 8), )

    
    designDescription = property(__designDescription.value, __designDescription.set, None, u'')

    
    # Element relatedProject uses Python identifier relatedProject
    __relatedProject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'relatedProject'), 'relatedProject', '__emlecoinformatics_orgproject_2_1_0_ResearchProjectType_relatedProject', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 401, 8), )

    
    relatedProject = property(__relatedProject.value, __relatedProject.set, None, u'')

    
    # Element references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'references'), 'references', '__emlecoinformatics_orgproject_2_1_0_ResearchProjectType_references', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6), )

    
    references = property(__references.value, __references.set, None, u'')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__emlecoinformatics_orgproject_2_1_0_ResearchProjectType_id', IDType)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 417, 4)
    __id._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 417, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgproject_2_1_0_ResearchProjectType_system', SystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 418, 4)
    __system._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 418, 4)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scope'), 'scope', '__emlecoinformatics_orgproject_2_1_0_ResearchProjectType_scope', ScopeType, unicode_default=u'document')
    __scope._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 419, 4)
    __scope._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 419, 4)
    
    scope = property(__scope.value, __scope.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __personnel.name() : __personnel,
        __abstract.name() : __abstract,
        __funding.name() : __funding,
        __studyAreaDescription.name() : __studyAreaDescription,
        __designDescription.name() : __designDescription,
        __relatedProject.name() : __relatedProject,
        __references.name() : __references
    })
    _AttributeMap.update({
        __id.name() : __id,
        __system.name() : __system,
        __scope.name() : __scope
    })
_Namespace_proj.addCategoryObject('typeBinding', u'ResearchProjectType', ResearchProjectType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 104, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgresource_2_1_0_CTD_ANON_3_system', SystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 107, 14)
    __system._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 107, 14)
    
    system = property(__system.value, __system.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __system.name() : __system
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = NonEmptyStringType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 294, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is NonEmptyStringType
    
    # Attribute keywordType uses Python identifier keywordType
    __keywordType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'keywordType'), 'keywordType', '__emlecoinformatics_orgresource_2_1_0_CTD_ANON_4_keywordType', KeyTypeCode)
    __keywordType._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 297, 20)
    __keywordType._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 297, 20)
    
    keywordType = property(__keywordType.value, __keywordType.set, None, u'')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __keywordType.name() : __keywordType
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 430, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgresource_2_1_0_CTD_ANON_5_system', SystemType, unicode_default=u'document')
    __system._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 433, 14)
    __system._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 433, 14)
    
    system = property(__system.value, __system.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __system.name() : __system
    })



# Complex type {eml://ecoinformatics.org/resource-2.1.0}DistributionType with content type ELEMENT_ONLY
class DistributionType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_res, u'DistributionType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 582, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'references'), 'references', '__emlecoinformatics_orgresource_2_1_0_DistributionType_references', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6), )

    
    references = property(__references.value, __references.set, None, u'')

    
    # Element online uses Python identifier online
    __online = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'online'), 'online', '__emlecoinformatics_orgresource_2_1_0_DistributionType_online', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 611, 8), )

    
    online = property(__online.value, __online.set, None, u'')

    
    # Element offline uses Python identifier offline
    __offline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'offline'), 'offline', '__emlecoinformatics_orgresource_2_1_0_DistributionType_offline', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 623, 8), )

    
    offline = property(__offline.value, __offline.set, None, u'')

    
    # Element inline uses Python identifier inline
    __inline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'inline'), 'inline', '__emlecoinformatics_orgresource_2_1_0_DistributionType_inline', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 634, 8), )

    
    inline = property(__inline.value, __inline.set, None, u'')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__emlecoinformatics_orgresource_2_1_0_DistributionType_id', IDType)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 647, 4)
    __id._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 647, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgresource_2_1_0_DistributionType_system', SystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 648, 4)
    __system._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 648, 4)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scope'), 'scope', '__emlecoinformatics_orgresource_2_1_0_DistributionType_scope', ScopeType, unicode_default=u'document')
    __scope._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 649, 4)
    __scope._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 649, 4)
    
    scope = property(__scope.value, __scope.set, None, None)

    _ElementMap.update({
        __references.name() : __references,
        __online.name() : __online,
        __offline.name() : __offline,
        __inline.name() : __inline
    })
    _AttributeMap.update({
        __id.name() : __id,
        __system.name() : __system,
        __scope.name() : __scope
    })
_Namespace_res.addCategoryObject('typeBinding', u'DistributionType', DistributionType)


# Complex type {eml://ecoinformatics.org/resource-2.1.0}ConnectionDefinitionType with content type ELEMENT_ONLY
class ConnectionDefinitionType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_res, u'ConnectionDefinitionType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 651, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'references'), 'references', '__emlecoinformatics_orgresource_2_1_0_ConnectionDefinitionType_references', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6), )

    
    references = property(__references.value, __references.set, None, u'')

    
    # Element schemeName uses Python identifier schemeName
    __schemeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'schemeName'), 'schemeName', '__emlecoinformatics_orgresource_2_1_0_ConnectionDefinitionType_schemeName', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 667, 8), )

    
    schemeName = property(__schemeName.value, __schemeName.set, None, u'')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__emlecoinformatics_orgresource_2_1_0_ConnectionDefinitionType_description', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 712, 8), )

    
    description = property(__description.value, __description.set, None, u'')

    
    # Element parameterDefinition uses Python identifier parameterDefinition
    __parameterDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'parameterDefinition'), 'parameterDefinition', '__emlecoinformatics_orgresource_2_1_0_ConnectionDefinitionType_parameterDefinition', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 740, 8), )

    
    parameterDefinition = property(__parameterDefinition.value, __parameterDefinition.set, None, u'')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__emlecoinformatics_orgresource_2_1_0_ConnectionDefinitionType_id', IDType)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 809, 4)
    __id._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 809, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgresource_2_1_0_ConnectionDefinitionType_system', SystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 810, 4)
    __system._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 810, 4)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scope'), 'scope', '__emlecoinformatics_orgresource_2_1_0_ConnectionDefinitionType_scope', ScopeType, unicode_default=u'document')
    __scope._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 811, 4)
    __scope._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 811, 4)
    
    scope = property(__scope.value, __scope.set, None, None)

    _ElementMap.update({
        __references.name() : __references,
        __schemeName.name() : __schemeName,
        __description.name() : __description,
        __parameterDefinition.name() : __parameterDefinition
    })
    _AttributeMap.update({
        __id.name() : __id,
        __system.name() : __system,
        __scope.name() : __scope
    })
_Namespace_res.addCategoryObject('typeBinding', u'ConnectionDefinitionType', ConnectionDefinitionType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 688, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgresource_2_1_0_CTD_ANON_6_system', SystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 691, 16)
    __system._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 691, 16)
    
    system = property(__system.value, __system.set, None, u'')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __system.name() : __system
    })



# Complex type {eml://ecoinformatics.org/resource-2.1.0}UrlType with content type SIMPLE
class UrlType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_res, u'UrlType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1034, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute function uses Python identifier function
    __function = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'function'), 'function', '__emlecoinformatics_orgresource_2_1_0_UrlType_function', FunctionType, unicode_default=u'download')
    __function._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1062, 8)
    __function._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1062, 8)
    
    function = property(__function.value, __function.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __function.name() : __function
    })
_Namespace_res.addCategoryObject('typeBinding', u'UrlType', UrlType)


# Complex type {eml://ecoinformatics.org/resource-2.1.0}ConnectionType with content type ELEMENT_ONLY
class ConnectionType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_res, u'ConnectionType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1069, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'references'), 'references', '__emlecoinformatics_orgresource_2_1_0_ConnectionType_references', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6), )

    
    references = property(__references.value, __references.set, None, u'')

    
    # Element connectionDefinition uses Python identifier connectionDefinition
    __connectionDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'connectionDefinition'), 'connectionDefinition', '__emlecoinformatics_orgresource_2_1_0_ConnectionType_connectionDefinition', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1098, 8), )

    
    connectionDefinition = property(__connectionDefinition.value, __connectionDefinition.set, None, u'')

    
    # Element parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'parameter'), 'parameter', '__emlecoinformatics_orgresource_2_1_0_ConnectionType_parameter', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1107, 8), )

    
    parameter = property(__parameter.value, __parameter.set, None, u'')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__emlecoinformatics_orgresource_2_1_0_ConnectionType_id', IDType)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1157, 4)
    __id._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1157, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgresource_2_1_0_ConnectionType_system', SystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1158, 4)
    __system._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1158, 4)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scope'), 'scope', '__emlecoinformatics_orgresource_2_1_0_ConnectionType_scope', ScopeType, unicode_default=u'document')
    __scope._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1159, 4)
    __scope._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1159, 4)
    
    scope = property(__scope.value, __scope.set, None, None)

    _ElementMap.update({
        __references.name() : __references,
        __connectionDefinition.name() : __connectionDefinition,
        __parameter.name() : __parameter
    })
    _AttributeMap.update({
        __id.name() : __id,
        __system.name() : __system,
        __scope.name() : __scope
    })
_Namespace_res.addCategoryObject('typeBinding', u'ConnectionType', ConnectionType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23 (TemporalCoverage):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 159, 10)
    _ElementMap = TemporalCoverage._ElementMap.copy()
    _AttributeMap = TemporalCoverage._AttributeMap.copy()
    # Base type is TemporalCoverage
    
    # Element singleDateTime (singleDateTime) inherited from {eml://ecoinformatics.org/coverage-2.1.0}TemporalCoverage
    
    # Element rangeOfDates (rangeOfDates) inherited from {eml://ecoinformatics.org/coverage-2.1.0}TemporalCoverage
    
    # Element references (references) inherited from {eml://ecoinformatics.org/coverage-2.1.0}TemporalCoverage
    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_11_system', SystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 162, 16)
    __system._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 162, 16)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scope'), 'scope', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_11_scope', ScopeType, unicode_default=u'document')
    __scope._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 163, 16)
    __scope._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 163, 16)
    
    scope = property(__scope.value, __scope.set, None, None)

    
    # Attribute id inherited from {eml://ecoinformatics.org/coverage-2.1.0}TemporalCoverage
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __system.name() : __system,
        __scope.name() : __scope
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24 (TaxonomicCoverage):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 181, 10)
    _ElementMap = TaxonomicCoverage._ElementMap.copy()
    _AttributeMap = TaxonomicCoverage._AttributeMap.copy()
    # Base type is TaxonomicCoverage
    
    # Element taxonomicSystem (taxonomicSystem) inherited from {eml://ecoinformatics.org/coverage-2.1.0}TaxonomicCoverage
    
    # Element generalTaxonomicCoverage (generalTaxonomicCoverage) inherited from {eml://ecoinformatics.org/coverage-2.1.0}TaxonomicCoverage
    
    # Element taxonomicClassification (taxonomicClassification) inherited from {eml://ecoinformatics.org/coverage-2.1.0}TaxonomicCoverage
    
    # Element references (references) inherited from {eml://ecoinformatics.org/coverage-2.1.0}TaxonomicCoverage
    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system'), 'system', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_12_system', SystemType)
    __system._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 184, 16)
    __system._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 184, 16)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scope'), 'scope', '__emlecoinformatics_orgcoverage_2_1_0_CTD_ANON_12_scope', ScopeType, unicode_default=u'document')
    __scope._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 185, 16)
    __scope._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 185, 16)
    
    scope = property(__scope.value, __scope.set, None, None)

    
    # Attribute id inherited from {eml://ecoinformatics.org/coverage-2.1.0}TaxonomicCoverage
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __system.name() : __system,
        __scope.name() : __scope
    })



# Complex type {eml://ecoinformatics.org/literature-2.1.0}ConferenceProceedings with content type ELEMENT_ONLY
class ConferenceProceedings (Chapter):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cit, u'ConferenceProceedings')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 581, 2)
    _ElementMap = Chapter._ElementMap.copy()
    _AttributeMap = Chapter._AttributeMap.copy()
    # Base type is Chapter
    
    # Element publisher (publisher) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element publicationPlace (publicationPlace) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element edition (edition) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element volume (volume) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element numberOfVolumes (numberOfVolumes) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element totalPages (totalPages) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element totalFigures (totalFigures) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element totalTables (totalTables) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element ISBN (ISBN) inherited from {eml://ecoinformatics.org/literature-2.1.0}Book
    
    # Element chapterNumber (chapterNumber) inherited from {eml://ecoinformatics.org/literature-2.1.0}Chapter
    
    # Element editor (editor) inherited from {eml://ecoinformatics.org/literature-2.1.0}Chapter
    
    # Element bookTitle (bookTitle) inherited from {eml://ecoinformatics.org/literature-2.1.0}Chapter
    
    # Element pageRange (pageRange) inherited from {eml://ecoinformatics.org/literature-2.1.0}Chapter
    
    # Element conferenceName uses Python identifier conferenceName
    __conferenceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'conferenceName'), 'conferenceName', '__emlecoinformatics_orgliterature_2_1_0_ConferenceProceedings_conferenceName', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 594, 10), )

    
    conferenceName = property(__conferenceName.value, __conferenceName.set, None, u'')

    
    # Element conferenceDate uses Python identifier conferenceDate
    __conferenceDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'conferenceDate'), 'conferenceDate', '__emlecoinformatics_orgliterature_2_1_0_ConferenceProceedings_conferenceDate', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 606, 10), )

    
    conferenceDate = property(__conferenceDate.value, __conferenceDate.set, None, u'')

    
    # Element conferenceLocation uses Python identifier conferenceLocation
    __conferenceLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'conferenceLocation'), 'conferenceLocation', '__emlecoinformatics_orgliterature_2_1_0_ConferenceProceedings_conferenceLocation', False, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 617, 10), )

    
    conferenceLocation = property(__conferenceLocation.value, __conferenceLocation.set, None, u'')

    _ElementMap.update({
        __conferenceName.name() : __conferenceName,
        __conferenceDate.name() : __conferenceDate,
        __conferenceLocation.name() : __conferenceLocation
    })
    _AttributeMap.update({
        
    })
_Namespace_cit.addCategoryObject('typeBinding', u'ConferenceProceedings', ConferenceProceedings)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (ResponsibleParty):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 129, 10)
    _ElementMap = ResponsibleParty._ElementMap.copy()
    _AttributeMap = ResponsibleParty._AttributeMap.copy()
    # Base type is ResponsibleParty
    
    # Element individualName (individualName) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element organizationName (organizationName) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element positionName (positionName) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element address (address) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element phone (phone) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element electronicMailAddress (electronicMailAddress) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element onlineUrl (onlineUrl) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element userId (userId) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element references (references) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element role uses Python identifier role
    __role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'role'), 'role', '__emlecoinformatics_orgproject_2_1_0_CTD_ANON_3_role', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 133, 18), )

    
    role = property(__role.value, __role.set, None, u'')

    
    # Attribute id inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Attribute system inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Attribute scope inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    _ElementMap.update({
        __role.name() : __role
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 226, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element descriptorValue uses Python identifier descriptorValue
    __descriptorValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'descriptorValue'), 'descriptorValue', '__emlecoinformatics_orgproject_2_1_0_CTD_ANON_4_descriptorValue', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 228, 20), )

    
    descriptorValue = property(__descriptorValue.value, __descriptorValue.set, None, u'')

    
    # Element citation uses Python identifier citation
    __citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'citation'), 'citation', '__emlecoinformatics_orgproject_2_1_0_CTD_ANON_4_citation', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 288, 20), )

    
    citation = property(__citation.value, __citation.set, None, u'')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__emlecoinformatics_orgproject_2_1_0_CTD_ANON_4_name', DescriptorType, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 300, 18)
    __name._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 300, 18)
    
    name = property(__name.value, __name.set, None, u'')

    
    # Attribute citableClassificationSystem uses Python identifier citableClassificationSystem
    __citableClassificationSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'citableClassificationSystem'), 'citableClassificationSystem', '__emlecoinformatics_orgproject_2_1_0_CTD_ANON_4_citableClassificationSystem', pyxb.binding.datatypes.boolean, required=True)
    __citableClassificationSystem._DeclarationLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 313, 18)
    __citableClassificationSystem._UseLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 313, 18)
    
    citableClassificationSystem = property(__citableClassificationSystem.value, __citableClassificationSystem.set, None, u'')

    _ElementMap.update({
        __descriptorValue.name() : __descriptorValue,
        __citation.name() : __citation
    })
    _AttributeMap.update({
        __name.name() : __name,
        __citableClassificationSystem.name() : __citableClassificationSystem
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (ResponsibleParty):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 188, 8)
    _ElementMap = ResponsibleParty._ElementMap.copy()
    _AttributeMap = ResponsibleParty._AttributeMap.copy()
    # Base type is ResponsibleParty
    
    # Element individualName (individualName) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element organizationName (organizationName) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element positionName (positionName) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element address (address) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element phone (phone) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element electronicMailAddress (electronicMailAddress) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element onlineUrl (onlineUrl) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element userId (userId) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element references (references) inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Element role uses Python identifier role
    __role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'role'), 'role', '__emlecoinformatics_orgresource_2_1_0_CTD_ANON_7_role', True, pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 192, 16), )

    
    role = property(__role.value, __role.set, None, u'')

    
    # Attribute id inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Attribute system inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    
    # Attribute scope inherited from {eml://ecoinformatics.org/party-2.1.0}ResponsibleParty
    _ElementMap.update({
        __role.name() : __role
    })
    _AttributeMap.update({
        
    })



access = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_acc, u'access'), AccessType, documentation=u'', location=pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 193, 2))
_Namespace_acc.addCategoryObject('elementBinding', access.name().localName(), access)

citation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cit, u'citation'), CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 81, 2))
_Namespace_cit.addCategoryObject('elementBinding', citation.name().localName(), citation)

party = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_rp, u'party'), ResponsibleParty, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 509, 2))
_Namespace_rp.addCategoryObject('elementBinding', party.name().localName(), party)

researchProject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_proj, u'researchProject'), ResearchProjectType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 70, 2))
_Namespace_proj.addCategoryObject('elementBinding', researchProject.name().localName(), researchProject)



AccessRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'principal'), NonEmptyStringType, scope=AccessRule, documentation=u'', location=pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 316, 6)))

AccessRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'permission'), STD_ANON_13, scope=AccessRule, documentation=u'', location=pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 334, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AccessRule._UseForTag(pyxb.namespace.ExpandedName(None, u'principal')), pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 316, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AccessRule._UseForTag(pyxb.namespace.ExpandedName(None, u'permission')), pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 334, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AccessRule._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'beginDate'), SingleDateTimeType, scope=CTD_ANON, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 245, 14)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'endDate'), SingleDateTimeType, scope=CTD_ANON, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 260, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'beginDate')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 245, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'endDate')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 260, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




SingleDateTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'calendarDate'), yearDate, scope=SingleDateTimeType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 298, 8)))

SingleDateTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'time'), pyxb.binding.datatypes.time, scope=SingleDateTimeType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 318, 8)))

SingleDateTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'alternativeTimeScale'), CTD_ANON_, scope=SingleDateTimeType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 348, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 318, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SingleDateTimeType._UseForTag(pyxb.namespace.ExpandedName(None, u'calendarDate')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 298, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SingleDateTimeType._UseForTag(pyxb.namespace.ExpandedName(None, u'time')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 318, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SingleDateTimeType._UseForTag(pyxb.namespace.ExpandedName(None, u'alternativeTimeScale')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 348, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SingleDateTimeType._Automaton = _BuildAutomaton_2()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'timeScaleName'), NonEmptyStringType, scope=CTD_ANON_, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 381, 12)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'timeScaleAgeEstimate'), NonEmptyStringType, scope=CTD_ANON_, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 398, 12)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'timeScaleAgeUncertainty'), NonEmptyStringType, scope=CTD_ANON_, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 423, 12)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'timeScaleAgeExplanation'), NonEmptyStringType, scope=CTD_ANON_, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 437, 12)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'timeScaleCitation'), CitationType, scope=CTD_ANON_, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 450, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 423, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 437, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 450, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'timeScaleName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 381, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'timeScaleAgeEstimate')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 398, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'timeScaleAgeUncertainty')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 423, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'timeScaleAgeExplanation')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 437, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'timeScaleCitation')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 450, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_3()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'westBoundingCoordinate'), STD_ANON_3, scope=CTD_ANON_2, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 575, 14)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'eastBoundingCoordinate'), STD_ANON_4, scope=CTD_ANON_2, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 607, 14)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'northBoundingCoordinate'), STD_ANON_5, scope=CTD_ANON_2, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 639, 14)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'southBoundingCoordinate'), STD_ANON_6, scope=CTD_ANON_2, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 667, 14)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'boundingAltitudes'), CTD_ANON_3, scope=CTD_ANON_2, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 695, 14)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 695, 14))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'westBoundingCoordinate')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 575, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'eastBoundingCoordinate')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 607, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'northBoundingCoordinate')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 639, 14))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'southBoundingCoordinate')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 667, 14))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'boundingAltitudes')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 695, 14))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_4()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'altitudeMinimum'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_3, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 713, 20)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'altitudeMaximum'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_3, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 728, 20)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'altitudeUnits'), _ImportedBinding__unit.LengthUnitType, scope=CTD_ANON_3, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 743, 20)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'altitudeMinimum')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 713, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'altitudeMaximum')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 728, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'altitudeUnits')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 743, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_5()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'datasetGPolygonOuterGRing'), CTD_ANON_5, scope=CTD_ANON_4, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 777, 14)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'datasetGPolygonExclusionGRing'), CTD_ANON_6, scope=CTD_ANON_4, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 837, 14)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 837, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, u'datasetGPolygonOuterGRing')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 777, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, u'datasetGPolygonExclusionGRing')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 837, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_6()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'gRingPoint'), GRingPointType, scope=CTD_ANON_5, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 811, 22)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'gRing'), GRingType, scope=CTD_ANON_5, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 822, 20)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 811, 22))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, u'gRingPoint')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 811, 22))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, u'gRing')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 822, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_7()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'gRingPoint'), GRingPointType, scope=CTD_ANON_6, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 869, 20)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'gRing'), GRingType, scope=CTD_ANON_6, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 881, 20)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, u'gRingPoint')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 869, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, u'gRing')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 881, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_8()




GRingPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'gRingLatitude'), STD_ANON_7, scope=GRingPointType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 916, 6)))

GRingPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'gRingLongitude'), STD_ANON_8, scope=GRingPointType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 942, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GRingPointType._UseForTag(pyxb.namespace.ExpandedName(None, u'gRingLatitude')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 916, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GRingPointType._UseForTag(pyxb.namespace.ExpandedName(None, u'gRingLongitude')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 942, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GRingPointType._Automaton = _BuildAutomaton_9()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'classificationSystem'), CTD_ANON_8, scope=CTD_ANON_7, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1041, 14)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'identificationReference'), CitationType, scope=CTD_ANON_7, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1079, 14)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'identifierName'), ResponsibleParty, scope=CTD_ANON_7, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1090, 14)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'taxonomicProcedures'), NonEmptyStringType, scope=CTD_ANON_7, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1101, 14)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'taxonomicCompleteness'), NonEmptyStringType, scope=CTD_ANON_7, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1114, 14)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'vouchers'), CTD_ANON_9, scope=CTD_ANON_7, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1130, 14)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1079, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1114, 14))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1130, 14))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, u'classificationSystem')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1041, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, u'identificationReference')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1079, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, u'identifierName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1090, 14))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, u'taxonomicProcedures')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1101, 14))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, u'taxonomicCompleteness')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1114, 14))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, u'vouchers')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1130, 14))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_10()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'classificationSystemCitation'), CitationType, scope=CTD_ANON_8, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1054, 20)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'classificationSystemModifications'), NonEmptyStringType, scope=CTD_ANON_8, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1064, 20)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1064, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, u'classificationSystemCitation')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1054, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, u'classificationSystemModifications')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1064, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_11()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'specimen'), NonEmptyStringType, scope=CTD_ANON_9, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1142, 20)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'repository'), CTD_ANON_10, scope=CTD_ANON_9, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1154, 20)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, u'specimen')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1142, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, u'repository')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1154, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_12()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'originator'), ResponsibleParty, scope=CTD_ANON_10, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1167, 26)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, u'originator')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1167, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_13()




TaxonomicClassificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'taxonRankName'), NonEmptyStringType, scope=TaxonomicClassificationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1248, 6)))

TaxonomicClassificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'taxonRankValue'), NonEmptyStringType, scope=TaxonomicClassificationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1262, 6)))

TaxonomicClassificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'commonName'), NonEmptyStringType, scope=TaxonomicClassificationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1283, 6)))

TaxonomicClassificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'taxonomicClassification'), TaxonomicClassificationType, scope=TaxonomicClassificationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1297, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1248, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1262, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1283, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1297, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TaxonomicClassificationType._UseForTag(pyxb.namespace.ExpandedName(None, u'taxonRankName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1248, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TaxonomicClassificationType._UseForTag(pyxb.namespace.ExpandedName(None, u'taxonRankValue')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1262, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TaxonomicClassificationType._UseForTag(pyxb.namespace.ExpandedName(None, u'commonName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1283, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TaxonomicClassificationType._UseForTag(pyxb.namespace.ExpandedName(None, u'taxonomicClassification')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1297, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TaxonomicClassificationType._Automaton = _BuildAutomaton_14()




Article._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'journal'), NonEmptyStringType, scope=Article, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 294, 6)))

Article._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'volume'), NonEmptyStringType, scope=Article, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 308, 6)))

Article._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'issue'), NonEmptyStringType, scope=Article, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 320, 6)))

Article._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'pageRange'), NonEmptyStringType, scope=Article, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 332, 6)))

Article._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'publisher'), ResponsibleParty, scope=Article, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 345, 6)))

Article._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'publicationPlace'), NonEmptyStringType, scope=Article, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 358, 6)))

Article._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ISSN'), NonEmptyStringType, scope=Article, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 372, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 308, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 320, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 332, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 345, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 358, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 372, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Article._UseForTag(pyxb.namespace.ExpandedName(None, u'journal')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 294, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Article._UseForTag(pyxb.namespace.ExpandedName(None, u'volume')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 308, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Article._UseForTag(pyxb.namespace.ExpandedName(None, u'issue')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 320, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Article._UseForTag(pyxb.namespace.ExpandedName(None, u'pageRange')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 332, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Article._UseForTag(pyxb.namespace.ExpandedName(None, u'publisher')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 345, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Article._UseForTag(pyxb.namespace.ExpandedName(None, u'publicationPlace')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 358, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Article._UseForTag(pyxb.namespace.ExpandedName(None, u'ISSN')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 372, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Article._Automaton = _BuildAutomaton_15()




Book._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'publisher'), ResponsibleParty, scope=Book, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 397, 6)))

Book._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'publicationPlace'), NonEmptyStringType, scope=Book, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 410, 6)))

Book._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'edition'), NonEmptyStringType, scope=Book, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 424, 6)))

Book._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'volume'), NonEmptyStringType, scope=Book, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 435, 6)))

Book._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'numberOfVolumes'), NonEmptyStringType, scope=Book, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 448, 6)))

Book._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'totalPages'), NonEmptyStringType, scope=Book, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 459, 6)))

Book._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'totalFigures'), NonEmptyStringType, scope=Book, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 471, 6)))

Book._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'totalTables'), NonEmptyStringType, scope=Book, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 483, 6)))

Book._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ISBN'), NonEmptyStringType, scope=Book, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 495, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 410, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 424, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 435, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 448, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 459, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 471, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 483, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 495, 6))
    counters.add(cc_7)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Book._UseForTag(pyxb.namespace.ExpandedName(None, u'publisher')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 397, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Book._UseForTag(pyxb.namespace.ExpandedName(None, u'publicationPlace')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 410, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Book._UseForTag(pyxb.namespace.ExpandedName(None, u'edition')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 424, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Book._UseForTag(pyxb.namespace.ExpandedName(None, u'volume')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 435, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Book._UseForTag(pyxb.namespace.ExpandedName(None, u'numberOfVolumes')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 448, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Book._UseForTag(pyxb.namespace.ExpandedName(None, u'totalPages')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 459, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Book._UseForTag(pyxb.namespace.ExpandedName(None, u'totalFigures')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 471, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Book._UseForTag(pyxb.namespace.ExpandedName(None, u'totalTables')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 483, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Book._UseForTag(pyxb.namespace.ExpandedName(None, u'ISBN')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 495, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Book._Automaton = _BuildAutomaton_16()




Manuscript._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'institution'), ResponsibleParty, scope=Manuscript, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 642, 6)))

Manuscript._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'totalPages'), NonEmptyStringType, scope=Manuscript, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 656, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 656, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Manuscript._UseForTag(pyxb.namespace.ExpandedName(None, u'institution')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 642, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Manuscript._UseForTag(pyxb.namespace.ExpandedName(None, u'totalPages')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 656, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Manuscript._Automaton = _BuildAutomaton_17()




Report._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reportNumber'), NonEmptyStringType, scope=Report, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 683, 6)))

Report._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'publisher'), ResponsibleParty, scope=Report, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 696, 6)))

Report._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'publicationPlace'), NonEmptyStringType, scope=Report, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 709, 6)))

Report._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'totalPages'), NonEmptyStringType, scope=Report, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 723, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 683, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 696, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 709, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 723, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Report._UseForTag(pyxb.namespace.ExpandedName(None, u'reportNumber')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 683, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Report._UseForTag(pyxb.namespace.ExpandedName(None, u'publisher')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 696, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Report._UseForTag(pyxb.namespace.ExpandedName(None, u'publicationPlace')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 709, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Report._UseForTag(pyxb.namespace.ExpandedName(None, u'totalPages')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 723, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Report._Automaton = _BuildAutomaton_18()




PersonalCommunication._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'publisher'), ResponsibleParty, scope=PersonalCommunication, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 748, 6)))

PersonalCommunication._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'publicationPlace'), NonEmptyStringType, scope=PersonalCommunication, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 761, 6)))

PersonalCommunication._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'communicationType'), NonEmptyStringType, scope=PersonalCommunication, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 775, 6)))

PersonalCommunication._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'recipient'), ResponsibleParty, scope=PersonalCommunication, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 789, 6)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 748, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 761, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 775, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 789, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PersonalCommunication._UseForTag(pyxb.namespace.ExpandedName(None, u'publisher')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 748, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PersonalCommunication._UseForTag(pyxb.namespace.ExpandedName(None, u'publicationPlace')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 761, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PersonalCommunication._UseForTag(pyxb.namespace.ExpandedName(None, u'communicationType')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 775, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(PersonalCommunication._UseForTag(pyxb.namespace.ExpandedName(None, u'recipient')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 789, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PersonalCommunication._Automaton = _BuildAutomaton_19()




Map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'publisher'), ResponsibleParty, scope=Map, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 815, 6)))

Map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'edition'), NonEmptyStringType, scope=Map, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 827, 6)))

Map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'geographicCoverage'), GeographicCoverage, scope=Map, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 838, 6)))

Map._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'scale'), NonEmptyStringType, scope=Map, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 850, 6)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 815, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 827, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 838, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 850, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Map._UseForTag(pyxb.namespace.ExpandedName(None, u'publisher')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 815, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Map._UseForTag(pyxb.namespace.ExpandedName(None, u'edition')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 827, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Map._UseForTag(pyxb.namespace.ExpandedName(None, u'geographicCoverage')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 838, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Map._UseForTag(pyxb.namespace.ExpandedName(None, u'scale')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 850, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Map._Automaton = _BuildAutomaton_20()




AudioVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'publisher'), ResponsibleParty, scope=AudioVisual, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 874, 6)))

AudioVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'publicationPlace'), NonEmptyStringType, scope=AudioVisual, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 888, 6)))

AudioVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'performer'), ResponsibleParty, scope=AudioVisual, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 902, 6)))

AudioVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ISBN'), NonEmptyStringType, scope=AudioVisual, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 915, 6)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 888, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 902, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 915, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AudioVisual._UseForTag(pyxb.namespace.ExpandedName(None, u'publisher')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 874, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AudioVisual._UseForTag(pyxb.namespace.ExpandedName(None, u'publicationPlace')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 888, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AudioVisual._UseForTag(pyxb.namespace.ExpandedName(None, u'performer')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 902, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AudioVisual._UseForTag(pyxb.namespace.ExpandedName(None, u'ISBN')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 915, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AudioVisual._Automaton = _BuildAutomaton_21()




Generic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'publisher'), ResponsibleParty, scope=Generic, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 932, 6)))

Generic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'publicationPlace'), NonEmptyStringType, scope=Generic, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 945, 6)))

Generic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'referenceType'), pyxb.binding.datatypes.anyType, scope=Generic, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 959, 6)))

Generic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'volume'), NonEmptyStringType, scope=Generic, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 972, 6)))

Generic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'numberOfVolumes'), NonEmptyStringType, scope=Generic, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 985, 6)))

Generic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'totalPages'), NonEmptyStringType, scope=Generic, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 996, 6)))

Generic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'totalFigures'), NonEmptyStringType, scope=Generic, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1009, 6)))

Generic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'totalTables'), NonEmptyStringType, scope=Generic, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1022, 6)))

Generic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'edition'), NonEmptyStringType, scope=Generic, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1035, 6)))

Generic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'originalPublication'), NonEmptyStringType, scope=Generic, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1048, 6)))

Generic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reprintEdition'), NonEmptyStringType, scope=Generic, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1061, 6)))

Generic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reviewedItem'), NonEmptyStringType, scope=Generic, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1074, 6)))

Generic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ISBN'), NonEmptyStringType, scope=Generic, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1090, 8)))

Generic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ISSN'), NonEmptyStringType, scope=Generic, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1103, 8)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 945, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 959, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 972, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 985, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 996, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1009, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1022, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1035, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1048, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1061, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1074, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1089, 6))
    counters.add(cc_11)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Generic._UseForTag(pyxb.namespace.ExpandedName(None, u'publisher')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 932, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Generic._UseForTag(pyxb.namespace.ExpandedName(None, u'publicationPlace')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 945, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Generic._UseForTag(pyxb.namespace.ExpandedName(None, u'referenceType')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 959, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Generic._UseForTag(pyxb.namespace.ExpandedName(None, u'volume')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 972, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Generic._UseForTag(pyxb.namespace.ExpandedName(None, u'numberOfVolumes')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 985, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Generic._UseForTag(pyxb.namespace.ExpandedName(None, u'totalPages')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 996, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Generic._UseForTag(pyxb.namespace.ExpandedName(None, u'totalFigures')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1009, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Generic._UseForTag(pyxb.namespace.ExpandedName(None, u'totalTables')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1022, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Generic._UseForTag(pyxb.namespace.ExpandedName(None, u'edition')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1035, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Generic._UseForTag(pyxb.namespace.ExpandedName(None, u'originalPublication')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1048, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Generic._UseForTag(pyxb.namespace.ExpandedName(None, u'reprintEdition')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1061, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Generic._UseForTag(pyxb.namespace.ExpandedName(None, u'reviewedItem')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1074, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Generic._UseForTag(pyxb.namespace.ExpandedName(None, u'ISBN')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1090, 8))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Generic._UseForTag(pyxb.namespace.ExpandedName(None, u'ISSN')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1103, 8))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Generic._Automaton = _BuildAutomaton_22()




Thesis._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'degree'), NonEmptyStringType, scope=Thesis, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1132, 6)))

Thesis._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'institution'), ResponsibleParty, scope=Thesis, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1146, 6)))

Thesis._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'totalPages'), NonEmptyStringType, scope=Thesis, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1159, 6)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1159, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Thesis._UseForTag(pyxb.namespace.ExpandedName(None, u'degree')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1132, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Thesis._UseForTag(pyxb.namespace.ExpandedName(None, u'institution')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1146, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Thesis._UseForTag(pyxb.namespace.ExpandedName(None, u'totalPages')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1159, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Thesis._Automaton = _BuildAutomaton_23()




Presentation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'conferenceName'), NonEmptyStringType, scope=Presentation, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1187, 6)))

Presentation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'conferenceDate'), NonEmptyStringType, scope=Presentation, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1199, 6)))

Presentation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'conferenceLocation'), Address, scope=Presentation, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1210, 6)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1187, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1199, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1210, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Presentation._UseForTag(pyxb.namespace.ExpandedName(None, u'conferenceName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1187, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Presentation._UseForTag(pyxb.namespace.ExpandedName(None, u'conferenceDate')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1199, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Presentation._UseForTag(pyxb.namespace.ExpandedName(None, u'conferenceLocation')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 1210, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Presentation._Automaton = _BuildAutomaton_24()




Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'salutation'), NonEmptyStringType, scope=Person, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 378, 6)))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'givenName'), NonEmptyStringType, scope=Person, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 391, 6)))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'surName'), NonEmptyStringType, scope=Person, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 409, 6)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 378, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 391, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(None, u'salutation')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 378, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(None, u'givenName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 391, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Person._UseForTag(pyxb.namespace.ExpandedName(None, u'surName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 409, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Person._Automaton = _BuildAutomaton_25()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'descriptor'), CTD_ANON_26, scope=CTD_ANON_13, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 210, 14)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'citation'), CitationType, scope=CTD_ANON_13, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 329, 14)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'coverage'), Coverage, scope=CTD_ANON_13, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 340, 14)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 329, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 340, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, u'descriptor')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 210, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, u'citation')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 329, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, u'coverage')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 340, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_26()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), _ImportedBinding__txt.TextType, scope=CTD_ANON_15, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 369, 14)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'citation'), CitationType, scope=CTD_ANON_15, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 384, 14)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 384, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 369, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, u'citation')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 384, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_27()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'keyword'), CTD_ANON_20, scope=CTD_ANON_16, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 280, 12)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'keywordThesaurus'), NonEmptyStringType, scope=CTD_ANON_16, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 316, 12)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 316, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, u'keyword')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 280, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, u'keywordThesaurus')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 316, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_28()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), NonEmptyStringType, scope=CTD_ANON_17, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 756, 14)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'definition'), NonEmptyStringType, scope=CTD_ANON_17, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 768, 14)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'defaultValue'), NonEmptyStringType, scope=CTD_ANON_17, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 784, 14)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 784, 14))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 756, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'definition')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 768, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'defaultValue')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 784, 14))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_29()




def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 838, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 838, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InlineType._Automaton = _BuildAutomaton_30()




OfflineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'mediumName'), NonEmptyStringType, scope=OfflineType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 856, 6)))

OfflineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'mediumDensity'), NonEmptyStringType, scope=OfflineType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 871, 6)))

OfflineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'mediumDensityUnits'), NonEmptyStringType, scope=OfflineType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 885, 6)))

OfflineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'mediumVolume'), NonEmptyStringType, scope=OfflineType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 896, 6)))

OfflineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'mediumFormat'), NonEmptyStringType, scope=OfflineType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 908, 6)))

OfflineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'mediumNote'), NonEmptyStringType, scope=OfflineType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 920, 6)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 871, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 885, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 896, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 908, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 920, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OfflineType._UseForTag(pyxb.namespace.ExpandedName(None, u'mediumName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 856, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OfflineType._UseForTag(pyxb.namespace.ExpandedName(None, u'mediumDensity')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 871, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(OfflineType._UseForTag(pyxb.namespace.ExpandedName(None, u'mediumDensityUnits')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 885, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(OfflineType._UseForTag(pyxb.namespace.ExpandedName(None, u'mediumVolume')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 896, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(OfflineType._UseForTag(pyxb.namespace.ExpandedName(None, u'mediumFormat')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 908, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(OfflineType._UseForTag(pyxb.namespace.ExpandedName(None, u'mediumNote')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 920, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OfflineType._Automaton = _BuildAutomaton_31()




OnlineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'onlineDescription'), NonEmptyStringType, scope=OnlineType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 962, 6)))

OnlineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'url'), UrlType, scope=OnlineType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 975, 8)))

OnlineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'connection'), ConnectionType, scope=OnlineType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 989, 8)))

OnlineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'connectionDefinition'), ConnectionDefinitionType, scope=OnlineType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1001, 8)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 962, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OnlineType._UseForTag(pyxb.namespace.ExpandedName(None, u'onlineDescription')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 962, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OnlineType._UseForTag(pyxb.namespace.ExpandedName(None, u'url')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 975, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OnlineType._UseForTag(pyxb.namespace.ExpandedName(None, u'connection')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 989, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OnlineType._UseForTag(pyxb.namespace.ExpandedName(None, u'connectionDefinition')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1001, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OnlineType._Automaton = _BuildAutomaton_32()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), NonEmptyStringType, scope=CTD_ANON_18, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1122, 14)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'value'), NonEmptyStringType, scope=CTD_ANON_18, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1135, 14)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1122, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, u'value')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1135, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_33()




AccessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'allow'), AccessRule, scope=AccessType, documentation=u'', location=pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 228, 8)))

AccessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'deny'), AccessRule, scope=AccessType, documentation=u'', location=pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 240, 8)))

AccessType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'references'), CTD_ANON_21, scope=AccessType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AccessType._UseForTag(pyxb.namespace.ExpandedName(None, u'allow')), pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 228, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AccessType._UseForTag(pyxb.namespace.ExpandedName(None, u'deny')), pyxb.utils.utility.Location('/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-access.xsd', 240, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AccessType._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AccessType._Automaton = _BuildAutomaton_34()




Coverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'geographicCoverage'), GeographicCoverage, scope=Coverage, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 131, 8)))

Coverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'temporalCoverage'), CTD_ANON_23, scope=Coverage, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 146, 8)))

Coverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'taxonomicCoverage'), CTD_ANON_24, scope=Coverage, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 168, 8)))

Coverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'references'), CTD_ANON_21, scope=Coverage, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Coverage._UseForTag(pyxb.namespace.ExpandedName(None, u'geographicCoverage')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 131, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Coverage._UseForTag(pyxb.namespace.ExpandedName(None, u'temporalCoverage')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 146, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Coverage._UseForTag(pyxb.namespace.ExpandedName(None, u'taxonomicCoverage')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 168, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Coverage._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Coverage._Automaton = _BuildAutomaton_35()




TemporalCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'singleDateTime'), SingleDateTimeType, scope=TemporalCoverage, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 212, 8)))

TemporalCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'rangeOfDates'), CTD_ANON, scope=TemporalCoverage, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 228, 8)))

TemporalCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'references'), CTD_ANON_21, scope=TemporalCoverage, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TemporalCoverage._UseForTag(pyxb.namespace.ExpandedName(None, u'singleDateTime')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 212, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TemporalCoverage._UseForTag(pyxb.namespace.ExpandedName(None, u'rangeOfDates')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 228, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TemporalCoverage._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TemporalCoverage._Automaton = _BuildAutomaton_36()




GeographicCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'geographicDescription'), NonEmptyStringType, scope=GeographicCoverage, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 487, 8)))

GeographicCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'boundingCoordinates'), CTD_ANON_2, scope=GeographicCoverage, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 536, 8)))

GeographicCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'datasetGPolygon'), CTD_ANON_4, scope=GeographicCoverage, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 758, 8)))

GeographicCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'references'), CTD_ANON_21, scope=GeographicCoverage, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 758, 8))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GeographicCoverage._UseForTag(pyxb.namespace.ExpandedName(None, u'geographicDescription')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 487, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeographicCoverage._UseForTag(pyxb.namespace.ExpandedName(None, u'boundingCoordinates')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 536, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeographicCoverage._UseForTag(pyxb.namespace.ExpandedName(None, u'datasetGPolygon')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 758, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeographicCoverage._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GeographicCoverage._Automaton = _BuildAutomaton_37()




TaxonomicCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'taxonomicSystem'), CTD_ANON_7, scope=TaxonomicCoverage, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1029, 8)))

TaxonomicCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'generalTaxonomicCoverage'), NonEmptyStringType, scope=TaxonomicCoverage, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1196, 8)))

TaxonomicCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'taxonomicClassification'), TaxonomicClassificationType, scope=TaxonomicCoverage, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1210, 8)))

TaxonomicCoverage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'references'), CTD_ANON_21, scope=TaxonomicCoverage, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1029, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1196, 8))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TaxonomicCoverage._UseForTag(pyxb.namespace.ExpandedName(None, u'taxonomicSystem')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1029, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TaxonomicCoverage._UseForTag(pyxb.namespace.ExpandedName(None, u'generalTaxonomicCoverage')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1196, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TaxonomicCoverage._UseForTag(pyxb.namespace.ExpandedName(None, u'taxonomicClassification')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1210, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TaxonomicCoverage._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TaxonomicCoverage._Automaton = _BuildAutomaton_38()




CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'contact'), ResponsibleParty, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 101, 8)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'article'), Article, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 112, 10)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'book'), Book, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 124, 10)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'chapter'), Chapter, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 135, 10)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'editedBook'), Book, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 149, 10)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'manuscript'), Manuscript, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 162, 10)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'report'), Report, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 173, 10)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'thesis'), Thesis, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 186, 10)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'conferenceProceedings'), ConferenceProceedings, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 200, 10)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'personalCommunication'), PersonalCommunication, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 211, 10)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'map'), Map, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 223, 10)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'generic'), Generic, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 235, 10)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'audioVisual'), AudioVisual, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 248, 10)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'presentation'), Presentation, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 260, 10)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'alternateIdentifier'), CTD_ANON_19, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 91, 6)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'shortName'), NonEmptyStringType, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 112, 6)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'title'), NonEmptyStringType, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 126, 6)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'creator'), ResponsibleParty, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 144, 6)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'metadataProvider'), ResponsibleParty, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 160, 6)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'associatedParty'), CTD_ANON_27, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 174, 6)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'pubDate'), yearDate, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 211, 6)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'language'), NonEmptyStringType, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 225, 6)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'series'), NonEmptyStringType, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 238, 6)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'abstract'), _ImportedBinding__txt.TextType, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 251, 6)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'keywordSet'), CTD_ANON_16, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 262, 6)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'additionalInfo'), _ImportedBinding__txt.TextType, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 332, 6)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'intellectualRights'), _ImportedBinding__txt.TextType, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 345, 6)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'distribution'), DistributionType, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 364, 6)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'coverage'), Coverage, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 377, 6)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'references'), CTD_ANON_21, scope=CitationType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 91, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 112, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 160, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 174, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 211, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 225, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 238, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 251, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 262, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 332, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 345, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 364, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 377, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 101, 8))
    counters.add(cc_13)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'alternateIdentifier')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 91, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'shortName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 112, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'title')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 126, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'creator')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 144, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'metadataProvider')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 160, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'associatedParty')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 174, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'pubDate')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 211, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'language')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 225, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'series')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 238, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'abstract')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 251, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'keywordSet')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 262, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'additionalInfo')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 332, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'intellectualRights')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 345, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'distribution')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 364, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'coverage')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 377, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'contact')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 101, 8))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'article')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 112, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'book')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 124, 10))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'chapter')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 135, 10))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'editedBook')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 149, 10))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'manuscript')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 162, 10))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'report')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 173, 10))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'thesis')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 186, 10))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'conferenceProceedings')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 200, 10))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'personalCommunication')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 211, 10))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'map')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 223, 10))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'generic')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 235, 10))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'audioVisual')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 248, 10))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'presentation')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 260, 10))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_29 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    st_16._set_transitionSet(transitions)
    transitions = []
    st_17._set_transitionSet(transitions)
    transitions = []
    st_18._set_transitionSet(transitions)
    transitions = []
    st_19._set_transitionSet(transitions)
    transitions = []
    st_20._set_transitionSet(transitions)
    transitions = []
    st_21._set_transitionSet(transitions)
    transitions = []
    st_22._set_transitionSet(transitions)
    transitions = []
    st_23._set_transitionSet(transitions)
    transitions = []
    st_24._set_transitionSet(transitions)
    transitions = []
    st_25._set_transitionSet(transitions)
    transitions = []
    st_26._set_transitionSet(transitions)
    transitions = []
    st_27._set_transitionSet(transitions)
    transitions = []
    st_28._set_transitionSet(transitions)
    transitions = []
    st_29._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CitationType._Automaton = _BuildAutomaton_39()




Chapter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'chapterNumber'), NonEmptyStringType, scope=Chapter, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 526, 10)))

Chapter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'editor'), ResponsibleParty, scope=Chapter, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 538, 10)))

Chapter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'bookTitle'), NonEmptyStringType, scope=Chapter, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 553, 10)))

Chapter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'pageRange'), NonEmptyStringType, scope=Chapter, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 564, 10)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 410, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 424, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 435, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 448, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 459, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 471, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 483, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 495, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 526, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 564, 10))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Chapter._UseForTag(pyxb.namespace.ExpandedName(None, u'publisher')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 397, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Chapter._UseForTag(pyxb.namespace.ExpandedName(None, u'publicationPlace')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 410, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Chapter._UseForTag(pyxb.namespace.ExpandedName(None, u'edition')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 424, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Chapter._UseForTag(pyxb.namespace.ExpandedName(None, u'volume')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 435, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Chapter._UseForTag(pyxb.namespace.ExpandedName(None, u'numberOfVolumes')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 448, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Chapter._UseForTag(pyxb.namespace.ExpandedName(None, u'totalPages')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 459, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Chapter._UseForTag(pyxb.namespace.ExpandedName(None, u'totalFigures')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 471, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Chapter._UseForTag(pyxb.namespace.ExpandedName(None, u'totalTables')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 483, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Chapter._UseForTag(pyxb.namespace.ExpandedName(None, u'ISBN')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 495, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Chapter._UseForTag(pyxb.namespace.ExpandedName(None, u'chapterNumber')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 526, 10))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Chapter._UseForTag(pyxb.namespace.ExpandedName(None, u'editor')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 538, 10))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Chapter._UseForTag(pyxb.namespace.ExpandedName(None, u'bookTitle')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 553, 10))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Chapter._UseForTag(pyxb.namespace.ExpandedName(None, u'pageRange')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 564, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Chapter._Automaton = _BuildAutomaton_40()




ResponsibleParty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'individualName'), Person, scope=ResponsibleParty, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 107, 10)))

ResponsibleParty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'organizationName'), NonEmptyStringType, scope=ResponsibleParty, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 141, 10)))

ResponsibleParty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'positionName'), NonEmptyStringType, scope=ResponsibleParty, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 176, 10)))

ResponsibleParty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'address'), Address, scope=ResponsibleParty, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 210, 8)))

ResponsibleParty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'phone'), CTD_ANON_11, scope=ResponsibleParty, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 223, 8)))

ResponsibleParty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'electronicMailAddress'), NonEmptyStringType, scope=ResponsibleParty, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 256, 8)))

ResponsibleParty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'onlineUrl'), pyxb.binding.datatypes.anyURI, scope=ResponsibleParty, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 270, 8)))

ResponsibleParty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'userId'), CTD_ANON_12, scope=ResponsibleParty, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 286, 8)))

ResponsibleParty._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'references'), CTD_ANON_21, scope=ResponsibleParty, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 210, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 223, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 256, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 270, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 286, 8))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResponsibleParty._UseForTag(pyxb.namespace.ExpandedName(None, u'individualName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 107, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResponsibleParty._UseForTag(pyxb.namespace.ExpandedName(None, u'organizationName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 141, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResponsibleParty._UseForTag(pyxb.namespace.ExpandedName(None, u'positionName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 176, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ResponsibleParty._UseForTag(pyxb.namespace.ExpandedName(None, u'address')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 210, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ResponsibleParty._UseForTag(pyxb.namespace.ExpandedName(None, u'phone')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 223, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ResponsibleParty._UseForTag(pyxb.namespace.ExpandedName(None, u'electronicMailAddress')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 256, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ResponsibleParty._UseForTag(pyxb.namespace.ExpandedName(None, u'onlineUrl')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 270, 8))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ResponsibleParty._UseForTag(pyxb.namespace.ExpandedName(None, u'userId')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 286, 8))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResponsibleParty._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ResponsibleParty._Automaton = _BuildAutomaton_41()




Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'deliveryPoint'), NonEmptyStringType, scope=Address, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 439, 8)))

Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'city'), NonEmptyStringType, scope=Address, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 452, 8)))

Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'administrativeArea'), NonEmptyStringType, scope=Address, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 463, 8)))

Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'postalCode'), NonEmptyStringType, scope=Address, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 476, 8)))

Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'country'), NonEmptyStringType, scope=Address, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 490, 8)))

Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'references'), CTD_ANON_21, scope=Address, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 439, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 452, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 463, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 476, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 490, 8))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(None, u'deliveryPoint')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 439, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(None, u'city')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 452, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(None, u'administrativeArea')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 463, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(None, u'postalCode')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 476, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(None, u'country')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 490, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Address._Automaton = _BuildAutomaton_42()




ResearchProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'title'), NonEmptyStringType, scope=ResearchProjectType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 102, 8)))

ResearchProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'personnel'), CTD_ANON_25, scope=ResearchProjectType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 115, 8)))

ResearchProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'abstract'), _ImportedBinding__txt.TextType, scope=ResearchProjectType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 168, 8)))

ResearchProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'funding'), _ImportedBinding__txt.TextType, scope=ResearchProjectType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 178, 8)))

ResearchProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'studyAreaDescription'), CTD_ANON_13, scope=ResearchProjectType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 191, 8)))

ResearchProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'designDescription'), CTD_ANON_15, scope=ResearchProjectType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 353, 8)))

ResearchProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'relatedProject'), ResearchProjectType, scope=ResearchProjectType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 401, 8)))

ResearchProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'references'), CTD_ANON_21, scope=ResearchProjectType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 168, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 178, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 191, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 353, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 401, 8))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ResearchProjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'title')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 102, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResearchProjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'personnel')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 115, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ResearchProjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'abstract')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 168, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ResearchProjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'funding')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 178, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ResearchProjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'studyAreaDescription')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 191, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ResearchProjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'designDescription')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 353, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ResearchProjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'relatedProject')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 401, 8))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResearchProjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ResearchProjectType._Automaton = _BuildAutomaton_43()




DistributionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'references'), CTD_ANON_21, scope=DistributionType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6)))

DistributionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'online'), OnlineType, scope=DistributionType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 611, 8)))

DistributionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'offline'), OfflineType, scope=DistributionType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 623, 8)))

DistributionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'inline'), InlineType, scope=DistributionType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 634, 8)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DistributionType._UseForTag(pyxb.namespace.ExpandedName(None, u'online')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 611, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DistributionType._UseForTag(pyxb.namespace.ExpandedName(None, u'offline')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 623, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DistributionType._UseForTag(pyxb.namespace.ExpandedName(None, u'inline')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 634, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DistributionType._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DistributionType._Automaton = _BuildAutomaton_44()




ConnectionDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'references'), CTD_ANON_21, scope=ConnectionDefinitionType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6)))

ConnectionDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'schemeName'), CTD_ANON_22, scope=ConnectionDefinitionType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 667, 8)))

ConnectionDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), _ImportedBinding__txt.TextType, scope=ConnectionDefinitionType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 712, 8)))

ConnectionDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'parameterDefinition'), CTD_ANON_17, scope=ConnectionDefinitionType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 740, 8)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConnectionDefinitionType._UseForTag(pyxb.namespace.ExpandedName(None, u'schemeName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 667, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConnectionDefinitionType._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 712, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConnectionDefinitionType._UseForTag(pyxb.namespace.ExpandedName(None, u'parameterDefinition')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 740, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConnectionDefinitionType._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ConnectionDefinitionType._Automaton = _BuildAutomaton_45()




ConnectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'references'), CTD_ANON_21, scope=ConnectionType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6)))

ConnectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'connectionDefinition'), ConnectionDefinitionType, scope=ConnectionType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1098, 8)))

ConnectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'parameter'), CTD_ANON_18, scope=ConnectionType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1107, 8)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1107, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConnectionType._UseForTag(pyxb.namespace.ExpandedName(None, u'connectionDefinition')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1098, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ConnectionType._UseForTag(pyxb.namespace.ExpandedName(None, u'parameter')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 1107, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConnectionType._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ConnectionType._Automaton = _BuildAutomaton_46()




def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(None, u'singleDateTime')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 212, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(None, u'rangeOfDates')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 228, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_47()




def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1029, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1196, 8))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(None, u'taxonomicSystem')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1029, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(None, u'generalTaxonomicCoverage')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1196, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(None, u'taxonomicClassification')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-coverage.xsd', 1210, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_48()




ConferenceProceedings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'conferenceName'), NonEmptyStringType, scope=ConferenceProceedings, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 594, 10)))

ConferenceProceedings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'conferenceDate'), NonEmptyStringType, scope=ConferenceProceedings, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 606, 10)))

ConferenceProceedings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'conferenceLocation'), Address, scope=ConferenceProceedings, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 617, 10)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 410, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 424, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 435, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 448, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 459, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 471, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 483, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 495, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 526, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 564, 10))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 594, 10))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 606, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 617, 10))
    counters.add(cc_12)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'publisher')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 397, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'publicationPlace')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 410, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'edition')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 424, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'volume')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 435, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'numberOfVolumes')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 448, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'totalPages')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 459, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'totalFigures')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 471, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'totalTables')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 483, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'ISBN')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 495, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'chapterNumber')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 526, 10))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'editor')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 538, 10))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'bookTitle')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 553, 10))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'pageRange')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 564, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'conferenceName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 594, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'conferenceDate')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 606, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(ConferenceProceedings._UseForTag(pyxb.namespace.ExpandedName(None, u'conferenceLocation')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-literature.xsd', 617, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ConferenceProceedings._Automaton = _BuildAutomaton_49()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'role'), RoleType, scope=CTD_ANON_25, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 133, 18)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 210, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 223, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 256, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 270, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 286, 8))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(None, u'individualName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 107, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(None, u'organizationName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 141, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(None, u'positionName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 176, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(None, u'address')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 210, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(None, u'phone')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 223, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(None, u'electronicMailAddress')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 256, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(None, u'onlineUrl')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 270, 8))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(None, u'userId')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 286, 8))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(None, u'role')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 133, 18))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_50()




CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'descriptorValue'), CTD_ANON_14, scope=CTD_ANON_26, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 228, 20)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'citation'), CitationType, scope=CTD_ANON_26, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 288, 20)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 288, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(None, u'descriptorValue')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 228, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(None, u'citation')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-project.xsd', 288, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_51()




CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'role'), RoleType, scope=CTD_ANON_27, documentation=u'', location=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 192, 16)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 188, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 210, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 223, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 256, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 270, 8))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 286, 8))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'individualName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 107, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'organizationName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 141, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'positionName')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 176, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'address')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 210, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'phone')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 223, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'electronicMailAddress')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 256, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'onlineUrl')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 270, 8))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'userId')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-party.xsd', 286, 8))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'references')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 404, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'role')), pyxb.utils.utility.Location(u'/home/dahl/d1/pasta_gmn_adapter/src/pasta_gmn_adapter/api_types/schemas/eml-resource.xsd', 192, 16))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_52()

