import unittest
from unittest.mock import patch, MagicMock
from tools.wireshark import capture_traffic

class TestWireshark(unittest.TestCase):
    @patch("subprocess.run")
    def test_capture_traffic(self, mock_subprocess):
        # Mock the subprocess.run output
        mock_subprocess.return_value = MagicMock(stdout="Capturing on 'eth0'")

        # Test the capture_traffic function
        interface = "eth0"
        duration = 10
        result = capture_traffic(interface, duration)

        # Assertions
        mock_subprocess.assert_called_once_with(f"tshark -i {interface} -a duration:{duration}", shell=True, capture_output=True, text=True)
        self.assertIn("Capturing", result)

if __name__ == "__main__":
    unittest.main()