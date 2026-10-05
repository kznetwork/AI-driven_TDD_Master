# 실습 프롬프트 — cart-a
실험 A — 테스트 없이 AI에게 맡기기 (Day 1 09:00)  
교안: `AI_TDD_2일과정_교안_v5.pptx`

## 쓰는 법
- 이 파일을 VS Code 에서 열어 두고(`Ctrl+Shift+V` 미리보기), 코드 블록을 복사해 Gemini CLI 에 붙여 넣습니다.
- **Gemini CLI 는 반드시 이 프로젝트 폴더에서 실행**합니다. `@파일`, `!명령` 이 이 폴더를 기준으로 동작합니다.
- `@경로` 는 파일을 대화에 넣고, `!명령` 은 셸 명령을 실행해 결과를 보여 줍니다.
- 'plan 모드' 표시는 수정 없이 계획 · 검토만 받는 단계입니다 (교안 안내대로 plan 모드로 전환하거나, 프롬프트의 '수정하지 마' 로 대신합니다).
- '일부러 나쁜 예' 는 실패를 체험하는 단계입니다. 실행 후 강사 안내에 따라 변경을 되돌립니다.
- 기대 결과는 요약입니다. **AI 응답 문구와 코드 모양은 실행마다 다릅니다.** 판단 기준은 언제나 `pytest` 결과입니다.

## Day 1 · 1.2

### 실험 A-1 · 합계
<sub>슬라이드 14</sub>

```text
cart.py 에 장바구니 합계를 계산하는 total(items) 함수를 만들어줘. items 는 {"price": 가격, "qty": 수량} 딕셔너리의 리스트야.
```

> python -c "from cart import total; print(total([{'price': 12000, 'qty': 3}, {'price': 24000, 'qty': 1}]))"

**확인** 결과를 직접 실행해 보고 기록표에 적으세요. 

### 실험 A-2 · 5만 원 이상 10% 할인
<sub>슬라이드 15</sub>

```text
합계가 50,000원 이상이면 10% 할인해줘.
```

> python -c "from cart import total; print(total([{'price': 12000, 'qty': 3}, {'price': 24000, 'qty': 1}]))"

**확인** 결과를 직접 실행해 보고 기록표에 적으세요. 

### 실험 A-3 · VIP 5% 추가 할인
<sub>슬라이드 16</sub>

```text
VIP 고객은 할인된 금액에서 5%를 추가로 할인해줘. total 에 is_vip 인자를 추가해.
```

> python -c "from cart import total; print(total([{'price': 12000, 'qty': 3}, {'price': 24000, 'qty': 1}], is_vip=True))"

**확인** 결과를 직접 실행해 보고 기록표에 적으세요. 

### 실험 A-4 · 정리 요청
<sub>슬라이드 17</sub>

```text
코드가 좀 지저분하네. 할인율을 상수로 빼고 깔끔하게 정리해줘. 금액은 정수로 나오게 해줘.
```
> python -c "from cart import total; print(total([{'price': 12000, 'qty': 3}, {'price': 24000, 'qty': 1}], is_vip=True))"

**확인** 결과를 직접 실행해 보고 기록표에 적으세요. 

### 추가 실험 : 경계값 50,000원을 직접 넣어서 기존 기능이 유지되는지 확인
<sub>슬라이드 18</sub>

> python -c "from cart import total; print(total([{'price':25000,'qty':2}]))"

현재 코드를 기준으로 독립적으로 연습할 수 있는 과제 5개입니다. 각 과제를 구현한 뒤 프로젝트 폴더에서 한 줄 명령으로 결과를 확인하세요.

### 실험 A-5 · 빈 장바구니 처리
<sub>슬라이드 20</sub>

빈 장바구니의 합계는 `0`이 되도록 하세요.

```
python -c "from cart import total; print(total([]))"  
# 예상: 0
```

### 실험 A-6 · 할인 경계값 확인
<sub>슬라이드 20</sub>

49,999원에는 할인이 적용되지 않고, 50,000원부터 적용되는지 확인하세요.

```
python -c "from cart import total; print(total([{'price':49999,'qty':1}])); print(total([{'price':50000,'qty':1}]))"  
# 예상: 49999, 45000
```

### 실험 A-7 · 정액 쿠폰 추가
<sub>슬라이드 21</sub>


`coupon` 인자를 추가하고, 모든 할인 적용 후 쿠폰 금액을 차감하세요. 최종 금액은 0원 미만이 되면 안 됩니다.

```
python -c "from cart import total; print(total([{'price':50000,'qty':1}], coupon=5000)); print(total([{'price':1000,'qty':1}], coupon=5000))"  
# 예상: 40000, 0
```

### 실험 A-8 · 잘못된 상품 검증
<sub>슬라이드 21</sub>

가격이 음수이거나 수량이 1보다 작으면 `ValueError`가 발생하도록 하세요.

```
python -c "from cart import total; total([{'price':-1000,'qty':1}])"  
# 예상: ValueError
```

### 실험 A-9 · 할인 내역 제공
<sub>슬라이드 22</sub>

최종 금액뿐 아니라 원래 합계와 할인 금액도 확인할 수 있는 `summary(items, is_vip=False)` 함수를 만들어 보세요. 반환 형식은 딕셔너리로 합니다.

```
python -c "from cart import summary; print(summary([{'price':50000,'qty':1}], True))"  
# 예상: {'subtotal': 50000, 'discount': 7250, 'total': 42750}
```
