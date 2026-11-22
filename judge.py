#!/usr/bin/env python3
"""실제 과제 재실행 결과의 익명 채점과 인용 사실 확인.

- blind: 후보 문서를 A, B, C…로 섞어 이름을 가린 뒤, 심사 모델 여러 개가 같은 기준표로 채점한다.
- cite : 후보마다 (주장, URL) 표본을 뽑아, 웹을 읽을 수 있는 검증자가 출처가 주장을 뒷받침하는지 확인한다.
"""
import argparse, concurrent.futures as cf, json, pathlib, random, re, sys, tempfile
import harness, replay_metrics
sys.path.insert(0, str(harness.TASKS))
from _util import last_json
ROOT = harness.ROOT
OUT = ROOT / "replay"

RUBRICS = {
    "w1": ("조사 노트", [
        ("coverage", "지시문이 요구한 게임·출처·질문을 빠짐없이 다뤘는가"),
        ("sourcing", "주장마다 출처가 붙어 있고, 개발자 본인의 글·발표·인터뷰 같은 1차 출처를 우선했는가"),
        ("depth", "각 사례가 어떻게 설계됐고 무엇이 왜 잘못됐는지를 구체적인 수치·규칙·인용으로 설명했는가"),
        ("honesty", "확인하지 못한 것, 커뮤니티 통념과 문서화된 사실의 구분, 출처 간 충돌을 드러냈는가"),
        ("usefulness", "이 노트만 읽고 보고서를 쓸 사람에게 바로 쓸 재료가 되는가"),
    ]),
    "w2": ("종합 보고서", [
        ("answers", "지시문의 (1)어떤 사례가 있었고 (2)어떻게 설계했고 (3)왜 실패했는지를 다섯 갈래에 걸쳐 답했는가"),
        ("synthesis", "사례 나열에 그치지 않고 갈래를 가로지르는 공통 실패 원인과 드문 성공의 이유를 뽑아냈는가"),
        ("lessons", "LIMEN 설계(design-v3)의 어느 부분이 실패를 피하고 어느 부분이 같은 함정에 빠질 위험이 있으며 무엇을 바꾸거나 더 정해야 하는지를, 설계의 실제 내용을 짚어 구체적으로 말했는가"),
        ("honesty", "확인된 근거와 확인되지 않은 근거를 구분해 밝혔는가"),
        ("writing", "평소에 쓰는 자연스러운 한국어인가(번역투·어려운 한자어 없이 읽히는가)"),
    ]),
}


def blind(kind, candidates, judges, task_prompt, extra=None, seed=7, effort="high"):
    name, rubric = RUBRICS[kind]
    labels = list(candidates)
    random.Random(seed).shuffle(labels)
    letters = {lab: chr(65 + i) for i, lab in enumerate(labels)}
    docs = "\n\n".join(f"<문서 {letters[lab]}>\n{pathlib.Path(candidates[lab]).read_text()}\n</문서 {letters[lab]}>" for lab in labels)
    crit = "\n".join(f"- {k}: {d}" for k, d in rubric)
    schema = "{" + ", ".join(f'"{letters[l]}": {{' + ", ".join(f'"{k}": 0' for k, _ in rubric) + ', "comment": ""}' for l in labels) + ', "ranking": ["가장 좋은 문서의 글자", "..."]}'
    prompt = f"""같은 지시문을 받아 서로 다른 작성자가 만든 {name} {len(labels)}편을 심사한다. 작성자는 가려져 있다.

<지시문>
{task_prompt}
</지시문>
{('<참고 자료>' + chr(10) + extra + chr(10) + '</참고 자료>' + chr(10)) if extra else ''}
{docs}

심사 기준(각 1~10점, 10이 가장 좋음). 분량이 아니라 기준의 충족 정도로 판단하라. 문서끼리 차이가 있으면 점수 차이로 드러내라.
{crit}

각 문서의 comment에는 다른 문서와 구별되는 강점·약점을 한두 문장으로 적어라. 마지막에 아래 모양의 JSON 코드블록 하나로 답하라.

```json
{schema}
```
"""
    def one(j):
        log = OUT / f"judge_{kind}_{j}.jsonl"
        r = harness.run_claude(prompt, j, effort, tempfile.mkdtemp(), "none", 6.0, 1500, log)
        res = r["result"] or {}
        return j, last_json(res.get("result") or ""), res.get("total_cost_usd")
    out = {}
    with cf.ThreadPoolExecutor(len(judges)) as ex:
        for j, verdict, cost in ex.map(one, judges):
            out[j] = dict(cost=cost, verdict=verdict)
    table = {}
    for lab in labels:
        table[lab] = {}
        for j in judges:
            v = (out[j]["verdict"] or {}).get(letters[lab]) or {}
            nums = [v.get(k) for k, _ in rubric if isinstance(v.get(k), (int, float))]
            rank = ((out[j]["verdict"] or {}).get("ranking") or [])
            table[lab][j] = dict(scores={k: v.get(k) for k, _ in rubric}, mean=round(sum(nums) / len(nums), 2) if nums else None,
                                 rank=(rank.index(letters[lab]) + 1) if letters[lab] in rank else None, comment=v.get("comment"))
    res = dict(kind=kind, letters=letters, judges={j: out[j]["cost"] for j in judges}, table=table)
    (OUT / f"blind_{kind}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1))
    return res


def cite(candidates, k=10, seed=11, verifier="sonnet"):
    def one(lab):
        items, total = replay_metrics.sample_citations(pathlib.Path(candidates[lab]).read_text(), k, seed)
        listing = "\n".join(f"{i + 1}. 주장: {it['claim']}\n   출처: {it['url']}" for i, it in enumerate(items))
        prompt = f"""아래 {len(items)}개 항목 각각에 대해, 출처 URL을 WebFetch로 직접 읽고 그 페이지가 주장을 뒷받침하는지 판정하라.

판정 값
- supported: 페이지에 주장의 핵심 사실(수치·인용문·사건)이 실제로 있다
- partial: 관련 내용은 있으나 주장의 일부(수치, 인용문의 문구, 주체)가 페이지와 다르거나 페이지에 없다
- unsupported: 페이지가 열리지만 주장의 근거가 없다
- unreachable: 페이지를 읽을 수 없다(차단·404·시간 초과). 이 경우 추측하지 마라.

주장은 한국어로 요약돼 있을 수 있다. 번역 차이는 문제 삼지 말고 사실만 본다. 페이지를 읽지 않고 기억으로 판정하지 마라.

{listing}

마지막에 아래 모양의 JSON 코드블록 하나로 답하라.

```json
[{{"n": 1, "verdict": "supported", "evidence": "페이지에서 찾은 근거 한 줄 또는 없는 이유"}}]
```
"""
        log = OUT / f"cite_{lab}.jsonl"
        r = harness.run_claude(prompt, verifier, "medium", tempfile.mkdtemp(), "WebFetch", 3.0, 1500, log)
        res = r["result"] or {}
        v = last_json(res.get("result") or "") or []
        cnt = {}
        for x in v if isinstance(v, list) else []:
            cnt[x.get("verdict")] = cnt.get(x.get("verdict"), 0) + 1
        return lab, dict(sampled=len(items), pool=total, counts=cnt, cost=res.get("total_cost_usd"), denials=len(res.get("permission_denials") or []), detail=v)
    out = {}
    with cf.ThreadPoolExecutor(len(candidates)) as ex:
        for lab, r in ex.map(one, list(candidates)):
            out[lab] = r
    (OUT / "cite_w1.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    return out
