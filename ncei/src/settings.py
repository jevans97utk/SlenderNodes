#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: settings

:Synopsis:
    Local settings for the NCEI Adapter
:Author:
    servilla
  
:Created:
    3/9/16
"""

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S%z',
                    filename='/Users/servilla/DataONE/NCEI/ncei.log',
                    )


MN_BASE_URL = 'https://ncei-node.dataone.org/mn'
CERTIFICATE_FOR_CREATE = '/Users/servilla/Certs/DataONE/urn_node_mnTestNCEI/urn_node_mnTestNCEI.crt'
CERTIFICATE_FOR_CREATE_KEY = '/Users/servilla/Certs/DataONE/urn_node_mnTestNCEI/private/urn_node_mnTestNCEI.key'
CACHE_PATH = '/Users/servilla/DataONE/NCEI/content_cache'
CACHE_DB = 'cache.sqlite'
CACHE_REFRESH_FILE = '/Users/servilla/DataONE/NCEI/d1_ncei_adapter/src/cache_refresh.txt'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S%z'