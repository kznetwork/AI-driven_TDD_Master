# 실습 프롬프트 — cart-a
실험 A — 테스트 없이 AI에게 맡기기 (Day 1 09:00)  
교안: `(교안) 실전-Coding Agent 실전 AI기반 TDD 마스터 과정_20261021_개정.pptx`

## 어디에서 실습하나 (작업 폴더)

| 항목 | 내용 |
|---|---|
| 작업 폴더 | `C:\DEV\tdd-course\cart-a` |
| 만드는 법 | 강사가 나눠 준 `starter\cart-a` 폴더를 `C:\DEV\tdd-course\` 아래로 **폴더째 복사**한다 (폴더를 새로 만들 필요는 없다) |
| 여는 법 | VS Code → 파일 → 폴더 열기 → `C:\DEV\tdd-course\cart-a` · 터미널과 코딩 에이전트도 **이 폴더에서** 실행한다 |
| 이 폴더의 특징 | 코드 파일이 없다 — 코딩 에이전트가 `cart.py` 를 만든다 (실험 A: 테스트 파일은 만들지 않는다) |
| 이 폴더를 쓰는 교안 슬라이드 | `(교안) 실전-Coding Agent 실전 AI기반 TDD 마스터 과정_20261021_개정.pptx` — 14–18, 20–23번 |

## 쓰는 법 (개정판)
- 각 항목은 **프롬프트 → 코드 → 실행 명령(기대 결과)** 순서로 모두 들어 있다. 코드는 직접 쓰는 테스트 · 소스이고, 프롬프트는 같은 일을 Gemini CLI 에 맡길 때 쓴다.
- 이 파일을 VS Code 에서 열어 두고(`Ctrl+Shift+V` 미리보기), 코드 블록을 복사해 Gemini CLI 에 붙여 넣는다. Gemini CLI 는 반드시 이 프로젝트 폴더에서 실행한다.
- `> ` 로 시작하는 줄은 터미널에서 실행하는 명령이고, 그 아래 줄은 실제로 실행해 얻은 결과다. AI 응답 문구와 코드 모양은 실행마다 다르다 — 판단 기준은 언제나 pytest 결과다.

### 슬라이드 14 — A-1 · 합계 — 결과는 그럴듯하다
<sub>Day 1 · 1교시  |  실험 A · A-1</sub>

**▶ 프롬프트 — Gemini CLI**

```text
cart.py 에 장바구니 합계를 계산하는 total(items) 함수를 만들어줘. items 는 {"price": 가격, "qty": 수량} 딕셔너리의 리스트야.
```

**AI 응답 예시 (실행마다 다름) — 결과 예시 · Gemini CLI — cart-a/cart.py**

```text
✦ cart.py에 total 함수를 만들었다.
+ def total(items):
+     return sum(item["price"] * item["qty"] for item in items)
```

**실행 명령 · 결과 — 눈으로 확인 (python 한 줄 실행) · 터미널**

```text
> python -c "from cart import total; print(total([{'price': 12000, 'qty': 3}, {'price': 24000, 'qty': 1}]))"

60000
```

### 슬라이드 15 — A-2 · 5만 원 이상 10% 할인 — 숫자 모양이 바뀌었다
<sub>Day 1 · 1교시  |  실험 A · A-2</sub>

**▶ 프롬프트 — Gemini CLI**

```text
합계가 50,000원 이상이면 10% 할인해줘.
```

**AI 응답 예시 (실행마다 다름) — 결과 예시 · Gemini CLI — cart-a/cart.py**

```text
✦ total 함수에 할인 조건을 추가했다.
+ def total(items):
+     amount = sum(item["price"] * item["qty"] for item in items)
+     if amount >= 50000:
+         amount = amount * 0.9
+     return amount
```

**실행 명령 · 결과 — 눈으로 확인 (python 한 줄 실행) · 터미널**

```text
> python -c "from cart import total; print(total([{'price': 12000, 'qty': 3}, {'price': 24000, 'qty': 1}]))"

54000.0
```

### 슬라이드 16 — A-3 · VIP 5% 추가 할인 — 이번에도 그럴듯하다
<sub>Day 1 · 1교시  |  실험 A · A-3</sub>

**▶ 프롬프트 — Gemini CLI**

```text
VIP 고객은 할인된 금액에서 5%를 추가로 할인해줘. total 에 is_vip 인자를 추가해.
```

**AI 응답 예시 (실행마다 다름) — 결과 예시 · Gemini CLI — cart-a/cart.py**

```text
✦ is_vip 매개변수를 추가했다.
+ def total(items, is_vip=False):
+     amount = sum(item["price"] * item["qty"] for item in items)
+     if amount >= 50000:
+         amount = amount * 0.9
+     if is_vip:
+         amount = amount * 0.95
+     return amount
```

**실행 명령 · 결과 — 눈으로 확인 (python 한 줄 실행) · 터미널**

```text
> python -c "from cart import total; print(total([{'price': 12000, 'qty': 3}, {'price': 24000, 'qty': 1}], is_vip=True))"

51300.0
```

### 슬라이드 17 — A-4 · 코드 정리 — 겉보기엔 더 깔끔해졌다
<sub>Day 1 · 1교시  |  실험 A · A-4</sub>

**▶ 프롬프트 — Gemini CLI**

```text
코드가 좀 지저분하네. 할인율을 상수로 빼고 50000원 이하는 할인 안 되게 해. 깔끔하게 정리해줘. 금액은 정수로 나오게 해줘.
```

**AI 응답 예시 (실행마다 다름) — 결과 예시 · Gemini CLI — cart-a/cart.py**

```text
✦ 상수를 분리하고 정리했다. 결과는 반올림한 정수이다.
+ THRESHOLD = 50000
+ THRESHOLD_RATE = 0.9
+ VIP_RATE = 0.95
+
+
+ def total(items, is_vip=False):
+     amount = sum(i["price"] * i["qty"] for i in items)
+     if amount > THRESHOLD:          # '50000원 이하는 할인 안 됨' → >
+         amount *= THRESHOLD_RATE
+     if is_vip:
+         amount *= VIP_RATE
+     return round(amount)
```

**코드 — 눈으로 확인 (python 한 줄 실행) · 터미널**

```python
>
python -c "from cart import total; print(total([{'price': 12000, 'qty': 3}, {'price': 24000, 'qty': 1}], is_vip=True))"

51300
```

### 슬라이드 18 — 정말 괜찮을까? — 정확히 50,000원을 넣어 보면
<sub>Day 1 · 1교시  |  실험 A · 반전</sub>

**코드 — A-2 때의 코드 예시**

```python
    if amount >= 50000:          # 이상
```

**코드 — A-4 '정리' 후의 코드 예시**

```python
    if amount > THRESHOLD:       # 초과
```

**실행 명령 · 결과 — 터미널**

```text
> python -c "from cart import total; print(total([{'price':25000,'qty':2}]))"
50000            # 기대값 45000 — 5만 원 손님이 할인을 못 받는 경우가 생길 수 있다.
```

### 슬라이드 20 — A-5. 빈 장바구니 처리
<sub>Day 1 · 2교시  |  실험 A · 복습</sub>

**▶ 프롬프트 — Gemini CLI**

```text
빈 장바구니의 합계는 `0`이 되도록 하세요.
```

**▶ 프롬프트 — Gemini CLI**

```text
49,999원에는 할인이 적용되지 않고, 50,000원부터 적용되는지 확인하세요.
```

**코드 — 눈으로 확인 (python 한 줄 실행) · 터미널**

```python
>
python -c "from cart import total; print(total([]))"  # 예상: 0
```

**코드 — 눈으로 확인 (python 한 줄 실행) · 터미널**

```python
>
python -c "from cart import total; print(total([{'price':49999,'qty':1}])); print(total([{'price':50000,'qty':1}]))"  # 예상: 49999, 45000
```

### 슬라이드 21 — A-7. 정액 쿠폰 추가
<sub>Day 1 · 2교시  |  실험 A · 복습</sub>

**▶ 프롬프트 — Gemini CLI**

```text
`coupon` 인자를 추가하고, 모든 할인 적용 후 쿠폰 금액을 차감하세요. 최종 금액은 0원 미만이 되면 안 된다.
```

**▶ 프롬프트 — Gemini CLI**

```text
가격이 음수이거나 수량이 1보다 작으면 `ValueError`가 발생하도록 하세요.
```

**코드 — 눈으로 확인 (python 한 줄 실행) · 터미널**

```python
>
python -c "from cart import total; print(total([{'price':50000,'qty':1}], coupon=5000)); print(total([{'price':1000,'qty':1}], coupon=5000))"  # 예상: 40000, 0
```

**코드 — 눈으로 확인 (python 한 줄 실행) · 터미널**

```python
>
python -c "from cart import total; total([{'price':-1000,'qty':1}])"  # 예상: ValueError
```

### 슬라이드 22 — A-9. 할인 내역 제공
<sub>Day 1 · 2교시  |  실험 A · 복습</sub>

**▶ 프롬프트 — Gemini CLI**

```text
최종 금액뿐 아니라 원래 합계와 할인 금액도 확인할 수 있는 `summary(items, is_vip=False)` 함수를 만들어 보세요. 반환 형식은 딕셔너리로 한다.
```

**코드 — 눈으로 확인 (python 한 줄 실행) · 터미널**

```python
>
python -c "from cart import summary; print(summary([{'price':50000,'qty':1}], True))"  # 예상: {'subtotal': 50000, 'discount': 7250, 'total': 42750}
```

### 슬라이드 23 — Python 테스트 기초 — 눈으로 하던 확인을 파일로 남긴다
<sub>Day 1 · 2교시  |  테스트 기초</sub>

**실행 명령 · 결과 — 지금까지 — 터미널에서 눈으로**

```text
> python -c "from cart import total;
  print(total([{'price':10000,'qty':2}]))"
20000
```

**실행 명령 · 결과 — 실행 — 저장해 둔 확인을 한 번에**

```text
> pytest -q
..  [100%]
2 passed in 0.00s
```

**코드 — pytest.ini — cart-a/pytest.ini 에 저장**

```ini
[pytest]
pythonpath = .
testpaths = tests
```

**코드 — 앞으로 — cart-a/tests/test_cart.py 에 저장**

```python
from cart import total

def test_empty_cart_is_zero():
    assert total([]) == 0

def test_total_below_threshold():
    items = [{"price": 10000, "qty": 2}]
    assert total(items) == 20000
```
