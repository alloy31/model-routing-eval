"""마커(#@Bn:앞:뒤)를 떼어 리뷰 대상 파일을 만들고, 결함별 허용 줄 범위를 기록한다."""
import json, pathlib, re
H = pathlib.Path(__file__).resolve().parent
src = (H / "settlement_marked.py").read_text().splitlines()
bugs, clean = {}, []
for i, line in enumerate(src, 1):
    m = re.search(r"\s*#@(B\d+):(\d+):(\d+)$", line)
    if m:
        bugs[m.group(1)] = [i - int(m.group(2)) - 1, i + int(m.group(3)) + 1]  # 표기 오차 ±1 허용
        line = line[:m.start()]
    clean.append(line)
(H / "settlement.py").write_text("\n".join(clean) + "\n")
(H / "bugs.json").write_text(json.dumps(bugs, indent=1))
numbered = "\n".join(f"{i:3d}| {l}" for i, l in enumerate(clean, 1))
prompt = f"""아래는 배포 전 코드 리뷰 대상 파일 `settlement.py`다(왼쪽 숫자는 줄 번호). 실행 환경은 없으니 읽어서 판단하라.

각 함수의 docstring과 파일 머리의 규약이 의도한 동작이다. **의도와 다르게 동작하는 결함**을 모두 찾아라.
스타일·성능·가독성 제안, 입력 검증 누락처럼 의도에 적히지 않은 요구는 결함이 아니다. 확신이 있는 것만 적어라(최대 20개).

```
{numbered}
```

마지막에 아래 형식의 JSON 코드블록 하나로 답하라. line 은 결함이 있는 줄 번호 하나다.

```json
[{{"line": 0, "issue": "무엇이 어떻게 틀렸는지 한 문장"}}]
```
"""
(H / "prompt.md").write_text(prompt)
print(len(clean), "lines;", bugs)
