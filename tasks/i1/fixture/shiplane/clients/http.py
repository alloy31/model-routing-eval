from ..errors import HttpError, TransientError

MAX_TIMEOUT = 15


class Http:
    """transport(method, url, body, timeout) -> (status, payload) 를 감싼 얇은 클라이언트."""

    def __init__(self, settings, transport):
        self.settings = settings
        self.transport = transport

    def request(self, method, url, body=None, timeout=None):
        timeout = min(timeout or self.settings.http_timeout, MAX_TIMEOUT)
        last = None
        for _ in range(self.settings.http_retries + 1):
            try:
                status, payload = self.transport(method, url, body, timeout)
            except ConnectionError as exc:
                last = exc
                continue
            if status >= 500:
                raise TransientError(f"{status} from {url}")
            if status >= 400:
                raise HttpError(status, payload)
            return payload
        raise TransientError(f"connection failed: {last}")
