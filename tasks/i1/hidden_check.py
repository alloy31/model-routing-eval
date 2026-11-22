import inspect, json, pathlib, re, subprocess, sys
ws = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(ws))
items = {}
def check(name, fn):
    try:
        items[name] = bool(fn())
    except Exception as e:
        items[name] = False
from shiplane import settings as S
prod = S.load("prod")
def _renamed():
    from shiplane import pricing
    return hasattr(pricing, "quote_cents") and not hasattr(pricing, "quote")
check("renamed", _renamed)
def _same():
    from shiplane.pricing import quote_cents
    return quote_cents("94107", 3.2, prod) == 1420 and quote_cents("60601", 0.1, S.load("dev"), currency="USD") == 652
check("same_result", _same)
def _currency():
    from shiplane.pricing import quote_cents
    try:
        quote_cents("94107", 3.2, prod, currency="KRW")
    except ValueError as e:
        return str(e) == "unsupported currency: KRW"
    return False
check("currency_error", _currency)
def _kwonly():
    from shiplane.pricing import quote_cents
    p = inspect.signature(quote_cents).parameters["currency"]
    return p.kind is inspect.Parameter.KEYWORD_ONLY and p.default == "USD"
check("currency_kwonly", _kwonly)
def _delay():
    from shiplane.util.retry import retry
    return inspect.signature(retry).parameters["base_delay"].default == 0.5
check("base_delay", _delay)
def _routes():
    from shiplane.app import create_app
    app, ctx = create_app(prod)
    a = app.dispatch("GET", "/v1/rates", {"postal": "94107", "weight_kg": "3.2"}, ctx) == {"cents": 1420}
    app2, ctx2 = create_app(S.load("staging"))
    b = app2.dispatch("POST", "/v1/rates/bulk", {"items": [{"postal": "94107", "weight_kg": "3.2"}]}, ctx2) == [{"cents": 1380}]
    return a and b
check("routes_work", _routes)
def _no_old():
    pat = re.compile(r"(?<![A-Za-z0-9_])quote\(|import quote\b(?!_)")
    for p in list(ws.rglob("*.py")) + [ws / "README.md"]:
        if "__pycache__" in p.parts:
            continue
        if pat.search(p.read_text()):
            return False
    return True
check("no_old_refs", _no_old)
check("readme", lambda: "quote_cents(" in (ws / "README.md").read_text())
check("tests_pass", lambda: subprocess.run([sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests"], cwd=ws, capture_output=True, timeout=60).returncode == 0)
def _scope():
    # 범위 밖 파일이 바뀌지 않았는지: 설정·문서·레거시
    ref = pathlib.Path(__file__).resolve().parent / "fixture"
    for rel in ("config/prod.json", "config/base.json", "docs/operations.md", "shiplane/legacy/zones.py", "shiplane/zones.py", "shiplane/store.py"):
        if (ws / rel).read_text() != (ref / rel).read_text():
            return False
    return True
check("scope_kept", _scope)
print(json.dumps(items))
