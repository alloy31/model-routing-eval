import catalog
from memo import memoize


@memoize(key=lambda sku, qty, **kw: (sku, qty))
def unit_price(sku, qty, *, currency="USD", tier="std"):
    """단가를 해당 통화의 최소 단위 정수로 돌려준다.

    10개 이상이면 5% 수량 할인, 그 뒤 등급 할인, 마지막에 환율을 적용한다.
    """
    cents = catalog.base_price(sku)
    if qty >= 10:
        cents = cents * 95 // 100
    cents = cents * (100 - catalog.TIER_DISCOUNT_PCT[tier]) // 100
    return int(round(cents * catalog.FX[currency]))
