import pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from _util import last_json


def grade(ws, final):
    a = last_json(final)
    if not isinstance(a, dict):
        return dict(score=0.0, passed=False, items={"rule_conflict_R5_R10": False, "example_conflict_E4": False}, notes="no json")
    issues = a.get("open_issues") or []
    refsets = []
    for it in issues:
        if isinstance(it, dict):
            raw = it.get("refs") or []
            raw = raw if isinstance(raw, list) else [raw]
            text = " ".join(map(str, raw)) + " " + str(it.get("question", ""))
            refsets.append(set(re.findall(r"\b[RE]\d+\b", text.upper())))
    A = any({"R5", "R10"} <= r for r in refsets)
    B = any("E4" in r for r in refsets)
    extra = sum(1 for r in refsets if not ({"R5", "R10"} <= r) and "E4" not in r)
    items = {"rule_conflict_R5_R10": A, "example_conflict_E4": B}
    return dict(score=(A + B) / 2, passed=A and B, items=items,
                notes=f"status={a.get('status')} issues={len(refsets)} extra={extra} refs={[sorted(r) for r in refsets]}")
