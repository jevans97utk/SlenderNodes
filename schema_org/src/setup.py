#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This work was created by participants in the DataONE project, and is
# jointly copyrighted by participating institutions in DataONE. For
# more information on DataONE, see our web site at http://dataone.org.
#
#   Copyright 2013-2019 DataONE
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
"""DataONE Schema.org package
"""
from setuptools import setup

kwargs = {
    'name': 'schema_org',
    'version': '4.0.0',
    'description': 'Interact with a schema.org resource provider',
    'author': 'DataONE Project',
    'author_email': 'developers@dataone.org',
    'url': 'https://github.com/DataONEorg/d1_python',
    'license': 'Apache License, Version 2.0',
    'packages': ['schema_org'],
    'package_date': {'schema_org': ['data/*.ttl']},
    'install_requires': [
        'aiohttp', 'aioresponses', 'dataone.scimeta', 'importlib_resources',
        'lxml', 'python-dateutil', 'requests', 'requests_mock',
    ],
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    'keywords': (
        'DataONE schema.org'
    ),
    'entry_points': {
        'console_scripts': [
            'dataone-validate=schema_org.commandline:validate',
            'd1-check-site=schema_org.commandline:d1_check_site',
            'd1-check-html=schema_org.commandline:d1_check_html',
            'harvest-arm=schema_org.commandline:arm',
            'harvest-ieda=schema_org.commandline:ieda',
        ],
    }
}
setup(**kwargs)
