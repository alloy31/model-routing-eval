import json, pathlib, random, sys, time
ws = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(ws)); sys.setrecursionlimit(10000)
from rangetree import RangeTree
items = {}
def fuzz(seed, ops, rounds=120, nmax=50):
    rng = random.Random(seed)
    for _ in range(rounds):
        n = rng.randint(1, nmax)
        ref = [rng.randint(-50, 50) for _ in range(n)]
        t = RangeTree(ref)
        for _ in range(80):
            l = rng.randint(0, n); r = rng.randint(l, n); op = rng.choice(ops)
            if op == "add":
                v = rng.randint(-20, 20); t.range_add(l, r, v)
                for i in range(l, r): ref[i] += v
            elif op == "assign":
                v = rng.randint(-20, 20); t.range_assign(l, r, v)
                for i in range(l, r): ref[i] = v
            elif op == "sum":
                if t.range_sum(l, r) != sum(ref[l:r]): return False
            elif l < r:
                if t.range_min(l, r) != min(ref[l:r]): return False
    return True
def safe(fn):
    try:
        return bool(fn())
    except Exception:
        return False
items["sum_ops"] = safe(lambda: all(fuzz(s, ["add", "assign", "sum"]) for s in (11, 12, 13)))
items["min_ops"] = safe(lambda: all(fuzz(s, ["add", "assign", "min"]) for s in (21, 22, 23)))
items["all_ops"] = safe(lambda: all(fuzz(s, ["add", "assign", "sum", "min"]) for s in (31, 32, 33, 34)))
def empty():
    t = RangeTree([3, 1, 2])
    if t.range_sum(1, 1) != 0: return False
    try:
        t.range_min(2, 2)
    except ValueError:
        return True
    return False
items["empty_range"] = safe(empty)
def perf():
    rng = random.Random(5); n = 20000
    t = RangeTree([rng.randint(-9, 9) for _ in range(n)]); t0 = time.time()
    for _ in range(20000):
        l = rng.randint(0, n - 1); r = rng.randint(l + 1, n); k = rng.randint(0, 3)
        if k == 0: t.range_add(l, r, 3)
        elif k == 1: t.range_assign(l, r, -2)
        elif k == 2: t.range_sum(l, r)
        else: t.range_min(l, r)
    return time.time() - t0 < 12
items["log_time"] = safe(perf)
ref = (pathlib.Path(__file__).resolve().parent / "fixture" / "test_fuzz.py").read_text()
items["test_untouched"] = (ws / "test_fuzz.py").read_text() == ref
print(json.dumps(items))
