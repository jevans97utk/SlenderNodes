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
        pass

    def validate(self, src, format_id='http://www.isotc211.org/2005/gmd'):
        """
        Validate the XML of the given schema.

        Parameters
        ----------
        src : str or file-like
           file or URL to validate
        """
        # Is it file or file-like, but not a path.
        try:
            doc = lxml.etree.parse(src)
        except Exception:
            # OSError:  if a string that doesn't exist on filesystem
            # TypeError:  if the item is already an ElementTree
            pass
        else:
            # The src was file or file-like object.
            d1_scimeta.validate.assert_valid(format_id, doc)
            return

        # Is it a URL?
        try:
            r = requests.get(src)
            r.raise_for_status()
        except Exception:
            # Not a valid URL
            pass
        else:
            doc = lxml.etree.parse(io.BytesIO(r.content))
            d1_scimeta.validate.assert_valid(format_id, doc)
            return

        # Is it a pathlib object?
        try:
            doc = lxml.etree.parse(str(src))
        except Exception:
            # OSError:  if a string that doesn't exist on filesystem
            # TypeError:  if the item is already an ElementTree
            pass
        else:
            # The src was file or file-like object.
            d1_scimeta.validate.assert_valid(format_id, doc)
            return

        # Assume it is already an ElementTree
        d1_scimeta.validate.assert_valid(format_id, src)
