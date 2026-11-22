import unittest

import tax


class TaxTest(unittest.TestCase):
    def test_rate(self):
        self.assertEqual(tax.rate_bp("KR", "general"), 1000)
        self.assertEqual(tax.rate_bp("US", "food"), 200)


if __name__ == "__main__":
    unittest.main()
