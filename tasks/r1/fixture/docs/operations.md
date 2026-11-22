# 운영 가이드

## 설정

`config/base.json`이 기본값이고 `config/<env>.json`이 덮어쓴다.
프로덕션의 HTTP 타임아웃은 `config/prod.json`의 `http.timeout`(12초)이다.

## 재시도

`shiplane.util.retry.retry` 데코레이터의 `max_attempts`는 최대 시도 횟수다.
라벨 발급은 2번까지만 시도한다(이중 발급 방지).

## 장애 격리

외부 호출(요율, 라벨, 지오코딩)은 모두 `CircuitBreaker`를 거친다. 임계값은 `breaker.threshold`다.

## 관리자 API

`/admin/*` 경로는 모든 환경에서 열려 있다. 방화벽으로 막을 것.
