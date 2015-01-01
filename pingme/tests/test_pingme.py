# pylint: disable=W0613,C0111,R0913

""" Run the tests for the pingme script."""

import unittest
from mock import patch
from pingme import pingme
import io


class PingmeTest(unittest.TestCase):
    """ Setup the test cases for the pingme script."""
    def __init__(self, *args, **kwargs):
        super(PingmeTest, self).__init__(*args, **kwargs)
        self.config_data = '[Default]\n' \
                           'devices=123456\n' \
                           'message=test message please ignore'

    @patch('sys.argv', return_value=[''])
    @patch('requests.post')
    @patch('os.access', return_value=True)
    @patch('os.path.isfile', return_value=True)
    @patch('__builtin__.open', return_value=io.BytesIO('[Default]\n'
                                                       'devices=123456\n'
                                                       'message=test message please ignore'))
    def test_send_ping_success(self, mock_file, mock_isfile, mock_access, mock_post, mock_argv):
        mock_post.return_value.status_code = 200
        with self.assertRaises(SystemExit) as excp:
            pingme.main()
        self.assertEqual(excp.exception.code, 0)

    @patch('sys.argv', return_value=[''])
    @patch('os.path.isfile', return_value=False)
    def test_send_ping_noarguments(self, mock_isfile, mock_argv):
        with self.assertRaises(SystemExit) as excp:
            pingme.main()
        self.assertEqual(excp.exception.code, 1)

    @patch('requests.post')
    def test_send_ping_server_error(self, mock_post):
        mock_post.return_value.status_code = 500
        with self.assertRaises(SystemExit) as excp:
            pingme.send_ping('123456', 'test message')
        self.assertEqual(excp.exception.code, 1)

    @patch('sys.argv', return_value=[''])
    @patch('os.access', return_value=True)
    @patch('os.path.isfile', return_value=True)
    @patch('__builtin__.open', return_value=io.BytesIO('[default]\n'
                                                       'devices=123456\n'
                                                       'message=test message please ignore'))
    def test_send_ping_badconfig(self, mock_file, mock_isfile, mock_access, mock_argv):
        with self.assertRaises(SystemExit) as excp:
            pingme.main()
        self.assertEqual(excp.exception.code, 1)
