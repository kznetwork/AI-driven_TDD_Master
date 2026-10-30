# 실습 프롬프트 — demo
강사 시연 — add · divide 로 RED → GREEN → REFACTOR (Day 1 4교시, 강사용)  
교안: `(교안) 실전-Coding Agent 실전 AI기반 TDD 마스터 과정_20261021_개정.pptx`

## 어디에서 실습하나 (작업 폴더)

| 항목 | 내용 |
|---|---|
| 작업 폴더 | `C:\DEV\tdd-course\demo` |
| 만드는 법 | 강사가 나눠 준 `starter\demo` 폴더를 `C:\DEV\tdd-course\` 아래로 **폴더째 복사**한다 (폴더를 새로 만들 필요는 없다) |
| 여는 법 | VS Code → 파일 → 폴더 열기 → `C:\DEV\tdd-course\demo` · 터미널과 코딩 에이전트도 **이 폴더에서** 실행한다 |
| 이 폴더의 특징 | 강사 시연용이다 — 수강생은 따라 하지 않아도 된다 |
| 이 폴더를 쓰는 교안 슬라이드 | `(교안) 실전-Coding Agent 실전 AI기반 TDD 마스터 과정_20261021_개정.pptx` — 82–83, 205번 |

## 쓰는 법 (개정판)
- 각 항목은 **프롬프트 → 코드 → 실행 명령(기대 결과)** 순서로 모두 들어 있다. 코드는 직접 쓰는 테스트 · 소스이고, 프롬프트는 같은 일을 Gemini CLI 에 맡길 때 쓴다.
- 이 파일을 VS Code 에서 열어 두고(`Ctrl+Shift+V` 미리보기), 코드 블록을 복사해 Gemini CLI 에 붙여 넣는다. Gemini CLI 는 반드시 이 프로젝트 폴더에서 실행한다.
- `> ` 로 시작하는 줄은 터미널에서 실행하는 명령이고, 그 아래 줄은 실제로 실행해 얻은 결과다. AI 응답 문구와 코드 모양은 실행마다 다르다 — 판단 기준은 언제나 pytest 결과다.

### 슬라이드 82 — 강사 시연 ① 미니 체험 — add 로 RED → GREEN → REFACTOR
<sub>Day 1 · 4교시  |  강사 시연</sub>

**▶ ① RED — 테스트만 먼저**

```text
tests/test_calc.py 에 test_add 테스트만 작성해줘.
src/calc.py 는 NotImplementedError 스텁으로 둬.
```

**▶ ② GREEN — 최소 구현**

```text
방금 테스트를 통과시키도록 add(a, b) 를
가장 단순하게 구현해줘. 테스트는 수정하지 마.
```

**▶ ③ REFACTOR — 동작 불변**

```text
동작은 바꾸지 말고 타입 힌트와 docstring 만
정리해줘. 끝나면 !pytest -q 결과를 보여줘.
```

**코드 — tests/test_calc.py**

```python
from calc import add


def test_add():
    assert add(2, 3) == 5
```

**코드 — src/calc.py — GREEN**

```python
def add(a, b):
    return a + b
```

**코드 — src/calc.py — REFACTOR**

```python
def add(a: float, b: float) -> float:
    """두 수의 합을 돌려준다."""
    return a + b
```

**실행 명령 · 결과 — 터미널**

```text
RED
> pytest -q --tb=short
F  [100%]
E   NotImplementedError
1 failed in 0.01s
# RED 직후
git add tests/test_calc.py
```

**실행 명령 · 결과 — 터미널**

```text
GREEN
> pytest -q
.  [100%]
1 passed in 0.01s
# GREEN 구현 후
git diff -- tests/   # 출력 없음
git diff -- src/     # 구현 변경만 표시
```

**실행 명령 · 결과 — 터미널**

```text
여전히 GREEN
> pytest -q
.  [100%]
1 passed in 0.01s
```

### 슬라이드 83 — 강사 시연 ② 경계값 — divide(1, 0) 을 테스트로 고정한다
<sub>Day 1 · 4교시  |  강사 시연</sub>

**▶ ④ 경계값 RED**

```text
tests/test_calc.py 에 divide(1, 0) 이 ZeroDivisionError 를 던지는지 검증하는 테스트만 추가해줘. src/ 는 수정하지 마.
```

**▶ ⑤ GREEN**

```text
!pytest -q 실패 로그를 보고, 방금 테스트만 통과시키는 최소 구현을 해줘. 다른 기능은 추가하지 마.
```

**코드 — tests/test_calc.py**

```python
import pytest

from calc import add, divide


def test_add():
    assert add(2, 3) == 5


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
```

**실행 명령 · 결과 — 터미널**

```text
RED — divide 는 아직 스텁
> pytest -q --tb=short
.F  [100%]
E   NotImplementedError
1 failed, 1 passed in 0.01s
```

**코드 — 파일**

```python
def divide(a: float, b: float) -> float:
    return a / b
```

**실행 명령 · 결과 — 터미널**

```text
2 passed in 0.01s
```

### 슬라이드 205 — Code Smell & Refactoring — 진단은 plan, 수정은 한 번에 하나
<sub>3장 · 시연  |  미니 체험 ④</sub>

**▶ 진단 (plan 모드)**

```text
@src/user_service.py 의 코드 스멜을 찾아줘. 수정하지 말고 [위치 | 스멜 | 근거 | 처방] 표로, 우선순위 순으로 보고해줘.
```

**▶ 리팩터 (default 모드)**

```text
1순위 스멜(중복 코드 — 3의 법칙) 하나만 고쳐줘. format_full_name() 으로 추출하고 외부 동작은 바꾸지 마. 적용 전 계획을 먼저 보여주고, 끝나면 !pytest -q 결과를 보고해.
```

**실행 명령 · 결과 — ① 읽기 전용으로 진단**

```text
$ gemini --approval-mode plan
# 읽기 전용 세션: 파일 수정 불가
```
