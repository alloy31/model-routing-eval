아래 파이썬 3 프로그램을 실행하면 표준 출력에 정확히 무엇이 찍히는가? 코드를 실행할 수 없으니 머리로 추적하라.

```python
def h(s):
    a, b, c = 11, 5, 2
    for i, ch in enumerate(s):
        a = (a * 37 + ord(ch) * (i + 1)) % 10007
        b = ((b ^ a) * 29 + c) % 9973
        c = (c + a * b) % 101
        if (a + b) % 5 == 0:
            a, b = b, a
    return a * 10000 + b

print(h("the quick brown fox jumps over the lazy dog"))
```

풀이는 자유롭게 쓰되, 응답의 마지막 줄은 반드시 `ANSWER: <답>` 형식 한 줄이어야 한다.
