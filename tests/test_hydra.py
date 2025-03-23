import unittest
from tools.hydra import brute_force

class TestHydra(unittest.TestCase):
    def test_brute_force(self):
        # Test the brute_force function
        target = "192.168.1.10"
        service = "ssh"
        username = "admin"
        wordlist = "wordlist.txt"
        result = brute_force(target, service, username, wordlist)

        # Assertions
        self.assertEqual(result, "Brute force successful")

if __name__ == "__main__":
    unittest.main()