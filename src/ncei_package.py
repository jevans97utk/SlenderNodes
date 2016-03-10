#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: ncei_package

:Synopsis:
    Helper package to access contents of an NCEI data package

:Author:
    servilla
  
:Created:
    2/11/16
"""

import logging

from nodc_connector import nodc_package

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y%m%d-%H:%M:%S')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('ncei_package')

__author__ = "servilla"


class NCEIPackage(object):

    def __init__(self, csw_record=None):
        try:
            packager = nodc_package.NODCPackageFTP()
            self.package = packager.fromIteratorEntry(csw_record)
        except Exception as e:
            logger.error('Failed to load NCEI package - {0}'.format(e.message))

    def get_pid(self):
        return self.package['pid']

    def get_sid(self):
        return self.package['sid']

    def get_manifest(self):
        return self.package['manifest']

    def get_metadata(self):
        return self.package['science_metadata']

    def get_data(self):
        return self.package['data']

    def get_resource_map(self):
        return self.package['resource_map']



def main():
    return 0

if __name__ == "__main__":
    main()