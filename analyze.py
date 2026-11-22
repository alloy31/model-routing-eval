#!/usr/bin/env python3
"""results.jsonl → 과제×모델 표, 최소 통과 모델, 예측 대조, 정책 비교."""
import collections, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent
ORDER = ["haiku", "sonnet", "opus", "fable"]
PRED = dict(r1="haiku", i2="sonnet", d2="opus", v1="opus", a1="opus", x1="haiku", x3="sonnet", x5="sonnet", x7="fable", x9="sonnet",
            r2="opus", i1="haiku", d1="haiku", d3="opus", i3="opus", x2="sonnet", x4="opus", x6="opus", x8="fable")


def load(effort="high", tag=""):
    rows = [json.loads(l) for l in open(ROOT / "results.jsonl")]
    return [r for r in rows if r["effort"] == effort and (r.get("tag") or "") == tag and r["task"] != "smoke"]


def table(rows, tasks=None):
    by = collections.defaultdict(list)
    for r in rows:
        by[(r["task"], r["model"])].append(r)
    tasks = tasks or sorted({r["task"] for r in rows})
    meta = {t: json.loads((ROOT / "tasks" / t / "task.json").read_text()) for t in tasks}
    print(f"{'과제':5s} {'설명':38s} " + " ".join(f"{m:>22s}" for m in ORDER) + "  최소통과  예측")
    out = {}
    for t in tasks:
        cells, minpass = [], None
        for m in ORDER:
            rs = by.get((t, m))
            if not rs:
                cells.append(f"{'-':>22s}"); continue
            k = sum(r["passed"] for r in rs); sc = sum(r["score"] or 0 for r in rs) / len(rs)
            cost = sum(r["cost"] or 0 for r in rs) / len(rs); dur = sum(r["dur_s"] for r in rs) / len(rs)
            mark = "O" if k == len(rs) else ("X" if k == 0 else f"{k}/{len(rs)}")
            cells.append(f"{mark:>3s} {sc:4.2f} ${cost:5.2f} {dur:5.0f}s")
            if minpass is None and k == len(rs):
                minpass = m
            out[(t, m)] = dict(passed=k == len(rs), rate=k / len(rs), score=sc, cost=cost, dur=dur, n=len(rs))
        pred = PRED.get(t, "")
        flag = "" if not pred else ("=" if pred == minpass else ("과대" if minpass and ORDER.index(pred) > ORDER.index(minpass) else "과소"))
        print(f"{t:5s} {meta[t]['desc'][:36]:38s} " + " ".join(cells) + f"  {str(minpass):8s} {pred:6s} {flag}")
    return out


def policies(cells, tasks, route=None):
    """정책별 성공 수·비용·시간. route: {task: model} (없으면 생략)."""
    def fixed(m):
        ok = sum(cells[(t, m)]["passed"] for t in tasks if (t, m) in cells)
        return ok, sum(cells[(t, m)]["cost"] for t in tasks if (t, m) in cells), sum(cells[(t, m)]["dur"] for t in tasks if (t, m) in cells)
    print(f"\n{'정책':28s} 성공  비용    시간(합)")
    for m in ORDER:
        ok, c, d = fixed(m); print(f"항상 {m:23s} {ok:2d}/{len(tasks)} ${c:6.2f} {d/60:6.1f}분")
    if route:
        ok = c = d = 0
        for t in tasks:
            x = cells.get((t, route[t]))
            if x: ok += x["passed"]; c += x["cost"]; d += x["dur"]
        print(f"{'기준대로 배분':26s} {ok:2d}/{len(tasks)} ${c:6.2f} {d/60:6.1f}분")
    ok = c = d = 0
    for t in tasks:  # 사후 최적(참고용 상한): 통과하는 가장 싼 모델
        for m in ORDER:
            x = cells.get((t, m))
            if x and x["passed"]:
                ok += 1; c += x["cost"]; d += x["dur"]; break
    print(f"{'사후 최적(통과하는 최저가)':20s} {ok:2d}/{len(tasks)} ${c:6.2f} {d/60:6.1f}분")


if __name__ == "__main__":
    tasks = sys.argv[1].split(",") if len(sys.argv) > 1 else None
    rows = load()
    cells = table(rows, tasks)
    policies(cells, tasks or sorted({r["task"] for r in rows}))
