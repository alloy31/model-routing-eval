import time


class CircuitOpen(Exception):
    pass


class CircuitBreaker:
    """연속 실패가 threshold 에 닿으면 reset_s 동안 호출을 막는다."""

    def __init__(self, threshold=5, reset_s=30, clock=time.monotonic):
        self.threshold = threshold
        self.reset_s = reset_s
        self._clock = clock
        self._failures = 0
        self._opened_at = None

    def call(self, fn, *args, **kwargs):
        if self._opened_at is not None:
            if self._clock() - self._opened_at < self.reset_s:
                raise CircuitOpen()
            self._opened_at = None
            self._failures = 0
        try:
            result = fn(*args, **kwargs)
        except Exception:
            self._failures += 1
            if self._failures >= self.threshold:
                self._opened_at = self._clock()
            raise
        self._failures = 0
        return result
