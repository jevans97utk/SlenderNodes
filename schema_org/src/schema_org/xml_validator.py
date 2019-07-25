# Standard library imports ...
import io

# Third party library imports ...
import lxml.etree
import requests
import d1_scimeta.validate

# local imports
from .common import FORMAT_IDS

class XMLValidator(object):
    """
    Validates XML files according to 19115-2 schema.
    """
    def __init__(self):
        """
        Load the 19115-2 schema so that every XML file produced is validated.
        """
        pass

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
            format_ids = FORMAT_IDS

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
