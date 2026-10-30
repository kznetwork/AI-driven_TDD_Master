# 프롬프트 — Gilded Rose 레거시 QA · 속성 테스트 (모든 코딩 에이전트 공통)

교안 `(교안) 실전-Coding Agent 실전 AI기반 TDD 마스터 과정_20261010_작업폴더안내.pptx` 부록 A · B · C 의 프롬프트입니다. 본문은 Gemini CLI · Claude Code · Copilot Chat · 그 밖의 코딩 에이전트에서 그대로 쓰고,
파일 첨부 표기(`@파일` / `#file:파일`)만 도구에 맞춥니다. 모든 프롬프트는 ‘한 번에 하나, 먼저 계획·진단, 수정은 테스트 GREEN 에서만’ 원칙을 따릅니다.

## 요구사항 분석 → 규칙표 · OQ
<sub>슬라이드 224 · 부록 A · A.1</sub>

```text
[역할] 레거시 코드 QA 분석가
[입력] GildedRoseRequirements.md · README.md  (코드는 보지 마)
[작업] 아이템 종류별(일반 · Aged Brie · Sulfuras · Backstage · Conjured) 규칙을 표로 정리해줘.
  열: 아이템 | 규칙 ID(R-n) | 규칙 | 경계 조건 | 출처(문서 위치)
  모호하거나 서로 충돌하는 곳은 표 아래 ‘열린 질문(OQ-n)’으로만 적어줘.
[제약] 파일 수정 금지. 요구사항에 없는 규칙을 만들지 마.
[출력] 마크다운 표 2개 (규칙표, OQ 표)
```

**기대 결과(요약)** 규칙표(R-n)와 열린 질문(OQ-n). 코드는 보지 않음

## 레거시 코드 읽기 → 분기 지도
<sub>슬라이드 228 · 부록 A · A.2</sub>

```text
[역할] 레거시 코드 리뷰어
@gilded_rose.py 의 update_quality() 를 읽고, 수정 없이 아래를 만들어줘.
1) 분기 지도: 조건 | 하는 일 | 대응하는 규칙(R-n)
2) 규칙표에 대응하지 않는 분기는 ‘의도 불명’으로 표시
3) 위험 지점 5개 이내: 위치 · 이유 · 리팩터링 전에 필요한 테스트
[제약] 코드와 Item 클래스는 수정 금지. 추측은 ‘추정’이라고 적어줘.
[출력] 표 3개
```

**기대 결과(요약)** 분기 지도 · 의도 불명 분기 · 위험 지점 5개 이내

## 테스트 케이스 설계
<sub>슬라이드 230 · 부록 A · A.3</sub>

```text
[역할] 테스트 설계자
[입력] 규칙표(R-n) + @gilded_rose.py
[작업] 규칙마다 테스트 케이스를 표로 설계해줘.
  열: TC | 규칙 | 유형(일반·경계·오류) | 입력(name, sell_in, quality) | 기대 결과 | 우선순위(★)
  경계는 바로 아래 · 정확히 · 바로 위를 짝으로 (Backstage 11/10 · 6/5 · 1/0, quality 0/49/50)
[제약] 기대값은 요구사항에서만 가져와. 현재 코드의 출력을 베끼지 마. 어긋나면 OQ 로.
[출력] 표 1개 + ★★★ 케이스 목록
```

**기대 결과(요약)** TC 표(경계 짝 · 우선순위 ★)

## 테스트 코드 작성
<sub>슬라이드 233 · 부록 A · A.3</sub>

```text
@docs/테스트케이스.md 의 ★★★ 케이스를 tests/test_gilded_rose.py 에 pytest 로 작성해줘.
- 규칙마다 함수 1개, 같은 규칙의 경계는 @pytest.mark.parametrize 로
- 함수 이름은 규칙을 말하게, docstring 에 TC · R 번호
- Item 클래스와 gilded_rose.py 는 수정하지 마
- 끝나면 !pytest -q 결과를 보여줘. 레거시에서 통과해야 정상(특성화) — 실패하면 먼저 기대값과 OQ 를 의심해줘
```

**기대 결과(요약)** 12 passed (레거시에서 통과)

## 상수 리팩터링
<sub>슬라이드 236 · 부록 A · A.4</sub>

```text
@gilded_rose.py 모든 테스트가 통과하는 상태야.
동작은 바꾸지 말고, 아이템 이름 문자열과 매직 넘버(0 · 50 · 80)를 constants.py 의 이름 있는 상수로 바꾸는 것만 해줘.
- Item 클래스 · 테스트 수정 금지, 구조 변경(메서드 추출 등) 금지
- 이름 하나를 바꿀 때마다 pytest 를 실행해줘
- 끝나면 pytest -q 결과와 git diff --stat 을 보여줘
```

**기대 결과(요약)** 동작 불변 · constants.py

## 골든 마스터(승인 테스트) 작성
<sub>슬라이드 239 · 부록 A · A.5</sub>

```text
@gilded_rose.py @texttest_fixture.py
update_quality() 의 현재 동작을 골든 마스터로 고정하는 테스트를 만들어줘.
- 아이템 6종(+5 Dexterity Vest · Aged Brie · Elixir · Sulfuras×2 · Backstage) × 30일. Conjured 는 넣지 마 (곧 바꿀 대상)
- tests/test_gilded_rose_approval.py: approvaltests 의 verify(), 또는 도구 없이 JSON 비교
- 승인 파일은 만들어 두되, 내가 읽고 승인하기 전에는 커밋하지 마
- 같은 코드를 두 번 돌려 결과가 같은지(결정성)도 확인해줘. 코드는 수정하지 마
```

**기대 결과(요약)** 첫 실행 FAIL → 사람이 승인 → PASS

## Conjured TDD (RED · GREEN · REFACTOR) — ① RED — 테스트만
<sub>슬라이드 242 · 부록 A · A.6</sub>

```text
@tests/test_conjured.py 에 Conjured Mana Cake 요구(일반의 2배: -2/일, 판매일 후 -4, 최소 0)의 테스트 3개만 작성해줘.
구현은 하지 마. 실행해서 실패 이유를 한 줄씩 설명하고, 이미 통과하는 테스트는 ‘이미 충족’이라고 보고해줘.
```

**기대 결과(요약)** RED 2 failed + 1 이미 충족 → GREEN → REFACTOR

## Conjured TDD (RED · GREEN · REFACTOR) — ② GREEN — 최소 구현
<sub>슬라이드 242 · 부록 A · A.6</sub>

```text
방금 실패한 Conjured 테스트만 통과하는 최소 코드를 gilded_rose.py 에 추가해줘.
다른 아이템 동작과 승인 파일은 바뀌면 안 돼. 테스트는 수정하지 마. 끝나면 pytest -q 결과를 보여줘.
```

**기대 결과(요약)** RED 2 failed + 1 이미 충족 → GREEN → REFACTOR

## Conjured TDD (RED · GREEN · REFACTOR) — ③ REFACTOR — 동작 불변 정리
<sub>슬라이드 242 · 부록 A · A.6</sub>

```text
모든 테스트가 통과하는 상태야. 동작은 바꾸지 말고 상·하한 처리를 _degrade / _upgrade 헬퍼로 모으는 것만 해줘.
승인 파일 diff 가 없어야 해.
```

**기대 결과(요약)** RED 2 failed + 1 이미 충족 → GREEN → REFACTOR

## 테스트 점검 (7가지 함정)
<sub>슬라이드 244 · 부록 A · A.7</sub>

```text
[역할] 테스트 리뷰어
@tests/ 를 아래 7가지 함정 관점으로 점검해줘. 파일은 수정하지 마.
함정: 가짜 RED · 변경 대상을 골든에 포함 · 골든 자동 갱신 · 비결정적 출력 · 현재 코드에서 예상값 베끼기 · 값만 확인하는 테스트 · 경계 한쪽만
[출력] 표: 함정 | 해당 여부 | 근거(파일:줄) | 제안   — 새 규칙은 만들지 마.
```

**기대 결과(요약)** 함정 표

## 코드 스멜 분석
<sub>슬라이드 248 · 부록 B · B.2</sub>

```text
[역할] 리팩터링 컨설턴트 (Fowler 『리팩토링』 기준)
@gilded_rose.py (상수 정리 후)의 코드 스멜을 분석해줘. 수정하지 마.
[출력] 표: 위치(함수·줄) | 스멜 | 근거 | 위험도(상·중·하) | 처방(기법 · 패턴 후보) | 난이도
후보: 긴 함수 · 깊은 중첩 · 중복 코드 · 매직 넘버 · 반복되는 switch · 기능 편애
마지막에 ‘고치는 순서’를 의존성 순으로 제안해줘.
[제약] 이미 통과하는 테스트가 있는 범위 안에서만 제안해줘.
```

**기대 결과(요약)** 스멜 표 + 고치는 순서

## 리팩토링 계획서
<sub>슬라이드 249 · 부록 B · B.2</sub>

```text
위 스멜 분석을 바탕으로 docs/refactoring-plan.md 를 작성해줘. 코드는 수정하지 마.
구성: 1) 목표와 비목표  2) 안전망(테스트 · 골든 마스터 상태, 실행 명령)
3) 단계표(STEP 1…n): 단계 | 변경 내용 | 리팩토링 기법 | 완료 기준(전체 테스트 GREEN) | 롤백 방법
4) 커밋 규칙(refactor: …, 구조 변경과 기능 변경 분리)  5) 위험과 대응
한 단계는 10분 이내, 단계마다 테스트 실행 → 커밋.
```

**기대 결과(요약)** docs/refactoring-plan.md (단계표)

## STEP 1 · 테스트 먼저
<sub>슬라이드 253 · 부록 B · B.4</sub>

```text
@docs/refactoring-plan.md 의 STEP 1 만 수행해줘.
- 부록 A 의 경계값 · 승인 테스트를 실행해 전체가 GREEN 인지 확인
- 빠진 경계(Backstage 11/10 · 6/5 · 1/0, quality 0/50)가 있으면 테스트만 추가
- 프로덕션 코드는 수정 금지
- 결과: 전체 테스트 수 · 통과 수 · 추가한 테스트 목록
```

**기대 결과(요약)** 전체 GREEN

## STEP 2 · 코드 정리
<sub>슬라이드 256 · 부록 B · B.5</sub>

```text
@docs/refactoring-plan.md 의 STEP 2 만 수행해줘. 동작은 바꾸지 마.
① 중복 조건 · 미사용 코드 제거  ② 인덱스 for → for item in self.items
한 가지씩 하고, 각각 pytest -q 를 실행해 결과를 보여줘.
메서드 추출 같은 구조 변경은 아직 하지 마. 테스트는 수정 금지.
```

**기대 결과(요약)** 각 변경 후 GREEN

## STEP 3 · 조건 분리
<sub>슬라이드 259 · 부록 B · B.6</sub>

```text
@docs/refactoring-plan.md 의 STEP 3 만 수행해줘.
부정 조건 반전(Invert if) · else + if → elif 병합 · 같은 타입 조건 합치기를 한 번에 하나씩.
적용 전에 ‘무엇을 어떻게 바꿀지’ 계획을 먼저 보여주고, 내가 승인하면 적용해줘.
조건의 의미(특히 sell_in < 0 경계)는 바뀌면 안 돼. 매 단계 pytest -q.
```

**기대 결과(요약)** 경계 불변 · GREEN

## STEP 4 · 메서드 추출
<sub>슬라이드 262 · 부록 B · B.7</sub>

```text
@docs/refactoring-plan.md 의 STEP 4 만 수행해줘.
update_quality() 의 타입별 분기를 _update_normal · _update_aged_brie · _update_backstage · _update_sulfuras 와 _update_sell_in 으로 Extract Method 해줘.
반환값과 부수효과는 그대로, 호출 순서(quality → sell_in → 판매일 후 처리)도 그대로.
메서드 하나 추출할 때마다 pytest -q 를 실행해줘.
```

**기대 결과(요약)** GREEN

## STEP 5 · 클래스 분리
<sub>슬라이드 265 · 부록 B · B.8</sub>

```text
@docs/refactoring-plan.md 의 STEP 5 만 수행해줘.
각 _update_* 메서드를 AgedBrieItem · BackstagePassItem · SulfurasItem · NormalItem 클래스로 옮겨줘 (파일 하나씩).
Item 클래스는 수정 금지 — 각 클래스가 item 을 감싸도록(self._item).
GildedRose 는 타입에 맞는 클래스를 골라 호출만 하게. 클래스 하나 옮길 때마다 pytest -q.
```

**기대 결과(요약)** Item diff 없음 · GREEN

## STEP 6 ① · 추상화 · 템플릿 메서드
<sub>슬라이드 272 · 부록 B · B.9</sub>

```text
@docs/refactoring-plan.md 의 STEP 6 중 ‘추상화’만 수행해줘.
공통 부모 GildedRoseItem(ABC)을 만들고 네 클래스가 상속하게 해줘. 필수 단계 update_quality() 는 추상 메서드로.
update() 에서 ‘quality 갱신 → sell_in 감소’ 순서를 고정(Template Method)하고, Sulfuras 만 update_sell_in() 을 재정의해줘.
클래스 하나씩 pytest -q.
```

**기대 결과(요약)** GREEN

## STEP 6 ② · Factory · 이름 통일 — 프롬프트 — Factory
<sub>슬라이드 273 · 부록 B · B.9</sub>

```text
create_item(item) Factory 함수를 만들어 타입 분기를 한 곳에 모으고, GildedRose.update_quality() 는 create_item(item).update() 만 호출하게 해줘.
동작은 그대로. pytest -q 결과를 보여줘.
```

**기대 결과(요약)** GREEN

## STEP 6 ② · Factory · 이름 통일 — 프롬프트 — 이름 통일
<sub>슬라이드 273 · 부록 B · B.9</sub>

```text
변수명 i · item · _item 이 섞여 있어. Rename 으로만 통일해줘 (논리 변경 금지). 한 이름씩 바꾸고 pytest -q.
```

**기대 결과(요약)** GREEN

## STEP 7 · F&B (TDD) — ① RED — 테스트만
<sub>슬라이드 276 · 부록 B · B.10</sub>

```text
이름에 ‘[F&B]’ 가 들어간 아이템: 일반의 2배 속도로 감소(-2/일), 판매일이 지나면 -4/일, 최소 0.
tests/test_food_beverage.py 에 테스트만 작성하고 실행해 실패 이유를 설명해줘. 구현 금지.
```

**기대 결과(요약)** 신규 + 기존 GREEN

## STEP 7 · F&B (TDD) — ② GREEN — 클래스 + Factory 한 줄
<sub>슬라이드 276 · 부록 B · B.10</sub>

```text
방금 테스트만 통과하게 FoodBeverageItem 클래스와 Factory 한 줄만 추가해줘.
기존 클래스 · 승인 파일 · 테스트는 수정 금지. 끝나면 pytest -q.
```

**기대 결과(요약)** 신규 + 기존 GREEN

## STEP 8–10 · 중복 제거
<sub>슬라이드 278 · 부록 B · B.11</sub>

```text
@docs/refactoring-plan.md 의 STEP 8~10 을 순서대로, 한 단계씩만 수행해줘.
8) 분기마다 반복되던 호출을 한 곳으로  9) 한 번만 쓰는 임시 변수 인라인  10) 남은 중복 제거
각 단계마다 변경 계획 → 적용 → pytest -q 결과를 보고해줘. 동작 · 테스트는 바꾸지 마.
```

**기대 결과(요약)** GREEN

## 레거시 대비 전수 비교
<sub>슬라이드 280 · 부록 B · B.12</sub>

```text
legacy/gilded_rose_legacy.py 와 현재 gilded_rose.py 를 비교하는 tests/test_golden_vs_legacy.py 를 만들어줘.
- 아이템 4종(일반 · Aged Brie · Sulfuras · Backstage) × sell_in -2~20 × quality 0~50 × 30일
- [F&B] 는 제외(의도한 동작 변경)
- 다르면 처음 5건을 ‘입력 · 레거시 결과 · 새 결과’ 표로 보여줘
- 프로덕션 코드는 수정하지 마.
```

**기대 결과(요약)** 차이 0 (F&B 제외)

## 최종 리뷰 · PR 설명
<sub>슬라이드 282 · 부록 B · B.13</sub>

```text
git diff main 을 읽고 PR 설명을 작성해줘. 코드는 수정하지 마.
구성: 변경 요약 · 단계별 커밋 목록 · 동작 불변의 근거(테스트 수 · 골든 · 레거시 비교) · 위험 · 남은 스멜
그다음 ‘리팩터링 함정 7가지’ 표로 점검해줘: 함정 | 해당 여부 | 근거 | 제안
```

**기대 결과(요약)** PR 설명 + 함정 점검 표

## 속성 테스트 작성 (hypothesis)
<sub>슬라이드 287 · 부록 C · C.4</sub>

```text
@src/cart.py @docs/예시표.md
예시 표 C6 과 같은 ‘불변식’을 hypothesis 로 tests/test_cart_property.py 에 작성해줘.
- 입력: price 0~1,000,000, qty 0~20 의 항목 리스트(최대 10개) × VIP 여부
- 성질: 0 ≤ 결제 ≤ 합계, VIP ≤ 일반
- 기대값을 구현 코드로 다시 계산하지 마 (성질만 assert)
- 반례가 나오면 고치지 말고 입력과 함께 보고해줘. src/ 는 수정 금지.
```

**기대 결과(요약)** 불변식 2개(0 ≤ 결제 ≤ 합계, VIP ≤ 일반) 통과. 반례가 나오면 입력과 함께 보고
