# ./generated/_res.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:3b8019e138aae2825d292eab040760fa22b9838e
# Generated 2017-01-12 00:01:43.091536 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace eml://ecoinformatics.org/resource-2.1.0 [xmlns:res]

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
import _nsgroup as _ImportedBinding__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('eml://ecoinformatics.org/resource-2.1.0', create_if_missing=True)
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

from _nsgroup import CTD_ANON_16 as CTD_ANON # None
from _nsgroup import KeyTypeCode # {eml://ecoinformatics.org/resource-2.1.0}KeyTypeCode
from _nsgroup import yearDate # {eml://ecoinformatics.org/resource-2.1.0}yearDate
from _nsgroup import IDType # {eml://ecoinformatics.org/resource-2.1.0}IDType
from _nsgroup import SystemType # {eml://ecoinformatics.org/resource-2.1.0}SystemType
from _nsgroup import ScopeType # {eml://ecoinformatics.org/resource-2.1.0}ScopeType
from _nsgroup import FunctionType # {eml://ecoinformatics.org/resource-2.1.0}FunctionType
from _nsgroup import CTD_ANON_17 as CTD_ANON_ # None
from _nsgroup import InlineType # {eml://ecoinformatics.org/resource-2.1.0}InlineType
from _nsgroup import OfflineType # {eml://ecoinformatics.org/resource-2.1.0}OfflineType
from _nsgroup import OnlineType # {eml://ecoinformatics.org/resource-2.1.0}OnlineType
from _nsgroup import CTD_ANON_18 as CTD_ANON_2 # None
from _nsgroup import NonEmptyStringType # {eml://ecoinformatics.org/resource-2.1.0}NonEmptyStringType
from _nsgroup import CTD_ANON_19 as CTD_ANON_3 # None
from _nsgroup import CTD_ANON_20 as CTD_ANON_4 # None
from _nsgroup import CTD_ANON_21 as CTD_ANON_5 # None
from _nsgroup import DistributionType # {eml://ecoinformatics.org/resource-2.1.0}DistributionType
from _nsgroup import ConnectionDefinitionType # {eml://ecoinformatics.org/resource-2.1.0}ConnectionDefinitionType
from _nsgroup import CTD_ANON_22 as CTD_ANON_6 # None
from _nsgroup import UrlType # {eml://ecoinformatics.org/resource-2.1.0}UrlType
from _nsgroup import ConnectionType # {eml://ecoinformatics.org/resource-2.1.0}ConnectionType
from _nsgroup import CTD_ANON_27 as CTD_ANON_7 # None
