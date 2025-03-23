import unittest
from unittest.mock import patch
from john import run_john

class TestJohn(unittest.TestCase):
    @patch('subprocess.run')
    def test_run_john_success(self, mock_run):
        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = 'Loaded 1 password hash (descrypt, traditional crypt(3) [DES 128/128 AVX])'
        result = run_john('passwords.txt')
        self.assertIn('Loaded', result)

    @patch('subprocess.run')
    def test_run_john_failure(self, mock_run):
        mock_run.return_value.returncode = 1
        mock_run.return_value.stderr = 'No such file or directory'
        result = run_john('nonexistent.txt')
        self.assertIn('No such file or directory', result)

if __name__ == '__main__':
    unittest.main()