import unittest

import durations


class Examples(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(durations.parse("1h30m"), 5400)
        self.assertEqual(durations.parse("1h 30m"), 5400)
        self.assertEqual(durations.parse("-1h30m"), -5400)
        self.assertEqual(durations.parse("1.5h"), 5400)
        with self.assertRaises(ValueError):
            durations.parse("30m1h")

    def test_format(self):
        self.assertEqual(durations.format(5400), "1h30m")
        self.assertEqual(durations.format(0), "0s")
        self.assertEqual(durations.format(14 * 86400), "2w")


if __name__ == "__main__":
    unittest.main()
