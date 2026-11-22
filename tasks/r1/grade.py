import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from _util import last_json, result


def grade(ws, final):
    a = last_json(final) or {}
    if not isinstance(a, dict):
        a = {}
    num = lambda k, v: isinstance(a.get(k), (int, float)) and not isinstance(a.get(k), bool) and abs(a[k] - v) < 1e-9
    items = {
        "a": num("a", 2),
        "b": str(a.get("b", "")).strip().lstrip("./") == "shiplane/util/breaker.py",
        "c": num("c", 0.2),
        "d": str(a.get("d", "")).strip().rstrip("()") == "healthz",
        "e": num("e", 5),
        "f": num("f", 15),
    }
    return result(items, notes=str({k: a.get(k) for k in "abcdef"}))
