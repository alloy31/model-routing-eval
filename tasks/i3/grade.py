import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from _util import run_hidden, result


def grade(ws, final):
    r = run_hidden(ws, HERE / "hidden_check.py", timeout=300)
    if "_error" in r:
        return dict(score=0.0, passed=False, items={}, notes="hidden check failed: " + r["_error"][:300])
    extra = {k: r.pop(k) for k in list(r) if k.startswith("_")}
    return result(r, notes=f"n={extra.get('_n')} sec={extra.get('_sec')} bad={extra.get('_bad')} slow={extra.get('_slow')}")
