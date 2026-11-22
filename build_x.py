"""순수 추론(도구 없음) 문항 생성기. 정답은 전부 코드 실행으로 만든다."""
import contextlib, io, itertools, json, pathlib, random
from fractions import Fraction
T = pathlib.Path(__file__).resolve().parent / "tasks"

def run(src):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(src, {})
    return buf.getvalue().strip()

ITEMS = []
def add(tid, level, desc, body, answer, kind="exact"):
    ITEMS.append(dict(id=tid, level=level, desc=desc, body=body, answer=str(answer), kind=kind))

TRACE_HEAD = "아래 파이썬 3 프로그램을 실행하면 표준 출력에 정확히 무엇이 찍히는가? 코드를 실행할 수 없으니 머리로 추적하라.\n\n```python\n{src}\n```\n"

# x1 — 클로저·기본 인자 (쉬움)
s1 = '''fs = []
for i in range(4):
    def f(x, i=i, acc=[]):
        acc.append(x + i)
        return sum(acc)
    fs.append(f)
g = [lambda x: x * j for j in range(3)]
print([fs[1](2), fs[1](3), fs[3](1), g[0](5), g[2](5)])'''
add("x1", 2, "클로저·가변 기본 인자 추적", TRACE_HEAD.format(src=s1), run(s1))

# x2 — 제너레이터 send/throw/finally
s2 = '''def gen():
    total = 0
    try:
        while True:
            try:
                x = yield total
                if x is None:
                    x = 1
                total += x
                if total > 10:
                    return total * 2
            except ValueError as e:
                total -= int(str(e))
            finally:
                total += 1
    finally:
        log.append(("closed", total))

log = []
g = gen()
log.append(next(g))
log.append(g.send(3))
log.append(g.throw(ValueError("2")))
log.append(next(g))
try:
    log.append(g.send(7))
except StopIteration as s:
    log.append(("stop", s.value))
print(log)'''
add("x2", 3, "제너레이터 send/throw/finally 순서 추적", TRACE_HEAD.format(src=s2), run(s2))

# x3 — 긴 산술 시뮬레이션
s3 = '''def h(s):
    a, b = 7, 3
    for ch in s:
        a = (a * 31 + ord(ch)) % 1009
        b = ((b ^ a) * 17) % 997
        if a % 3 == 0:
            a, b = b, a
    return a * 1000 + b

print(h("orchestrate"))'''
add("x3", 4, "11회 반복 모듈러·XOR 해시 손계산", TRACE_HEAD.format(src=s3), run(s3))

# x4 — 정수론 개수 세기
n4 = sum(1 for a in range(1, 201) for b in range(1, 201) if (a * a + b * b) % 91 == 0)
add("x4", 4, "a²+b²≡0 (mod 91) 순서쌍 개수", "1 ≤ a ≤ 200, 1 ≤ b ≤ 200 인 정수 순서쌍 (a, b) 가운데 a² + b² 이 91의 배수인 것은 모두 몇 개인가?\n", n4)

# x5 — 함정: 존재하지 않는 값
def Z(n):
    z = 0
    while n:
        n //= 5; z += n
    return z
hits = [n for n in range(1, 20000) if Z(n) == 2028]
assert not hits and Z(8124) == 2026 and Z(8125) == 2030
add("x5", 3, "n! 끝자리 0이 정확히 2028개 — 존재하지 않음을 알아채기", "n! (n 팩토리얼)을 십진법으로 썼을 때 끝에 연속으로 붙는 0의 개수가 정확히 2028개인 양의 정수 n 가운데 가장 작은 것은? 그런 n이 없으면 NONE 이라고 답하라.\n", "NONE")

# x6 — 3문자 패턴 경주 (정확한 마르코프 연쇄)
def race(p1, p2, alphabet="ABC"):
    pats = [p1, p2]
    states = sorted({p[:i] for p in pats for i in range(len(p) + 1)}, key=lambda s: (len(s), s))
    def step(s, c):
        t = s + c
        while t not in states:
            t = t[1:]
        return t
    idx = {s: i for i, s in enumerate(states)}
    trans = [s for s in states if s not in pats]
    n = len(trans); ti = {s: i for i, s in enumerate(trans)}
    A = [[Fraction(0)] * (n + 1) for _ in range(n)]
    for s in trans:
        i = ti[s]; A[i][i] += 1
        for c in alphabet:
            t = step(s, c)
            if t == p1: A[i][n] += Fraction(1, len(alphabet))
            elif t == p2: pass
            else: A[i][ti[t]] -= Fraction(1, len(alphabet))
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        A[col] = [v / A[col][col] for v in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                A[r] = [a - A[r][col] * b for a, b in zip(A[r], A[col])]
    return A[ti[""]][n]
p6 = race("ABA", "BAA")
# 몬테카를로로 교차 검증
rng = random.Random(1); w = 0; N = 200000
for _ in range(N):
    s = ""
    while True:
        s = (s + rng.choice("ABC"))[-3:]
        if s == "ABA": w += 1; break
        if s == "BAA": break
assert abs(w / N - float(p6)) < 0.01, (w / N, p6)
add("x6", 4, "3문자 무작위열에서 ABA가 BAA보다 먼저 나올 확률", "A, B, C 세 글자가 각각 확률 1/3로 독립적으로 이어지는 무한 문자열이 있다. 연속 부분 문자열 \"ABA\"가 \"BAA\"보다 먼저 나타날 확률을 기약분수로 답하라 (예: 3/7).\n", f"{p6.numerator}/{p6.denominator}", kind="fraction")

# x7 — 3×5 타일링 (도미노 + L-트로미노)
def tilings(R, C):
    full = R * C
    shapes = [[(0, 0), (0, 1)], [(0, 0), (1, 0)],
              [(0, 0), (0, 1), (1, 0)], [(0, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (1, 1)], [(0, 0), (1, 0), (1, -1)]]
    from functools import lru_cache
    @lru_cache(None)
    def go(mask):
        if mask == (1 << full) - 1: return 1
        pos = next(i for i in range(full) if not mask >> i & 1)
        r, c = divmod(pos, C); tot = 0
        for sh in shapes:
            m = 0; ok = True
            for dr, dc in sh:
                rr, cc = r + dr, c + dc
                if not (0 <= rr < R and 0 <= cc < C) or (mask | m) >> (rr * C + cc) & 1: ok = False; break
                m |= 1 << (rr * C + cc)
            if ok: tot += go(mask | m)
        return tot
    return go(0)
assert tilings(2, 2) == 2 + 4 * 0 and tilings(2, 3) == 3 + 2  # 2x3: 도미노 3가지 + L 두 개 조합 2가지
t7 = tilings(3, 5)
add("x7", 5, "3×5 격자의 도미노+L-트로미노 타일링 수", "3행 5열 격자를 1×2 도미노(가로·세로 모두 가능)와 L-트로미노(2×2 정사각형에서 한 칸을 뺀 3칸 모양, 네 방향 회전 모두 가능)로 겹치지 않게 빈틈없이 덮는 방법은 모두 몇 가지인가? 두 종류를 섞어 써도 되고 한 종류만 써도 된다. 놓인 조각의 위치·방향이 하나라도 다르면 다른 방법이다.\n", t7)

# x8 — 금지 부분문자열 회피 이진열 개수
n8 = sum(1 for bits in itertools.product("01", repeat=16) if "0101" not in (s := "".join(bits)) and "1100" not in s)
add("x8", 5, "길이 16 이진열 중 0101·1100 회피 개수", "길이가 16인 이진 문자열(0과 1로만 이루어짐) 가운데, 연속 부분 문자열로 \"0101\"도 \"1100\"도 포함하지 않는 것은 모두 몇 개인가?\n", n8)

# x9 — 유일해 좌석 퍼즐 (후보 조건 풀에서 탐색, 전수 검증, 모든 조건이 필수인 최소 집합)
people = "ABCDEFG"
POOL = [
    ("A는 양 끝자리에 앉지 않는다", lambda p: p["A"] not in (1, 7)),
    ("B는 C보다 왼쪽에 앉는다", lambda p: p["B"] < p["C"]),
    ("D와 E 사이에는 정확히 두 사람이 앉는다", lambda p: abs(p["D"] - p["E"]) == 3),
    ("F는 A의 바로 옆에 앉지 않는다", lambda p: abs(p["F"] - p["A"]) != 1),
    ("G는 B의 바로 오른쪽에 앉거나 맨 오른쪽 끝에 앉는데, 둘 다는 아니다", lambda p: (p["G"] == p["B"] + 1) != (p["G"] == 7)),
    ("C가 짝수 번 자리에 앉으면 E는 홀수 번 자리에 앉는다", lambda p: p["C"] % 2 == 1 or p["E"] % 2 == 1),
    ("A는 D보다 오른쪽에 앉는다", lambda p: p["A"] > p["D"]),
    ("E와 F 사이에는 정확히 한 사람이 앉는다", lambda p: abs(p["E"] - p["F"]) == 2),
    ("B는 1번 자리에 앉지 않는다", lambda p: p["B"] != 1),
    ("C와 A 사이에는 적어도 두 사람이 앉는다", lambda p: abs(p["C"] - p["A"]) >= 3),
    ("G의 자리 번호는 F의 자리 번호보다 크다", lambda p: p["G"] > p["F"]),
    ("D는 4번 자리에 앉지 않는다", lambda p: p["D"] != 4),
    ("B와 E의 자리 번호의 합은 홀수다", lambda p: (p["B"] + p["E"]) % 2 == 1),
    ("F가 A보다 왼쪽에 앉으면 C는 G보다 왼쪽에 앉는다", lambda p: p["F"] > p["A"] or p["C"] < p["G"]),
    ("가운데(4번) 자리에는 A, C, E 가운데 한 사람이 앉는다", lambda p: 4 in (p["A"], p["C"], p["E"])),
    ("D와 G는 서로 바로 옆에 앉지 않는다", lambda p: abs(p["D"] - p["G"]) != 1),
]
def solve(cs):
    out = []
    for perm in itertools.permutations(range(1, 8)):
        p = dict(zip(people, perm))
        if all(f(p) for _, f in cs):
            out.append("".join(sorted(people, key=lambda k: p[k])))
    return out
best = None
for seed in range(400):
    rng = random.Random(seed); order = POOL[:]; rng.shuffle(order)
    cs = []; cur = solve(cs)
    for c in order:
        nxt = solve(cs + [c])
        if 1 <= len(nxt) < len(cur):
            cs.append(c); cur = nxt
        if len(cur) == 1: break
    if len(cur) != 1: continue
    cs = [c for c in cs]  # 불필요 조건 제거
    for c in cs[:]:
        rest = [d for d in cs if d is not c]
        if len(solve(rest)) == 1: cs = rest
    # 가장 덜 풀리는(단일 조건 제거 시 해가 가장 적게 늘어나는=촘촘한) 큰 집합을 고른다
    if best is None or len(cs) > len(best[0]):
        best = (cs, cur)
cons, sols = best
cons = sorted(cons, key=lambda c: [t for t, _ in POOL].index(c[0]))
assert solve(cons) == sols and len(sols) == 1
print("x9 constraints:", len(cons), "solution:", sols)

def emit():
    for it in ITEMS:
        d = T / it["id"]; d.mkdir(parents=True, exist_ok=True)
        (d / "task.json").write_text(json.dumps(dict(id=it["id"], family="추론", level=it["level"], desc=it["desc"], tools="none", budget=2.5, timeout=1500), ensure_ascii=False))
        (d / "prompt.md").write_text(it["body"] + "\n풀이는 자유롭게 쓰되, 응답의 마지막 줄은 반드시 `ANSWER: <답>` 형식 한 줄이어야 한다.\n")
        (d / "grade.py").write_text(GRADER.replace("__ANS__", repr(it["answer"])).replace("__KIND__", repr(it["kind"])))
        print(it["id"], "L%d" % it["level"], it["desc"], "=>", it["answer"])

GRADER = '''import re
from fractions import Fraction
ANS, KIND = __ANS__, __KIND__
def norm(s):
    return re.sub(r"[\\s`*]", "", s).replace('"', "'").rstrip(".")
def grade(ws, final):
    m = re.findall(r"ANSWER\\s*[:：]\\s*(.+)", final)
    got = m[-1].strip() if m else ""
    ok = norm(got) == norm(ANS)
    if not ok and KIND == "fraction":
        try:
            a, b = norm(got).split("/"); c, d = ANS.split("/")
            ok = Fraction(int(a), int(b)) == Fraction(int(c), int(d))
        except Exception:
            ok = False
    if not ok and KIND == "exact":
        ok = norm(got).replace(",", "") == norm(ANS).replace(",", "") and norm(ANS).isdigit()
    return dict(score=float(ok), passed=ok, items={"answer": ok}, notes=f"got={got[:80]!r}")
'''
if __name__ == "__main__":
    if len(sols) == 1:
        body = "일곱 사람 A, B, C, D, E, F, G가 왼쪽부터 1번~7번 자리가 한 줄로 놓인 의자에 한 명씩 앉는다. 다음 조건을 모두 만족하는 배치는 하나뿐이다.\n\n" + "\n".join(f"{i}. {t}" for i, (t, _) in enumerate(cons, 1)) + "\n\n1번 자리부터 7번 자리까지 앉은 사람을 순서대로 붙여 쓴 7글자 문자열로 답하라 (예: ABCDEFG).\n"
        add("x9", 4, "7인 좌석 배치 유일해 논리 퍼즐", body, sols[0])
    emit()
