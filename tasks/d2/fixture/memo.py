"""아주 단순한 메모이제이션 도우미."""
import functools


def memoize(key):
    """key(*args, **kwargs) 가 돌려준 값을 캐시 키로 써서 함수 결과를 기억한다.

    key 는 결과에 영향을 주는 입력을 빠짐없이 구분해야 한다.
    """
    def deco(fn):
        cache = {}

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            k = key(*args, **kwargs)
            if k not in cache:
                cache[k] = fn(*args, **kwargs)
            return cache[k]

        wrapper.cache = cache
        return wrapper
    return deco
