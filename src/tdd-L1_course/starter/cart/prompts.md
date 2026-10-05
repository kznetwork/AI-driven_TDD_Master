# 실습 프롬프트 — cart
장바구니 할인 — 예시 표 → 테스트 → 구현 (Day 2)  
교안: `AI_TDD_2일과정_교안_v5.pptx`

## 쓰는 법
- 이 파일을 VS Code 에서 열어 두고(`Ctrl+Shift+V` 미리보기), 코드 블록을 복사해 Gemini CLI 에 붙여 넣습니다.
- **Gemini CLI 는 반드시 이 프로젝트 폴더에서 실행**합니다. `@파일`, `!명령` 이 이 폴더를 기준으로 동작합니다.
- `@경로` 는 파일을 대화에 넣고, `!명령` 은 셸 명령을 실행해 결과를 보여 줍니다.
- 'plan 모드' 표시는 수정 없이 계획 · 검토만 받는 단계입니다 (교안 안내대로 plan 모드로 전환하거나, 프롬프트의 '수정하지 마' 로 대신합니다).
- '일부러 나쁜 예' 는 실패를 체험하는 단계입니다. 실행 후 강사 안내에 따라 변경을 되돌립니다.
- 기대 결과는 요약입니다. **AI 응답 문구와 코드 모양은 실행마다 다릅니다.** 판단 기준은 언제나 `pytest` 결과입니다.

## Day 2 · 1교시

### 예시 표 빈틈 찾기 (plan 모드)  `plan 모드`
<sub>슬라이드 113</sub>

```text
아래 할인 규칙 예시 표를 검토만 해줘. 새 규칙을 만들지 말고, 빠진 경계값이나 서로 충돌하는 규칙만 질문 형태로 알려줘.
(예시 표 C1~C7 붙여넣기)
```

**기대 결과(요약)** 빠진 경계 · 충돌을 질문 형태로. 새 규칙은 만들지 않음

## Day 2 · 2교시

### L1 · 빈 장바구니 · 합계
<sub>슬라이드 117</sub>

```text
@tests/test_cart.py @src/cart.py
test_empty_cart_subtotal_is_zero, test_subtotal_sums_price_times_qty 만 통과하는 최소 구현을 해줘.
테스트 파일은 수정하지 마. 다른 기능은 추가하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**기대 결과(요약)** 2 passed

### L2 · 5만 원 경계 할인
<sub>슬라이드 120</sub>

```text
@tests/test_cart.py @src/cart.py
test_threshold_discount_boundary 만 통과하는 최소 구현을 해줘.
테스트 파일은 수정하지 마. 다른 기능은 추가하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**기대 결과(요약)** 5 passed

## Day 2 · 3교시

### 나쁜 예 — 금지 줄 없음 (GEMINI.md 만들기 전)  `일부러 나쁜 예`
<sub>슬라이드 123 · 11:30–12:00</sub>

```text
@tests/test_cart.py @src/cart.py 테스트가 다 통과하게 고쳐줘.  (← 금지 줄이 없다)
```

**기대 결과(요약)** AI가 테스트 기대값을 고쳐서 5 passed — 이게 문제

### 같은 나쁜 예 — GEMINI.md 만든 후  `일부러 나쁜 예`
<sub>슬라이드 125</sub>

```text
@tests/test_cart.py @src/cart.py 테스트가 다 통과하게 고쳐줘.
```

**기대 결과(요약)** 'tests/ 는 수정하지 않습니다'라며 멈추고 질문

## Day 2 · 4교시

### L3 · VIP 추가 할인 (순서 포함)
<sub>슬라이드 127 · 13:00–14:00</sub>

```text
@tests/test_cart.py @src/cart.py @docs/예시표.md
C3와 C4를 기준으로 다음 테스트를 통과하는 최소 구현을 해줘.
- test_vip_gets_extra_5_percent_after_threshold
- test_non_vip_gets_threshold_discount_only
기존 테스트도 계속 통과해야 해.
테스트 파일은 수정하지 마.
문서에 없는 기능은 추가하지 마.
끝나면 pytest -q --tb=short 결과를 보여줘.
```

**기대 결과(요약)** 2 failed → 7 passed

### L4 · 음수 가격 · 수량 거부
<sub>슬라이드 131</sub>

```text
@tests/test_cart.py @src/cart.py
test_negative_price_is_rejected 만 통과하는 최소 구현을 해줘.
테스트 파일은 수정하지 마. 다른 기능은 추가하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**기대 결과(요약)** 18 passed

## Day 2 · 6교시

### 리팩터링 후보 고르기 (plan 모드)  `plan 모드`
<sub>슬라이드 160 · 14:00–14:40</sub>

```text
@src/cart.py 모든 테스트가 통과하는 상태야. 동작은 바꾸지 않고 읽기 쉽게 만들 리팩터링 후보를
작은 것부터 3개 이하로 제안만 해줘. 파일은 수정하지 마.
```

**기대 결과(요약)** 후보 3개 이하 목록. 파일 변경 없음

### 리팩터링 1단계 · 상수 이름 붙이기
<sub>슬라이드 161</sub>

```text
@src/cart.py 모든 테스트가 통과하는 상태야.
동작은 바꾸지 말고 매직 넘버 50000, 90, 95 를 이름 있는 상수로 바꾸는 것만 해줘.
테스트 파일은 수정하지 마. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**기대 결과(요약)** 18 passed

### 리팩터링 2단계 · _percent_of 헬퍼
<sub>슬라이드 161</sub>

```text
좋아. 이번에는 '× 퍼센트 // 100' 반복을 _percent_of 헬퍼로 뽑는 것만 해줘. 나머지 조건은 같아.
```

**기대 결과(요약)** 18 passed

### 실험 B · 어제 A-4와 같은 '정리해줘'  `일부러 나쁜 예`
<sub>슬라이드 162 · 14:50–15:40</sub>

```text
@src/cart.py 코드가 좀 지저분하네. 깔끔하게 정리해줘. 끝나면 !pytest -q --tb=short 결과를 보여줘.
```

**확인** 결과를 직접 실행해 보고 기록표에 적으세요. (결과 예시는 실습 후 공개)
