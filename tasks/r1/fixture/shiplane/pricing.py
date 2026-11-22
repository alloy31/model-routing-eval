import math

from .zones import PER_KG_CENTS, ZONE_BASE_CENTS, zone_for


def quote(postal, weight_kg, settings):
    """배송 견적(센트). 무게는 0.5kg 단위로 올림해 계산한다."""
    zone = zone_for(postal)
    billable = math.ceil(weight_kg * 2) / 2
    base = ZONE_BASE_CENTS[zone] + int(billable * PER_KG_CENTS[zone])
    fuel = base * settings.get("pricing.fuel_surcharge_pct") / 100
    total = int(base + fuel + 0.5)
    return max(total, settings.get("pricing.min_charge_cents"))
