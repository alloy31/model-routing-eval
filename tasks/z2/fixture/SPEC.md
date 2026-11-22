# minisql 사양

`minisql.py`에 `run(tables, sql) -> list[tuple]`을 구현한다.

- `tables`: `{"테이블이름": (["컬럼", ...], [(값, ...), ...])}`. 값은 int, str, None(NULL)뿐이다. 한 컬럼의 값은 NULL을 빼면 모두 같은 타입이다.
- `sql`: 아래 문법의 SELECT 문 하나. 항상 문법에 맞는 입력이 온다.
- 반환: 결과 행의 리스트(각 행은 tuple). ORDER BY가 있으면 그 순서대로다. 없으면 순서는 상관없다.
- **의미는 SQLite 3과 같아야 한다.** 결과 값과 그 타입(int/str/None)이 파이썬 `sqlite3` 모듈로 같은 질의를 실행한 것과 같아야 한다. (테이블은 정수 컬럼을 `INTEGER`, 문자열 컬럼을 `TEXT`로 선언했다고 본다.)

## 문법

```
SELECT [DISTINCT] 선택목록
FROM 테이블 [별칭] [ [INNER | LEFT] JOIN 테이블 별칭 ON 조건 ]
[WHERE 조건]
[GROUP BY 컬럼, ...] [HAVING 조건]
[ORDER BY 위치 [ASC | DESC], ...]
[LIMIT n [OFFSET m]]
```

- 선택목록: `*` 또는 `식 [AS 이름], ...`
- JOIN은 최대 한 번이다. JOIN이 있으면 컬럼은 항상 `별칭.컬럼`으로 쓴다. 같은 테이블끼리 조인할 수 있다.
- ORDER BY는 선택목록의 위치 번호(1부터)로만 쓴다.
- 식: 정수 리터럴(음수 포함), 문자열 리터럴 `'...'`(작은따옴표, 이스케이프 없음), `NULL`, 컬럼, 괄호, 산술 `+ - * / %`, 문자열 연결 `||`, 함수 `ABS`, `LENGTH`, `UPPER`, `LOWER`, `COALESCE(a, b)`, `CASE WHEN 조건 THEN 식 [ELSE 식] END`
- 집계: `COUNT(*)`, `COUNT(식)`, `COUNT(DISTINCT 식)`, `SUM(식)`, `MIN(식)`, `MAX(식)`. 집계는 선택목록과 HAVING에만 온다. GROUP BY 없이 집계만 있는 질의도 있다.
- 조건: 비교 `= != <> < <= > >=`, `IS NULL`, `IS NOT NULL`, `[NOT] IN (리터럴, ...)`, `[NOT] BETWEEN a AND b`, `[NOT] LIKE '패턴'`, `AND`, `OR`, `NOT`, 괄호
- 연산자 우선순위는 SQLite를 따른다. 키워드와 함수 이름은 대문자로만 온다.
- 비교와 산술은 항상 같은 타입끼리(정수와 정수, 문자열과 문자열) 이루어진다. NULL은 어디에나 올 수 있다.

## 제약

- `minisql.py`에서 `sqlite3`를 비롯한 SQL 엔진·DB 라이브러리(pandas, duckdb 등)를 import하거나 호출하면 안 된다. `eval`/`exec`/동적 import도 금지다. 표준 라이브러리의 다른 모듈은 써도 된다.
- 직접 만든 테스트 코드에서 대조용으로 `sqlite3`를 쓰는 것은 괜찮다.

## 예시

```python
tables = {
    "emp": (["id", "name", "dept", "salary", "boss"], [(1, "ab", 2, 5, None), (2, None, 2, -3, 1), (3, "Abc", None, 7, 1)]),
    "dept": (["id", "title", "floor"], [(2, "hello", 1), (4, "B", None)]),
}
run(tables, "SELECT name, salary / 2 FROM emp WHERE dept = 2 ORDER BY 2, 1")
# [(None, -1), ('ab', 2)]
run(tables, "SELECT x.id, y.title FROM emp x LEFT JOIN dept y ON x.dept = y.id ORDER BY 1 DESC, 2")
# [(3, None), (2, 'hello'), (1, 'hello')]
run(tables, "SELECT dept, COUNT(*), SUM(salary) FROM emp GROUP BY dept HAVING COUNT(*) >= 1 ORDER BY 1, 2, 3")
# [(None, 1, 7), (2, 2, 2)]
```
