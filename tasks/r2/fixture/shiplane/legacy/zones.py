"""구역 계산 (v1). 요율표 개편 전 방식."""

PREFIX_ZONES = {"941": "SF", "94": "BAY", "9": "WEST", "1": "EAST"}
ZONE_BASE_CENTS = {"SF": 900, "BAY": 850, "WEST": 800, "EAST": 700, "OTHER": 650}
PER_KG_CENTS = {"SF": 160, "BAY": 150, "WEST": 140, "EAST": 125, "OTHER": 115}


def zone_for(postal):
    for n in (3, 2, 1):
        if postal[:n] in PREFIX_ZONES:
            return PREFIX_ZONES[postal[:n]]
    return "OTHER"
