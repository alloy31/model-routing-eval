import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from _util import run_hidden


def grade(ws, final):
    r = run_hidden(ws, HERE / "hidden_check.py", timeout=900)
    if "_error" in r:
        return dict(score=0.0, passed=False, items={}, notes="hidden check failed: " + r["_error"][:300])
    sc = r.pop("_score"); bad = r.pop("_bad")
    return dict(score=round(sc, 4), passed=all(r.values()), items=r, notes=f"match={sc:.3f} bad={bad[:3]}")
