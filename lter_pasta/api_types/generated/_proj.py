# ./generated/_proj.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:03db8071ff38047292e6baee97aac91699b0c402
# Generated 2014-03-16 22:56:49.636919 by PyXB version 1.2.3
# Namespace eml://ecoinformatics.org/project-2.1.0 [xmlns:proj]

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
import _nsgroup as _ImportedBinding__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'eml://ecoinformatics.org/project-2.1.0', create_if_missing=True)
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

from _nsgroup import researchProject # {eml://ecoinformatics.org/project-2.1.0}researchProject
from _nsgroup import CTD_ANON_13 as CTD_ANON # None
from _nsgroup import CTD_ANON_14 as CTD_ANON_ # None
from _nsgroup import CTD_ANON_15 as CTD_ANON_2 # None
from _nsgroup import STD_ANON_11 as STD_ANON # None
from _nsgroup import STD_ANON_12 as STD_ANON_ # None
from _nsgroup import ResearchProjectType # {eml://ecoinformatics.org/project-2.1.0}ResearchProjectType
from _nsgroup import DescriptorType # {eml://ecoinformatics.org/project-2.1.0}DescriptorType
from _nsgroup import CTD_ANON_25 as CTD_ANON_3 # None
from _nsgroup import CTD_ANON_26 as CTD_ANON_4 # None
