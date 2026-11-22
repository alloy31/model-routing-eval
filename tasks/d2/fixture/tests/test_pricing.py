import unittest

import pricing


class PricingTest(unittest.TestCase):
    def test_bulk_discount(self):
        self.assertEqual(pricing.unit_price("B200", 10), 4322)

    def test_currency_switch(self):
        self.assertEqual(pricing.unit_price("A100", 1), 1200)
        self.assertEqual(pricing.unit_price("A100", 1, currency="KRW"), 1620000)


if __name__ == "__main__":
    unittest.main()
