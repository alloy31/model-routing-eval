import re
from fractions import Fraction
ANS, KIND = '15171', 'exact'
def norm(s):
    return re.sub(r"[\s`*]", "", s).replace('"', "'").rstrip(".")
def grade(ws, final):
    m = re.findall(r"ANSWER\s*[:：]\s*(.+)", final)
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
