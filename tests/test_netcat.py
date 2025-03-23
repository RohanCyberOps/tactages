import unittest
from unittest.mock import patch
from netcat import run_netcat

class TestNetcat(unittest.TestCase):
    @patch('subprocess.run')
    def test_run_netcat_success(self, mock_run):
        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = 'Connection to localhost 80 port [tcp/http] succeeded!'
        result = run_netcat('localhost', '80')
        self.assertIn('succeeded', result)

    @patch('subprocess.run')
    def test_run_netcat_failure(self, mock_run):
        mock_run.return_value.returncode = 1
        mock_run.return_value.stderr = 'Connection to localhost 9999 port [tcp/*] failed: Connection refused'
        result = run_netcat('localhost', '9999')
        self.assertIn('failed', result)

if __name__ == '__main__':
    unittest.main()