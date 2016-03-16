#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: cache_refresh

:Synopsis:

:Author:
    servilla
  
:Created:
    3/15/16
"""

import logging

from nodc_connector import content_cache
from nodc_connector.ogc_content_iterator import OGCContentIterator

import settings


logger = logging.getLogger('cache_refresh')


def main():

    cache = content_cache.ContentCache(settings.CACHE_PATH, settings.CACHE_DB)
    entries = OGCContentIterator(max_entries=100)
    cache.refresh(entries)

    return 0


if __name__ == "__main__":
    main()