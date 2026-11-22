아래 파이썬 3 프로그램을 실행하면 표준 출력에 정확히 무엇이 찍히는가? 코드를 실행할 수 없으니 머리로 추적하라.

```python
def gen():
    total = 0
    try:
        while True:
            try:
                x = yield total
                if x is None:
                    x = 1
                total += x
                if total > 10:
                    return total * 2
            except ValueError as e:
                total -= int(str(e))
            finally:
                total += 1
    finally:
        log.append(("closed", total))

log = []
g = gen()
log.append(next(g))
log.append(g.send(3))
log.append(g.throw(ValueError("2")))
log.append(next(g))
try:
    log.append(g.send(7))
except StopIteration as s:
    log.append(("stop", s.value))
print(log)
```

풀이는 자유롭게 쓰되, 응답의 마지막 줄은 반드시 `ANSWER: <답>` 형식 한 줄이어야 한다.
