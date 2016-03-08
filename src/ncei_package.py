#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: ncei_package

:Synopsis:

:Author:
    servilla
  
:Created:
    2/11/16
"""

import logging
import datetime

from nodc_connector import nodc_package
from nodc_connector import ogc_content_iterator

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y%m%d-%H:%M:%S')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('ncei_package')

__author__ = "servilla"


class NCEIPackage(object):

    def __init__(self, ncei_index=None):
        csw_page_size = 1
        start = int(ncei_index)
        csw = ogc_content_iterator.OGCContentIterator(start_position=start,
                                                    page_size=csw_page_size)
        entries = []
        n = 0
        while n < csw_page_size:
            entries.append(csw.next())
            n += 1
        packager = nodc_package.NODCPackageFTP()
        self.package = packager.fromIteratorEntry(entries[0])


    def print_sysmeta_to_stdio(self):

        now = datetime.datetime.now()
        print('--------------- {0} ---------------'.format(now))

        print('--ORE--')
        for ident in self.package['package']:
            print(self.package['package'][ident]['sysmeta'])
        print('\n')

        print('--Metadata--')
        for ident in self.package['metadata']:
            print(self.package['metadata'][ident]['sysmeta'])
        print('\n')

        print('--Data--')
        for ident in self.package['data']:
            print(self.package['data'][ident]['sysmeta'])


    def write_to_files(self):
        pass


    def insert_into_gmn(self):
        pass


def main():

    p = NCEIPackage(ncei_index=35)
    p.print_sysmeta_to_stdio()

    return 0


if __name__ == "__main__":
    main()