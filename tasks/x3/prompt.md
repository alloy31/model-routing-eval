아래 파이썬 3 프로그램을 실행하면 표준 출력에 정확히 무엇이 찍히는가? 코드를 실행할 수 없으니 머리로 추적하라.

```python
def h(s):
    a, b = 7, 3
    for ch in s:
        a = (a * 31 + ord(ch)) % 1009
        b = ((b ^ a) * 17) % 997
        if a % 3 == 0:
            a, b = b, a
    return a * 1000 + b

print(h("orchestrate"))
```

풀이는 자유롭게 쓰되, 응답의 마지막 줄은 반드시 `ANSWER: <답>` 형식 한 줄이어야 한다.
