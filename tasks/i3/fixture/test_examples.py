import unittest

import rx


class Examples(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(rx.fullmatch("ab*c", "abbbc"))
        self.assertFalse(rx.fullmatch("ab*c", "abbb"))
        self.assertTrue(rx.fullmatch("(a|b)+", "abba"))
        self.assertTrue(rx.fullmatch("[a-c]{2,3}x?", "cab"))
        self.assertFalse(rx.fullmatch("[^a-c]", "b"))
        self.assertTrue(rx.fullmatch("a\\.b", "a.b"))
        self.assertTrue(rx.fullmatch("(|b)a", "a"))
        self.assertTrue(rx.fullmatch("", ""))

    def test_no_blowup(self):
        self.assertFalse(rx.fullmatch("(a*)*b", "a" * 40))


if __name__ == "__main__":
    unittest.main()
