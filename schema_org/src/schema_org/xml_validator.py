# Standard library imports ...
import io

# Third party library imports ...
import lxml.etree
import requests
import d1_scimeta.validate


class XMLValidator(object):
    """
    Validates XML files according to 19115-2 schema.
    """
    def __init__(self):
        """
        Load the 19115-2 schema so that every XML file produced is validated.
        """
        self.format_ids = [
            'eml://ecoinformatics.org/eml-2.0.0',
            'eml://ecoinformatics.org/eml-2.0.1',
            'eml://ecoinformatics.org/eml-2.1.0',
            'eml://ecoinformatics.org/eml-2.1.1',
            'http://www.esri.com/metadata/esriprof80.dtd',
            'FGDC-STD-001.1-1999',
            'FGDC-STD-001.2-1999',
            'FGDC-STD-001-1998',
            'INCITS-453-2009',
            'http://www.unidata.ucar.edu/namespaces/netcdf/ncml-2.2',
            'http://www.cuahsi.org/waterML/1.0/',
            'http://www.cuahsi.org/waterML/1.1/',
            'http://www.loc.gov/METS/',
            'http://rs.tdwg.org/dwc/xsd/simpledarwincore/',
            'http://digir.net/schema/conceptual/darwin/2003/1.0/darwin2.xsd',
            'http://datadryad.org/profile/v3.1',
            'http://purl.org/dryad/terms/',
            '-//ecoinformatics.org//eml-access-2.0.0beta4//EN',
            '-//ecoinformatics.org//eml-attribute-2.0.0beta4//EN',
            '-//ecoinformatics.org//eml-constraint-2.0.0beta4//EN',
            '-//ecoinformatics.org//eml-coverage-2.0.0beta4//EN',
            '-//ecoinformatics.org//eml-dataset-2.0.0beta4//EN',
            '-//ecoinformatics.org//eml-distribution-2.0.0beta4//EN',
            '-//ecoinformatics.org//eml-entity-2.0.0beta4//EN',
            '-//ecoinformatics.org//eml-literature-2.0.0beta4//EN',
            '-//ecoinformatics.org//eml-party-2.0.0beta4//EN',
            '-//ecoinformatics.org//eml-physical-2.0.0beta4//EN',
            '-//ecoinformatics.org//eml-project-2.0.0beta4//EN',
            '-//ecoinformatics.org//eml-protocol-2.0.0beta4//EN',
            '-//ecoinformatics.org//eml-resource-2.0.0beta4//EN',
            '-//ecoinformatics.org//eml-software-2.0.0beta4//EN',
            '-//ecoinformatics.org//eml-access-2.0.0beta6//EN',
            '-//ecoinformatics.org//eml-attribute-2.0.0beta6//EN',
            '-//ecoinformatics.org//eml-constraint-2.0.0beta6//EN',
            '-//ecoinformatics.org//eml-coverage-2.0.0beta6//EN',
            '-//ecoinformatics.org//eml-dataset-2.0.0beta6//EN',
            '-//ecoinformatics.org//eml-distribution-2.0.0beta6//EN',
            '-//ecoinformatics.org//eml-entity-2.0.0beta6//EN',
            '-//ecoinformatics.org//eml-literature-2.0.0beta6//EN',
            '-//ecoinformatics.org//eml-party-2.0.0beta6//EN',
            '-//ecoinformatics.org//eml-physical-2.0.0beta6//EN',
            '-//ecoinformatics.org//eml-project-2.0.0beta6//EN',
            '-//ecoinformatics.org//eml-protocol-2.0.0beta6//EN',
            '-//ecoinformatics.org//eml-resource-2.0.0beta6//EN',
            '-//ecoinformatics.org//eml-software-2.0.0beta6//EN',
            'ddi:codebook:2_5',
            'http://www.icpsr.umich.edu/DDI',
            'http://purl.org/ornl/schema/mercury/terms/v1.0',
            'http://datacite.org/schema/kernel-3.0',
            'http://datacite.org/schema/kernel-3.1',
            'http://ns.dataone.org/metadata/schema/onedcx/v1.0',
            'http://www.isotc211.org/2005/gmd',
            'http://www.isotc211.org/2005/gmd-noaa',
            'http://www.isotc211.org/2005/gmd-pangaea',
            'http://www.openarchives.org/OAI/2.0/oai_dc/'
        ]

    def validate(self, src, format_id=None):
        """
        Validate the XML of the given schema.

        Parameters
        ----------
        src : str or file-like
            file or URL to validate
        format_id : str or None
            If None, check against all format IDs.  Otherwise just check this
            particular one.
        """
        try:
            doc = self.build_document_out_of_source(src)
        except Exception as e:
            # If we can't even build a document, then we have to at least say
            # why.
            return repr(e)

        # If a specific format ID was specified, check against only it.
        # Otherwise check against all known format IDs.
        if format_id is not None:
            format_ids = [format_id]
        else:
            format_ids = self.format_ids

        successes = []
        for format_id in format_ids:
            try:
                d1_scimeta.validate.assert_valid(format_id, doc)
            except Exception:
                pass
            else:
                # Ok, the current format ID worked.  We're good.
                successes.append(format_id)

        if len(successes) > 0:
            # If we actually found something, maybe more than one format ID
            # that works, return list of all of them.
            return ", ".join(successes)

        # If we are here, then none of the IDs have worked.  We will try again
        # with the default ID and let that error message speak for itself.
        format_id = 'http://www.isotc211.org/2005/gmd'
        try:
            d1_scimeta.validate.assert_valid(format_id, doc)
        except Exception as e:
            return repr(e)

    def build_document_out_of_source(self, src):
        """
        Parameters
        ----------
        src : file or file-like or URL or path or lxml.etree
        """
        # Is it file or file-like, but not a path.
        try:
            doc = lxml.etree.parse(src)
        except (OSError, TypeError):
            # OSError:  if a string that doesn't exist on filesystem
            # TypeError:  if the item is already an ElementTree
            pass
        except lxml.etree.XMLSyntaxError:
            # It WAS a file or file-like, but we just could not parse it.
            raise
        else:
            return doc

        # Is it a URL?
        try:
            r = requests.get(src)
            r.raise_for_status()
        except Exception:
            # Not a valid URL
            pass
        else:
            doc = lxml.etree.parse(io.BytesIO(r.content))
            return doc

        # Is it a pathlib object?
        try:
            doc = lxml.etree.parse(str(src))
        except Exception:
            # OSError:  if a string that doesn't exist on filesystem
            # TypeError:  if the item is already an ElementTree
            pass
        else:
            # The src was file or file-like object.
            return doc

        # Assume it is already an ElementTree
        return src
