#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: ncei_catalog

:Synopsis:
    Iterates through the NCEI data catalog using the CSW endpoint for the
    purpose building data packages and inserting into the NCEI member node.

:Author:
    servilla
  
:Created:
    2/5/16
"""

import logging

from nodc_connector import ogc_content_iterator
from nodc_connector import nodc_package
import scimeta_bundle
import ncei_package


logger = logging.getLogger('ncei_catalog')


def main():

    csw_page_size = 500
    entries = []
    start = 1
    packager = nodc_package.NODCPackageFTP()
    record_cnt = start

    try:
        while True:
            csw = ogc_content_iterator.OGCContentIterator(start_position=start,
                                                          page_size=csw_page_size)
            n = 0
            while n < csw_page_size:
                entries.append(csw.next())
                n += 1

            for e in entries:
                print('{0:6d}: {1}'.format(record_cnt, e))
                record_cnt += 1
                try:
                    scimeta = ncei_package.Science_Metadata(e)
                    doc = scimeta.get_document()
                    sysmeta = scimeta.get_sysmeta()
                    smb = scimeta_bundle.Scimeta_Bundle(doc, sysmeta)
                    smb.gmn_create()
                except Exception as e:
                    logger.error("Unknown fromIteratorEntry error: {0}".format(e.message))

            entries = []
            start = start + n

    except StopIteration as e:
        logger.error("OGC Content Iterator failure: {0}".format(e.message))
        if len(entries) > 0:
            for e in entries:
               record_cnt += 1
               print('{0:6d}: {1}'.format(record_cnt, e))

    return 0


if __name__ == "__main__":
    main()
