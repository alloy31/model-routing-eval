from ..util.retry import retry

RATES_URL = "https://rates.internal/v2/table"


class RatesClient:
    SLOW_FACTOR = 2  # 요율 API 는 느려서 기본 타임아웃의 두 배를 준다

    def __init__(self, http, settings):
        self.http = http
        self.settings = settings

    @retry()
    def fetch_rates(self, zone):
        return self.http.request(
            "GET", f"{RATES_URL}?zone={zone}",
            timeout=self.settings.http_timeout * self.SLOW_FACTOR,
        )
