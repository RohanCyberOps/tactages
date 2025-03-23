import unittest
from SQLMap import run_sqlmap

class TestSQLMap(unittest.TestCase):
    def test_run_sqlmap(self):
        url = "http://testphp.vulnweb.com"
        try:
            run_sqlmap(url)
        except Exception as e:
            self.fail(f"run_sqlmap() raised {e} unexpectedly!")

if __name__ == "__main__":
    unittest.main()