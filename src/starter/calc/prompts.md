# 실습 프롬프트 — calc
문자열 계산기 — RED · GREEN · REFACTOR · 골든 마스터 (Day 1)  
교안: `(교안) 실전-Coding Agent 실전 AI기반 TDD 마스터 과정_20261021_개정.pptx`

## 어디에서 실습하나 (작업 폴더)

| 항목 | 내용 |
|---|---|
| 작업 폴더 | `C:\DEV\tdd-course\calc` |
| 만드는 법 | 강사가 나눠 준 `starter\calc` 폴더를 `C:\DEV\tdd-course\` 아래로 **폴더째 복사**한다 (폴더를 새로 만들 필요는 없다) |
| 여는 법 | VS Code → 파일 → 폴더 열기 → `C:\DEV\tdd-course\calc` · 터미널과 코딩 에이전트도 **이 폴더에서** 실행한다 |
| 처음 한 번 | `cd C:\DEV\tdd-course\calc` → `pip install -r requirements.txt   (C:\DEV\tdd-course 에서 한 번)` |
| 막히면 | `checkpoints\1.5_실습2완료\calc` · `checkpoints\1.7_점검실습완료\calc` 중 막힌 단계의 폴더를 복사해 그 단계부터 이어서 한다 |
| 이 폴더를 쓰는 교안 슬라이드 | `(교안) 실전-Coding Agent 실전 AI기반 TDD 마스터 과정_20261021_개정.pptx` — 11, 87–92, 96–100, 103, 105, 108, 110번 |

## 쓰는 법 (개정판)
- 각 항목은 **프롬프트 → 코드 → 실행 명령(기대 결과)** 순서로 모두 들어 있다. 코드는 직접 쓰는 테스트 · 소스이고, 프롬프트는 같은 일을 Gemini CLI 에 맡길 때 쓴다.
- 이 파일을 VS Code 에서 열어 두고(`Ctrl+Shift+V` 미리보기), 코드 블록을 복사해 Gemini CLI 에 붙여 넣는다. Gemini CLI 는 반드시 이 프로젝트 폴더에서 실행한다.
- `> ` 로 시작하는 줄은 터미널에서 실행하는 명령이고, 그 아래 줄은 실제로 실행해 얻은 결과다. AI 응답 문구와 코드 모양은 실행마다 다르다 — 판단 기준은 언제나 pytest 결과다.

### 슬라이드 11 — 환경 확인
<sub>Day 1 · 오리엔테이션  |  오리엔테이션</sub>

**▶ 프롬프트**

```text
이 폴더에 어떤 파일과 폴더가 있는지 목록만 알려줘. 아무것도 수정하지 마.
```

**실행 명령 · 결과 — 터미널**

```text
> cd C:\DEV\tdd-course\calc
> python --version
Python 3.11.9
> pytest -q
no tests ran in 0.01s        # 테스트가 아직 없으니 정상
> gemini
(로그인 후 대화창이 열리면 성공)
```

**AI 응답 예시 (실행마다 다름) — 결과 예시**

```text
✦ 현재 폴더(calc) 구성이다.
  pytest.ini · src/ (비어 있음) · tests/ (비어 있음)
```

### 슬라이드 87 — R1 · 빈 문자열이면 0 — 테스트부터
<sub>Day 1 · 5교시  |  실습 1 · R1</sub>

**▶ 프롬프트 — 테스트를 AI 에게 맡길 때 (직접 쓰기 어려우면)**

```text
@src/calculator.py
tests/test_calculator.py 를 새로 만들고 테스트 1개만 작성해줘: test_empty_string_returns_zero — add("") 가 0 을 돌려주는지 검증한다.
src/ 는 수정하지 마. 구현은 하지 마. 끝나면 !pytest -q --tb=short 로 실패 이유를 보여줘.
```

**코드 — ① 직접 작성(또는 위 프롬프트로) — tests/test_calculator.py**

```python
from calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0
```

**실행 명령 · 결과 — ② 실행 → RED 확인 · 터미널**

```text
> pytest -q --tb=short
F  [100%]
=== FAILURES ===
___ test_empty_string_returns_zero ___
tests/test_calculator.py:5: in test_empty_string_returns_zero
    assert add("") == 0
           ^^^^^^^
src/calculator.py:2: in add
    raise NotImplementedError
E   NotImplementedError
=== short test summary info ===
FAILED tests/test_calculator.py::test_empty_string_returns_zero
1 failed in 0.02s
```

### 슬라이드 88 — R1 · AI에게 최소 구현을 맡긴다
<sub>Day 1 · 5교시  |  실습 1 · R1</sub>

**▶ 프롬프트 — Gemini CLI**

```text
@tests/test_calculator.py @src/calculator.py
test_empty_string_returns_zero 만 통과하는 최소 구현을 해줘.
테스트 파일은 수정하지 마. 다른 기능은 추가하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**AI 응답 예시 (실행마다 다름) — 결과 예시 · Gemini CLI**

```text
✦ test_empty_string_returns_zero만 통과하도록
  최소 구현을 하겠다.
  Edit src/calculator.py
-     raise NotImplementedError
+     return 0
✦ 테스트 파일은 수정하지 않았다.
  1 passed
```

**실행 명령 · 결과 — ③ 다시 실행 → GREEN · 터미널**

```text
> pytest -q --tb=short
.  [100%]
1 passed in 0.02s
```

### 슬라이드 89 — R2 · 숫자 하나 입력 — 해당 숫자 반환
<sub>Day 1 · 5교시  |  실습 1 · R2</sub>

**▶ 프롬프트 — 테스트를 AI 에게 맡길 때 (직접 쓰기 어려우면)**

```text
@tests/test_calculator.py @src/calculator.py
기존 테스트는 수정하지 말고 test_single_number_returns_itself 1개만 추가해줘: add("7") 이 7 을 돌려주는지 검증한다.
src/ 는 수정하지 마. 구현은 하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**코드 — ① 직접 작성(또는 위 프롬프트로) — tests/test_calculator.py**

```python
from calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_itself():
    assert add("7") == 7
```

**실행 명령 · 결과 — ② 실행 → RED 확인 · 터미널**

```text
> pytest -q --tb=short
.F  [100%]
=== FAILURES ===
___ test_single_number_returns_itself ___
tests/test_calculator.py:9: in test_single_number_returns_itself
    assert add("7") == 7
E   AssertionError: assert 0 == 7
E    +  where 0 = add('7')
=== short test summary info ===
FAILED tests/test_calculator.py::test_single_number_returns_itself
1 failed, 1 passed in 0.02s
```

### 슬라이드 90 — R2 · 최소 구현
<sub>Day 1 · 5교시  |  실습 1 · R2</sub>

**▶ 프롬프트 — Gemini CLI**

```text
@tests/test_calculator.py @src/calculator.py
test_single_number_returns_itself 만 통과하는 최소 구현을 해줘.
테스트 파일은 수정하지 마. 다른 기능은 추가하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**AI 응답 예시 (실행마다 다름) — 결과 예시 · Gemini CLI**

```text
✦ 빈 문자열은 0, 그 외에는 정수로 변환하겠다.
  Edit src/calculator.py
-     return 0
+     if numbers == "":
+         return 0
+     return int(numbers)
✦ 2 passed
```

**실행 명령 · 결과 — ③ 다시 실행 → GREEN · 터미널**

```text
> pytest -q --tb=short
..  [100%]
2 passed in 0.02s
```

### 슬라이드 91 — R3·R4 · 쉼표로 구분된 여러 숫자
<sub>Day 1 · 5교시  |  실습 1 · R3·R4</sub>

**▶ 프롬프트 — 테스트를 AI 에게 맡길 때 (직접 쓰기 어려우면)**

```text
@tests/test_calculator.py @src/calculator.py
기존 테스트는 그대로 두고 2개만 추가해줘: test_two_numbers_separated_by_comma (add("1,2") == 3), test_many_numbers (add("1,2,3,4") == 10).
src/ 는 수정하지 마. 구현은 하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**코드 — ① 직접 작성(또는 위 프롬프트로) — tests/test_calculator.py**

```python
from calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_itself():
    assert add("7") == 7

def test_two_numbers_separated_by_comma():
    assert add("1,2") == 3

def test_many_numbers():
    assert add("1,2,3,4") == 10
```

**실행 명령 · 결과 — ② 실행 → RED 확인 · 터미널**

```text
> pytest -q --tb=short
..FF  [100%]
=== FAILURES ===
___ test_two_numbers_separated_by_comma ___
tests/test_calculator.py:13: in test_two_numbers_separated_by_comma
    assert add("1,2") == 3
           ^^^^^^^^^^
src/calculator.py:4: in add
    return int(numbers)
…
=== short test summary info ===
FAILED tests/test_calculator.py::test_two_numbers_separated_by_comma
FAILED tests/test_calculator.py::test_many_numbers - ValueError...
2 failed, 2 passed in 0.02s
```

### 슬라이드 92 — R3·R4 · 최소 구현
<sub>Day 1 · 5교시  |  실습 1 · R3·R4</sub>

**▶ 프롬프트 — Gemini CLI**

```text
@tests/test_calculator.py @src/calculator.py
test_two_numbers_separated_by_comma, test_many_numbers 만 통과하는 최소 구현을 해줘.
테스트 파일은 수정하지 마. 다른 기능은 추가하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**AI 응답 예시 (실행마다 다름) — 결과 예시 · Gemini CLI**

```text
✦ 쉼표로 나눈 뒤 각 값을 더하겠다.
  Edit src/calculator.py
-     return int(numbers)
+     return sum(int(n) for n in numbers.split(","))
✦ 4 passed
```

**실행 명령 · 결과 — ③ 다시 실행 → GREEN · 터미널**

```text
> pytest -q --tb=short
....  [100%]
4 passed in 0.02s
```

### 슬라이드 96 — R5 · 세미콜론 구분자 — 테스트부터
<sub>Day 1 · 6교시  |  실습 2 · R5</sub>

**▶ 프롬프트 — 테스트를 AI 에게 맡길 때 (직접 쓰기 어려우면)**

```text
@tests/test_calculator.py @src/calculator.py
R1~R4 테스트는 그대로 두고 2개만 추가해줘: test_semicolon_is_also_a_delimiter (add("1;2") == 3), test_mixed_delimiters (add("1,2;3") == 6).
src/ 는 수정하지 마. 구현은 하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**코드 — ① 직접 작성(또는 위 프롬프트로) — tests/test_calculator.py**

```python
from calculator import add
…  (R1~R4 테스트 그대로)

def test_semicolon_is_also_a_delimiter():
    assert add("1;2") == 3

def test_mixed_delimiters():
    assert add("1,2;3") == 6
```

**실행 명령 · 결과 — ② 실행 → RED 확인 · 터미널**

```text
> pytest -q --tb=short
....FF  [100%]
=== FAILURES ===
___ test_semicolon_is_also_a_delimiter ___
tests/test_calculator.py:21: in test_semicolon_is_also_a_delimiter
    assert add("1;2") == 3
           ^^^^^^^^^^
…
=== short test summary info ===
FAILED tests/test_calculator.py::test_semicolon_is_also_a_delimiter
FAILED tests/test_calculator.py::test_mixed_delimiters - ValueE...
2 failed, 4 passed in 0.02s
```

### 슬라이드 97 — 평소처럼 짧게 요청하면 — AI가 기존 기능을 깨뜨린다
<sub>Day 1 · 6교시  |  실습 2 · R5</sub>

**▶ 프롬프트 — 일부러 짧게**

```text
@src/calculator.py 세미콜론도 구분자로 쓸 수 있게 바꿔줘.
```

**AI 응답 예시 (실행마다 다름) — 결과 예시 · Gemini CLI**

```text
✦ 구분자를 세미콜론으로 변경했다.
  Edit src/calculator.py
-     return sum(int(n) for n in numbers.split(","))
+     return sum(int(n) for n in numbers.split(";"))
```

**실행 명령 · 결과 — pytest가 바로 알려 준다 · 터미널**

```text
> pytest -q --tb=short
..FF.F  [100%]
=== FAILURES ===
___ test_two_numbers_separated_by_comma ___
tests/test_calculator.py:13: in test_two_numbers_separated_by_comma
…  (실패 3건 상세 생략)
=== short test summary info ===
FAILED tests/test_calculator.py::test_two_numbers_separated_by_comma
FAILED tests/test_calculator.py::test_many_numbers - ValueError...
FAILED tests/test_calculator.py::test_mixed_delimiters - ValueE...
3 failed, 3 passed in 0.02s
```

### 슬라이드 98 — 회귀를 고친다 — 기준은 '모든 테스트'
<sub>Day 1 · 6교시  |  실습 2 · R5</sub>

**▶ 프롬프트 — Gemini CLI**

```text
@tests/test_calculator.py @src/calculator.py
방금 변경으로 기존 테스트 3개가 실패해. 쉼표와 세미콜론을 모두 구분자로 지원해서 모든 테스트를 통과시켜줘. 테스트 파일은 수정하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**AI 응답 예시 (실행마다 다름) — 결과 예시 · Gemini CLI**

```text
✦ 쉼표와 세미콜론 둘 다로 나누도록
  정규식을 쓰겠다.
  Edit src/calculator.py
+ import re
-     return sum(int(n) for n in numbers.split(";"))
+     return sum(int(n) for n in
+                re.split(r"[,;]", numbers))
✦ 6 passed
```

**실행 명령 · 결과 — ③ 다시 실행 → GREEN · 터미널**

```text
> pytest -q --tb=short
......  [100%]
6 passed in 0.02s
```

### 슬라이드 99 — R6 · 음수는 오류 — 예외도 테스트한다
<sub>Day 1 · 6교시  |  실습 2 · R6</sub>

**▶ 프롬프트 — 테스트를 AI 에게 맡길 때 (직접 쓰기 어려우면)**

```text
@tests/test_calculator.py @src/calculator.py
기존 테스트는 그대로 두고 test_negative_numbers_raise_error 1개만 추가해줘: add("-1,2,-3") 이 ValueError 를 던지고,
메시지가 '음수는 허용하지 않습니다: -1, -3' 인지 pytest.raises(ValueError, match=...) 로 검증한다.
src/ 는 수정하지 마. 구현은 하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**코드 — ① 직접 작성(또는 위 프롬프트로) — tests/test_calculator.py**

```python
import pytest
…  (기존 테스트 그대로)

def test_negative_numbers_raise_error():
    message = "음수는 허용하지 않습니다: -1, -3"
    with pytest.raises(ValueError, match=message):
        add("-1,2,-3")
```

**실행 명령 · 결과 — ② 실행 → RED 확인 · 터미널**

```text
> pytest -q --tb=short
......F  [100%]
=== FAILURES ===
___ test_negative_numbers_raise_error ___
tests/test_calculator.py:31: in test_negative_numbers_raise_error
    with pytest.raises(ValueError, match=message):
E   Failed: DID NOT RAISE ValueError
=== short test summary info ===
FAILED tests/test_calculator.py::test_negative_numbers_raise_error
1 failed, 6 passed in 0.02s
```

### 슬라이드 100 — R6 · 최소 구현
<sub>Day 1 · 6교시  |  실습 2 · R6</sub>

**▶ 프롬프트 — Gemini CLI**

```text
@tests/test_calculator.py @src/calculator.py
test_negative_numbers_raise_error 만 통과하는 최소 구현을 해줘.
테스트 파일은 수정하지 마. 다른 기능은 추가하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**AI 응답 예시 (실행마다 다름) — 결과 예시 · Gemini CLI**

```text
✦ 값을 먼저 정수 목록으로 만든 뒤 음수를 모아
  메시지에 넣겠다.
  Edit src/calculator.py
+     if numbers == "":
+         return 0
+     values = [int(n) for n in re.split(r"[,;]", numbers)]
+     negatives = [v for v in values if v < 0]
+     if negatives:
+         listed = ", ".join(map(str, negatives))
+         raise ValueError(f"음수는 허용하지 않습니다: {listed}")
+     return sum(values)
✦ 7 passed
```

**실행 명령 · 결과 — ③ 다시 실행 → GREEN · 터미널**

```text
> pytest -q --tb=short
.......  [100%]
7 passed in 0.02s
```

### 슬라이드 103 — AI에게 테스트를 리뷰받는다 — plan 모드, 수정 없이
<sub>Day 1 · 7교시  |  테스트 리뷰</sub>

**▶ 프롬프트 — REVIEW 템플릿**

```text
@tests/test_calculator.py 테스트를 검토만 해줘. 파일은 수정하지 마.
관점: 테스트 이름, AAA 구조, 한 테스트에 한 규칙, 빠진 경계값.
표로: 테스트 | 문제 | 제안
```

**AI 응답 예시 (실행마다 다름) — 결과 예시 · Gemini CLI (plan 모드)**

```text
✦ 전반적으로 이름이 규칙을 잘 설명한다. 제안 세 가지이다.
  1. test_many_numbers
     문제: '많은'이 몇 개인지 모호  →  제안: test_four_numbers_are_summed
  2. test_negative_numbers_raise_error
     문제: 음수가 하나뿐인 경우가 없음  →  제안: add("-5") 케이스 추가
  3. (없음)
     문제: 공백만 있는 입력이 정의되지 않음  →  제안: 요구사항 확인 후 테스트
```

### 슬라이드 105 — R7 · 테스트를 AI 에게 맡길 때 — 프롬프트 · 결과 · 실행
<sub>Day 1 · 7교시  |  점검 실습 · 풀이</sub>

**▶ 프롬프트 — Gemini CLI**

```text
@src/calculator.py @tests/test_calculator.py
기존 테스트는 수정하지 말고 test_whitespace_only_returns_zero 1개만 추가해줘: add("   ") 이 0 을 돌려주는지 검증한다.
src/ 는 수정하지 마. 구현은 하지 마. 끝나면 !pytest -q --tb=short 로 실패 이유(int('   '))를 보여줘.
```

**AI 응답 예시 (실행마다 다름) — 결과 예시**

```text
결과 예시 — Gemini CLI
✦ 테스트 1개를 추가했다.
  Edit tests/test_calculator.py
+ def test_whitespace_only_returns_zero():
+     assert add("   ") == 0
✦ 1 failed, 7 passed — int('   ') 변환에서 실패한다.
```

**실행 명령 · 결과 — ② 실행 → RED 확인 · 터미널**

```text
> pytest -q --tb=short
.......F  [100%]
=== FAILURES ===
___ test_whitespace_only_returns_zero ___
…  (상세 생략)
=== short test summary info ===
FAILED tests/test_calculator.py::test_whitespace_only_returns_zero
1 failed, 7 passed in 0.02s
```

### 슬라이드 108 — 골든 마스터 작성 프롬프트 — 입력 목록과 비교 테스트를 AI 에게
<sub>Day 1 · 7교시  |  골든 마스터</sub>

**▶ 프롬프트 — Gemini CLI**

```text
@src/calculator.py @tests/test_calculator.py
add() 의 '현재 동작'을 골든 마스터로 고정하는 테스트를 tests/test_golden_master.py 에 만들어줘.
- 입력 16개: 빈 문자열 · 공백만 · 숫자 하나 · 쉼표 · 세미콜론 · 혼합 · 음수 · 잘못된 값(a,b) · 빈 항목(1,,2 / 1,2,)
- 각 입력의 결과(정수) 또는 오류 종류(ValueError)를 tests/golden/add.golden.json 에 저장
- 골든 파일이 있으면 비교만, UPDATE_GOLDEN=1 일 때만 갱신. 골든이 없으면 FAIL
- src/ 와 기존 테스트는 수정하지 마. 끝나면 !pytest -q 결과를 보여줘.
```

**AI 응답 예시 (실행마다 다름) — 결과 예시 · 터미널**

```text
> pytest -q --tb=line
E   Failed: 골든 파일이 없다 — UPDATE_GOLDEN=1 로 만든 뒤 …
FAILED tests/test_golden_master.py::test_golden_master
1 failed, 8 passed in 0.12s

> UPDATE_GOLDEN=1 pytest -q tests/test_golden_master.py
1 passed in 0.02s                 # PowerShell: $env:UPDATE_GOLDEN=1

> pytest -q
9 passed in 0.02s

✦ 골든 파일을 읽고 승인한 뒤 커밋한다  (git add tests/golden)
```

**코드 — 파일**

```python
읽을 것
// tests/golden/add.golden.json (일부)
"":        {"result": 0},
"   ":     {"result": 0},
"1,2;3":   {"result": 6},
"-1,2,-3": {"error": "ValueError"},
"a,b":     {"error": "ValueError"},
"1,,2":    {"error": "ValueError"},   # ← 의도?
"1,2,":    {"error": "ValueError"},   # ← 의도?
...
```

### 슬라이드 110 — 보너스 — GREEN 상태에서 리팩터링 맛보기
<sub>Day 1 · 7교시  |  보너스</sub>

**▶ 프롬프트 — REFACTOR 템플릿**

```text
@src/calculator.py 모든 테스트가 통과하는 상태야. 동작은 바꾸지 말고 함수를 읽기 쉽게 작은 함수로 나눠줘.
테스트 파일은 수정하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**코드 — 결과 예시**

```python
import re

DELIMITERS = r"[,;]"

def add(numbers: str) -> int:
    if not numbers.strip():
        return 0
    values = _parse(numbers)
    _reject_negatives(values)
    return sum(values)

def _parse(numbers: str) -> list[int]:
    return [int(n) for n in re.split(DELIMITERS, numbers)]

def _reject_negatives(values: list[int]) -> None:
    negatives = [v for v in values if v < 0]
    if negatives:
        listed = ", ".join(map(str, negatives))
        raise ValueError(f"음수는 허용하지 않습니다: {listed}")
```

**실행 명령 · 결과 — 터미널**

```text
> pytest -q --tb=short
.........  [100%]
9 passed in 0.02s
```
