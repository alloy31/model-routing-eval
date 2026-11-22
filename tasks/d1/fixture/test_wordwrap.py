import unittest

from wordwrap import wrap


class WrapTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(wrap("aa bb cc", 6), ["aa bb", "cc"])

    def test_exact_fit(self):
        self.assertEqual(wrap("aa bb cc", 5), ["aa bb", "cc"])

    def test_empty(self):
        self.assertEqual(wrap("", 10), [])


if __name__ == "__main__":
    unittest.main()
