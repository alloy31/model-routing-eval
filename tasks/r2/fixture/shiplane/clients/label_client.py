from ..util.retry import retry

LABEL_URL = "https://labels.internal/v1/labels"


class LabelClient:
    def __init__(self, http, settings):
        self.http = http
        self.settings = settings

    @retry(max_attempts=2)
    def post_label(self, shipment):
        return self.http.request("POST", LABEL_URL, body=shipment)
