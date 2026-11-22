import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from _util import last_json

BUGS = json.loads((HERE / "bugs.json").read_text())
EASY, MID, HARD = ("B3", "B4", "B9", "B10", "B14"), ("B1", "B2", "B6", "B8", "B11"), ("B5", "B7", "B12", "B13")


def grade(ws, final):
    found = last_json(final)
    if not isinstance(found, list):
        return dict(score=0.0, passed=False, items={}, notes="no json list")
    lines = [f.get("line") for f in found if isinstance(f, dict) and isinstance(f.get("line"), int)]
    items = {b: any(lo <= ln <= hi for ln in lines) for b, (lo, hi) in BUGS.items()}
    fp = sum(1 for ln in lines if not any(lo <= ln <= hi for lo, hi in BUGS.values()))
    k = sum(items.values())
    tier = lambda g: f"{sum(items[b] for b in g)}/{len(g)}"
    return dict(score=round(k / len(BUGS), 3), passed=k >= 12, items=dict(sorted(items.items(), key=lambda kv: int(kv[0][1:]))),
                notes=f"found {k}/{len(BUGS)} easy {tier(EASY)} mid {tier(MID)} hard {tier(HARD)} | findings {len(lines)} fp {fp}")
