이 디렉터리는 `shiplane`이라는 파이썬 서비스의 저장소다. 아래 변경을 그대로 적용하라. 설계는 이미 정해졌으니 다시 설계하지 마라.

변경 사항
1. `shiplane/pricing.py`의 `quote` 함수 이름을 `quote_cents`로 바꾼다. 옛 이름은 남기지 않는다. 저장소 안의 모든 호출부와 import를 새 이름으로 고친다(테스트 포함).
2. `quote_cents`에 키워드 전용 인자 `currency`를 추가한다. 기본값은 `"USD"`다. `"USD"`가 아닌 값이 오면 `ValueError("unsupported currency: <받은 값>")`를 던진다. 계산 결과는 지금과 같아야 한다.
3. `shiplane/util/retry.py`의 `retry` 데코레이터에서 `base_delay` 기본값을 `0.2`에서 `0.5`로 바꾼다.
4. `README.md`에서 `quote(`를 언급한 곳을 `quote_cents(`로 고친다.
5. `python3 -m unittest discover -s tests`가 통과하는지 확인한다.

하지 말 것: 위 범위 밖의 수정, 동작 변경, 새 의존성 추가.

마지막에 바꾼 파일 목록과 테스트 실행 결과를 짧게 보고하라.
