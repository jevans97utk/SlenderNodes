import os
import sys

# Discover the path of this module
_here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

# Adding "." to the sys path here allows the folder that this file is in to be
# used as the root of import statements.
sys.path.append(_here('.'))
sys.path.append(_here('..'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'pasta_gmn_adapter.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
