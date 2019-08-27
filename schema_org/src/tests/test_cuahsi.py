# Standard library imports
import importlib.resources as ir
import io
import json
import unittest

# 3rd party library imports
import dateutil
import lxml.etree

# Local imports
from schema_org.check_sitemap import D1CheckSitemap


class TestSuite(unittest.TestCase):

    def test_no_lastmod_time_in_sitemap_leaf(self):
        """
        SCENARIO:  A sitemap leaf XML file has <loc> entries, but no <lastmod>
        entries.  In this case, we should look to the lastModified field in the
        JSON-LD for guidance.

        CUAHSI has no <lastmod> entries in their sitemap.

        EXPECTED RESULT:  The entries in the sitemap are NOT skipped.
        """
        content = ir.read_binary('tests.data.cuahsi', 'sitemap-pages.xml')
        doc = lxml.etree.parse(io.BytesIO(content))

        last_harvest_time_str = '1900-01-01T00:00:00Z'
        last_harvest_time = dateutil.parser.parse(last_harvest_time_str)

        obj = D1CheckSitemap()

        with self.assertLogs(logger=obj.logger, level='DEBUG'):
            records = obj.extract_records_from_sitemap(doc, last_harvest_time)
        self.assertEqual(len(records), 3)

    def test_jsonld_script_found_in_body_rather_than_head(self):
        """
        SCENARIO:  The JSON-LD <SCRIPT> element is located in the <body> of the
        landing page element rather than the <head>.

        CUAHSI puts the <SCRIPT> element in the body, while ARM puts it in the
        <HEAD>.

        EXPECTED RESULT:  The JSON-LD is successfully extracted from the
        landing page document.
        """
        parts = ['tests', 'data', 'cuahsi', 'aadd7dd60f31498590de32c9b14446c3']
        package = '.'.join(parts)
        text = ir.read_text(package, 'landing_page.html')
        doc = lxml.etree.HTML(text)

        obj = D1CheckSitemap()

        with self.assertLogs(logger=obj.logger, level='DEBUG'):
            j = obj.extract_jsonld(doc)

        json.dumps(j)

        self.assertTrue(True)
