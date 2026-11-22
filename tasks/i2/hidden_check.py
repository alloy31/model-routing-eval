import json, pathlib, random, sys
ws = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(ws))
try:
    import durations as D
except Exception as e:
    print(json.dumps({"_import": False, "_err": repr(e)[:200]})); sys.exit(0)
V, O, Ty = ValueError, OverflowError, TypeError
W, Dd, H, M = 604800, 86400, 3600, 60
PARSE = {
 "P1": [("1w", W), ("2d", 2*Dd), ("3h", 3*H), ("4m", 240), ("5s", 5), ("1w2d3h4m5s", W+2*Dd+3*H+240+5), ("0h30m", 1800), ("1h0m", H)],
 "P2": [("1H", H), ("2W3D", 2*W+3*Dd), ("5S", 5), ("1h30M", V), ("5M", V), ("1D2h", Dd+2*H)],
 "P3": [("30m1h", V), ("1h1h", V), ("1s1s", V), ("1d1w", V), ("1h30m15s", 5415), ("1w1s", W+1), ("1m1h1s", V)],
 "P4": [("  1h30m  ", 5400), ("1h 30m", 5400), ("1w 2d 3h", W+2*Dd+3*H), ("1 h", V), ("1h  30m", V), ("1h\t30m", V), ("1h30m\n", V), ("\t1h", V), ("1h 30m", V), ("1h30m 15s", 5415)],
 "P5": [("05m", V), ("007s", V), ("0s", 0), ("10m", 600), ("00s", V), ("１h", V), ("١h", V), ("1h05m", V), ("1" + chr(0xff10) + "m", V), ("1" + chr(0x0660) + "s", V)],
 "P6": [("1.5h", 5400), ("0.25m", 15), ("1h1.5m", H+90), ("1.5h30m", V), (".5h", V), ("1.h", V), ("1.2345s", V), ("1.5w", 907200), ("01.5h", V), ("1.5h 30m", V), ("0.125h", 450), ("1.\uff15h", V)],
 "P7": [("0.5s", 1), ("2.5s", 3), ("1.5s", 2), ("0.4s", 0), ("-0.5s", -1), ("-2.5s", -3), ("0.001h", 4), ("1.005m", 60), ("1m0.5s", 61), ("-1m0.5s", -61), ("0.575m", 35), ("1.115m", 67), ("-0.4s", 0)],
 "P8": [("-1h30m", -5400), ("+1h", V), ("- 1h", V), ("--1h", V), ("-0s", 0), (" -5s ", -5), ("-", V), ("1h-30m", V), ("-1h 30m", -5400)],
 "P9": [("0", 0), ("-0", 0), ("5", V), ("00", V), ("0.0", V), (" 0 ", 0), ("0 0", V), ("0 1h", V), ("1h 0", V)],
 "P10": [("", V), ("   ", V)],
 "P11": [("3650d", 315360000), ("3650d1s", O), ("-3650d", -315360000), ("-3650d1s", O), ("99999999999w", O), ("3650d0.4s", 315360000), ("3650d0.5s", O), ("99999999999w 05m", V), ("522w", O), ("521w3d", 315360000)],
 "P12": [(None, Ty), (5, Ty), (b"1h", Ty), (1.5, Ty)],
}
FORMAT = {
 "F1": [(5400, "1h30m"), (90061, "1d1h1m1s"), (3600, "1h"), (86400 + 5, "1d5s"), (59, "59s"), (3661, "1h1m1s")],
 "F2": [(0, "0s")],
 "F3": [(-90, "-1m30s"), (-5400, "-1h30m"), (-1, "-1s")],
 "F4": [(8*Dd, "8d"), (14*Dd, "2w"), (14*Dd + 1, "14d1s"), (W, "1w"), (-W, "-1w"), (W + H, "7d1h"), (315360000, "3650d"), (3647*Dd, "521w")],
 "F5": [(1.0, Ty), ("60", Ty), (True, Ty), (False, Ty), (None, Ty), (315360001, O), (-315360001, O)],
}
def run(fn, arg, exp):
    try:
        got = fn(arg)
    except Exception as e:
        return isinstance(exp, type) and type(e) is exp
    return (not isinstance(exp, type)) and got == exp and type(got) is type(exp)
items, fails = {}, []
for group, fn in ((PARSE, D.parse), (FORMAT, D.format)):
    for rule, cases in group.items():
        bad = [repr(a) for a, e in cases if not run(fn, a, e)]
        items[rule] = not bad
        fails += [f"{rule}:{b}" for b in bad]
rng = random.Random(7); ok = True
for n in [rng.randint(-315360000, 315360000) for _ in range(3000)] + list(range(-200, 200)) + [k * W for k in (-521, -1, 1, 2, 521)]:
    try:
        if D.parse(D.format(n)) != n: ok = False; fails.append(f"F6:{n}"); break
    except Exception as e:
        ok = False; fails.append(f"F6:{n}:{type(e).__name__}"); break
items["F6"] = ok
items["_fails"] = fails[:12]
print(json.dumps(items, ensure_ascii=False))
