# shiplane

소형 화물 배송 견적·접수 서비스.

## 실행

```
SHIPLANE_ENV=prod python3 -m shiplane.app
```

`SHIPLANE_ENV`를 주지 않으면 `dev`로 뜬다.

## 운영 메모

- 외부 API 타임아웃은 30초다.
- 모든 외부 호출은 서킷 브레이커(임계값 5)로 보호한다.
- 일시 오류는 최대 3회 시도한다.
- 라벨 발급이 실패하면 `audit_log`에 기록을 남긴다.
- 견적은 `shiplane.pricing.quote(postal, weight_kg, settings)`로 계산한다.

## 테스트

```
python3 -m unittest discover -s tests
```
