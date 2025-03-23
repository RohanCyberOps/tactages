import unittest
from tools.metasploit import exploit

class TestMetasploit(unittest.TestCase):
    def test_exploit(self):
        # Test the exploit function
        target = "192.168.1.10"
        payload = "windows/meterpreter/reverse_tcp"
        result = exploit(target, payload)

        # Assertions
        self.assertEqual(result, "Exploit successful")

if __name__ == "__main__":
    unittest.main()