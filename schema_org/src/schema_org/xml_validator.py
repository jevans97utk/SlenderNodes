# Standard library imports ...
import io
import logging
import urllib.parse

# Third party library imports ...
import lxml.etree
import requests
import d1_scimeta.validate
import d1_scimeta.util


class XMLValidator(object):
    """
    Validates XML files according to 19115-2 schema.
    """
    def __init__(self, verbosity='INFO'):
        """
        Load the 19115-2 schema so that every XML file produced is validated.
        """
        self.setup_logging(verbosity)
        self.session = requests.Session()

    def setup_logging(self, verbosity):
        """
        Parameters
        ----------
        verbosity : str
            Level of logging verbosity.
        """
        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        level = getattr(logging, verbosity)
        logging.basicConfig(format=format, level=level)

        self.logger = logging.getLogger(__name__)

        # Disable d1_scimeta logging
        logger = logging.getLogger('d1_scimeta.util')
        logger.disabled = True
        logger = logging.getLogger('d1_scimeta.validate')
        logger.disabled = True

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
            self.logger.debug(repr(e))
            self.logger.error(e)
            return

        # If a specific format ID was specified, check against only it.
        # Otherwise check against all known format IDs.
        if format_id is not None:
            self.logger.info(f'Running validation against {format_id}.')
            format_ids = [format_id]
        else:
            self.logger.info(f'Running validation against all format IDs.')
            format_ids = d1_scimeta.util.get_supported_format_id_list()

        for format_id_item in format_ids:
            try:
                d1_scimeta.validate.assert_valid(format_id_item, doc)
            except Exception:
                pass
            else:
                # Ok, the current format ID worked.  We're good.
                msg = f"Validated against {format_id_item}"
                self.logger.info(msg)

        # If we are here, then none of the IDs have worked.  We will try again
        # with the default ID and let that error message speak for itself.
        if format_id is None:
            format_id = 'http://www.isotc211.org/2005/gmd'
        try:
            d1_scimeta.validate.assert_valid(format_id, doc)
        except Exception as e:
            self.logger.debug(repr(e))
            self.logger.error(e)
            return

    def build_document_out_of_source(self, src):
        """
        Parameters
        ----------
        src : file or file-like or URL or path or lxml.etree
        """
        # Is it a URL?
        try:
            urllib.parse.urlparse(src)
        except AttributeError:
            pass
        else:
            # Yes, a URL.
            try:
                r = self.session.get(src)
                r.raise_for_status()
            except Exception:
                raise
            else:
                doc = lxml.etree.parse(io.BytesIO(r.content))
                return doc

        # Is it file or file-like, but not a path.
        try:
            doc = lxml.etree.parse(src)
        except (OSError, TypeError):
            # OSError:  if a string that doesn't exist on filesystem
            # TypeError:  if the item is already an ElementTree
            pass
        else:
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
