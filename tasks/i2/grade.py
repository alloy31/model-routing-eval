import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from _util import run_hidden, result


def grade(ws, final):
    r = run_hidden(ws, HERE / "hidden_check.py", timeout=120)
    if "_error" in r or r.get("_import") is False:
        return dict(score=0.0, passed=False, items={}, notes="hidden check failed: " + str(r)[:300])
    fails = r.pop("_fails", [])
    out = result(r, notes="fails: " + ", ".join(fails) if fails else "")
    return out
