"""느린 외부 조회를 흉내 낸다. calls 로 실제 조회 횟수를 센다."""

BASE_CENTS = {"A100": 1200, "B200": 4550, "C300": 99}
FX = {"USD": 1.0, "KRW": 1350.0, "EUR": 0.92}
TIER_DISCOUNT_PCT = {"std": 0, "gold": 5, "vip": 12}
ZONE_CENTS = {"near": 300, "far": 800}
TAX_BP = {("KR", "food"): 0, ("KR", "general"): 1000, ("US", "general"): 725, ("US", "food"): 200}

calls = {"base_price": 0, "zone_rate": 0, "tax_rate": 0}


def base_price(sku):
    calls["base_price"] += 1
    return BASE_CENTS[sku]


def zone_rate(zone):
    calls["zone_rate"] += 1
    return ZONE_CENTS[zone]


def tax_rate(region, category):
    calls["tax_rate"] += 1
    return TAX_BP[(region, category)]
