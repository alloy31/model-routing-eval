import unittest

import shipping


class ShippingTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(shipping.estimate("near", 1.0), 420)
        self.assertEqual(shipping.estimate("far", 2.0), 1040)


if __name__ == "__main__":
    unittest.main()
