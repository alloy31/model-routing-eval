import re
from decimal import ROUND_HALF_UP, Decimal

UNITS = {"w": 604800, "d": 86400, "h": 3600, "m": 60, "s": 1}
ORDER = "wdhms"
LIMIT = 315360000
_COMP = re.compile(r"(0|[1-9][0-9]*)(?:\.([0-9]{1,3}))?([wdhmsWDHS])")


def parse(text):
    if not isinstance(text, str):
        raise TypeError("text must be str")
    s = text.strip(" ")
    if not s:
        raise ValueError("empty")
    neg = s[0] == "-"
    if neg:
        s = s[1:]
    if s == "0":
        return 0
    comps = []
    for part in s.split(" "):
        if not part:
            raise ValueError("bad spacing")
        pos = 0
        while pos < len(part):
            m = _COMP.match(part, pos)
            if not m:
                raise ValueError("bad component")
            comps.append(m.groups())
            pos = m.end()
    total, last = Decimal(0), -1
    for i, (ip, fp, unit) in enumerate(comps):
        rank = ORDER.index(unit.lower())
        if rank <= last:
            raise ValueError("unit order")
        last = rank
        if fp is not None and i != len(comps) - 1:
            raise ValueError("fraction only on last")
        total += Decimal(ip + ("." + fp if fp else "")) * UNITS[unit.lower()]
    secs = int(total.quantize(Decimal(1), rounding=ROUND_HALF_UP))
    if secs > LIMIT:
        raise OverflowError("too large")
    return -secs if neg else secs


def format(seconds):
    if isinstance(seconds, bool) or not isinstance(seconds, int):
        raise TypeError("seconds must be int")
    if abs(seconds) > LIMIT:
        raise OverflowError("too large")
    if seconds == 0:
        return "0s"
    sign, n = ("-" if seconds < 0 else ""), abs(seconds)
    if n % UNITS["w"] == 0:
        return f"{sign}{n // UNITS['w']}w"
    out = []
    for u in "dhms":
        q, n = divmod(n, UNITS[u])
        if q:
            out.append(f"{q}{u}")
    return sign + "".join(out)
