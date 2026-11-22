class TransientError(Exception):
    """잠시 뒤 다시 시도하면 성공할 수 있는 오류."""


class HttpError(Exception):
    def __init__(self, status, payload=None):
        super().__init__(f"http {status}")
        self.status = status
        self.payload = payload


class LabelFailed(Exception):
    pass
