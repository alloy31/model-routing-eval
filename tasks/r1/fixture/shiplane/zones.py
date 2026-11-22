"""우편번호 → 배송 구역. 가장 긴 접두사가 이긴다."""

PREFIX_ZONES = {
    "94": "W1",
    "9": "W2",
    "10": "E1",
    "1": "E2",
    "6": "C1",
}
DEFAULT_ZONE = "C2"

ZONE_BASE_CENTS = {"W1": 820, "W2": 760, "E1": 690, "E2": 640, "C1": 580, "C2": 610}
PER_KG_CENTS = {"W1": 145, "W2": 130, "E1": 120, "E2": 110, "C1": 95, "C2": 100}


def zone_for(postal):
    best = None
    for prefix in PREFIX_ZONES:
        if postal.startswith(prefix) and (best is None or len(prefix) > len(best)):
            best = prefix
    return PREFIX_ZONES[best] if best else DEFAULT_ZONE
