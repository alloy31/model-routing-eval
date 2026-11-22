class RangeTree:
    """정수 배열에 대한 구간 연산 자료구조.

    모든 구간은 반열린 구간 [l, r) 이고 0 <= l <= r <= n 이다.

    - range_add(l, r, v): 구간의 모든 원소에 v 를 더한다.
    - range_assign(l, r, v): 구간의 모든 원소를 v 로 바꾼다.
    - range_sum(l, r): 구간의 합. 빈 구간이면 0.
    - range_min(l, r): 구간의 최솟값. 빈 구간이면 ValueError.

    연산 하나는 O(log n) 에 끝나야 한다.

    내부 표현: 노드마다 합(sm)·최솟값(mn)과, 아직 자식에게 내려보내지 않은 지연 태그 두 개
    (assign, add)를 둔다. 한 노드에 두 태그가 함께 있으면 "assign 을 먼저 하고 그다음 add" 라는 뜻이다.
    """

    def __init__(self, values):
        self.n = len(values)
        size = 4 * max(1, self.n)
        self.sm = [0] * size
        self.mn = [0] * size
        self.add = [0] * size
        self.assign = [None] * size
        if self.n:
            self._build(1, 0, self.n, values)

    def _build(self, node, lo, hi, values):
        if hi - lo == 1:
            self.sm[node] = self.mn[node] = values[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, values)
        self._build(2 * node + 1, mid, hi, values)
        self._pull(node)

    def _pull(self, node):
        self.sm[node] = self.sm[2 * node] + self.sm[2 * node + 1]
        self.mn[node] = min(self.mn[2 * node], self.mn[2 * node + 1])

    def _apply_assign(self, node, lo, hi, v):
        self.sm[node] = v * (hi - lo)
        self.mn[node] = v
        self.assign[node] = v
        self.add[node] = 0

    def _apply_add(self, node, lo, hi, v):
        self.sm[node] += v * (hi - lo)
        self.mn[node] += v
        self.add[node] += v

    def _push(self, node, lo, hi):
        mid = (lo + hi) // 2
        if self.assign[node] is not None:
            self._apply_assign(2 * node, lo, mid, self.assign[node])
            self._apply_assign(2 * node + 1, mid, hi, self.assign[node])
            self.assign[node] = None
        if self.add[node]:
            self._apply_add(2 * node, lo, mid, self.add[node])
            self._apply_add(2 * node + 1, mid, hi, self.add[node])
            self.add[node] = 0

    def _update(self, node, lo, hi, l, r, v, assign):
        if r <= lo or hi <= l:
            return
        if l <= lo and hi <= r:
            if assign:
                self._apply_assign(node, lo, hi, v)
            else:
                self._apply_add(node, lo, hi, v)
            return
        self._push(node, lo, hi)
        mid = (lo + hi) // 2
        self._update(2 * node, lo, mid, l, r, v, assign)
        self._update(2 * node + 1, mid, hi, l, r, v, assign)
        self._pull(node)

    def _sum(self, node, lo, hi, l, r):
        if r <= lo or hi <= l:
            return 0
        if l <= lo and hi <= r:
            return self.sm[node]
        self._push(node, lo, hi)
        mid = (lo + hi) // 2
        return self._sum(2 * node, lo, mid, l, r) + self._sum(2 * node + 1, mid, hi, l, r)

    def _min(self, node, lo, hi, l, r):
        if l <= lo and hi <= r:
            return self.mn[node]
        self._push(node, lo, hi)
        mid = (lo + hi) // 2
        if r <= mid:
            return self._min(2 * node, lo, mid, l, r)
        if l >= mid:
            return self._min(2 * node + 1, mid, hi, l, r)
        return min(self._min(2 * node, lo, mid, l, r), self._min(2 * node + 1, mid, hi, l, r))

    def _check(self, l, r):
        if not (0 <= l <= r <= self.n):
            raise IndexError(f"bad range [{l}, {r})")

    def range_add(self, l, r, v):
        self._check(l, r)
        if l < r:
            self._update(1, 0, self.n, l, r, v, False)

    def range_assign(self, l, r, v):
        self._check(l, r)
        if l < r:
            self._update(1, 0, self.n, l, r, v, True)

    def range_sum(self, l, r):
        self._check(l, r)
        return self._sum(1, 0, self.n, l, r) if l < r else 0

    def range_min(self, l, r):
        self._check(l, r)
        if l == r:
            raise ValueError("empty range")
        return self._min(1, 0, self.n, l, r)
