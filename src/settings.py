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

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y%m%d-%H:%M:%S')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('settings')

__author__ = "servilla"


MN_BASE_URL = 'https://ncei-node.dataone.org/mn'
CERTIFICATE_FOR_CREATE = '/Users/servilla/Certs/DataONE/urn_node_mnTestNCEI/urn_node_mnTestNCEI.crt'
CERTIFICATE_FOR_CREATE_KEY = '/Users/servilla/Certs/DataONE/urn_node_mnTestNCEI/private/urn_node_mnTestNCEI.key'


def main():
    return 0


if __name__ == "__main__":
    main()