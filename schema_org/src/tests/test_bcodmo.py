# Standard library imports
import asyncio
import importlib.resources as ir
import re
import unittest
from unittest.mock import patch

# 3rd party library imports
from aioresponses import aioresponses

# Local imports
from schema_org.bcodmo import BCODMOHarvester
from .test_common import TestCommon


class TestSuite(TestCommon):

    def setUp(self):
        self.regex = re.compile(r'https?://www.bco-dmo.org/')

    @patch('schema_org.d1_client_manager.D1ClientManager.get_last_harvest_time')  # noqa: E501
    def test_not_a_dataset(self, mock_harvest_time):
        """
        SCENARIO:  BCO-DMO sitemaps tell us whether a URL leads to a Dataset or
        not.  The URL has "dataset" in it.  This one has "deployment" instead.

        EXPECTED RESULT:  No documents are harvested.  The URLset is empty.  No
        errors are logged.
        """
        s = """
        <?xml-stylesheet type="text/xsl" href="//www.bco-dmo.org/sitemap.xsl"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
          <url>
            <loc>http://www.bco-dmo.org/deployment/57668</loc>
            <lastmod>2011-01-28T15:46Z</lastmod>
            <priority>0.6</priority>
          </url>
        </urlset>
        """
        mock_harvest_time.return_value = '1999-01-01T00:00:00Z'

        sitemap_content = s.encode('utf-8')

        contents = sitemap_content
        status_code = 200
        headers = {'Content-Type': 'application/xml'}

        with aioresponses() as m:
            m.get(self.regex,
                  body=contents, status=status_code, headers=headers)

            harvester = BCODMOHarvester()
            with self.assertLogs(logger=harvester.logger, level='DEBUG') as cm:
                asyncio.run(harvester.run())

        urlset = harvester.get_sitemaps_urlset()
        self.assertEqual(len(urlset), 0)

        self.assertErrorLogCallCount(cm.output, n=0)

    @patch('schema_org.d1_client_manager.D1ClientManager.get_last_harvest_time')  # noqa: E501
    def test_load_run(self, mock_harvest_time):
        """
        SCENARIO:  We have a valid dataset to harvest for the first time.

        EXPECTED RESULT:  The URLset has one document.  XML validation fails.
        """
        s = """
        <?xml-stylesheet type="text/xsl" href="//www.bco-dmo.org/sitemap.xsl"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
          <url>
            <loc>http://www.bco-dmo.org/dataset/559701</loc>
            <lastmod>2016-08-20T03:10Z</lastmod>
            <priority>0.9</priority>
          </url>
        </urlset>
        """
        mock_harvest_time.return_value = '1999-01-01T00:00:00Z'

        sitemap_content = s.encode('utf-8')

        # Network calls
        #
        # 1) Sitemap
        # 2) landing page
        # 3) associated JSON-LD data package
        # 4) XML document
        contents = [
            sitemap_content,
            ir.read_binary('tests.data.bcodmo.559701', 'landing_page.html'),
            ir.read_binary('tests.data.bcodmo.559701', 'datapackage.json'),
            ir.read_binary('tests.data.bcodmo.559701', 'iso19115-2.xml'),
        ]
        status = [200, 200, 200, 200]
        headers = [
            {'Content-Type': 'application/xml'},
            {'Content-Type': 'text/html'},
            {'Content-Type': 'application/vnd.datapackage+json'},
            {'Content-Type': 'application/xml'},
        ]

        with aioresponses() as m:
            for contents, status, headers in zip(contents, status, headers):
                m.get(self.regex,
                      body=contents, status=status, headers=headers)

            harvester = BCODMOHarvester()
            with self.assertLogs(logger=harvester.logger, level='DEBUG') as cm:
                asyncio.run(harvester.run())
                # print('\n'.join(cm.output))

        urlset = harvester.get_sitemaps_urlset()
        self.assertEqual(len(urlset), 1)

        self.assertErrorLogCallCount(cm.output, n=3)
