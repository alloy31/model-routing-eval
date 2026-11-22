import unittest

from shiplane import settings
from shiplane.pricing import quote


class PricingTest(unittest.TestCase):
    def setUp(self):
        self.s = settings.load("dev")

    def test_min_charge(self):
        self.assertEqual(quote("60601", 0.1, self.s), 652)

    def test_west(self):
        self.assertEqual(quote("90210", 2.0, self.s), 1061)

    def test_rounds_weight_up(self):
        self.assertEqual(quote("10001", 1.2, self.s), quote("10001", 1.5, self.s))


if __name__ == "__main__":
    unittest.main()
