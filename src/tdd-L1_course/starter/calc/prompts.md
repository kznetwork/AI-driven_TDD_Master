# 실습 프롬프트 — calc
문자열 계산기 — RED · GREEN · REFACTOR 첫 사이클 (Day 1)  
교안: `AI_TDD_2일과정_교안_v5.pptx`

## 쓰는 법
- 이 파일을 VS Code 에서 열어 두고(`Ctrl+Shift+V` 미리보기), 코드 블록을 복사해 Gemini CLI 에 붙여 넣습니다.
- **Gemini CLI 는 반드시 이 프로젝트 폴더에서 실행**합니다. `@파일`, `!명령` 이 이 폴더를 기준으로 동작합니다.
- `@경로` 는 파일을 대화에 넣고, `!명령` 은 셸 명령을 실행해 결과를 보여 줍니다.
- 'plan 모드' 표시는 수정 없이 계획 · 검토만 받는 단계입니다 (교안 안내대로 plan 모드로 전환하거나, 프롬프트의 '수정하지 마' 로 대신합니다).
- '일부러 나쁜 예' 는 실패를 체험하는 단계입니다. 실행 후 강사 안내에 따라 변경을 되돌립니다.
- 기대 결과는 요약입니다. **AI 응답 문구와 코드 모양은 실행마다 다릅니다.** 판단 기준은 언제나 `pytest` 결과입니다.

## Day 1 · 오리엔테이션

### 환경 확인 — Gemini CLI가 폴더를 읽는지
<sub>슬라이드 11 · 08:30–09:00</sub>

```text
이 폴더에 어떤 파일과 폴더가 있는지 목록만 알려줘. 아무것도 수정하지 마.
```

**기대 결과(요약)** pytest.ini, src/, tests/ 목록. 아무 파일도 바뀌지 않아야 함

## Day 1 · 5교시

### R1 · 빈 문자열 → 0
<sub>슬라이드 86</sub>

```text
@tests/test_calculator.py @src/calculator.py
test_empty_string_returns_zero 만 통과하는 최소 구현을 해줘.
테스트 파일은 수정하지 마. 다른 기능은 추가하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**기대 결과(요약)** 1 passed

### R2 · 숫자 하나
<sub>슬라이드 88</sub>

```text
@tests/test_calculator.py @src/calculator.py
test_single_number_returns_itself 만 통과하는 최소 구현을 해줘.
테스트 파일은 수정하지 마. 다른 기능은 추가하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**기대 결과(요약)** 2 passed

### R3 · R4 · 쉼표 구분 · 여러 숫자
<sub>슬라이드 90</sub>

```text
@tests/test_calculator.py @src/calculator.py
test_two_numbers_separated_by_comma, test_many_numbers 만 통과하는 최소 구현을 해줘.
테스트 파일은 수정하지 마. 다른 기능은 추가하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**기대 결과(요약)** 4 passed

## Day 1 · 6교시

### R5 · 일부러 짧게 요청 (회귀 체험)  `일부러 나쁜 예`
<sub>슬라이드 95</sub>

```text
@src/calculator.py 세미콜론도 구분자로 쓸 수 있게 바꿔줘.
```

**기대 결과(요약)** 구분자가 세미콜론으로 '바뀌어' 3 failed, 3 passed

### R5 · 회귀 복구
<sub>슬라이드 96</sub>

```text
@tests/test_calculator.py @src/calculator.py
방금 변경으로 기존 테스트 3개가 실패해. 쉼표와 세미콜론을 모두 구분자로 지원해서 모든 테스트를 통과시켜줘. 테스트 파일은 수정하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**기대 결과(요약)** 6 passed

### R6 · 음수 오류
<sub>슬라이드 98</sub>

```text
@tests/test_calculator.py @src/calculator.py
test_negative_numbers_raise_error 만 통과하는 최소 구현을 해줘.
테스트 파일은 수정하지 마. 다른 기능은 추가하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**기대 결과(요약)** 7 passed (ValueError 메시지에 음수 목록)

## Day 1 · 7교시

### 테스트 리뷰 (plan 모드)
<sub>슬라이드 101</sub>

```text
@tests/test_calculator.py 테스트를 검토만 해줘. 파일은 수정하지 마.
관점: 테스트 이름, AAA 구조, 한 테스트에 한 규칙, 빠진 경계값.
표로: 테스트 | 문제 | 제안
```

**기대 결과(요약)** 테스트 | 문제 | 제안 표. 파일 변경 없음

### R7 · 공백만 있는 입력 → 0
<sub>슬라이드 103</sub>

```text
@tests/test_calculator.py @src/calculator.py
test_whitespace_only_returns_zero 만 통과하는 최소 구현을 해줘. 테스트 파일은 수정하지 마. 다른 기능은 추가하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**기대 결과(요약)** 1 failed → 8 passed

### 보너스 · 리팩터링
<sub>슬라이드 104</sub>

```text
@src/calculator.py 모든 테스트가 통과하는 상태야. 동작은 바꾸지 말고 함수를 읽기 쉽게 작은 함수로 나눠줘.
테스트 파일은 수정하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**기대 결과(요약)** 8 passed 유지
