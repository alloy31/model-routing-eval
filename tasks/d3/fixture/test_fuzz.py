import random
import unittest

from rangetree import RangeTree


class Fuzz(unittest.TestCase):
    def test_against_naive(self):
        rng = random.Random(1234)
        for _ in range(150):
            n = rng.randint(1, 40)
            ref = [rng.randint(-50, 50) for _ in range(n)]
            tree = RangeTree(ref)
            for step in range(60):
                l = rng.randint(0, n)
                r = rng.randint(l, n)
                op = rng.choice(["add", "assign", "sum"])
                if op == "add":
                    v = rng.randint(-20, 20)
                    tree.range_add(l, r, v)
                    for i in range(l, r):
                        ref[i] += v
                elif op == "assign":
                    v = rng.randint(-20, 20)
                    tree.range_assign(l, r, v)
                    for i in range(l, r):
                        ref[i] = v
                else:
                    self.assertEqual(tree.range_sum(l, r), sum(ref[l:r]), f"n={n} step={step} sum[{l},{r})")


if __name__ == "__main__":
    unittest.main()
