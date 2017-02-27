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
''':mod:`views.admin`
=====================

:Synopsis:
  Administrator functionality.
:Author: Roger Dahl
'''
# Stdlib.

# Django.
from django.shortcuts import render_to_response
from django.http import HttpResponse

# D1.
import d1_common.const

# App.
import adapter.restrict_to_verb
import adapter.sql
import settings

# ------------------------------------------------------------------------------
# Admin portal.
# ------------------------------------------------------------------------------


@adapter.restrict_to_verb.get
def admin(request):
  if settings.GMN_ADAPTER_DEBUG:
    if 'clear_database' in request.GET:
      adapter.sql.clear_database()
  return render_to_response(
    'admin.html', {'debug': settings.GMN_ADAPTER_DEBUG},
    content_type=d1_common.const.CONTENT_TYPE_XHTML
  )

# Statistics


@adapter.restrict_to_verb.get
def get_statistics(request):
  p = adapter.sql.select_statistics()
  return render_to_response(
    'statistics.xml', {'statistics': p},
    content_type=d1_common.const.CONTENT_TYPE_XML
  )


@adapter.restrict_to_verb.get
def get_statistics_xsl(request):
  return render_to_response(
    'statistics.xsl', content_type=d1_common.const.CONTENT_TYPE_XML
  )

# Population Queue


@adapter.restrict_to_verb.get
def get_population_queue(request):
  if 'excludecompleted' in request.GET:
    p = adapter.sql.select_population_queue_with_latest_status_uncompleted()
  else:
    p = adapter.sql.select_population_queue_with_latest_status()
  #return HttpResponse(p)
  return render_to_response(
    'population_queue.xml', {'population_queue': p},
    content_type=d1_common.const.CONTENT_TYPE_XML
  )


@adapter.restrict_to_verb.get
def get_population_queue_xsl(request):
  return render_to_response(
    'population_queue.xsl', content_type=d1_common.const.CONTENT_TYPE_XML
  )

# Status


@adapter.restrict_to_verb.get
def get_status(request, population_queue_id):
  p = adapter.sql.select_status(population_queue_id)
  return render_to_response(
    'status.xml', {'status': p}, content_type=d1_common.const.CONTENT_TYPE_XML
  )


@adapter.restrict_to_verb.get
def get_status_xsl(request):
  return render_to_response(
    'status.xsl', content_type=d1_common.const.CONTENT_TYPE_XML
  )
