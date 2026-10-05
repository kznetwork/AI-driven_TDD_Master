# 실습 프롬프트 — demo
강사 시연 — add · divide 로 RED → GREEN → REFACTOR (Day 1 4교시)  
교안: `AI_TDD_2일과정_교안_v5.pptx`

## 쓰는 법
- 이 파일을 VS Code 에서 열어 두고(`Ctrl+Shift+V` 미리보기), 코드 블록을 복사해 Gemini CLI 에 붙여 넣습니다.
- **Gemini CLI 는 반드시 이 프로젝트 폴더에서 실행**합니다. `@파일`, `!명령` 이 이 폴더를 기준으로 동작합니다.
- `@경로` 는 파일을 대화에 넣고, `!명령` 은 셸 명령을 실행해 결과를 보여 줍니다.
- 'plan 모드' 표시는 수정 없이 계획 · 검토만 받는 단계입니다 (교안 안내대로 plan 모드로 전환하거나, 프롬프트의 '수정하지 마' 로 대신합니다).
- '일부러 나쁜 예' 는 실패를 체험하는 단계입니다. 실행 후 강사 안내에 따라 변경을 되돌립니다.
- 기대 결과는 요약입니다. **AI 응답 문구와 코드 모양은 실행마다 다릅니다.** 판단 기준은 언제나 `pytest` 결과입니다.

## Day 1 · 4교시

### 강사 시연 ① RED — 테스트만 먼저 (스텁)
<sub>슬라이드 80</sub>

```text
tests/test_calc.py 에 test_add 테스트만 작성해줘.
src/calc.py 는 NotImplementedError 스텁으로 둬.
```

**기대 결과(요약)** 1 failed — NotImplementedError (아직 구현 없음)

### 강사 시연 ① GREEN — 가장 단순한 구현
<sub>슬라이드 80</sub>

```text
방금 테스트를 통과시키도록 add(a, b) 를
가장 단순하게 구현해줘. 테스트는 수정하지 마.
```

**기대 결과(요약)** 1 passed · tests/ 변경 없음

### 강사 시연 ① REFACTOR — 타입 힌트 · docstring
<sub>슬라이드 80</sub>

```text
동작은 바꾸지 말고 타입 힌트와 docstring 만
정리해줘. 끝나면 !pytest -q 결과를 보여줘.
```

**기대 결과(요약)** 여전히 1 passed

### 강사 시연 ② 경계값 RED — divide(1, 0)
<sub>슬라이드 81</sub>

```text
tests/test_calc.py 에 divide(1, 0) 이 ZeroDivisionError 를
던지는지 검증하는 테스트만 추가해줘. src/ 는 수정하지 마.
```

**기대 결과(요약)** 1 failed, 1 passed (NotImplementedError)

### 강사 시연 ② GREEN
<sub>슬라이드 81</sub>

```text
!pytest -q 실패 로그를 보고, 방금 테스트만 통과시키는
최소 구현을 해줘. 다른 기능은 추가하지 마.
```

**기대 결과(요약)** 2 passed
