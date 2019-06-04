# Standard library imports
import datetime as dt
import unittest
from unittest.mock import patch

# local imports
from schema_org.d1_client_manager import D1ClientManager


class TestD1ClientManager(unittest.TestCase):

    def setUp(self):
        self.gmn_base_url = 'https://localhost/gm'
        self.auth_cert = None
        self.auth_cert_key = None
        self.sysmeta_settings_dict = {}

    @unittest.skip('TODO')
    def test_get_last_harvest_time_with_objects_in_the_system(self):
        """
        SCENARIO:  There are valid objects in the system and we ask for the
        last harvest time.

        EXPECTED RESULT:  The last harvest time is earlier than logically
        possible.
        """
        patchee = (
            'schema_org'
            '.d1_client_manager.d1_client.mnclient_2_0'
            '.MemberNodeClient_2_0'
        )

        with patch(patchee, autospec=True) as client_mock:
            client_mock.return_value.listObjects.return_value.total = 1

            the_time = dt.datetime.now()
            client_mock.return_value.listObjects.return_value.objectInfo.return_value.dateSysMetadataModified = the_time  # noqa: E501

            client_mgr = D1ClientManager(self.gmn_base_url,
                                         self.auth_cert,
                                         self.auth_cert_key,
                                         self.sysmeta_settings_dict)
            time = client_mgr.get_last_harvest_time()
            print(time)

            self.assertEqual(time, '1900-01-01T00:00:00Z')

    def test_get_last_harvest_time_shows_no_objects_are_there(self):
        """
        SCENARIO:  There are no objects in the system and we ask for the last
        harvest time.

        EXPECTED RESULT:  The last harvest time is earlier than logically
        possible.
        """
        patchee = (
            'schema_org'
            '.d1_client_manager.d1_client.mnclient_2_0'
            '.MemberNodeClient_2_0'
        )

        with patch(patchee, autospec=True) as client_mock:
            client_mock.return_value.listObjects.return_value.total = 0

            client_mgr = D1ClientManager(self.gmn_base_url,
                                         self.auth_cert,
                                         self.auth_cert_key,
                                         self.sysmeta_settings_dict)
            time = client_mgr.get_last_harvest_time()

            self.assertEqual(time, '1900-01-01T00:00:00Z')

    def test_get_last_harvest_time_fails(self):
        """
        SCENARIO:  We fail to get the last harvest time.

        EXPECTED RESULT:  There are two calls to the logger at the error level.
        The system attempts to exit.
        """
        patchee = (
            'schema_org'
            '.d1_client_manager.d1_client.mnclient_2_0'
            '.MemberNodeClient_2_0.listObjects'
        )
        with patch(patchee) as mock_d1:

            # This causes the failure.
            mock_d1.side_effect = RuntimeError('something bad')

            with patch('schema_org.d1_client_manager.sys.exit') as exit_mock:
                with patch('schema_org.d1_client_manager.logging') as log_mock:

                    client_mgr = D1ClientManager(self.gmn_base_url,
                                                 self.auth_cert,
                                                 self.auth_cert_key,
                                                 self.sysmeta_settings_dict)
                    client_mgr.get_last_harvest_time()

                    self.assertEqual(exit_mock.call_count, 1)
                    self.assertEqual(log_mock.error.call_count, 2)
