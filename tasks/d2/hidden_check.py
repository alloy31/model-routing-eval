import json, pathlib, subprocess, sys
ws = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(ws))
import catalog, pricing, shipping, tax
items = {}
def safe(name, fn):
    try:
        items[name] = bool(fn())
    except Exception:
        items[name] = False
safe("currency", lambda: pricing.unit_price("A100", 1) == 1200 and pricing.unit_price("A100", 1, currency="KRW") == 1620000
     and pricing.unit_price("A100", 1, currency="EUR") == 1104)
safe("tier", lambda: pricing.unit_price("C300", 2) == 99 and pricing.unit_price("C300", 2, tier="vip") == 87
     and pricing.unit_price("C300", 2, tier="gold") == 94)
safe("express", lambda: shipping.estimate("near", 3.0) == 660 and shipping.estimate("near", 3.0, express=True) == 1320)
safe("weight_step", lambda: shipping.estimate("far", 0.6) == 920 and shipping.estimate("far", 1.4) == 980
     and shipping.estimate("far", 1.6) == 1040 and shipping.estimate("far", 2.4) == 1100)
def cached():
    for k in catalog.calls: catalog.calls[k] = 0
    for _ in range(3):
        pricing.unit_price("B200", 3, currency="EUR", tier="gold")
        shipping.estimate("far", 7.5, express=True)
        tax.rate_bp("US", "general")
    return catalog.calls == {"base_price": 1, "zone_rate": 1, "tax_rate": 1}
safe("still_cached", cached)
safe("tax_ok", lambda: tax.rate_bp("KR", "food") == 0 and tax.rate_bp("KR", "general") == 1000)
ref = pathlib.Path(__file__).resolve().parent / "fixture"
safe("files_untouched", lambda: all((ws / f).read_text() == (ref / f).read_text() for f in ("catalog.py", "tests/test_pricing.py", "tests/test_shipping.py", "tests/test_tax.py")))
safe("visible_tests", lambda: subprocess.run([sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests"], cwd=ws, capture_output=True, timeout=60).returncode == 0)
print(json.dumps(items))
