아래는 배포 전 코드 리뷰 대상 파일 `settlement.py`다(왼쪽 숫자는 줄 번호). 실행 환경은 없으니 읽어서 판단하라.

각 함수의 docstring과 파일 머리의 규약이 의도한 동작이다. **의도와 다르게 동작하는 결함**을 모두 찾아라.
스타일·성능·가독성 제안, 입력 검증 누락처럼 의도에 적히지 않은 요구는 결함이 아니다. 확신이 있는 것만 적어라(최대 20개).

```
  1| """settlement.py — 가맹점 일일 정산 배치
  2| 
  3| 규약
  4| - 금액은 모두 '센트' 단위 정수(int)다. 십진 문자열 금액은 parse_amount 에서만 받는다.
  5| - 시각은 모두 timezone-aware UTC datetime 이다.
  6| - 정산일(business day)은 KST(UTC+9) 달력 날짜다.
  7| """
  8| import threading
  9| import uuid
 10| from dataclasses import dataclass
 11| from datetime import datetime, timedelta, timezone
 12| 
 13| KST = timezone(timedelta(hours=9))
 14| KINDS = ("sale", "refund", "fee")
 15| ACCOUNTS = {"sale": "revenue", "refund": "refunds", "fee": "fees"}
 16| 
 17| 
 18| class Insufficient(Exception):
 19|     pass
 20| 
 21| 
 22| class GatewayTimeout(Exception):
 23|     pass
 24| 
 25| 
 26| @dataclass
 27| class Event:
 28|     event_id: str
 29|     merchant_id: str
 30|     kind: str              # KINDS 중 하나
 31|     amount: int            # 센트
 32|     ts: datetime           # 발생 시각 (UTC, aware)
 33|     received_at: datetime  # 수신 시각 (UTC, aware)
 34| 
 35| 
 36| def parse_amount(text):
 37|     """'19.99' 같은 십진 문자열(소수 둘째 자리까지)을 센트 정수로 정확히 변환한다."""
 38|     return int(float(text) * 100)
 39| 
 40| 
 41| def business_day(ts):
 42|     """UTC aware datetime 이 속한 KST 정산일(date)을 돌려준다."""
 43|     return ts.replace(tzinfo=KST).date()
 44| 
 45| 
 46| def is_settleable(event, now):
 47|     """이벤트는 발생 후 24시간이 지나면 정산할 수 있다. 정확히 24시간째인 순간도 포함한다."""
 48|     return now - event.ts > timedelta(hours=24)
 49| 
 50| 
 51| def chunked(items, size):
 52|     """items 를 size 개씩 잘라 리스트로 내놓는다. 마지막 묶음은 size 보다 작을 수 있다."""
 53|     for i in range(len(items) // size):
 54|         yield items[i * size:(i + 1) * size]
 55| 
 56| 
 57| def dedupe(events):
 58|     """event_id 가 같은 이벤트가 여럿이면 received_at 이 가장 늦은 것 하나만 남긴다.
 59|     결과는 남긴 이벤트들을 received_at 오름차순으로 정렬한 리스트다."""
 60|     newest_first = sorted(events, key=lambda e: e.received_at, reverse=True)
 61|     by_id = {e.event_id: e for e in newest_first}
 62|     return sorted(by_id.values(), key=lambda e: e.received_at)
 63| 
 64| 
 65| def apply_fee(amount, rate_bp):
 66|     """수수료(센트)를 계산한다. rate_bp 는 베이시스포인트(1bp = 0.01%)다.
 67|     센트 미만은 사사오입한다(정확히 0.5 는 올린다)."""
 68|     return round(amount * rate_bp / 10000)
 69| 
 70| 
 71| def split_payout(total, weights):
 72|     """total(센트)을 weights 비율로 나눈다. 몫은 내림하고, 남는 센트는 앞에서부터 1센트씩 준다.
 73|     결과의 합은 항상 total 과 같다. total 은 0 이상, weights 는 양의 정수들이다."""
 74|     s = sum(weights)
 75|     shares = [total * w // s for w in weights]
 76|     for i in range(total - sum(shares)):
 77|         shares[i % len(shares)] += 1
 78|     return shares
 79| 
 80| 
 81| class Ledger:
 82|     """계정별 잔액 원장. 여러 스레드에서 동시에 써도 안전해야 한다."""
 83| 
 84|     def __init__(self):
 85|         self._bal = {}
 86|         self._lock = threading.Lock()
 87| 
 88|     def post(self, account, cents):
 89|         with self._lock:
 90|             self._bal[account] = self._bal.get(account, 0) + cents
 91| 
 92|     def balance(self, account):
 93|         with self._lock:
 94|             return self._bal.get(account, 0)
 95| 
 96|     def transfer(self, src, dst, cents):
 97|         """src 에서 dst 로 옮긴다. 잔액이 모자라면 Insufficient 를 던지고 아무것도 바꾸지 않는다.
 98|         다른 스레드는 출금만 되고 입금은 아직 안 된 중간 상태를 볼 수 없어야 한다."""
 99|         with self._lock:
100|             if self._bal.get(src, 0) < cents:
101|                 raise Insufficient(src)
102|             self._bal[src] = self._bal.get(src, 0) - cents
103|         self.post(dst, cents)
104| 
105| 
106| def make_handlers(ledger):
107|     """이벤트 종류별 처리 함수를 만든다. 각 함수는 그 종류에 해당하는 계정에 금액을 기입한다."""
108|     return {kind: (lambda e: ledger.post(ACCOUNTS[kind], e.amount)) for kind in KINDS}
109| 
110| 
111| def group_by_day(events):
112|     """정산일별로 이벤트를 묶는다. 각 묶음 안의 순서는 입력 순서를 따른다."""
113|     groups = {}
114|     for e in events:
115|         groups.setdefault(business_day(e.ts), []).append(e)
116|     return groups
117| 
118| 
119| def settle_batch(events, ledger, now, seen=set()):
120|     """정산 가능한 이벤트를 원장에 반영하고, 반영한 이벤트 수를 돌려준다.
121| 
122|     - 금액이 0 인 이벤트는 건너뛴다.
123|     - 같은 event_id 는 한 번만 반영한다. seen 을 넘기면 호출 사이에도 중복을 추적하고,
124|       생략하면 이번 호출 안에서만 추적한다.
125|     - 인자로 받은 events 리스트는 변경하지 않는다.
126|     """
127|     handlers = make_handlers(ledger)
128|     for e in events:
129|         if e.amount == 0:
130|             events.remove(e)
131|     applied = 0
132|     for e in dedupe(events):
133|         if e.event_id in seen or not is_settleable(e, now):
134|             continue
135|         handlers[e.kind](e)
136|         seen.add(e.event_id)
137|         applied += 1
138|     return applied
139| 
140| 
141| def charge_with_retry(gateway, order_id, cents, attempts=3):
142|     """게이트웨이에 청구한다. GatewayTimeout 이면 최대 attempts 번까지 시도한다.
143| 
144|     gateway.charge 는 idempotency_key 가 같은 요청을 한 번만 청구한다고 보장한다.
145|     따라서 재시도는 첫 시도와 같은 키로 보내야 이중 청구가 생기지 않는다.
146|     """
147|     last = None
148|     for _ in range(attempts):
149|         key = f"{order_id}-{uuid.uuid4().hex}"
150|         try:
151|             return gateway.charge(order_id, cents, idempotency_key=key)
152|         except GatewayTimeout as exc:
153|             last = exc
154|     raise last
155| 
156| 
157| def merchant_totals(events):
158|     """가맹점별 순매출을 '달러' 단위 float 로 돌려준다(화면 표시용). sale 은 더하고 refund 는 뺀다."""
159|     totals = {}
160|     for e in events:
161|         if e.kind == "sale":
162|             totals[e.merchant_id] = totals.get(e.merchant_id, 0) + e.amount
163|         elif e.kind == "refund":
164|             totals[e.merchant_id] = totals.get(e.merchant_id, 0) - e.amount
165|     return {m: cents / 100 for m, cents in totals.items()}
166| 
167| 
168| def top_merchants(events, n):
169|     """순매출 상위 n 개 가맹점의 (merchant_id, 순매출) 목록.
170|     순매출 내림차순이고, 순매출이 같으면 merchant_id 오름차순이다."""
171|     totals = merchant_totals(events)
172|     return sorted(totals.items(), key=lambda kv: kv[1], reverse=True)[:n]
173| 
174| 
175| def refund_ratio(events, merchant_id):
176|     """가맹점의 환불 비율 = 환불액 합계 / 순매출 (같은 단위끼리의 비). 순매출이 0 이하이면 0.0."""
177|     refunded = sum(e.amount for e in events if e.kind == "refund" and e.merchant_id == merchant_id)
178|     net = merchant_totals(events).get(merchant_id, 0)
179|     if net <= 0:
180|         return 0.0
181|     return refunded / net
182| 
183| 
184| def daily_report(events, day):
185|     """정산일 day 에 속한 이벤트의 건수와 금액 합계(센트)를 돌려준다."""
186|     todays = (e for e in events if business_day(e.ts) == day)
187|     count = sum(1 for _ in todays)
188|     total = sum(e.amount for e in todays)
189|     return {"day": day, "count": count, "total": total}
```

마지막에 아래 형식의 JSON 코드블록 하나로 답하라. line 은 결함이 있는 줄 번호 하나다.

```json
[{"line": 0, "issue": "무엇이 어떻게 틀렸는지 한 문장"}]
```
