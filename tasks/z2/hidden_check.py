import json, pathlib, re, signal, sys
HERE = pathlib.Path(__file__).resolve().parent
ws = pathlib.Path(sys.argv[1])
sys.path.insert(0, str(HERE)); import sqlgen
cs = sqlgen.cases(20261115, 500)
sys.path.insert(0, str(ws))
src = (ws / "minisql.py").read_text() if (ws / "minisql.py").exists() else ""
items = {"no_sql_lib": bool(src) and not re.search(
    r"^\s*(import|from)\s+(sqlite3|duckdb|pandas|sqlalchemy|apsw|importlib|subprocess)\b|__import__|\beval\s*\(|\bexec\s*\(", src, re.M)}
class TO(BaseException): pass
def alarm(*a): raise TO()
signal.signal(signal.SIGALRM, alarm)
ok, bad = 0, []
try:
    import minisql
    for db, sql, ordered, want in cs:
        signal.alarm(3)
        try:
            got = sqlgen.canon([tuple(r) for r in minisql.run({t: (list(c), list(r)) for t, (c, r) in db.items()}, sql)], ordered)
            good = got == want and all(type(a) is type(b) for ra, rb in zip(got, want) for a, b in zip(ra, rb))
        except TO:
            good, got = False, "TIMEOUT"
        except Exception as e:
            good, got = False, f"EXC {type(e).__name__}: {str(e)[:60]}"
        signal.alarm(0)
        ok += good
        if not good and len(bad) < 5:
            bad.append([sql[:160], str(want)[:80], str(got)[:80]])
except TO:
    pass
except Exception as e:
    bad.append(["import", "", repr(e)[:160]])
signal.alarm(0)
items["_score"] = ok / len(cs); items["_bad"] = bad
items["match_99"] = ok / len(cs) >= 0.99
print(json.dumps(items, ensure_ascii=False))
