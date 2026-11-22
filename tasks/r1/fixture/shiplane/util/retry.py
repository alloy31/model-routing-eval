import functools
import time

from ..errors import TransientError

_sleep = time.sleep


def retry(max_attempts=None, base_delay=0.2):
    """TransientError 가 나면 지수 백오프로 다시 시도한다.

    max_attempts 를 생략하면 self.settings.http_retries 를 쓴다.
    """
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(self, *args, **kwargs):
            limit = max_attempts if max_attempts is not None else self.settings.http_retries
            for attempt in range(limit + 1):
                try:
                    return fn(self, *args, **kwargs)
                except TransientError:
                    if attempt == limit:
                        raise
                    _sleep(base_delay * 2 ** attempt)
        return wrapper
    return deco
