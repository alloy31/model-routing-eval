"""심은 결함이 실제로 오동작하는지, 미끼 함수는 정상인지 실행으로 확인한다."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import settlement as S
from datetime import datetime, timedelta, timezone, date
U = timezone.utc
t0 = datetime(2026, 1, 1, 20, 0, tzinfo=U)
ev = lambda i, m="m1", k="sale", a=100, ts=t0, r=t0: S.Event(i, m, k, a, ts, r)
P = {}
P["B1"] = S.parse_amount("19.99") != 1999
P["B2"] = S.business_day(t0) != date(2026, 1, 2)
P["B3"] = S.is_settleable(ev("a"), t0 + timedelta(hours=24)) is False
P["B4"] = list(S.chunked([1, 2, 3, 4, 5], 2)) != [[1, 2], [3, 4], [5]]
P["B5"] = S.dedupe([ev("a", r=t0), ev("a", a=999, r=t0 + timedelta(hours=1))])[0].amount != 999
P["B6"] = S.apply_fee(250, 100) != 3
led = S.Ledger(); h = S.make_handlers(led); h["sale"](ev("s"))
P["B8"] = led.balance("revenue") != 100
now = t0 + timedelta(days=3); l2 = S.Ledger()
S.settle_batch([ev("x")], l2, now); P["B9"] = S.settle_batch([ev("x")], l2, now) != 1
evs = [ev("z1", a=0), ev("z2", a=0), ev("n1")]; S.settle_batch(evs, S.Ledger(), now, set())
P["B10"] = len(evs) != 3
class G:
    keys = []
    def charge(self, o, c, idempotency_key):
        self.keys.append(idempotency_key)
        if len(self.keys) < 2: raise S.GatewayTimeout()
        return "ok"
g = G(); S.charge_with_retry(g, "o1", 5); P["B11"] = len(set(g.keys)) != 1
P["B12"] = S.top_merchants([ev("1", m="zeta"), ev("2", m="alpha")], 2)[0][0] != "alpha"
P["B13"] = abs(S.refund_ratio([ev("1", a=1000), ev("2", k="refund", a=200)], "m1") - 0.25) > 1e-9
P["B14"] = S.daily_report([ev("1"), ev("2")], S.business_day(t0))["total"] != 200
P["B7(정적)"] = "self.post(dst, cents)" in open(S.__file__).read()
ok = S.split_payout(100, [1, 1, 1]) == [34, 33, 33] and sum(S.split_payout(1001, [3, 2, 7, 1])) == 1001
print("결함 실증:", {k: v for k, v in P.items()}); print("전부 실증:", all(P.values()), "| 미끼 split_payout 정상:", ok)
