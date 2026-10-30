# 실습 프롬프트 — ship
확인 실습 — 배송비 계산기 (계약표 · 테스트 플랜 · TDD · 골든 마스터 · 전략 패턴)  
교안: `(교안) 실전-Coding Agent 실전 AI기반 TDD 마스터 과정_20261021_개정.pptx`


## 진행 순서 (교안 슬라이드 211–225 · 시간 14:20–15:30 개인 + 15:30–15:50 짝 검토)
1. 요구 1~3 을 **계약표**로 (`docs/계약표_템플릿.md` → `docs/계약표.md`) — 슬라이드 214
2. 계약표 → **테스트 플랜** → **스켈레톤 코드**(`5 skipped`) — 슬라이드 215
3. 요구 1~3 을 하나씩 RED → GREEN (`5 passed`), 35분에 **요구 4** 발표 → 회귀 확인(`8 passed`)
4. 리팩터링 전에 **골든 마스터**(`9 passed`), 52분에 **요구 5** 발표 → **전략 패턴** 리팩터링 — 슬라이드 216
5. **추적성 매트릭스**와 체크리스트 점검 — 슬라이드 217 · 225 (모범 답안은 218–224)

프롬프트는 아래를 쓰되, 평가는 **프롬프트가 아니라 테스트와 기록**으로 합니다.
프롬프트에 꼭 들어가야 할 네 가지: 대상 파일(`@…`) · 범위(`… 만`) · 금지(`테스트 파일은 수정하지 마`) · 확인(`끝나면 !pytest -q 결과를 보여줘`).
GREEN 구현 프롬프트는 `../../프롬프트_템플릿.md` 의 GREEN 템플릿을 채워 씁니다.

## 어디에서 실습하나 (작업 폴더)

| 항목 | 내용 |
|---|---|
| 작업 폴더 | `C:\DEV\tdd-course\ship` |
| 만드는 법 | 강사가 나눠 준 `starter\ship` 폴더를 `C:\DEV\tdd-course\` 아래로 **폴더째 복사**한다 (폴더를 새로 만들 필요는 없다) |
| 여는 법 | VS Code → 파일 → 폴더 열기 → `C:\DEV\tdd-course\ship` · 터미널과 코딩 에이전트도 **이 폴더에서** 실행한다 |
| 처음 한 번 | `cd C:\DEV\tdd-course\ship` → `pip install -r requirements.txt   (C:\DEV\tdd-course 에서 한 번)` |
| 이 폴더를 쓰는 교안 슬라이드 | `(교안) 실전-Coding Agent 실전 AI기반 TDD 마스터 과정_20261021_개정.pptx` — 214–224번 |

## 쓰는 법 (개정판)
- 각 항목은 **프롬프트 → 코드 → 실행 명령(기대 결과)** 순서로 모두 들어 있다. 코드는 직접 쓰는 테스트 · 소스이고, 프롬프트는 같은 일을 Gemini CLI 에 맡길 때 쓴다.
- 이 파일을 VS Code 에서 열어 두고(`Ctrl+Shift+V` 미리보기), 코드 블록을 복사해 Gemini CLI 에 붙여 넣는다. Gemini CLI 는 반드시 이 프로젝트 폴더에서 실행한다.
- `> ` 로 시작하는 줄은 터미널에서 실행하는 명령이고, 그 아래 줄은 실제로 실행해 얻은 결과다. AI 응답 문구와 코드 모양은 실행마다 다르다 — 판단 기준은 언제나 pytest 결과다.

### 슬라이드 214 — ① 요구사항 → 계약표(Contract) — 테스트를 쓰기 전에
<sub>Day 2 · 7교시  |  확인 실습 ①</sub>

**▶ 프롬프트 — 계약표 (읽기 전용 · 모든 코딩 에이전트 공통)**

```text
역할: 요구사항 분석가. 아래 요구사항 1~3 을 계약표로 바꿔줘. 파일은 수정하지 마.
열: 계약 ID(CT-n) | 규칙 | 사전조건(입력) | 사후조건(출력) | 오류
별도 표: 불변식(INV-n), 열린 질문(OQ-n). 새 규칙을 만들지 말고, 모호한 곳은 OQ 로만 적어줘.
(요구사항 1~3 붙여넣기)
```

**표 — 결과 예시**

| 계약 ID | 규칙 | 사전조건 (입력) | 사후조건 (출력) | 오류 |
|---|---|---|---|---|
| CT-1 | 기본 배송비 3,000원 | 0 < order_amount < 30,000 | 3,000 | — |
| CT-2 | 30,000원 이상 무료 | order_amount ≥ 30,000 | 0 | — |
| CT-3 | 0원 이하는 오류 | order_amount ≤ 0 | — | ValueError |
| INV-1 | 배송비는 항상 0 또는 3,000 | order_amount > 0 | fee ∈ {0, 3000} | — |
| OQ-1 | 소수 금액이면? (예: 29,999.5) | 미정 | 미정 | 사람이 결정 |

### 슬라이드 215 — ② 계약표 → 테스트 플랜 → 스켈레톤 코드
<sub>Day 2 · 7교시  |  확인 실습 ②</sub>

**▶ 프롬프트 — 테스트 플랜**

```text
@docs/계약표.md 의 계약마다 테스트 케이스(TC-n)를 표로 펼쳐줘.
열: TC | 계약 | 유형(일반·경계·오류) | 입력 | 기대 결과
경계값은 바로 아래 · 정확히 · 바로 위를 짝으로. 파일은 수정하지 마.
```

**▶ 프롬프트 — 스켈레톤 코드**

```text
@docs/테스트플랜.md 대로 tests/test_shipping.py 골격만 만들어줘.
함수마다 docstring 에 TC · CT 번호, 본문은 pytest.skip("TODO").
src/shipping.py 는 시그니처 + docstring + NotImplementedError 만.
```

**표 — 테스트 플랜 (일부)**

| TC | 계약 | 유형 | 입력 | 기대 |
|---|---|---|---|---|
| TC-01 | CT-1 | 일반 | 10,000 | 3,000 |
| TC-02 | CT-2 | 경계 | 29,999 | 3,000 |
| TC-03 | CT-2 | 경계 | 30,000 | 0 |
| TC-04·05 | CT-3 | 오류 | 0 · -1 | ValueError |

**실행 명령 · 결과 — 스켈레톤 → 실행**

```text
tests/test_shipping.py
def test_basic_fee_is_3000():
    """TC-01 · CT-1 · 기본 배송비 3,000원"""
    pytest.skip("TODO TC-01")

> pytest -q -rs
SKIPPED [1] tests\test_shipping.py:9: TODO TC-01
5 skipped in 0.01s
```

### 슬라이드 216 — ③ 골든 마스터 → ④ 전략 패턴 리팩터링 프롬프트
<sub>Day 2 · 7교시  |  확인 실습 ③</sub>

**▶ 프롬프트 — 골든 마스터 (리팩터링 전)**

```text
@src/shipping.py @tests/test_shipping.py @docs/계약표.md
shipping_fee() 의 '현재 동작'을 골든 마스터로 고정하는 테스트를 tests/test_golden_master.py 에 만들어줘.
- 등급 NORMAL · GOLD × 금액 -1, 0, 1, 10000, 19999, 20000, 29999, 30000, 30001, 100000 = 20개 조합
- 결과(정수) 또는 오류 종류(ValueError)를 tests/golden/shipping.golden.json 에 저장, UPDATE_GOLDEN=1 일 때만 갱신, 골든이 없으면 FAIL
- src/ 와 기존 테스트는 수정하지 마. 끝나면 !pytest -q 결과를 보여줘.
```

**▶ 프롬프트 — 전략 패턴 리팩터링 (동작 불변)**

```text
@src/shipping.py 모든 테스트(골든 마스터 포함)가 통과하는 상태야.
동작은 바꾸지 말고 등급별 배송비 규칙을 전략 패턴으로 리팩터링해줘.
- ShippingPolicy(ABC) 에 fee(order_amount) 추상 메서드, NormalPolicy · GoldPolicy 클래스
- POLICIES 딕셔너리로 등급 → 정책을 연결하고, shipping_fee() 는 검증 후 위임만
- 한 단계씩, 매번 !pytest -q. 테스트와 골든 파일은 수정하지 마.
- 끝나면 if grade 분기가 남았는지, 새 등급을 추가하려면 무엇을 바꾸는지 한 줄로 알려줘.
```

**실행 명령 · 결과 — 결과 예시**

```text
골든 마스터 생성 · 승인
> pytest -q
FAILED tests/test_golden_master.py   # 골든 없음
1 failed, 8 passed

> UPDATE_GOLDEN=1 pytest -q tests/test_golden_master.py
1 passed

> pytest -q
9 passed in 0.02s
```

**AI 응답 예시 (실행마다 다름) — Gemini CLI**

```text
전략 패턴 리팩터링 후
✦ ShippingPolicy · NormalPolicy · GoldPolicy 로 분리했다.
> pytest -q
9 passed in 0.02s   # 전 · 후 동일 · tests/ diff 없음
```

### 슬라이드 217 — ⑤ 추적성 매트릭스와 체크리스트 점검 프롬프트
<sub>Day 2 · 7교시  |  확인 실습 ④</sub>

**▶ 프롬프트 — 추적성 매트릭스**

```text
@docs/계약표.md @docs/테스트플랜.md @tests/ @src/ 로 docs/추적성매트릭스.md 를 만들어줘.
열: 요구 | 계약 | 테스트 케이스 | 테스트 함수 | 구현(함수·클래스) | 상태
- 테스트 함수 이름과 구현 위치는 실제 코드에서 찾아 적고, 찾지 못한 칸은 비우지 말고 ‘없음’으로 표시
- 요구 없이 존재하는 테스트나 코드가 있으면 표 아래에 따로 나열
- 만드는 파일은 docs/추적성매트릭스.md 하나뿐.
```

**▶ 프롬프트 — 체크리스트 점검 (읽기 전용)**

```text
@docs/확인체크리스트.md 의 11개 항목을 현재 저장소 상태로 점검해줘. 파일은 수정하지 마.
표: 항목 | 충족 / 미충족 | 증거(파일 · 실행 명령) | 부족한 것
- pytest -q 를 실행해 통과 수를 직접 확인하고, tests/ 가 바뀌었는지 git diff 로 확인해줘
- 미충족 항목은 ‘무엇을 하면 충족되는지’를 한 줄로 제안만 해줘 (직접 고치지 마).
```

**표 — 기대 산출물 — 추적성 매트릭스 (일부)**

| 요구 | 계약 | TC | 구현 |
|---|---|---|---|
| 요구 1 | CT-1 | TC-01 | NormalPolicy.fee |
| 요구 2 | CT-2 | TC-02·03 | NormalPolicy.fee |
| 요구 3 | CT-3 | TC-04·05 | shipping_fee |
| 요구 4 | CT-4·5 | TC-06~08 | GoldPolicy.fee |
| 요구 5 | INV | TC-09 | ShippingPolicy |

### 슬라이드 218 — 계약표 · 테스트 플랜 — 테스트 코드를 쓰기 전의 산출물
<sub>Day 2 · 7교시  |  강사용 모범 답안 ⓪</sub>

**표 — docs/계약표.md (요구 1~4 반영)**

| ID | 규칙 | 사전조건 (입력) | 사후조건 | 오류 |
|---|---|---|---|---|
| CT-1 | 기본 배송비 3,000원 | 0 < order_amount < 30,000 | 3,000 | — |
| CT-2 | 30,000원 이상 무료 | order_amount ≥ 30,000 | 0 | — |
| CT-3 | 0원 이하는 오류 | order_amount ≤ 0 | — | ValueError |
| CT-4 | GOLD 는 20,000원 이상 무료 | grade="GOLD" · order_amount ≥ 20,000 | 0 | — |
| CT-5 | grade 생략 = NORMAL (회귀) | grade 생략 | NORMAL 과 동일 | — |
| INV-1·2 | 배송비 ∈ {0, 3000} · 금액이 늘어도 배송비는 늘지 않는다 | order_amount > 0 | — | — |

**표 — docs/테스트플랜.md**

| TC | 계약 | 유형 | 입력 (금액 · 등급) | 기대 | 테스트 함수 |
|---|---|---|---|---|---|
| TC-01 | CT-1 | 일반 | 10,000 · NORMAL | 3,000 | test_basic_fee_is_3000 |
| TC-02 · 03 | CT-2 | 경계 짝 | 29,999 · 30,000 | 3,000 · 0 | test_free_shipping_boundary |
| TC-04 · 05 | CT-3 | 오류 | 0 · -1 | ValueError | test_non_positive_amount_raises |
| TC-06 · 07 | CT-4 | 경계 짝 | 19,999 · 20,000 · GOLD | 3,000 · 0 | test_gold_free_shipping_boundary |
| TC-08 | CT-5 | 회귀 | 20,000 · NORMAL | 3,000 | test_normal_member_keeps_30000_rule |
| TC-09 | INV | 골든 | 등급 2 × 금액 10 | 전후 동일 | test_golden_master |

### 슬라이드 219 — 모범 답안 — 요구 1~3 테스트와 GREEN
<sub>Day 2 · 7교시  |  강사용 모범 답안 ①</sub>

**▶ 프롬프트 — 테스트를 AI 에게 맡길 때 (직접 쓰기 어려우면)**

```text
@docs/테스트플랜.md @tests/test_shipping.py @src/shipping.py
스켈레톤의 TC-01~05 에서 pytest.skip 을 지우고 본문을 채워줘. 경계(TC-02 · 03)와 오류(TC-04 · 05)는 @pytest.mark.parametrize 로.
src/ 는 수정하지 마. 구현은 하지 마. 끝나면 !pytest -q --tb=short 로 실패 이유(NotImplementedError)를 보여줘.
```

**코드 — ① 직접 작성(또는 위 프롬프트로) — tests/test_shipping.py**

```python
import pytest
from shipping import shipping_fee

def test_basic_fee_is_3000():
    assert shipping_fee(10000) == 3000

@pytest.mark.parametrize("amount, expected", [
    (29999, 3000),   # 기준 바로 아래
    (30000, 0),      # 기준 정확히: 무료
])
def test_free_shipping_boundary(amount, expected):
    assert shipping_fee(amount) == expected

@pytest.mark.parametrize("amount", [0, -1])
def test_non_positive_amount_raises(amount):
    with pytest.raises(ValueError):
        shipping_fee(amount)
```

**실행 명령 · 결과 — ② 구현 후 실행 → GREEN · 터미널**

```text
> pytest -q --tb=short
.....  [100%]
5 passed in 0.02s
```

### 슬라이드 220 — 요구 4 (GOLD) 테스트를 AI 에게 맡길 때 — 프롬프트 · 결과 · 실행
<sub>Day 2 · 7교시  |  강사용 모범 답안 ②</sub>

**▶ 프롬프트 — Gemini CLI**

```text
@docs/계약표.md @docs/테스트플랜.md @tests/test_shipping.py @src/shipping.py
요구 4(GOLD)의 TC-06 ~ 08 을 tests/test_shipping.py 에 추가해줘.
- TC-06 · 07 : test_gold_free_shipping_boundary — grade="GOLD" 로 19,999 → 3,000 · 20,000 → 0 (@pytest.mark.parametrize)
- TC-08 : test_normal_member_keeps_30000_rule — 일반 회원 20,000원은 3,000원 (회귀)
기존 테스트 5개와 src/ 는 수정하지 마. 구현은 하지 마. 끝나면 !pytest -q --tb=short 로 실패 이유를 보여줘.
```

**AI 응답 예시 (실행마다 다름) — 결과 예시**

```text
결과 예시 — Gemini CLI
✦ 요구 4 의 테스트 3개를 추가했다. 기존 5개는 그대로다.
  Edit tests/test_shipping.py
+ @pytest.mark.parametrize("amount, expected", [
+     (19999, 3000),   # TC-06
+     (20000, 0),      # TC-07
+ ])
+ def test_gold_free_shipping_boundary(amount, expected):
+     assert shipping_fee(amount, grade="GOLD") == expected
+ def test_normal_member_keeps_30000_rule():   # TC-08
+     assert shipping_fee(20000, grade="NORMAL") == 3000
✦ 3 failed, 5 passed — shipping_fee 에 grade 인자가 아직 없다.
```

**실행 명령 · 결과 — ② 실행 → RED 확인 · 터미널**

```text
> pytest -q --tb=short
.....FFF  [100%]
E   TypeError: shipping_fee() got an unexpected keyword
    argument 'grade'              # 3개 모두 같은 이유
FAILED …test_gold_free_shipping_boundary[19999-3000]
FAILED …test_gold_free_shipping_boundary[20000-0]
FAILED …test_normal_member_keeps_30000_rule
3 failed, 5 passed in 0.12s
```

### 슬라이드 221 — 요구 4 (GOLD) — 기존 테스트가 회귀를 지켜 본다
<sub>Day 2 · 7교시  |  강사용 모범 답안 ②</sub>

**코드 — 추가 테스트 (요구 4) — TC-06 ~ 08**

```python
tests/test_shipping.py
@pytest.mark.parametrize("amount, expected", [
    (19999, 3000),   # TC-06
    (20000, 0),      # TC-07
])
def test_gold_free_shipping_boundary(amount, expected):
    assert shipping_fee(amount, grade="GOLD") == expected

def test_normal_member_keeps_30000_rule():   # TC-08
    assert shipping_fee(20000, grade="NORMAL") == 3000
```

**실행 명령 · 결과 — RED — 기존 5개는 통과 · 새 3개 실패 (이유: grade 인자가 없다) · 터미널**

```text
> pytest -q --tb=short
.....FFF  [100%]
E   TypeError: shipping_fee() got an unexpected keyword
    argument 'grade'              # 3개 모두 같은 이유
FAILED …test_gold_free_shipping_boundary[19999-3000]
FAILED …test_gold_free_shipping_boundary[20000-0]
FAILED …test_normal_member_keeps_30000_rule
3 failed, 5 passed in 0.12s
```

**코드 — GREEN — 요구 4 구현 (리팩터링 전)**

```python
src/shipping.py
BASE_FEE = 3000
def shipping_fee(order_amount, grade="NORMAL"):
    if order_amount <= 0:
        raise ValueError("주문 금액은 0보다 커야 합니다")
    if grade == "GOLD":
        if order_amount >= 20000:
            return 0
    elif order_amount >= 30000:
        return 0
    return BASE_FEE
```

**실행 명령 · 결과 — 최종 GREEN · 터미널**

```text
> pytest -q --tb=short
........  [100%]
8 passed in 0.02s
```

### 슬라이드 222 — 요구 5 준비 — 리팩터링 전에 골든 마스터를 만든다
<sub>Day 2 · 7교시  |  강사용 모범 답안 ③</sub>

**코드 — tests/test_golden_master.py — 등급 2 × 금액 10 = 20개 조합**

```python
tests/test_golden_master.py (발췌)
GRADES = ["NORMAL", "GOLD"]
AMOUNTS = [-1, 0, 1, 10000, 19999, 20000,
           29999, 30000, 30001, 100000]

def capture(amount, grade):
    try:
        return {"fee": shipping_fee(amount, grade=grade)}
    except ValueError:
        return {"error": "ValueError"}

def test_golden_master():            # TC-09
    actual = {f"{g}/{a}": capture(a, g)
              for g in GRADES for a in AMOUNTS}
    # UPDATE_GOLDEN=1 일 때만 골든 파일 갱신 (발췌)
    expected = json.loads(GOLDEN.read_text())
    assert actual == expected
```

**실행 명령 · 결과 — 리팩터링 전에 생성 · 승인 · 터미널**

```text
> pytest -q
FAILED tests/test_golden_master.py   # 골든 없음
1 failed, 8 passed

> UPDATE_GOLDEN=1 pytest -q tests/test_golden_master.py
1 passed

> pytest -q
9 passed in 0.02s
```

### 슬라이드 223 — 요구 5 — if grade 분기를 전략(Strategy)으로 리팩터링
<sub>Day 2 · 7교시  |  강사용 모범 답안 ④</sub>

**코드 — ✗ Before — 등급이 늘수록 분기가 늘어난다**

```python
src/shipping.py (요구 4 GREEN)
BASE_FEE = 3000

def shipping_fee(order_amount, grade="NORMAL"):
    if order_amount <= 0:
        raise ValueError("주문 금액은 0보다 커야 합니다")
    if grade == "GOLD":
        if order_amount >= 20000:
            return 0
    elif order_amount >= 30000:
        return 0
    return BASE_FEE
결과
```

**코드 — ✓ After — 등급 = 전략 클래스, 함수는 위임만**

```python
src/shipping.py (전략 패턴 · import 생략)
BASE_FEE = 3000

class ShippingPolicy(ABC):          # Strategy
    @abstractmethod
    def fee(self, order_amount): ...

class NormalPolicy(ShippingPolicy):
    def fee(self, order_amount):
        return 0 if order_amount >= 30000 else BASE_FEE

class GoldPolicy(ShippingPolicy):
    def fee(self, order_amount):
        return 0 if order_amount >= 20000 else BASE_FEE

POLICIES = {"NORMAL": NormalPolicy(),
            "GOLD": GoldPolicy()}

def shipping_fee(order_amount, grade="NORMAL"):
    if order_amount <= 0:
        raise ValueError("주문 금액은 0보다 커야 합니다")
    return POLICIES[grade].fee(order_amount)
```

**실행 명령 · 결과 — 결과**

```text
> pytest -q   # 전 · 후 동일
9 passed in 0.02s
새 등급 SILVER → 클래스 + 등록 한 줄
shipping_fee() 수정 0줄
```

### 슬라이드 224 — 추적성 매트릭스 — 요구 ↔ 계약 ↔ 테스트 ↔ 코드, 빈 칸이 없어야 한다
<sub>Day 2 · 7교시  |  강사용 모범 답안 ⑤</sub>

**표 — 문서 내용**

| 요구 | 계약 | 테스트 케이스 | 테스트 함수 | 구현 (src/shipping.py) | 상태 |
|---|---|---|---|---|---|
| 요구 1 기본 3,000원 | CT-1 | TC-01 | test_basic_fee_is_3000 | BASE_FEE · NormalPolicy.fee | GREEN |
| 요구 2 30,000원 이상 무료 | CT-2 | TC-02 · 03 | test_free_shipping_boundary | NormalPolicy.fee | GREEN |
| 요구 3 0원 이하 오류 | CT-3 | TC-04 · 05 | test_non_positive_amount_raises | shipping_fee (ValueError) | GREEN |
| 요구 4 GOLD 20,000원 이상 무료 | CT-4 · 5 | TC-06 · 07 · 08 | test_gold_free_shipping_boundary · test_normal_member_keeps_30000_rule | GoldPolicy.fee · POLICIES | GREEN |
| 요구 5 전략 패턴 리팩터링 | INV-1 · 2 | TC-09 | test_golden_master | ShippingPolicy · NormalPolicy · GoldPolicy | GREEN |
