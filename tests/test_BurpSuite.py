import unittest
from BurpSuite import run_burpsuite

class TestBurpSuite(unittest.TestCase):
    def test_run_burpsuite(self):
        try:
            run_burpsuite()
        except Exception as e:
            self.fail(f"run_burpsuite() raised {e} unexpectedly!")

if __name__ == "__main__":
    unittest.main()