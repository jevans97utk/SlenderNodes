#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: scimeta_bundle

:Synopsis:

:Author:
    servilla
  
:Created:
    3/4/16
"""

import logging
import StringIO

import requests

from d1_client import mnclient
from d1_common.types import dataoneTypes as d1_types


logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y%m%d-%H:%M:%S')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('sciemeta_bundle')

__author__ = "servilla"


MN_BASE_URL = 'https://ncei-node.dataone.org/mn'
CERTIFICATE_FOR_CREATE = '/Users/servilla/Certs/DataONE/urn_node_mnTestNCEI/urn_node_mnTestNCEI.crt'
CERTIFICATE_FOR_CREATE_KEY = '/Users/servilla/Certs/DataONE/urn_node_mnTestNCEI/private/urn_node_mnTestNCEI.key'


class Scimeta_Bundle(object):

    def __init__(self, doc=None, sysmeta_xml=None):

        if not doc or not sysmeta_xml:
            raise ValueError('Either science metadata "doc" or "sysmeta_xml" is None.')

        self.doc = doc
        self.sysmeta = d1_types.CreateFromDocument(sysmeta_xml)
        self.pid = self.sysmeta.identifier.value()
        pass

    def gmn_create(self):
        client = mnclient.MemberNodeClient(MN_BASE_URL,
                                           cert_path=CERTIFICATE_FOR_CREATE,
                                           key_path=CERTIFICATE_FOR_CREATE_KEY)
        client.create(self.pid, StringIO.StringIO(self.doc), self.sysmeta)

    def _get_scimeta(self, iso_url):
        iso = None
        try:
            iso = requests.get(iso_url)
        except (requests.RequestException,
                requests.ConnectionError,
                requests.HTTPError,
                requests.URLRequired,
                requests.TooManyRedirects,
                requests.Timeout) as e:
            logger.error('Error connecting to NCEI for CSW metadata - {0}'.format(e.message))
        else:
            if iso.status_code != requests.codes.ok:
                logger.error('NCEI CSW metadata response code not OK: {0}'.format(iso.status_code))
                raise ValueError('NCEI CSW metadata response code not OK: {0}'.format(iso.status_code))
            return iso.content


def main():
    return 0


if __name__ == "__main__":
    main()