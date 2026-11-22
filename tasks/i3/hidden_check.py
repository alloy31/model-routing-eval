import itertools, json, pathlib, random, re, subprocess, sys, time
ws = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(ws))
items = {}
src = (ws / "rx.py").read_text() if (ws / "rx.py").exists() else ""
items["no_regex_lib"] = bool(src) and not re.search(
    r"^\s*(import\s+(re|regex|fnmatch|glob|importlib)\b|from\s+(re|regex|fnmatch|glob|importlib)\b)|__import__|\beval\s*\(|\bexec\s*\(", src, re.M)

def gen_atom(rng, depth):
    r = rng.random()
    if depth > 0 and r < 0.28:
        return "(" + gen_alt(rng, depth - 1) + ")"
    if r < 0.40:
        return rng.choice(["[ab]", "[^a]", "[a-c]", "[^b-c]", "[ac.]", "[b-b]", "[a-bx]"])
    if r < 0.48:
        return "."
    if r < 0.56:
        return rng.choice(["\\.", "\\*", "\\(", "\\|", "\\\\", "\\+", "\\["])
    return rng.choice("aaabbc")

def gen_rep(rng, depth):
    a = gen_atom(rng, depth)
    r = rng.random()
    if r < 0.40:
        q = rng.choice(["*", "+", "?", "*", "+", "?", "{2}", "{0}", "{1,}", "{0,2}", "{1,3}", "{2,2}", "{0,}", "{3}"])
        return a + q
    return a

def gen_cat(rng, depth):
    return "".join(gen_rep(rng, depth) for _ in range(rng.choice([0, 1, 1, 2, 2, 3, 4])))

def gen_alt(rng, depth):
    return "|".join(gen_cat(rng, depth) for _ in range(rng.choice([1, 1, 1, 2, 2, 3])))

rng = random.Random(20261115)
short = ["".join(t) for n in range(4) for t in itertools.product("ab", repeat=n)]
cases = []
for _ in range(450):
    p = gen_alt(rng, 3)
    texts = set(short)
    for _ in range(14):
        texts.add("".join(rng.choice("aaabbc.*(|\\+[x") for _ in range(rng.randint(0, 9))))
    for t in sorted(texts):
        cases.append((p, t, re.fullmatch(p, t) is not None))
fixed = [("", "", True), ("", "a", False), ("()", "", True), ("a|", "", True), ("(|b)a", "ba", True), ("a{0}", "", True),
         ("a{0}", "a", False), ("(a|b){2,}", "a", False), ("[a-c]{2,3}x?", "abcx", True), ("(ab|a)(bc|c)", "abc", True),
         ("\\\\", "\\", True), ("(a*)+", "", True), ("((a|)|b)*", "abab", True), ("(a{2}){2}", "aaaa", True), ("(a{2}){2}", "aaa", False),
         ("a{30}", "a" * 30, True), ("a{30}", "a" * 29, False), ("(a|b){0,30}c", "ab" * 15 + "c", True), ("[^a-c]+", "xyz", True)]
cases += fixed
import signal
class _TO(BaseException):
    pass
def _alarm(*a):
    raise _TO('differential >120s')
signal.signal(signal.SIGALRM, _alarm); signal.alarm(120)
try:
    import rx
    bad = []
    t0 = time.time()
    for p, t, exp in cases:
        try:
            got = rx.fullmatch(p, t)
        except Exception as e:
            got = f"EXC {type(e).__name__}"
        if got is not exp:
            bad.append((p, t, exp, str(got)))
            if len(bad) >= 8: break
    items["matches_re"] = not bad
    items["_bad"] = bad[:6]
    items["_n"] = len(cases); items["_sec"] = round(time.time() - t0, 1)
except BaseException as e:
    items["matches_re"] = False; items["_bad"] = [repr(e)[:200]]
signal.alarm(0)
PATHO = [("(a*)*b", "a" * 40, False), ("(a|aa)+c", "a" * 40, False), ("(a?){25}a{25}", "a" * 25, True),
         ("(a*)*", "a" * 1000, True), ("(.*)*x", "abc" * 20, False), ("((a+)+)+b", "a" * 35, False),
         ("(a|b|ab)*c", "ab" * 25, False), ("[a-c]*.{3}[^a]", "abc" * 300 + "b", True),
         ("(a{0,30}){0,30}b", "a" * 60, False), ("(x+x+)+y", "x" * 30, False)]
slow = []
for p, t, exp in PATHO:
    code = "import sys; sys.path.insert(0, %r); import rx; print(rx.fullmatch(%r, %r))" % (str(ws), p, t)
    try:
        r = subprocess.run([sys.executable, "-B", "-c", code], capture_output=True, text=True, timeout=3)
        if r.stdout.strip() != str(exp):
            slow.append((p, "wrong:" + (r.stdout.strip() or r.stderr.strip()[-80:])))
    except subprocess.TimeoutExpired:
        slow.append((p, "timeout"))
items["polynomial"] = not slow
items["_slow"] = slow[:6]
print(json.dumps(items, ensure_ascii=False))
