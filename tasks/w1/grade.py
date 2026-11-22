import re


def grade(ws, final):
    p = ws / "notes.md"
    if not p.exists():
        return dict(score=0.0, passed=False, items={"notes": False}, notes="no notes.md")
    t = p.read_text()
    urls = set(re.findall(r"https?://[^\s)\]>\"']+", t))
    return dict(score=1.0, passed=True, items={"notes": True}, notes=f"chars={len(t)} urls={len(urls)} domains={len({u.split('/')[2] for u in urls})}")
