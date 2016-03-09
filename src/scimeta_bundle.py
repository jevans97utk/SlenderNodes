#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: scimeta_bundle

:Synopsis:
    To aggregate science metadata and system metadata for insertion into the
    NCEI GMN member node.

:Author:
    servilla
  
:Created:
    3/4/16
"""

import logging
import StringIO

from d1_client import mnclient
from d1_common.types import dataoneTypes as d1_types

import settings

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y%m%d-%H:%M:%S')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('sciemeta_bundle')

__author__ = "servilla"



class Scimeta_Bundle(object):

    def __init__(self, doc=None, sysmeta_xml=None):

        if not doc or not sysmeta_xml:
            raise ValueError('Either science metadata "doc" or "sysmeta_xml" is None.')

        self.doc = doc
        self.sysmeta = d1_types.CreateFromDocument(sysmeta_xml)
        self.pid = self.sysmeta.identifier.value()

    def get_sysmeta_binding(self):
        """Returns the pyxb XML binding for an XML system metadata document.

        :return: pyxb XML binding
        """
        return self.sysmeta

    def gmn_create(self):
        """Create a new science metadata object into the NCEI GMN

        :return: None
        """
        try:
            client = mnclient.MemberNodeClient(settings.MN_BASE_URL,
                                               cert_path=settings.CERTIFICATE_FOR_CREATE,
                                               key_path=settings.CERTIFICATE_FOR_CREATE_KEY)
            client.create(self.pid, StringIO.StringIO(self.doc), self.sysmeta)
        except Exception as e:
            logger.error('GMN create error in science metadata bundle: {0}'.format(e.message))

    def gmn_update(self, old_pid):
        """Update an existing science metadata object with a new science
           metadata object in the NCEI GMN - requires the previous pid to set
           obsolescence chain.

        :param old_pid: String
        :return: None
        """
        try:
            client = mnclient.MemberNodeClient(settings.MN_BASE_URL,
                                               cert_path=settings.CERTIFICATE_FOR_CREATE,
                                               key_path=settings.CERTIFICATE_FOR_CREATE_KEY)
            client.update(old_pid, StringIO.StringIO(self.doc), self.pid, self.sysmeta)
        except Exception as e:
            logger.error('GMN update error in science metadata bundle: {0}'.format(e.message))



def main():
    return 0


if __name__ == "__main__":
    main()