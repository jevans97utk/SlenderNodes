# Standard library imports
import unittest

# 3rd party libraries
import requests_mock

# Local imports
import schema_org


class TestCommon(unittest.TestCase):

    def assertSuccessfulIngest(self, cm_output, n=1):
        """
        Verify the successful ingest.  There will be messages logged at the
        INFO level, and one of them must be the successful ingest message.

        Parameters
        ----------
        n : int
            Number of successful ingests.
        """
        # print('\n'.join(cm_output))

        info_msgs = [msg for msg in cm_output if msg.startswith('INFO')]
        self.assertTrue(len(info_msgs) > 1)

        successful_ingest = [
            msg.find(schema_org.common.SUCCESSFUL_INGEST_MESSAGE) > -1
            for msg in info_msgs
        ]
        self.assertEqual(sum(successful_ingest), n,
                         f"Did not verify {n} records successfully ingested.")

    def assertLogMessage(self, cm_output, expected_message, level='ERROR'):
        """
        Verify we see this log message with the given level.

        Parameters
        ----------
        cm_output : list of str
            Provided by assertLogs
        expected_message : str
            Look for this message in the cm_output
        level : optional, str
            Specify the log level.
        """
        count = sum(
            msg.startswith(level)
            for msg in cm_output
            if expected_message in msg
        )

        message = (
            f"Did not find \"{expected_message}\" in the logs at level {level}"
        )
        self.assertTrue(count >= 1, message)

    def assertLogLevelCallCount(self, cm_output, level='ERROR', n=1,
                                tokens=None, debug=False):
        """
        Verify we see this many log messages with the specified level.

        Parameters
        ----------
        tokens : str or list
            Verify that these strings appear in the messages.
        """
        if debug:
            print('\n'.join(cm_output))
        msgs = [msg for msg in cm_output if msg.startswith(level)]
        actual_count = len(msgs)

        if actual_count > 0:
            printable = '\n'.join(msgs)
            msg = (
                f"Detected messages a log level {level} are as follows:"
                "\n\n"
                f"{printable}"
            )
        else:
            msg = ''
        self.assertEqual(actual_count, n, msg)

        # Check the tokens
        if tokens is None:
            return

        if isinstance(tokens, str):
            tokens = [tokens]

        for token in tokens:
            count = sum(msg.find(token) > -1 for msg in msgs)
            self.assertTrue(count >= 1, f"Failed to verify token {token}")

    def setUpRequestsMocking(self, harvester, contents=None, status_codes=None,
                             headers=None, protocol='https'):
        """
        """
        if contents is None and status_codes is None:
            msg = 'not both contents and status_codes can be none.'
            raise RuntimeError(msg)

        if status_codes is None:
            status_codes = [200 for item in contents]

        if contents is None:
            contents = [None for item in status_codes]

        # This will work for headers in most cases.
        if headers is None:
            headers = [{'Content-Type': 'text/html'} for item in contents]

        adapter = requests_mock.Adapter()
        harvester.session.mount(f'{self.protocol}://', adapter)

        z = zip(contents, status_codes, headers)
        response_list = [
            {
                'content': content,
                'status_code': status_code,
                'headers': headers,
            }
            for content, status_code, headers in z
        ]

        adapter.register_uri(requests_mock.ANY, requests_mock.ANY,
                             response_list=response_list)
