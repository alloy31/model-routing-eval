"""참조 구현: 파싱 → Thompson NFA → 상태 집합 시뮬레이션."""
META = set(".*+?|()[]{}\\")


def _parse(p):
    pos = 0

    def alt():
        nonlocal pos
        branches = [cat()]
        while pos < len(p) and p[pos] == "|":
            pos += 1
            branches.append(cat())
        return branches[0] if len(branches) == 1 else ("alt", branches)

    def cat():
        nonlocal pos
        items = []
        while pos < len(p) and p[pos] not in "|)":
            items.append(rep())
        return ("cat", items)

    def rep():
        nonlocal pos
        node = atom()
        if pos < len(p) and p[pos] in "*+?{":
            c = p[pos]
            if c == "*":
                pos += 1
                return ("rep", node, 0, None)
            if c == "+":
                pos += 1
                return ("rep", node, 1, None)
            if c == "?":
                pos += 1
                return ("rep", node, 0, 1)
            end = p.index("}", pos)
            body = p[pos + 1:end]
            pos = end + 1
            if "," not in body:
                return ("rep", node, int(body), int(body))
            lo, hi = body.split(",")
            return ("rep", node, int(lo), int(hi) if hi else None)
        return node

    def atom():
        nonlocal pos
        c = p[pos]
        if c == "(":
            pos += 1
            node = alt()
            pos += 1  # ')'
            return node
        if c == "[":
            pos += 1
            neg = p[pos] == "^"
            if neg:
                pos += 1
            ranges = []
            while p[pos] != "]":
                if p[pos + 1] == "-" and p[pos + 2] != "]":
                    ranges.append((p[pos], p[pos + 2]))
                    pos += 3
                else:
                    ranges.append((p[pos], p[pos]))
                    pos += 1
            pos += 1
            return ("set", neg, tuple(ranges))
        if c == ".":
            pos += 1
            return ("any",)
        if c == "\\":
            pos += 2
            return ("lit", p[pos - 1])
        pos += 1
        return ("lit", c)

    return alt()


class _NFA:
    def __init__(self):
        self.eps = []
        self.edge = []

    def new(self):
        self.eps.append([])
        self.edge.append(None)
        return len(self.eps) - 1

    def build(self, node):
        kind = node[0]
        if kind in ("lit", "any", "set"):
            s, e = self.new(), self.new()
            self.edge[s] = (node, e)
            return s, e
        if kind == "cat":
            s = e = self.new()
            for item in node[1]:
                a, b = self.build(item)
                self.eps[e].append(a)
                e = b
            return s, e
        if kind == "alt":
            s, e = self.new(), self.new()
            for br in node[1]:
                a, b = self.build(br)
                self.eps[s].append(a)
                self.eps[b].append(e)
            return s, e
        _, sub, lo, hi = node
        s = e = self.new()
        for _ in range(lo):
            a, b = self.build(sub)
            self.eps[e].append(a)
            e = b
        if hi is None:
            a, b = self.build(sub)
            loop, out = self.new(), self.new()
            self.eps[e].append(loop)
            self.eps[loop] += [a, out]
            self.eps[b].append(loop)
            return s, out
        out = self.new()
        for _ in range(hi - lo):
            a, b = self.build(sub)
            self.eps[e] += [a, out]
            e = b
        self.eps[e].append(out)
        return s, out


def _closure(nfa, states):
    seen, stack = set(states), list(states)
    while stack:
        for t in nfa.eps[stack.pop()]:
            if t not in seen:
                seen.add(t)
                stack.append(t)
    return seen


def _ok(test, ch):
    if test[0] == "lit":
        return ch == test[1]
    if test[0] == "any":
        return True
    hit = any(a <= ch <= b for a, b in test[2])
    return hit != test[1]


def fullmatch(pattern, text):
    nfa = _NFA()
    start, accept = nfa.build(_parse(pattern))
    cur = _closure(nfa, {start})
    for ch in text:
        nxt = {nfa.edge[s][1] for s in cur if nfa.edge[s] and _ok(nfa.edge[s][0], ch)}
        if not nxt:
            return False
        cur = _closure(nfa, nxt)
    return accept in cur
