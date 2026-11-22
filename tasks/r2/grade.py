import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from _util import last_json, result

# 정답은 fixtures/shiplane_truth.py 실행 결과(손계산 아님)
TRUTH = {"q1": 15, "q2": 6, "q3": 18, "q5": 6, "q6": 1420}


def grade(ws, final):
    a = last_json(final) or {}
    if not isinstance(a, dict):
        a = {}
    def num(k):
        v = a.get(k)
        return isinstance(v, (int, float)) and not isinstance(v, bool) and abs(v - TRUTH[k]) < 1e-9
    q7 = a.get("q7") if isinstance(a.get("q7"), dict) else {}
    items = {k: num(k) for k in TRUTH}
    items["q4"] = "q4" in a and a.get("q4") is None
    items["q7"] = (str(q7.get("status", "")).strip() == "label_failed" and q7.get("outbox") == 1
                   and q7.get("audit_log") == 0)
    items = dict(sorted(items.items()))
    return result(items, notes=str({k: a.get(k) for k in ("q1", "q2", "q3", "q4", "q5", "q6", "q7")}))
