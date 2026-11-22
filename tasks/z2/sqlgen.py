"""무작위 DB·질의 생성기 + sqlite3 오라클. 결정적이지 않은 질의는 행 순서를 섞어 걸러낸다."""
import random, sqlite3

SCHEMA = {"emp": [("id", "int"), ("name", "text"), ("dept", "int"), ("salary", "int"), ("boss", "int")],
          "dept": [("id", "int"), ("title", "text"), ("floor", "int")],
          "log": [("emp", "int"), ("kind", "text"), ("n", "int")]}
WORDS = ["a", "ab", "Abc", "b_c", "x%", "", "hello", "Hello", "abc", "B"]
LIKES = ["%", "a%", "%b", "_b%", "A%", "%_c", "h_llo", "", "%l%", "ab"]


def make_db(rng):
    db = {}
    for t, cols in SCHEMA.items():
        rows = []
        for _ in range(rng.randint(5, 11) if t != "dept" else rng.randint(3, 5)):
            row = []
            for c, ty in cols:
                if rng.random() < 0.14:
                    row.append(None)
                elif ty == "int":
                    row.append(rng.randint(-3, 9))
                else:
                    row.append(rng.choice(WORDS))
            rows.append(tuple(row))
        db[t] = ([c for c, _ in cols], rows)
    return db


class Q:
    def __init__(self, rng):
        self.r = rng

    def lit(self, ty):
        if self.r.random() < 0.06:
            return "NULL"
        return str(self.r.randint(-5, 12)) if ty == "int" else "'" + self.r.choice(WORDS) + "'"

    def par(self, s):
        return "(" + s + ")"

    def expr(self, ty, d, cols):
        r = self.r
        pool = [c for c, t in cols if t == ty]
        x = r.random()
        if d <= 0 or x < 0.30:
            return r.choice(pool) if pool and r.random() < 0.75 else self.lit(ty)
        if ty == "int":
            if x < 0.62:
                op = r.choice(["+", "-", "*", "/", "%", "+", "-", "*"])
                a, b = self.expr("int", d - 1, cols), self.expr("int", d - 1, cols)
                s = f"{a} {op} {b}"
                return self.par(s) if r.random() < 0.7 else s
            if x < 0.70:
                return f"ABS({self.expr('int', d - 1, cols)})"
            if x < 0.78:
                return f"LENGTH({self.expr('text', d - 1, cols)})"
        else:
            if x < 0.50:
                return self.par(f"{self.expr('text', d - 1, cols)} || {self.expr('text', d - 1, cols)}")
            if x < 0.66:
                return f"{r.choice(['UPPER', 'LOWER'])}({self.expr('text', d - 1, cols)})"
        if x < 0.88:
            return f"COALESCE({self.expr(ty, d - 1, cols)}, {self.expr(ty, d - 1, cols)})"
        els = f" ELSE {self.expr(ty, d - 1, cols)}" if r.random() < 0.6 else ""
        return f"CASE WHEN {self.cond(d - 1, cols)} THEN {self.expr(ty, d - 1, cols)}{els} END"

    def cond(self, d, cols, leaf=None):
        r = self.r
        x = r.random()
        leaf = leaf or self.leaf
        if d > 0 and x < 0.34:
            a, b = self.cond(d - 1, cols, leaf), self.cond(d - 1, cols, leaf)
            s = f"{a} {r.choice(['AND', 'OR'])} {b}"
            return self.par(s) if r.random() < 0.6 else s
        if d > 0 and x < 0.44:
            return f"NOT {self.par(self.cond(d - 1, cols, leaf))}" if r.random() < 0.7 else f"NOT {leaf(cols)}"
        return leaf(cols)

    def leaf(self, cols):
        r = self.r
        ty = r.choice(["int", "int", "text"])
        e = self.expr(ty, 1, cols)
        x = r.random()
        if x < 0.45:
            return f"{e} {r.choice(['=', '!=', '<>', '<', '<=', '>', '>='])} {self.expr(ty, 1, cols)}"
        if x < 0.58:
            return f"{e} IS {'NOT ' if r.random() < 0.5 else ''}NULL"
        if x < 0.74:
            items = ", ".join(self.lit(ty) for _ in range(r.randint(1, 4)))
            return f"{e} {'NOT ' if r.random() < 0.4 else ''}IN ({items})"
        if ty == "int":
            return f"{e} {'NOT ' if r.random() < 0.25 else ''}BETWEEN {self.expr('int', 0, cols)} AND {self.expr('int', 0, cols)}"
        return f"{e} {'NOT ' if r.random() < 0.3 else ''}LIKE '{r.choice(LIKES)}'"

    def agg(self, cols):
        r = self.r
        x = r.random()
        if x < 0.2:
            return "COUNT(*)"
        ty = r.choice(["int", "int", "text"])
        e = self.expr(ty, 1, cols)
        if x < 0.4:
            return f"COUNT({'DISTINCT ' if r.random() < 0.5 else ''}{e})"
        if x < 0.65:
            return f"SUM({self.expr('int', 1, cols)})"
        return f"{r.choice(['MIN', 'MAX'])}({e})"

    def having_leaf(self, cols):
        return f"{self.agg(cols)} {self.r.choice(['=', '!=', '<', '<=', '>', '>='])} {self.r.randint(-2, 9)}"

    def query(self):
        r = self.r
        names = list(SCHEMA)
        base = r.choice(names)
        joined = r.random() < 0.45
        if not joined:
            frm = base
            cols = [(c, t) for c, t in SCHEMA[base]]
            ncols = len(cols)
        else:
            other = r.choice(names)
            a, b = "x", "y"
            cols = [(f"{a}.{c}", t) for c, t in SCHEMA[base]] + [(f"{b}.{c}", t) for c, t in SCHEMA[other]]
            ia = r.choice([c for c, t in cols if c.startswith("x.") and t == "int"])
            ib = r.choice([c for c, t in cols if c.startswith("y.") and t == "int"])
            on = f"{ia} = {ib}" + (f" AND {self.leaf(cols)}" if r.random() < 0.25 else "")
            frm = f"{base} {a} {r.choice(['JOIN', 'INNER JOIN', 'LEFT JOIN', 'LEFT JOIN'])} {other} {b} ON {on}"
            ncols = len(cols)
        where = f" WHERE {self.cond(2, cols)}" if r.random() < 0.7 else ""
        mode = r.random()
        if mode < 0.36:  # 집계
            gcols = r.sample([c for c, _ in cols], r.randint(0, 2))
            sel = gcols + [self.agg(cols) + (f" AS v{i}" if r.random() < 0.3 else "") for i in range(r.randint(1, 3))]
            group = f" GROUP BY {', '.join(gcols)}" if gcols else ""
            having = f" HAVING {self.cond(1, cols, self.having_leaf)}" if gcols and r.random() < 0.4 else ""
            sql = f"SELECT {', '.join(sel)} FROM {frm}{where}{group}{having}"
            k = len(sel)
        else:
            star = r.random() < 0.12
            if star:
                sel, k = ["*"], ncols
            else:
                sel = [self.expr(r.choice(["int", "int", "text"]), 2, cols) + (f" AS c{i}" if r.random() < 0.25 else "") for i in range(r.randint(1, 4))]
                k = len(sel)
            sql = f"SELECT {'DISTINCT ' if r.random() < 0.25 else ''}{', '.join(sel)} FROM {frm}{where}"
        ordered = r.random() < 0.5
        if ordered:
            pos = list(range(1, k + 1)); r.shuffle(pos)
            sql += " ORDER BY " + ", ".join(f"{p}{r.choice(['', ' ASC', ' DESC'])}" for p in pos)
            if r.random() < 0.5:
                sql += f" LIMIT {r.randint(0, 6)}" + (f" OFFSET {r.randint(0, 3)}" if r.random() < 0.5 else "")
        return sql, ordered


def oracle(db, sql, shuffle_rng=None):
    con = sqlite3.connect(":memory:")
    for t, (cols, rows) in db.items():
        decl = ", ".join(f"{c} {'INTEGER' if ty == 'int' else 'TEXT'}" for c, ty in SCHEMA[t])
        con.execute(f"CREATE TABLE {t} ({decl})")
        rows = list(rows)
        if shuffle_rng:
            shuffle_rng.shuffle(rows)
        con.executemany(f"INSERT INTO {t} VALUES ({', '.join('?' * len(cols))})", rows)
    return [tuple(r) for r in con.execute(sql).fetchall()]


def canon(rows, ordered):
    key = lambda row: tuple((v is None, type(v).__name__, v if v is not None else 0) for v in row)
    return list(rows) if ordered else sorted(rows, key=key)


def cases(seed, n):
    rng = random.Random(seed)
    out = []
    while len(out) < n:
        db = make_db(rng)
        q = Q(rng)
        for _ in range(25):
            sql, ordered = q.query()
            try:
                want = oracle(db, sql)
                if any(canon(oracle(db, sql, random.Random(s)), ordered) != canon(want, ordered) for s in (1, 2, 3)):
                    continue  # 행 순서에 따라 답이 달라지는 질의는 버린다
            except sqlite3.Error:
                continue
            out.append((db, sql, ordered, canon(want, ordered)))
    return out[:n]


if __name__ == "__main__":
    cs = cases(7, 400)
    import collections
    kinds = collections.Counter()
    for db, sql, o, want in cs:
        for kw in ("JOIN", "LEFT JOIN", "GROUP BY", "HAVING", "DISTINCT", "ORDER BY", "LIMIT", "CASE", "LIKE", " IN (", "BETWEEN", "COALESCE", "||", "COUNT(DISTINCT"):
            kinds[kw] += kw in sql
        kinds["nonempty"] += bool(want)
    print(len(cs), dict(kinds))
    for db, sql, o, want in cs[:6]:
        print(o, sql, "=>", want[:3])
