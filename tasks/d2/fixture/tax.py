import catalog
from memo import memoize


@memoize(key=lambda region, category: (region, category))
def rate_bp(region, category):
    """세율(베이시스포인트)."""
    return catalog.tax_rate(region, category)
