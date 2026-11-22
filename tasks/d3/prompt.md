`python3 -m unittest test_fuzz`가 실패한다. `rangetree.py`의 결함을 **모두** 찾아 고쳐라. 클래스 docstring에 적힌 동작이 기준이다.

- 숨은 테스트는 공개 메서드 전체(`range_add`, `range_assign`, `range_sum`, `range_min`)를 다른 시드·크기로 검증하고, 연산이 O(log n)인지도 큰 입력으로 확인한다.
- `test_fuzz.py`는 고치지 마라. 테스트 파일을 새로 추가하는 것은 괜찮다.

마지막에 찾은 결함 각각의 원인과 고친 내용을 짧게 보고하라.
