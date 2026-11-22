from ..util.breaker import CircuitBreaker

GEOCODE_URL = "https://geo.internal/v1/lookup"


class GeocodeClient:
    def __init__(self, http, settings):
        self.http = http
        self.settings = settings
        self.breaker = CircuitBreaker(
            threshold=settings.get("breaker.threshold"),
            reset_s=settings.get("breaker.reset_s"),
        )

    def lookup(self, postal):
        return self.breaker.call(self.http.request, "GET", f"{GEOCODE_URL}?postal={postal}")
