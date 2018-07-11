# -*- coding: utf-8 -*-

# This work was created by participants in the DataONE project, and is
# jointly copyrighted by participating institutions in DataONE. For
# more information on DataONE, see our web site at http://dataone.org.
#
#   Copyright 2009-2016 DataONE
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Test subject extraction from certificate and SubjectInfo
"""

import responses

import schema_org
import pytest

class TestSchemaOrg:
  def test_1000(self):
    sitemap = "http://get.iedadata.org/sitemaps/usap_sitemap.xml"
    resource_list = schema_org.load_resources_from_sitemap(sitemap)

    print('Found resources: {}'.format(len(resource_list)))

    for resource_dict in resource_list:
      entry_dict = schema_org.load_schema_org(resource_dict)
      result = {**resource_dict, **entry_dict}
      try:
        print("{date_modified}, {url}, {id}, {metadata_url}".format(**result))
      except KeyError as e:
        print("{date_modified}, {url}, {error}".format(**result))
      break

