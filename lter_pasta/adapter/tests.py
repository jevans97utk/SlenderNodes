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
''':mod:`tests`
===============

:Synopsis:
  Unit tests for the adapter.

  May have to give the pasta_gmn_adapter user createdb permission:

  $ sudo -u postgres psql template1
  template1=# alter user pasta_gmn_adapter createdb

  Run the tests with: ./manage.py test

:Author:
  Roger Dahl
'''

# Django.
import django.utils.unittest
import django.test

# D1.
import d1_common.types.generated.dataoneTypes as dataoneTypes

# App.
import pasta_gmn_adapter.adapter.sql as sql
import pasta_gmn_adapter.adapter.management.commands.data_package_manager_client as pasta_client
import pasta_gmn_adapter.adapter.management.commands.process_population_queue as proc
import pasta_gmn_adapter.api_types.eml_access

TEST_EML_ACCESS_XML = '''<access:access xmlns:access="eml://ecoinformatics.org/access-2.1.0" authSystem="https://pasta.lternet.edu/authentication" order="allowFirst" system="https://pasta.lternet.edu">
  <allow>
    <principal>uid=dcosta,o=LTER,dc=ecoinformatics,dc=org</principal>
    <permission>changePermission</permission>
  </allow>
  <allow>
    <principal>uid=PIE,o=lter,dc=ecoinformatics,dc=org</principal>
    <permission>changePermission</permission>
  </allow>
  <allow>
    <principal>public</principal>
    <permission>read</permission>
  </allow>
</access:access>
'''


class TestSQL(django.test.TestCase):

  # Tried using setUpClass() to get Django to retain the table contents between
  # tests, but couldn't get it to work. Also tried forcing transactions to be
  # committed.
  @classmethod
  def setUpClass(cls):
    pass

  @classmethod
  def tearDownClass(cls):
    pass

  def setUp(self):
    # Create a blank copy of the database. This is equivalent to the fixures
    # Django would normally create from the models in models.py.
    create_sql = open('pasta_gmn_adapter.sql').read()
    cursor = django.db.connection.cursor()
    cursor.execute(create_sql)
    django.db.transaction.commit_unless_managed()

  def tearDown(self):
    pass

  def _populate_with_test_objects(self):
    sql.insert_population_queue_item('test_package', 111, 222)
    sql.insert_population_queue_item('test_package_2', 333, 444)
    sql.insert_population_queue_item('test_package_2', 333, 445)
    sql.insert_population_queue_item('test_package_3', 555, 666)

  def _add_processing_statuses(self):
    sql.insert_status()

  def test_100_insert_population_queue_item(self):
    self._populate_with_test_objects()
    q = sql.select_population_queue_all()
    self.assertEqual(len(q), 4)
    self.assertEqual(q[0]['package_identifier'], 111)
    self.assertEqual(q[2]['package_revision'], 445)
    self.assertEqual(q[3]['package_scope'], 'test_package_3')

  def test_110_select_population_queue_unprocessed(self):
    self._populate_with_test_objects()
    q = sql.select_population_queue_uncompleted()
    self.assertEqual(len(q), 4)

  def test_120_select_population_queue_all(self):
    self._populate_with_test_objects()
    q = sql.select_population_queue_all()
    self.assertEqual(len(q), 4)

  def test_130_insert_status_error(self):
    self._populate_with_test_objects()
    package_id = sql.select_population_queue_all()[1]['task_id']
    sql.insert_process_status(
      package_id, '_test_status', 404, 'test_return_body'
    )
    q = sql.select_population_queue_uncompleted()
    self.assertEqual(len(q), 4)

  def test_140_insert_status_completed(self):
    self._populate_with_test_objects()
    package_id = sql.select_population_queue_all()[1]['task_id']
    sql.insert_process_status(package_id, 'completed', 200, 'OK')
    q = sql.select_population_queue_uncompleted()
    self.assertEqual(len(q), 3)

  def test_150_insert_status_error(self):
    self._populate_with_test_objects()
    package_id = sql.select_population_queue_all()[1]['task_id']
    sql.insert_process_status(package_id, 'error', 404, 'test_return_body')
    q = sql.select_process_status_by_package_id('test_package_2', 333, 444)
    self.assertEqual(len(q), 1)
    self.assertEqual(q[0]['status'], 'error')
    self.assertEqual(q[0]['return_code'], 404)
    self.assertEqual(q[0]['return_body'], 'test_return_body')

  def test_160_select_latest_package_revision(self):
    self._populate_with_test_objects()
    self.assertEqual(
      sql.select_latest_package_revision('test_package_2', 333), 445
    )
    self.assertTrue(
      sql.select_latest_package_revision('test_package_2', 334) is None
    )
    self.assertTrue(
      sql.select_latest_package_revision('non_existing_package', 333) is None
    )


class TestDataPackageManagerClient(django.test.TestCase):
  @classmethod
  def setUpClass(self):
    self.c = pasta_client.DataPackageManagerClient()

  @classmethod
  def tearDownClass(self):
    pass

  def test_100_initialize(self):
    pass


class TestDataEMLAccess(django.test.TestCase):
  @classmethod
  def setUpClass(self):
    self.e = pasta_gmn_adapter.api_types.eml_access.EMLAccess(
      TEST_EML_ACCESS_XML
    )

  @classmethod
  def tearDownClass(self):
    pass

  def test_100_initialize(self):
    pass

  def test_200_eml_as_dataone(self):
    d = self.e.get_as_dataone_rules()
    self.assertTrue(isinstance(d, dataoneTypes.AccessPolicy))
