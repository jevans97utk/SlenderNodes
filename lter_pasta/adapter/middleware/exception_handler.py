#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

'''
:mod:`exception_handler`
========================

:Synopsis:
  Catch, log and serialize any exceptions that are raised when processing a
  request.

  When running in Django production mode (settings.DEBUG = False), all
  exceptions are returned to the client as AdapterErrors serialized to XML.
  adapterErrors are thrown by any code in the adapter itself when an error is
  detected. When an AdapterError is caught here, it is serialized directly. When
  processing a request, Python, the standard library and 3rd party libraries can
  also throw exceptions. These are caught here, wrapped in an AdapterError and
  then serialized.

  When running in Django debug mode (settings.DEBUG = True), all exceptions are
  returned as Django HTML exception pages.

:Author: Roger Dahl
'''

# Stdlib.
import httplib
import logging
import os
import sys
import traceback

# Django.
from django.http import HttpResponse

# D1
import d1_common.types.exceptions

# App.
import settings
import pasta_gmn_adapter.api_types.adapter_error
import api_types.adapter_error


class exception_handler():
  def process_exception(self, request, exception):
    self.request = request
    self.exception = exception

    logging.exception('Exception:')

    if isinstance(exception, pasta_gmn_adapter.api_types.adapter_error.AdapterError):
      return self.serialize_adapter_exception()
    else:
      return self.handle_unknown_exception()


  def serialize_adapter_exception(self):
    exception_serialized = self.exception.serialize()
    return HttpResponse(exception_serialized,
                        status=self.exception.http_status_code,
                        content_type=d1_common.const.CONTENT_TYPE_XML)


  def serialize_dataone_exception_for_head_request(self):
    exception_headers = self.exception.serialize_to_headers()
    http_response = HttpResponse('', status=self.exception.errorCode,
                                 content_type=d1_common.const.CONTENT_TYPE_XML)
    for k, v in exception_headers:
      http_response[k] = v.encode('utf8')
    return http_response


  def handle_unknown_exception(self):
    if settings.DEBUG == True:
      return self.django_html_exception_page()
    else:
      return self.wrap_internal_exception_in_adapter_exception()


  def django_html_exception_page(self):
    # Returning None from the exception handler causes Django to generate
    # an HTML exception page.
    return None


  def wrap_internal_exception_in_adapter_exception(self):
    return api_types.adapter_error.AdapterError(
      description=self.traceback_to_text(),
      http_status_code=httplib.INTERNAL_SERVER_ERROR)


  def traceback_to_text(self):
    exception_type, exception_value, exception_traceback = sys.exc_info()
    tb = []
    while exception_traceback:
      co = exception_traceback.tb_frame.f_code
      tb.append('{0}({1})'.format(str(os.path.basename(co.co_filename)), str(traceback.tb_lineno(exception_traceback))))
      exception_traceback = exception_traceback.tb_next
    if not isinstance(exception_value, d1_common.types.exceptions.DataONEException):
      tb.append('Type: {0}'.format(exception_type))
      tb.append('Value: {0}'.format(exception_value))
    return '\n'.join(tb)
