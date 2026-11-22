이 디렉터리는 `shiplane`이라는 파이썬 서비스의 저장소다. 운영 문의에 답하기 위한 조사다. 아래 질문에 대해 **실제로 동작하는 값**을 답하라. 저장소 파일은 수정하지 마라.

전제: 프로덕션(`SHIPLANE_ENV=prod`)이고 `SHIPLANE__` 환경변수 오버라이드는 없다.

질문
q1. 요율 API 호출(`RatesClient.fetch_rates`)이 transport에 넘기는 타임아웃(초)
q2. 요율 API가 계속 503을 돌려줄 때, `fetch_rates` 한 번 호출로 나가는 HTTP 요청 수
q3. 라벨 API 서버가 연결 거부(ConnectionError) 상태일 때, `LabelClient.post_label` 한 번 호출로 일어나는 transport 호출 수
q4. 요율 API 호출에 적용되는 서킷 브레이커의 실패 임계값(threshold)
q5. 실제로 등록되는 HTTP 라우트 수
q6. 우편번호 "94107", 무게 3.2kg 화물의 견적(센트)
q7. `POST /v1/shipments` 처리 중 라벨 API가 계속 503이어서 라벨 발급이 최종 실패했을 때, 요청이 끝난 뒤 그 화물의 `shipments.status` 값, `outbox` 행 수, `audit_log` 행 수

질문의 전제가 틀렸거나 해당하는 값이 없으면 그 항목은 null로 답하고 notes에 이유를 적어라.

마지막에 아래 형식의 JSON 코드블록 하나로 답하라.

```json
{"q1": 0, "q2": 0, "q3": 0, "q4": 0, "q5": 0, "q6": 0, "q7": {"status": "", "outbox": 0, "audit_log": 0}, "notes": ""}
```
