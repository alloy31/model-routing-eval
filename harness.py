#!/usr/bin/env python3
"""모델 배분 실험 하네스.

과제(tasks/<id>) x 모델 x effort 를 격리된 headless Claude Code로 실행하고,
과제별 채점기(grade.py)로 채점해 runs/<run_id>/result.json 과 results.jsonl 에 남긴다.

- 모델이 보는 작업 디렉터리(mr-work/<난수>/ws)와 채점기·숨은 테스트(tasks/)는 분리한다.
- 훅·CLAUDE.md·플러그인·MCP는 끈다(--safe-mode --strict-mcp-config). herdr/세션 환경변수도 지운다.
"""
import argparse, concurrent.futures as cf, importlib.util, json, os, pathlib, shutil
import subprocess, sys, threading, time, uuid

ROOT = pathlib.Path(__file__).resolve().parent
TASKS = ROOT / "tasks"
RUNS = ROOT / "runs"
WORK = ROOT.parent / "mr-work"
RESULTS = ROOT / "results.jsonl"
_lock = threading.Lock()
_state = {"api_errors": 0}
TOOLSET = "Bash,Read,Edit,Write,Glob,Grep"


def clean_env():
    return {k: v for k, v in os.environ.items()
            if not (k.startswith("HERDR_") or k.startswith("CLAUDE_CODE_") or k == "CLAUDECODE")}


def load_task(tid):
    d = TASKS / tid
    meta = json.loads((d / "task.json").read_text())
    meta["dir"] = d
    meta["prompt"] = (d / "prompt.md").read_text()
    return meta


def run_claude(prompt, model, effort, cwd, tools, budget, timeout, log_path):
    cmd = ["claude", "-p", "--model", model, "--effort", effort,
           "--no-session-persistence", "--output-format", "stream-json", "--verbose",
           "--max-budget-usd", str(budget)]
    if not os.environ.get("MR_REALCONF"):  # 기본은 격리 실행. MR_REALCONF=1 이면 사용자 설정(전역 CLAUDE.md·플러그인·MCP)을 그대로 싣는다
        cmd += ["--safe-mode", "--strict-mcp-config"]
    if tools == "none":
        cmd += ["--tools", ""]
    else:
        cmd += ["--tools", tools, "--permission-mode", "auto"]
    t0 = time.time()
    timed_out = False
    with open(log_path, "w") as lf:
        p = subprocess.Popen(cmd, cwd=cwd, env=clean_env(), stdin=subprocess.PIPE, stdout=lf,
                             stderr=subprocess.PIPE, text=True)
        try:
            _, err = p.communicate(prompt, timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            p.kill()
            _, err = p.communicate()
    wall = time.time() - t0
    res, tools_used, cmds = None, {}, []
    for line in open(log_path):
        try:
            o = json.loads(line)
        except Exception:
            continue
        if o.get("type") == "result":
            res = o
        elif o.get("type") == "assistant":
            for c in (o.get("message") or {}).get("content") or []:
                if c.get("type") == "tool_use":
                    tools_used[c["name"]] = tools_used.get(c["name"], 0) + 1
                    inp = c.get("input") or {}
                    cmds.append(json.dumps(inp, ensure_ascii=False)[:400])
    return dict(result=res, wall_s=round(wall, 1), timed_out=timed_out, stderr=(err or "")[-500:],
                tools_used=tools_used, cmds=cmds, exit=p.returncode)


def grade(task, workdir, final_text):
    spec = importlib.util.spec_from_file_location(f"grade_{task['id']}", task["dir"] / "grade.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    try:
        return mod.grade(pathlib.Path(workdir), final_text or "")
    except Exception as e:  # 채점기 오류는 실패와 구분해 남긴다
        return dict(score=0.0, passed=False, items={}, notes=f"GRADER_ERROR {type(e).__name__}: {e}")


def run_one(tid, model, effort, trial, tag=""):
    if _state["api_errors"] >= 3:
        return dict(passed=False, score=None, cost=0, dur_s=0, turns=0, terminal="skipped_after_api_errors", escaped=[], notes="", invalid=True)
    task = load_task(tid)
    run_id = f"{tid}__{model}__{effort}__t{trial}" + (f"__{tag}" if tag else "")
    rdir = RUNS / run_id
    if (rdir / "result.json").exists():
        return json.loads((rdir / "result.json").read_text())
    rdir.mkdir(parents=True, exist_ok=True)
    ws = WORK / uuid.uuid4().hex[:10] / "ws"
    ws.parent.mkdir(parents=True)
    fx = task["dir"] / "fixture"
    if fx.exists():
        shutil.copytree(fx, ws)
    else:
        ws.mkdir()
    r = run_claude(task["prompt"], model, effort, str(ws), task.get("tools", TOOLSET),
                   task.get("budget", 3.0), task.get("timeout", 1500), rdir / "stream.jsonl")
    res = r["result"] or {}
    final = res.get("result") or ""
    (rdir / "final.txt").write_text(final)
    g = grade(task, ws, final)
    escaped = [c for c in r["cmds"] if "mr/tasks" in c or str(TASKS) in c or (ROOT.name + "/tasks") in c or "mr-work" in c.replace(str(ws), "")
               or "/runs/" in c]
    mu = res.get("modelUsage") or {}
    out = dict(run_id=run_id, task=tid, model=model, effort=effort, trial=trial, tag=tag,
               passed=bool(g.get("passed")), score=g.get("score"), items=g.get("items"),
               notes=g.get("notes"), cost=res.get("total_cost_usd"), dur_s=round((res.get("duration_ms") or 0) / 1000, 1),
               wall_s=r["wall_s"], turns=res.get("num_turns"), terminal=res.get("terminal_reason") or res.get("subtype"),
               is_error=res.get("is_error"), timed_out=r["timed_out"], models=list(mu.keys()),
               out_tokens=sum(v.get("outputTokens", 0) for v in mu.values()),
               think_tokens=sum(v.get("thinkingTokens", 0) for v in mu.values()),
               tools_used=r["tools_used"], denials=len(res.get("permission_denials") or []),
               escaped=escaped[:3], ws=str(ws), stderr=r["stderr"] if not res else "")
    invalid = (not res) or out["terminal"] in ("api_error", None) or (res.get("api_error_status") is not None)
    out["invalid"] = bool(invalid)
    if invalid:
        with _lock:
            _state["api_errors"] += 1
            with open(ROOT / "results_invalid.jsonl", "a") as f:
                f.write(json.dumps(out, ensure_ascii=False) + "\n")
        shutil.rmtree(rdir, ignore_errors=True)
        return out
    (rdir / "result.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    with _lock:
        with open(RESULTS, "a") as f:
            f.write(json.dumps(out, ensure_ascii=False) + "\n")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tasks", required=True)
    ap.add_argument("--models", default="haiku,sonnet,opus,fable")
    ap.add_argument("--effort", default="high")
    ap.add_argument("--trials", default="1")
    ap.add_argument("--par", type=int, default=4)
    ap.add_argument("--tag", default="")
    a = ap.parse_args()
    trials = [int(x) for x in a.trials.split(",")]
    jobs = [(t, m, e, k) for t in a.tasks.split(",") for m in a.models.split(",")
            for e in a.effort.split(",") for k in trials]
    with cf.ThreadPoolExecutor(a.par) as ex:
        futs = {ex.submit(run_one, t, m, e, k, a.tag): (t, m, e, k) for t, m, e, k in jobs}
        for f in cf.as_completed(futs):
            t, m, e, k = futs[f]
            try:
                o = f.result()
                if o.get("invalid"):
                    print(f"{t:10s} {m:7s} {e:6s} t{k} INVALID term={o['terminal']}", flush=True)
                    continue
                print(f"{t:10s} {m:7s} {e:6s} t{k} pass={o['passed']!s:5s} score={o['score']} "
                      f"cost=${(o['cost'] or 0):.3f} dur={o['dur_s']}s turns={o['turns']} term={o['terminal']} "
                      f"{'ESCAPED' if o['escaped'] else ''} {(o['notes'] or '')[:110]}", flush=True)
            except Exception as ex_:
                print(f"{t} {m} {e} t{k} HARNESS_ERROR {ex_!r}", flush=True)


if __name__ == "__main__":
    main()
