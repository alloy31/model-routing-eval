def grade(ws, final):
    p = ws / "report.md"
    if not p.exists():
        return dict(score=0.0, passed=False, items={"report": False}, notes="no report.md")
    return dict(score=1.0, passed=True, items={"report": True}, notes=f"chars={len(p.read_text())}")
