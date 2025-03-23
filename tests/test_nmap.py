import unittest
from unittest.mock import patch, MagicMock
from tools.nmap import scan_network

class TestNmap(unittest.TestCase):
    @patch("subprocess.run")
    def test_scan_network(self, mock_subprocess):
        # Mock the subprocess.run output
        mock_subprocess.return_value = MagicMock(stdout="Nmap scan report for 192.168.1.1")

        # Test the scan_network function
        target = "192.168.1.1"
        result = scan_network(target)

        # Assertions
        mock_subprocess.assert_called_once_with(f"nmap -sP {target}", shell=True, capture_output=True, text=True)
        self.assertIn("Nmap scan report", result)

if __name__ == "__main__":
    unittest.main()