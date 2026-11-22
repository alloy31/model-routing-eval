"""2차 순수 추론 문항(도구 없음) — 1차가 전 모델 통과라 난도를 크게 올린 사다리. 정답은 전부 코드로 산출."""
import itertools, json, pathlib, random
from functools import lru_cache
import build_x as BX
T = pathlib.Path(__file__).resolve().parent / "tasks"
ITEMS = []
def add(tid, level, desc, body, answer):
    ITEMS.append(dict(id=tid, level=level, desc=desc, body=body, answer=str(answer)))

TIL = "{R}행 {C}열 격자를 1×2 도미노(가로·세로 모두 가능)와 L-트로미노(2×2 정사각형에서 한 칸을 뺀 3칸 모양, 네 방향 회전 모두 가능)로 겹치지 않게 빈틈없이 덮는 방법은 모두 몇 가지인가? 두 종류를 섞어 써도 되고 한 종류만 써도 된다. 놓인 조각의 위치·방향이 하나라도 다르면 다른 방법이다.\n"
add("y1", 6, "3×8 도미노+L-트로미노 타일링 수", TIL.format(R=3, C=8), BX.tilings(3, 8))
add("y2", 7, "4×6 도미노+L-트로미노 타일링 수", TIL.format(R=4, C=6), BX.tilings(4, 6))

# y3 — 40회 반복 해시 (더 큰 법)
s3 = '''def h(s):
    a, b, c = 11, 5, 2
    for i, ch in enumerate(s):
        a = (a * 37 + ord(ch) * (i + 1)) % 10007
        b = ((b ^ a) * 29 + c) % 9973
        c = (c + a * b) % 101
        if (a + b) % 5 == 0:
            a, b = b, a
    return a * 10000 + b

print(h("the quick brown fox jumps over the lazy dog"))'''
add("y3", 6, "43회 반복 모듈러·XOR 해시 손계산", BX.TRACE_HEAD.format(src=s3), BX.run(s3))

# y4 — 금지 부분문자열 3개, 길이 30
pats = ("0101", "1100", "0011")
def count_avoid(n):
    @lru_cache(None)
    def go(k, tail):
        if k == n: return 1
        tot = 0
        for c in "01":
            t = (tail + c)[-4:]
            if any(t.endswith(p) for p in pats): continue
            tot += go(k + 1, t[-3:])
        return tot
    return go(0, "")
assert count_avoid(12) == sum(1 for b in itertools.product("01", repeat=12) if not any(p in "".join(b) for p in pats))
add("y4", 6, "길이 30 이진열 중 0101·1100·0011 회피 개수", "길이가 30인 이진 문자열(0과 1로만 이루어짐) 가운데, 연속 부분 문자열로 \"0101\", \"1100\", \"0011\" 가운데 어느 것도 포함하지 않는 것은 모두 몇 개인가?\n", count_avoid(30))

# y5 — 가중 편집 거리
A, B = "interoperability", "representational"
def wed(a, b, ins=2, dele=3, sub=4):
    D = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1): D[i][0] = i * dele
    for j in range(1, len(b) + 1): D[0][j] = j * ins
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            D[i][j] = min(D[i-1][j] + dele, D[i][j-1] + ins, D[i-1][j-1] + (0 if a[i-1] == b[j-1] else sub))
    return D[-1][-1]
add("y5", 6, "16글자 두 문자열의 가중 편집 거리", f"문자열 A = \"{A}\" 를 문자열 B = \"{B}\" 로 바꾸는 최소 비용을 구하라. 쓸 수 있는 연산과 비용은 다음과 같다: A에 문자 하나 삽입 = 2, A에서 문자 하나 삭제 = 3, A의 문자 하나를 다른 문자로 교체 = 4. (교체가 삭제+삽입보다 싸니 주의하라.)\n", wed(A, B))

# y6 — 순열 세기 (전수 검증 가능, 손으로는 포함-배제/전이 필요)
def ok6(p):
    return all(abs(p[i] - p[i+1]) != 1 for i in range(len(p) - 1)) and p[0] < p[-1] and p[3] != 4
n6 = sum(1 for p in itertools.permutations(range(1, 9)) if ok6(p))
add("y6", 7, "제약 3개를 동시에 만족하는 1..8 순열 수", "1부터 8까지의 수를 한 줄로 늘어놓는 순열 p(1), …, p(8) 가운데 다음 세 조건을 모두 만족하는 것은 몇 개인가?\n\n1. 이웃한 두 수의 차가 1인 곳이 없다 (모든 i에 대해 |p(i) − p(i+1)| ≠ 1).\n2. p(1) < p(8).\n3. p(4) ≠ 4.\n", n6)

# y7 — 3×3 배치 논리 퍼즐 (유일해 탐색)
people = "ABCDEFGHI"
def pos(p, k): return divmod(p[k], 3)
def adj(p, a, b):
    (r1, c1), (r2, c2) = pos(p, a), pos(p, b); return abs(r1 - r2) + abs(c1 - c2) == 1
POOL = [
    ("A는 모서리(네 귀퉁이) 칸에 있지 않다", lambda p: p["A"] not in (0, 2, 6, 8)),
    ("B는 C와 같은 행에 있고 C보다 왼쪽이다", lambda p: pos(p, "B")[0] == pos(p, "C")[0] and pos(p, "B")[1] < pos(p, "C")[1]),
    ("D는 E와 변을 맞대고 있지 않다", lambda p: not adj(p, "D", "E")),
    ("F는 가운데 칸에 있지 않고, G와 같은 열에 있다", lambda p: p["F"] != 4 and pos(p, "F")[1] == pos(p, "G")[1]),
    ("H는 맨 아래 행에 있다", lambda p: pos(p, "H")[0] == 2),
    ("I는 A와 변을 맞대고 있다", lambda p: adj(p, "I", "A")),
    ("C는 맨 오른쪽 열에 있지 않다", lambda p: pos(p, "C")[1] != 2),
    ("E는 D보다 위쪽 행에 있다", lambda p: pos(p, "E")[0] < pos(p, "D")[0]),
    ("G는 H와 변을 맞대고 있지 않다", lambda p: not adj(p, "G", "H")),
    ("A와 F는 같은 행에도 같은 열에도 있지 않다", lambda p: pos(p, "A")[0] != pos(p, "F")[0] and pos(p, "A")[1] != pos(p, "F")[1]),
    ("B가 맨 위 행에 있으면 I는 맨 아래 행에 있다", lambda p: pos(p, "B")[0] != 0 or pos(p, "I")[0] == 2),
    ("D는 가운데 열에 있다", lambda p: pos(p, "D")[1] == 1),
    ("E와 I는 대각선으로만 맞닿아 있다(변은 맞대지 않고 꼭짓점만 공유)", lambda p: abs(pos(p, "E")[0] - pos(p, "I")[0]) == 1 and abs(pos(p, "E")[1] - pos(p, "I")[1]) == 1),
    ("G는 F보다 아래쪽 행에 있다", lambda p: pos(p, "G")[0] > pos(p, "F")[0]),
    ("H는 왼쪽 열에 있지 않다", lambda p: pos(p, "H")[1] != 0),
    ("C와 G는 변을 맞대고 있다", lambda p: adj(p, "C", "G")),
    ("A는 E보다 오른쪽 열에 있다", lambda p: pos(p, "A")[1] > pos(p, "E")[1]),
    ("B는 D와 같은 열에 있지 않다", lambda p: pos(p, "B")[1] != pos(p, "D")[1]),
]
PERMS = [dict(zip(people, perm)) for perm in itertools.permutations(range(9))]
def solve(cs, cand=PERMS):
    return [p for p in cand if all(f(p) for _, f in cs)]
best = None
for seed in range(60):
    rng = random.Random(seed); order = POOL[:]; rng.shuffle(order); cs = []; cur = PERMS
    for c in order:
        nxt = [p for p in cur if c[1](p)]
        if 1 <= len(nxt) < len(cur): cs.append(c); cur = nxt
        if len(cur) == 1: break
    if len(cur) != 1: continue
    for c in cs[:]:
        rest = [d for d in cs if d is not c]
        if len(solve(rest)) == 1: cs = rest
    if best is None or len(cs) > len(best[0]): best = (cs, cur[0])
cons, sol = best
cons = sorted(cons, key=lambda c: [t for t, _ in POOL].index(c[0]))
assert len(solve(cons)) == 1
grid = "".join(sorted(people, key=lambda k: sol[k]))
body7 = "아홉 사람 A~I가 3×3 격자의 칸에 한 명씩 들어간다. 행은 위에서 아래로, 열은 왼쪽에서 오른쪽으로 센다. 다음 조건을 모두 만족하는 배치는 하나뿐이다.\n\n" + "\n".join(f"{i}. {t}" for i, (t, _) in enumerate(cons, 1)) + "\n\n맨 위 행의 왼쪽부터 오른쪽, 그다음 가운데 행, 맨 아래 행 순서로 칸에 들어간 사람을 이어 쓴 9글자 문자열로 답하라 (예: ABCDEFGHI).\n"
add("y7", 6, f"3×3 배치 유일해 논리 퍼즐(조건 {len(cons)}개)", body7, grid)

# y8 — 최단 경로(가중 그래프 20노드)
rng = random.Random(42); N = 18
edges = {}
for i in range(N):
    for j in rng.sample(range(N), 4):
        if i != j: edges[(min(i, j), max(i, j))] = rng.randint(3, 29)
import heapq
def dijk(src):
    dist = {src: 0}; pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, 1e9): continue
        for (a, b), w in edges.items():
            v = b if a == u else a if b == u else None
            if v is not None and d + w < dist.get(v, 1e9):
                dist[v] = d + w; heapq.heappush(pq, (d + w, v))
    return dist
dist = dijk(0); far = max(dist, key=lambda k: (dist[k], k))
el = ", ".join(f"{a}-{b}:{w}" for (a, b), w in sorted(edges.items()))
add("y8", 6, "18노드 가중 그래프에서 가장 먼 노드까지의 최단 거리", f"노드가 0부터 {N-1}까지 있는 무방향 가중 그래프가 있다. 간선은 `a-b:가중치` 형식으로 다음과 같다.\n\n{el}\n\n노드 0에서 출발했을 때, 최단 거리가 가장 큰 노드까지의 최단 거리는 얼마인가? (모든 노드는 0에서 도달 가능하다.)\n", dist[far])
assert len(dist) == N

for it in ITEMS:
    d = T / it["id"]; d.mkdir(parents=True, exist_ok=True)
    (d / "task.json").write_text(json.dumps(dict(id=it["id"], family="추론", level=it["level"], desc=it["desc"], tools="none", budget=4.0, timeout=2400), ensure_ascii=False))
    (d / "prompt.md").write_text(it["body"] + "\n풀이는 자유롭게 쓰되, 응답의 마지막 줄은 반드시 `ANSWER: <답>` 형식 한 줄이어야 한다.\n")
    (d / "grade.py").write_text(BX.GRADER.replace("__ANS__", repr(it["answer"])).replace("__KIND__", repr("exact")))
    print(it["id"], "L%d" % it["level"], it["desc"], "=>", it["answer"])
