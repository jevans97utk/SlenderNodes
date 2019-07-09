# Standard library imports
import datetime as dt
import json
import unittest
from unittest.mock import patch

# 3rd party libraries
import requests

# Local imports
import schema_org


class MockRequestsResponse(object):
    """
    Mock out the actions of the response of a requests.get operation.  The
    expected sequence of events in a "good" requests.get operation would be

    >>> r = requests.get(url)
    >>> r.content

    Attributes
    ----------
    content, text, status_code, elapsed
        Corresponds to the same items in a requests.Response object
    """
    def __init__(self, content=None, status_code=200, headers=None):
        """
        """
        self.content = content

        # Allow for the possibility of a text response.
        try:
            self.text = content.decode('utf-8')
        except (AttributeError, UnicodeDecodeError):
            # AttributeError if content was None, UnicodeDecodeError if the
            # content was binary.
            self.text = ''

        # We might have a JSON response as well.
        try:
            self._json = json.loads(content.decode('utf-8'))
        except AttributeError:
            # AttributeError if content was None.
            self._json = None
        except UnicodeDecodeError:
            # UnicodeDecodeError if the content was binary.
            self._json = None
        except json.decoder.JSONDecodeError:
            self._json = None

        self.headers = headers
        self.status_code = status_code
        self.elapsed = dt.timedelta(seconds=1)

    def raise_for_status(self):
        """
        Mock out the following sequence of events.

        >>> r = requests.get(bad url)
        >>> r.raise_for_status()
        """
        if self.status_code != 200:
            raise requests.HTTPError('bad url')

    def json(self):
        """
        Mock out these sequence of events.

        >>> r = requests.get(blahblahblah)
        >>> r.json()
        """
        return self._json


class TestCommon(unittest.TestCase):

    def setup_requests_session_patcher(self,
                                       contents=None,
                                       status_codes=None,
                                       headers=None):
        """
        Mock out the outcome of calling 'requests.Session.get'
        """
        if contents is None and status_codes is None:
            msg = 'not both contents and status_codes can be none.'
            raise RuntimeError(msg)

        # But if only "contents" was provided, assume all the status codes
        # are good.
        if status_codes is None:
            status_codes = [200 for item in contents]

        if contents is None:
            contents = [None for item in status_codes]

        if headers is None:
            headers = [{'Content-Type': 'text/html'} for _ in contents]

        items = zip(contents, status_codes, headers)
        side_effect = [
            MockRequestsResponse(content=content,
                                 status_code=status_code,
                                 headers=headers)
            for content, status_code, headers in items
        ]

        patchee = 'schema_org.common.requests.Session.get'
        self.session_patcher = patch(patchee, side_effect=side_effect)
        self.addCleanup(self.session_patcher.stop)
        self.session_patcher.start()

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

    def assertErrorCount(self, cm_output, n=1):
        """
        Verify we see this many log messages with ERROR.
        """
        error_count = sum(msg.startswith('ERROR') for msg in cm_output)
        self.assertEqual(error_count, 1)
