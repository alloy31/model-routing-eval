import math

import catalog
from memo import memoize


@memoize(key=lambda zone, weight_kg, **kw: (zone, round(weight_kg)))
def estimate(zone, weight_kg, *, express=False):
    """배송비(센트). 무게는 0.5kg 단위로 올림해 계산하고, 특급이면 두 배다."""
    billable = math.ceil(weight_kg * 2) / 2
    cost = catalog.zone_rate(zone) + int(billable * 120)
    return cost * 2 if express else cost
