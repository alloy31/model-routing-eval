"""R2 정답을 실행으로 산출한다 (손계산 금지)."""
import json, sys
sys.path.insert(0, sys.argv[1])
from shiplane import settings as S
from shiplane.app import create_app
from shiplane.errors import LabelFailed
from shiplane.pricing import quote
from shiplane.util import retry as R
R._sleep = lambda s: None
out = {}
prod = S.load("prod")
seen = {}
def t503(method, url, body, timeout):
    seen.setdefault("timeouts", []).append(timeout); seen["n"] = seen.get("n", 0) + 1
    return 503, None
def tconn(method, url, body, timeout):
    seen["n"] = seen.get("n", 0) + 1
    raise ConnectionError("refused")
app, ctx = create_app(prod, t503)
seen.clear()
try: ctx.rates.fetch_rates("W1")
except Exception: pass
out["q1_rates_timeout_prod"] = seen["timeouts"][0]
out["q2_fetch_rates_503_requests"] = seen["n"]
app, ctx = create_app(prod, tconn); seen.clear()
try: ctx.labels.post_label({"id": 1})
except Exception: pass
out["q3_post_label_connerr_transport_calls"] = seen["n"]
out["q4_rates_has_breaker"] = hasattr(ctx.rates, "breaker")
out["q5_routes"] = {e: len(create_app(S.load(e))[0].routes) for e in ("dev", "staging", "prod")}
out["q6_quote"] = {e: quote("94107", 3.2, S.load(e)) for e in ("dev", "staging", "prod")}
app, ctx = create_app(prod, t503)
try: app.dispatch("POST", "/v1/shipments", {"postal": "94107", "weight_kg": 3.2}, ctx)
except LabelFailed: pass
out["q7"] = {"status": ctx.store.get_shipment(1)["status"], "outbox": ctx.store.count("outbox"), "audit_log": ctx.store.count("audit_log")}
print(json.dumps(out, ensure_ascii=False, indent=1))
