#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: ncei_cache_reader

:Synopsis:

:Author:
    servilla
  
:Created:
    3/13/16
"""

import logging
from datetime import datetime

from dateutil import parser
from nodc_connector import content_cache

import settings
import scimeta_bundle


logger = logging.getLogger('ncei_cache_reader')


def main():

    f = open(settings.CACHE_REFRESH_FILE, 'r')
    cache_refresh_date = f.readline().strip()
    f.close()

    cnt = 0
    logger.info('Beginning cache read for new content since: {0}'.format(cache_refresh_date))
    cache = content_cache.ContentCache(settings.CACHE_PATH, settings.CACHE_DB)
    for record in cache.listNewSince(parser.parse(cache_refresh_date)):
        try:
            pid = record['pid']
            sid = record['sid']
            sci_metadata = record['sci_metadata']
            sci_sysmeta = record['sci_sysmeta']
            date_modified = record['date_modified']
            smb = scimeta_bundle.Scimeta_Bundle(pid, sci_metadata, sci_sysmeta)
            predecessor = cache.getPredecessorPID(sid, date_modified)
            cache_refresh_date = date_modified
            logger.info('Adding PID-SID "{0}-{1}" with date "{2}"'.format(pid, sid, date_modified))
            if  predecessor is None:
                smb.gmn_create()
                cnt += 1
            else:
                smb.gmn_update(predecessor)
                cnt += 1
        except Exception as e:
            logger.error("Unknown fromIteratorEntry error: {0}".format(e.message))

    logger.info('Ending cache read for new content up to: {0}'.format(cache_refresh_date))
    f = open(settings.CACHE_REFRESH_FILE, 'w')
    f.write(cache_refresh_date)
    f.close()

    return 0


if __name__ == "__main__":
    main()