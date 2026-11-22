"""채점기 공용 도구."""
import json, re, subprocess, sys


def last_json(text):
    """최종 응답에서 마지막 JSON 값(코드블록 우선)을 꺼낸다. 없으면 None."""
    blocks = re.findall(r"```(?:json)?\s*\n(.*?)```", text, flags=re.S)
    for cand in reversed(blocks):
        try:
            return json.loads(cand)
        except Exception:
            continue
    dec = json.JSONDecoder()
    best = None
    for m in re.finditer(r"[\[{]", text):
        try:
            obj, _ = dec.raw_decode(text[m.start():])
            best = obj if best is None or len(json.dumps(obj)) >= len(json.dumps(best)) else best
        except Exception:
            continue
    return best


def run_hidden(ws, script, timeout=120, args=()):
    """숨은 검사 스크립트를 작업 디렉터리에서 실행하고 마지막 줄 JSON 을 돌려준다."""
    try:
        p = subprocess.run([sys.executable, "-B", str(script), str(ws), *map(str, args)], cwd=str(ws),
                           capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"_error": "timeout"}
    lines = [l for l in p.stdout.strip().splitlines() if l.strip()]
    try:
        return json.loads(lines[-1])
    except Exception:
        return {"_error": (p.stderr or p.stdout)[-400:]}


def result(items, notes="", need_all=True):
    n = len(items)
    k = sum(1 for v in items.values() if v)
    return dict(score=round(k / n, 3) if n else 0.0, passed=(k == n) if need_all else k > 0, items=items, notes=notes)
