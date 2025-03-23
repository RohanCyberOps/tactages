import unittest
from Nikto import run_nikto

class TestNikto(unittest.TestCase):
    def test_run_nikto(self):
        target = "http://testphp.vulnweb.com"
        try:
            run_nikto(target)
        except Exception as e:
            self.fail(f"run_nikto() raised {e} unexpectedly!")

if __name__ == "__main__":
    unittest.main()