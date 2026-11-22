"""settlement.py — 가맹점 일일 정산 배치

규약
- 금액은 모두 '센트' 단위 정수(int)다. 십진 문자열 금액은 parse_amount 에서만 받는다.
- 시각은 모두 timezone-aware UTC datetime 이다.
- 정산일(business day)은 KST(UTC+9) 달력 날짜다.
"""
import threading
import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))
KINDS = ("sale", "refund", "fee")
ACCOUNTS = {"sale": "revenue", "refund": "refunds", "fee": "fees"}


class Insufficient(Exception):
    pass


class GatewayTimeout(Exception):
    pass


@dataclass
class Event:
    event_id: str
    merchant_id: str
    kind: str              # KINDS 중 하나
    amount: int            # 센트
    ts: datetime           # 발생 시각 (UTC, aware)
    received_at: datetime  # 수신 시각 (UTC, aware)


def parse_amount(text):
    """'19.99' 같은 십진 문자열(소수 둘째 자리까지)을 센트 정수로 정확히 변환한다."""
    return int(float(text) * 100)  #@B1:0:0


def business_day(ts):
    """UTC aware datetime 이 속한 KST 정산일(date)을 돌려준다."""
    return ts.replace(tzinfo=KST).date()  #@B2:0:0


def is_settleable(event, now):
    """이벤트는 발생 후 24시간이 지나면 정산할 수 있다. 정확히 24시간째인 순간도 포함한다."""
    return now - event.ts > timedelta(hours=24)  #@B3:0:0


def chunked(items, size):
    """items 를 size 개씩 잘라 리스트로 내놓는다. 마지막 묶음은 size 보다 작을 수 있다."""
    for i in range(len(items) // size):  #@B4:0:1
        yield items[i * size:(i + 1) * size]


def dedupe(events):
    """event_id 가 같은 이벤트가 여럿이면 received_at 이 가장 늦은 것 하나만 남긴다.
    결과는 남긴 이벤트들을 received_at 오름차순으로 정렬한 리스트다."""
    newest_first = sorted(events, key=lambda e: e.received_at, reverse=True)
    by_id = {e.event_id: e for e in newest_first}  #@B5:1:0
    return sorted(by_id.values(), key=lambda e: e.received_at)


def apply_fee(amount, rate_bp):
    """수수료(센트)를 계산한다. rate_bp 는 베이시스포인트(1bp = 0.01%)다.
    센트 미만은 사사오입한다(정확히 0.5 는 올린다)."""
    return round(amount * rate_bp / 10000)  #@B6:0:0


def split_payout(total, weights):
    """total(센트)을 weights 비율로 나눈다. 몫은 내림하고, 남는 센트는 앞에서부터 1센트씩 준다.
    결과의 합은 항상 total 과 같다. total 은 0 이상, weights 는 양의 정수들이다."""
    s = sum(weights)
    shares = [total * w // s for w in weights]
    for i in range(total - sum(shares)):
        shares[i % len(shares)] += 1
    return shares


class Ledger:
    """계정별 잔액 원장. 여러 스레드에서 동시에 써도 안전해야 한다."""

    def __init__(self):
        self._bal = {}
        self._lock = threading.Lock()

    def post(self, account, cents):
        with self._lock:
            self._bal[account] = self._bal.get(account, 0) + cents

    def balance(self, account):
        with self._lock:
            return self._bal.get(account, 0)

    def transfer(self, src, dst, cents):
        """src 에서 dst 로 옮긴다. 잔액이 모자라면 Insufficient 를 던지고 아무것도 바꾸지 않는다.
        다른 스레드는 출금만 되고 입금은 아직 안 된 중간 상태를 볼 수 없어야 한다."""
        with self._lock:
            if self._bal.get(src, 0) < cents:
                raise Insufficient(src)
            self._bal[src] = self._bal.get(src, 0) - cents
        self.post(dst, cents)  #@B7:1:0


def make_handlers(ledger):
    """이벤트 종류별 처리 함수를 만든다. 각 함수는 그 종류에 해당하는 계정에 금액을 기입한다."""
    return {kind: (lambda e: ledger.post(ACCOUNTS[kind], e.amount)) for kind in KINDS}  #@B8:0:0


def group_by_day(events):
    """정산일별로 이벤트를 묶는다. 각 묶음 안의 순서는 입력 순서를 따른다."""
    groups = {}
    for e in events:
        groups.setdefault(business_day(e.ts), []).append(e)
    return groups


def settle_batch(events, ledger, now, seen=set()):  #@B9:0:0
    """정산 가능한 이벤트를 원장에 반영하고, 반영한 이벤트 수를 돌려준다.

    - 금액이 0 인 이벤트는 건너뛴다.
    - 같은 event_id 는 한 번만 반영한다. seen 을 넘기면 호출 사이에도 중복을 추적하고,
      생략하면 이번 호출 안에서만 추적한다.
    - 인자로 받은 events 리스트는 변경하지 않는다.
    """
    handlers = make_handlers(ledger)
    for e in events:
        if e.amount == 0:
            events.remove(e)  #@B10:2:0
    applied = 0
    for e in dedupe(events):
        if e.event_id in seen or not is_settleable(e, now):
            continue
        handlers[e.kind](e)
        seen.add(e.event_id)
        applied += 1
    return applied


def charge_with_retry(gateway, order_id, cents, attempts=3):
    """게이트웨이에 청구한다. GatewayTimeout 이면 최대 attempts 번까지 시도한다.

    gateway.charge 는 idempotency_key 가 같은 요청을 한 번만 청구한다고 보장한다.
    따라서 재시도는 첫 시도와 같은 키로 보내야 이중 청구가 생기지 않는다.
    """
    last = None
    for _ in range(attempts):
        key = f"{order_id}-{uuid.uuid4().hex}"  #@B11:1:1
        try:
            return gateway.charge(order_id, cents, idempotency_key=key)
        except GatewayTimeout as exc:
            last = exc
    raise last


def merchant_totals(events):
    """가맹점별 순매출을 '달러' 단위 float 로 돌려준다(화면 표시용). sale 은 더하고 refund 는 뺀다."""
    totals = {}
    for e in events:
        if e.kind == "sale":
            totals[e.merchant_id] = totals.get(e.merchant_id, 0) + e.amount
        elif e.kind == "refund":
            totals[e.merchant_id] = totals.get(e.merchant_id, 0) - e.amount
    return {m: cents / 100 for m, cents in totals.items()}


def top_merchants(events, n):
    """순매출 상위 n 개 가맹점의 (merchant_id, 순매출) 목록.
    순매출 내림차순이고, 순매출이 같으면 merchant_id 오름차순이다."""
    totals = merchant_totals(events)
    return sorted(totals.items(), key=lambda kv: kv[1], reverse=True)[:n]  #@B12:0:0


def refund_ratio(events, merchant_id):
    """가맹점의 환불 비율 = 환불액 합계 / 순매출 (같은 단위끼리의 비). 순매출이 0 이하이면 0.0."""
    refunded = sum(e.amount for e in events if e.kind == "refund" and e.merchant_id == merchant_id)
    net = merchant_totals(events).get(merchant_id, 0)
    if net <= 0:
        return 0.0
    return refunded / net  #@B13:4:0


def daily_report(events, day):
    """정산일 day 에 속한 이벤트의 건수와 금액 합계(센트)를 돌려준다."""
    todays = (e for e in events if business_day(e.ts) == day)
    count = sum(1 for _ in todays)
    total = sum(e.amount for e in todays)  #@B14:2:0
    return {"day": day, "count": count, "total": total}
