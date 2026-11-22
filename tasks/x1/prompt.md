아래 파이썬 3 프로그램을 실행하면 표준 출력에 정확히 무엇이 찍히는가? 코드를 실행할 수 없으니 머리로 추적하라.

```python
fs = []
for i in range(4):
    def f(x, i=i, acc=[]):
        acc.append(x + i)
        return sum(acc)
    fs.append(f)
g = [lambda x: x * j for j in range(3)]
print([fs[1](2), fs[1](3), fs[3](1), g[0](5), g[2](5)])
```

풀이는 자유롭게 쓰되, 응답의 마지막 줄은 반드시 `ANSWER: <답>` 형식 한 줄이어야 한다.
