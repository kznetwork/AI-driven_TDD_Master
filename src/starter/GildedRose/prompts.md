# 실습 프롬프트 — GildedRose
교안: `(교안) 실전-Coding Agent 실전 AI기반 TDD 마스터 과정_20261021_개정.pptx`

## 어디에서 실습하나 (작업 폴더)

| 항목 | 내용 |
|---|---|
| 작업 폴더 | `C:\DEV\tdd-course\GildedRose` |
| 만드는 법 | 강사가 나눠 준 `starter\GildedRose` 폴더를 `C:\DEV\tdd-course\` 아래로 **폴더째 복사**한다 |
| 처음 한 번 | `cd C:\DEV\tdd-course\GildedRose` → `python -m venv .venv` → `pip install -r requirements.txt` |
| 막히면 | `checkpoints\A.3_테스트케이스완료\GildedRose` · `A.5_골든마스터완료` · `A.6_Conjured완료` 중 막힌 단계의 폴더를 복사해 이어서 한다 |

## 쓰는 법 (개정판)
- 각 항목은 **프롬프트 → 코드 → 실행 명령(기대 결과)** 순서로 모두 들어 있다. 코드는 직접 쓰는 테스트 · 소스이고, 프롬프트는 같은 일을 Gemini CLI 에 맡길 때 쓴다.
- 이 파일을 VS Code 에서 열어 두고(`Ctrl+Shift+V` 미리보기), 코드 블록을 복사해 Gemini CLI 에 붙여 넣는다. Gemini CLI 는 반드시 이 프로젝트 폴더에서 실행한다.
- `> ` 로 시작하는 줄은 터미널에서 실행하는 명령이고, 그 아래 줄은 실제로 실행해 얻은 결과다. AI 응답 문구와 코드 모양은 실행마다 다르다 — 판단 기준은 언제나 pytest 결과다.

### 슬라이드 232 — 요구사항 분석 프롬프트 — 문서에서 규칙표 뽑기
<sub>부록 A · A.1  |  프롬프트</sub>

**▶ 프롬프트 — 요구사항 분석 (docs/규칙표.md 저장)**

```text
[역할] 레거시 코드 QA 분석가
[입력] @GildedRoseRequirements.txt @README.md  (코드는 보지 마)
[작업] 아이템 종류별(일반 · Aged Brie · Sulfuras · Backstage · Conjured) 규칙을 표로 정리해줘.
  열: 아이템 | 규칙 ID(R-n) | 규칙 | 경계 조건 | 출처(문서 위치)
  모호하거나 서로 충돌하는 곳은 표 아래 ‘열린 질문(OQ-n)’으로만 적어줘.
[제약] 코드 파일은 만들거나 고치지 마. 요구사항에 없는 규칙을 만들지 마.
[출력] 마크다운 표 2개(규칙표, OQ 표)를 docs/규칙표.md 로 저장해줘. 다른 파일은 만들지 마.
```

**실행 명령 · 결과 — 터미널**

```text
저장 확인 · 커밋 (GildedRose/ 폴더)
> dir docs        # macOS/Linux: ls docs
규칙표.md
> git add docs && git commit -m "docs: 규칙표 R-1~R-8 · OQ-1~2"
```

### 슬라이드 233 — 레거시 코드 이해와 문제점 파악
<sub>부록 A · A.2</sub>

**코드 — item.py — Item 클래스 (수정 금지 구역)**

```python
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in   # 판매까지 남은 일수
        self.quality = quality   # 품질 (0~50)
```

### 슬라이드 234 — 레거시 update_quality() — ① 판매일 전 갱신
<sub>부록 A · A.2</sub>

**코드 — gilded_rose.py — 레거시 원본**

```python
class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != 'Aged Brie' and \
               item.name != 'Backstage passes to a TAFKAL80ETC concert':
                if item.quality > 0:
                    if item.name != 'Sulfuras, Hand of Ragnaros':
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == 'Backstage passes to a TAFKAL80ETC concert':
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
```

### 슬라이드 235 — 레거시 update_quality() — ② sellIn 감소와 판매일 후 처리
<sub>부록 A · A.2</sub>

**코드 — gilded_rose.py — 이어서 (for 루프 안)**

```python
            if item.name != 'Sulfuras, Hand of Ragnaros':
                item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                if item.name != 'Aged Brie':
                    if item.name != 'Backstage passes to a TAFKAL80ETC concert':
                        if item.quality > 0:
                            if item.name != 'Sulfuras, Hand of Ragnaros':
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality  # 0
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
```

### 슬라이드 236 — 레거시 코드 읽기 프롬프트 — 분기 지도와 위험 지점
<sub>부록 A · A.2  |  프롬프트</sub>

**▶ 프롬프트 — 코드 읽기 (docs/분기지도.md 저장)**

```text
[역할] 레거시 코드 리뷰어
@gilded_rose.py @docs/규칙표.md 로 update_quality() 를 읽고, 코드 수정 없이 아래를 만들어줘.
1) 분기 지도: 조건 | 하는 일 | 대응하는 규칙(R-n)
2) 규칙표에 대응하지 않는 분기는 ‘의도 불명’으로 표시
3) 위험 지점 5개 이내: 위치 · 이유 · 리팩터링 전에 필요한 테스트
[제약] 코드와 Item 클래스는 수정 금지. 추측은 ‘추정’이라고 적어줘.
[출력] 표 3개를 docs/분기지도.md 로 저장해줘. 다른 파일은 만들지 마.
```

**실행 명령 · 결과 — 터미널**

```text
저장 확인 · 코드가 그대로인지 확인
> python -m pytest -q          # 1 failed (test_foo) — 코드는 바뀌지 않았다
> git add docs && git commit -m "docs: 분기 지도 · 위험 지점"
```

### 슬라이드 239 — 테스트 케이스 설계 프롬프트 — 경계값을 표로 먼저
<sub>부록 A · A.3  |  프롬프트</sub>

**▶ 프롬프트 — 테스트 케이스 설계 (docs/테스트케이스.md 저장)**

```text
[역할] 테스트 설계자
[입력] @docs/규칙표.md @docs/분기지도.md @gilded_rose.py
[작업] 규칙마다 테스트 케이스를 표로 설계해줘.
  열: TC | 규칙 | 유형(일반·경계·불변) | 입력(name, sell_in, quality) | 기대 quality | 우선순위(★)
  경계는 바로 아래 · 정확히 · 바로 위를 짝으로 (Backstage 11/10 · 6/5 · 1/0, quality 0/49/50)
[제약] 기대값은 규칙표(요구사항)에서만 가져와. 현재 코드의 출력을 베끼지 마. 어긋나면 OQ 로. Conjured(R-8)는 ‘미구현’으로 표시.
[출력] 표 1개 + ★★★ 케이스 목록을 docs/테스트케이스.md 로 저장해줘.
```

**실행 명령 · 결과 — 터미널**

```text
저장 확인 · 커밋
> dir docs                     # 규칙표.md · 분기지도.md · 테스트케이스.md
> git add docs && git commit -m "docs: 테스트 케이스 TC-01~13"
```

### 슬라이드 240 — 특성화 케이스 프롬프트 — 명세에 없는 ‘지금 동작’을 기록한다
<sub>부록 A · A.3  |  프롬프트</sub>

**▶ 프롬프트 — 특성화 케이스 (docs/특성화.md 저장)**

```text
[역할] 레거시 코드 특성화 분석가
[입력] @docs/테스트케이스.md @gilded_rose.py @item.py
[작업] 1) 테스트 케이스 표의 입력을 현재 코드에 그대로 넣어 실제 출력을 구하고, 명세 기대값과 비교해 일치 · 불일치를 표로 정리해줘.
     (코드는 python -c 로 실행만 한다. 파일은 만들지 마.)
   2) 명세에 없는 입력(quality 50 초과 · 음수, 다른 이름의 아이템, Sulfuras quality 80 아님 등)을 6개 이내로 골라 현재 출력을 기록해줘 — 이것이 특성화 케이스(CH-n)다.
[제약] 기대값을 현재 코드에 맞춰 고치지 마. 불일치는 OQ 로 남겨. gilded_rose.py · item.py 는 수정 금지.
[출력] 표 2개 + 사람이 결정할 것을 docs/특성화.md 로 저장해줘. 다른 파일은 만들지 마.
```

**실행 명령 · 결과 — 터미널**

```text
실행 명령 — 현재 동작을 실제로 돌려 본다
> python -c "from gilded_rose import GildedRose; from item import Item; i = Item('Normal Item', 5, 60); GildedRose([i]).update_quality(); print(i)"
Normal Item, 4, 59        # 현재 동작 그대로 기록 → CH-1
> git add docs/특성화.md && git commit -m "docs: 특성화 CH-1~6 (현재 동작 기록)"
```

### 슬라이드 241 — 테스트 코드 작성 프롬프트 — 표를 pytest 로
<sub>부록 A · A.3  |  프롬프트</sub>

**▶ 프롬프트 — 테스트 코드 작성 (명세 + 특성화)**

```text
@docs/테스트케이스.md @docs/특성화.md @gilded_rose.py @item.py
1) 테스트케이스.md 의 ★★★ 케이스(TC-01~06)를 tests/test_gilded_rose.py 에 pytest 로 작성해줘 (명세 테스트).
   - 규칙마다 함수 1개, 같은 규칙의 경계는 @pytest.mark.parametrize 로, 주석에 TC · R 번호
2) 특성화.md 의 CH-1~6 을 tests/test_characterization.py 에 작성해줘 (특성화 테스트). 기대값은 문서의 ‘출력’ 그대로.
- Item 클래스와 gilded_rose.py 는 수정하지 마. Conjured(TC-11~13)는 쓰지 마 (A.6 에서 RED 부터).
- 끝나면 !pytest -q 결과를 보여줘. 레거시에서 통과해야 정상 — 실패하면 기대값과 OQ 부터 의심해줘.
```

**실행 명령 · 결과 — 기대 결과**

```text
tests/test_gilded_rose.py
# tests/test_gilded_rose.py  (명세 12개 — TC-01~06)
# tests/test_characterization.py  (특성화 6개 — CH-1~6)
> pytest -q
..................  [100%]
18 passed in 0.03s     # 레거시에서 이미 통과 (12 + 6)
```

**실행 명령 · 결과 — 터미널**

```text
실행 명령 · 커밋
> python -m pytest -q tests/test_gilded_rose.py        # 12 passed (명세)
> python -m pytest -q tests/test_characterization.py   # 6 passed (특성화)
> python -m pytest -q                                 # 18 passed
> git add tests && git commit -m "test: 명세 12 + 특성화 6"
```

### 슬라이드 242 — 경계값 테스트 코드 (pytest)
<sub>부록 A · A.3</sub>

**코드 — tests/test_gilded_rose.py — 명세 테스트 (프롬프트: 앞 장 241)**

```python
# TC-01 · R-3 경계값: quality는 0 미만이 되지 않는다
def test_quality_never_negative():
    items = [Item('Normal Item', 5, 0)]
    GildedRose(items).update_quality()
    assert items[0].quality == 0

# TC-03 · R-5 경계값: quality는 50을 넘지 않는다
def test_aged_brie_quality_max_50():
    items = [Item('Aged Brie', 5, 50)]
    GildedRose(items).update_quality()
    assert items[0].quality == 50

# TC-02 · R-2 경계값: 판매일이 지나면 2배 감소
def test_normal_item_degrades_twice_after_sell_date():
    items = [Item('Normal Item', 0, 10)]
    GildedRose(items).update_quality()
    assert items[0].quality == 8   # 10 - 2
실행 명령
```

**실행 명령 · 결과 — 실행 명령**

```text
> python -m pytest -q tests/test_gilded_rose.py
12 passed in 0.02s     # 이 장 + 다음 장의 테스트 합계 — 레거시에서 이미 통과 (특성화)
```

### 슬라이드 243 — Backstage 경계값 — pytest.mark.parametrize
<sub>부록 A · A.3</sub>

**코드 — tests/test_gilded_rose.py — Backstage passes · TC-04~06 (프롬프트: 241)**

```python
import pytest

@pytest.mark.parametrize('sell_in,init_q,expected_q', [
    (15, 20, 21), (11, 20, 21),   # > 10: +1 · 경계 11
    (10, 20, 22), ( 6, 20, 22),   # +2 시작 10 · 경계 6
    ( 5, 20, 23), ( 1, 20, 23),   # +3 시작 5 · 경계 1
    ( 0, 20,  0),                 # 콘서트 후 0
    ( 5, 50, 50), ( 0, 50,  0),   # 상한 50 · 0으로
])
def test_backstage_pass_quality(sell_in, init_q, expected_q):
    items = [Item('Backstage passes to a TAFKAL80ETC concert', sell_in, init_q)]
    GildedRose(items).update_quality()
    assert items[0].quality == expected_q
```

**실행 명령 · 결과 — 터미널**

```text
실행 명령
> python -m pytest -q tests/test_gilded_rose.py -k backstage     # 9 passed (경계 짝 · 상한 · 콘서트 후 0)
```

### 슬라이드 244 — 특성화 테스트 코드 (pytest) — 현재 동작을 그대로 고정한다
<sub>부록 A · A.3</sub>

**코드 — tests/test_characterization.py — 특성화 테스트 (프롬프트: 241)**

```python
tests/test_characterization.py — 현재 동작 기준 (docs/특성화.md)
from gilded_rose import GildedRose
from item import Item
def update(name, sell_in, quality):
    item = Item(name, sell_in, quality)
    GildedRose([item]).update_quality()
    return item
# CH-1 · quality 가 50 을 넘어 들어와도 일반 아이템은 -1 만 줄어든다 (50 으로 깎지 않는다)
def test_ch1_normal_above_50_decreases_by_one():
    assert update('Normal Item', 5, 60).quality == 59
# CH-2 · quality 가 음수로 들어오면 그대로 둔다 (0 으로 올리지 않는다)
def test_ch2_negative_quality_is_left_as_is():
    assert update('Normal Item', 5, -3).quality == -3
# CH-3 · quality 가 50 이상이면 Aged Brie 는 더 오르지 않고 그대로다
def test_ch3_aged_brie_at_55_does_not_increase():
    assert update('Aged Brie', 5, 55).quality == 55
# CH-4 · 이름이 정확히 같을 때만 특수 규칙 — 다른 이름은 일반 아이템으로 취급한다
def test_ch4_similar_name_is_treated_as_normal():
    assert update('Backstage passes to a TAFKAL80ETC concert Foo', 5, 20).quality == 19
# CH-5 · Sulfuras 는 quality 를 80 으로 맞추지 않는다 — 입력 그대로 둔다 (OQ-2 의 현재 답)
def test_ch5_sulfuras_quality_is_not_forced_to_80():
    assert update('Sulfuras, Hand of Ragnaros', 0, 40).quality == 40
# CH-6 · Sulfuras 는 sell_in 이 음수여도 그대로다
def test_ch6_sulfuras_keeps_negative_sell_in():
    assert update('Sulfuras, Hand of Ragnaros', -1, 80).sell_in == -1
```

**실행 명령 · 결과 — 실행 → 처음부터 GREEN · 터미널**

```text
> pytest -v tests/test_characterization.py
test_ch1_normal_above_50_decreases_by_one PASSED [ 16%]
test_ch2_negative_quality_is_left_as_is PASSED [ 33%]
test_ch3_aged_brie_at_55_does_not_increase PASSED [ 50%]
test_ch4_similar_name_is_treated_as_normal PASSED [ 66%]
test_ch5_sulfuras_quality_is_not_forced_to_80 PASSED [ 83%]
test_ch6_sulfuras_keeps_negative_sell_in PASSED [100%]
6 passed in 0.0Xs
```

**실행 명령 · 결과 — 터미널 — 전체**

```text
> pytest -q
18 passed in 0.03s     # 명세 12 + 특성화 6
```

### 슬라이드 245 — 상수 리팩터링 프롬프트 — 매직 스트링을 이름으로
<sub>부록 A · A.4  |  프롬프트</sub>

**▶ 프롬프트 — 상수 추출 (동작 불변)**

```text
@gilded_rose.py 모든 테스트가 통과하는 상태야.
동작은 바꾸지 말고, 아이템 이름 문자열과 매직 넘버(0 · 50 · 80)를 constants.py 의 이름 있는 상수로 바꾸는 것만 해줘.
- Item 클래스 · 테스트 수정 금지, 구조 변경(메서드 추출 등) 금지
- 이름 하나를 바꿀 때마다 pytest 를 실행해줘
- 끝나면 pytest -q 결과와 git diff --stat 을 보여줘
```

**▶ 프롬프트 — 보조 확인 테스트 (선택)**

```text
@constants.py
tests/test_constants.py 에 상수 값(MAX_QUALITY 50 · MIN_QUALITY 0 · SULFURAS_QUALITY 80)을 확인하는 테스트 1개만 작성해줘.
동작은 검증하지 못한다는 점을 주석으로 적고, pytest -q 결과를 보여줘.
```

**코드 — 기대 결과 — constants.py**

```python
constants.py
# constants.py
AGED_BRIE = 'Aged Brie'
BACKSTAGE_PASS = ('Backstage passes to a '
                  'TAFKAL80ETC concert')
SULFURAS = 'Sulfuras, Hand of Ragnaros'
CONJURED = 'Conjured Mana Cake'
MAX_QUALITY, MIN_QUALITY = 50, 0
SULFURAS_QUALITY = 80
```

**실행 명령 · 결과 — 터미널**

```text
실행 명령
> python -m pytest -q    # 19 passed (12 + 6 + 상수 1)  ·  git diff --stat 로 constants.py 추가 확인
```

### 슬라이드 246 — 상수 리팩터링 — 매직 스트링을 이름 있는 상수로
<sub>부록 A · A.4</sub>

**코드 — ✗ Before — 문자열이 곳곳에 흩어짐**

```python
def update_quality(self):
    for item in self.items:
        if item.name != 'Aged Brie' and \
           item.name != 'Backstage passes to …':
            if item.name != 'Sulfuras, Hand of …':
                item.quality -= 1
        # 'Aged Brie'가 여러 곳에 반복
        # → 하나만 오타가 나도 버그
```

**코드 — ✓ After — constants.py로 추출**

```python
# constants.py
AGED_BRIE = 'Aged Brie'
BACKSTAGE_PASS = ('Backstage passes to a '
                  'TAFKAL80ETC concert')
SULFURAS = 'Sulfuras, Hand of Ragnaros'
CONJURED = 'Conjured Mana Cake'
MAX_QUALITY, MIN_QUALITY = 50, 0
SULFURAS_QUALITY = 80
```

**코드 — gilded_rose.py — 상수로 바꾼 뒤 (동작 불변 → 기존 테스트 전부 GREEN)**

```python
from constants import AGED_BRIE, BACKSTAGE_PASS, SULFURAS, MIN_QUALITY
if item.name not in (AGED_BRIE, BACKSTAGE_PASS):
    if item.name != SULFURAS and item.quality > MIN_QUALITY:
        item.quality -= 1
```

### 슬라이드 247 — 상수 정리 뒤의 확인 — 무엇이 안전망인가
<sub>부록 A · A.4</sub>

**코드 — test_constants.py — 보조 확인**

```python
import constants

def test_quality_bounds_defined():
    assert constants.MAX_QUALITY == 50
    assert constants.MIN_QUALITY == 0
    assert constants.SULFURAS_QUALITY == 80
```

### 슬라이드 248 — 승인 테스트(ApprovalTests) — 레거시 보호막
<sub>부록 A · A.5</sub>

**실행 명령 · 결과 — 터미널 · test_gilded_rose_approval.py**

```text
$ pip install approvaltests

from approvaltests import verify

def test_thirty_day_simulation():
    # 처음에는 approved 파일이 없어 반드시 FAIL
    # → received 파일을 읽고 승인해야 보호막이 완성된다
    verify(simulate_30_days(make_items()))
```

### 슬라이드 249 — 골든 마스터 작성 프롬프트 — 30일 시뮬레이션 고정
<sub>부록 A · A.5  |  프롬프트</sub>

**▶ 프롬프트 — 승인 테스트(골든 마스터)**

```text
@gilded_rose.py @item.py
update_quality() 의 현재 동작을 골든 마스터로 고정하는 테스트를 만들어줘.
- 아이템 6종(+5 Dexterity Vest · Aged Brie · Elixir · Sulfuras×2 · Backstage) × 30일. Conjured 는 넣지 마 (곧 바꿀 대상)
- tests/test_gilded_rose_approval.py: approvaltests 의 verify(), 또는 도구 없이 JSON 비교
- 승인 파일은 만들어 두되, 내가 읽고 승인하기 전에는 커밋하지 마
- 같은 코드를 두 번 돌려 결과가 같은지(결정성)도 확인해줘. 코드는 수정하지 마
```

**실행 명령 · 결과 — 터미널**

```text
실행 · 승인 (실제 결과)
> pytest -q tests/test_gilded_rose_approval.py
  → 1 failed, 1 passed  (approved 파일이 아직 없다)
  → …received.txt 를 읽는다 (day 0 · day 30 · Sulfuras 80 · Backstage 0)
> ren …received.txt …approved.txt   # 사람이 승인 (mac/Linux: mv)
> pytest -q   → 21 passed  (12 + 6 + 1 + 2)
# tests/conftest.py : diff 도구(GUI) 대신 터미널에 차이를 보여 준다
```

### 슬라이드 250 — 30일 시뮬레이션과 승인 테스트 코드
<sub>부록 A · A.5</sub>

**코드 — test_gilded_rose_approval.py**

```python
def make_items():
    return [
        Item('+5 Dexterity Vest', 10, 20),
        Item('Aged Brie', 2, 0),
        Item('Elixir of the Mongoose', 5, 7),
        Item('Sulfuras, Hand of Ragnaros', 0, 80),
        Item('Sulfuras, Hand of Ragnaros', -1, 80),
        Item('Backstage passes to a TAFKAL80ETC concert', 15, 20),
        # Conjured는 넣지 않는다 — 곧 동작을 바꿀 대상
    ]

def simulate_30_days(items):
    gr, lines = GildedRose(items), []
    for day in range(31):
        lines.append(f'-------- day {day} --------')
        lines += [f'{i.name}, {i.sell_in}, {i.quality}' for i in gr.items]
        if day < 30:
            gr.update_quality()
    return '\n'.join(lines)
```

### 슬라이드 251 — Conjured TDD 프롬프트 — RED → GREEN → REFACTOR
<sub>부록 A · A.6  |  프롬프트</sub>

**실행 명령 · 결과 — 터미널**

```text
실행 결과 (실제)
> pytest -q tests/test_conjured.py    # RED : 2 failed, 1 passed
> pytest -q                         # GREEN : 24 passed
> pytest -q                         # REFACTOR 뒤 : 24 passed
```

### 슬라이드 252 — Conjured를 TDD로 추가 — ① RED
<sub>부록 A · A.6</sub>

**코드 — test_conjured.py**

```python
def test_conjured_degrades_twice_as_fast():
    items = [Item('Conjured Mana Cake', 10, 20)]
    GildedRose(items).update_quality()
    assert items[0].quality == 18   # 레거시는 19 → 올바른 이유로 FAIL

def test_conjured_degrades_four_after_sell_date():
    items = [Item('Conjured Mana Cake', 0, 10)]
    GildedRose(items).update_quality()
    assert items[0].quality == 6    # 레거시는 8 → FAIL

def test_conjured_quality_never_negative():
    items = [Item('Conjured Mana Cake', 5, 1)]
    GildedRose(items).update_quality()
    assert items[0].quality == 0    # 레거시도 1-1=0 → 이미 PASS
```

### 슬라이드 253 — Conjured — ② GREEN과 ③ REFACTOR
<sub>부록 A · A.6</sub>

**코드 — gilded_rose.py — ② GREEN: 최소 코드**

```python
def update_quality(self):
    for item in self.items:
        if item.name == CONJURED:
            degrade_by = 2 if item.sell_in > 0 else 4
            item.quality = max(MIN_QUALITY, item.quality - degrade_by)
            item.sell_in -= 1
            continue
        ...  # 기존 로직은 그대로
```

**코드 — gilded_rose.py — ③ REFACTOR: 상·하한 처리를 헬퍼로**

```python
def _degrade(item, amount):
    item.quality = max(MIN_QUALITY, item.quality - amount)

def _upgrade(item, amount):
    item.quality = min(MAX_QUALITY, item.quality + amount)
```

### 슬라이드 255 — 테스트 점검 프롬프트 — 안전망의 구멍 찾기
<sub>부록 A · A.7  |  프롬프트</sub>

**▶ 프롬프트 — 테스트 리뷰 (읽기 전용)**

```text
[역할] 테스트 리뷰어
@tests/ 를 아래 7가지 함정 관점으로 점검해줘. 파일은 수정하지 마.
함정: 가짜 RED · 변경 대상을 골든에 포함 · 골든 자동 갱신 · 비결정적 출력 · 현재 코드에서 예상값 베끼기 · 값만 확인하는 테스트 · 경계 한쪽만
[출력] 표: 함정 | 해당 여부 | 근거(파일:줄) | 제안   — 새 규칙은 만들지 마.
```

### 슬라이드 257 — 출발점 — 한 함수에 모든 규칙이 들어 있다
<sub>부록 B · B.1</sub>

**코드 — gilded_rose.py — 상수만 뽑은 레거시 (부록 A.4 이후)**

```python
def update_quality(self):
    for item in self.items:
        if item.name != AGED_BRIE and item.name != BACKSTAGE_PASS:
            if item.quality > 0:
                if item.name != SULFURAS:
                    item.quality -= 1
        else:
            if item.quality < 50:
                item.quality += 1
                if item.name == BACKSTAGE_PASS:
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality += 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality += 1
        # sellIn 감소 … 그리고 또 조건문 …
```

### 슬라이드 259 — 코드 스멜 분석 프롬프트 — 무엇을, 왜 고칠지 먼저
<sub>부록 B · B.2  |  프롬프트</sub>

**▶ 프롬프트 — 코드 스멜 분석 (읽기 전용)**

```text
[역할] 리팩터링 컨설턴트 (Fowler 『리팩토링』 기준)
@gilded_rose.py (상수 정리 후)의 코드 스멜을 분석해줘. 수정하지 마.
[출력] 표: 위치(함수·줄) | 스멜 | 근거 | 위험도(상·중·하) | 처방(기법 · 패턴 후보) | 난이도
후보: 긴 함수 · 깊은 중첩 · 중복 코드 · 매직 넘버 · 반복되는 switch · 기능 편애
마지막에 ‘고치는 순서’를 의존성 순으로 제안해줘.
[제약] 이미 통과하는 테스트가 있는 범위 안에서만 제안해줘.
```

### 슬라이드 260 — 리팩토링 계획서 작성 프롬프트 — 단계 · 완료 기준 · 롤백
<sub>부록 B · B.2  |  프롬프트</sub>

**▶ 프롬프트 — 리팩토링 계획서 (코드 수정 금지)**

```text
위 스멜 분석을 바탕으로 docs/refactoring-plan.md 를 작성해줘. 코드는 수정하지 마.
구성: 1) 목표와 비목표  2) 안전망(테스트 · 골든 마스터 상태, 실행 명령)
3) 단계표(STEP 1…n): 단계 | 변경 내용 | 리팩토링 기법 | 완료 기준(전체 테스트 GREEN) | 롤백 방법
4) 커밋 규칙(refactor: …, 구조 변경과 기능 변경 분리)  5) 위험과 대응
한 단계는 10분 이내, 단계마다 테스트 실행 → 커밋.
```

### 슬라이드 261 — 조건문을 다형성으로 — Employee 예제
<sub>부록 B · B.3  |  설계 원칙</sub>

**코드 — ✗ Before — 타입 코드로 분기**

```python
class Employee:
    ENGINEER, MANAGER, INTERN = range(3)

    def __init__(self, emp_type):
        self.type = emp_type

    def get_pay(self):
        if self.type == Employee.ENGINEER:
            return 5000
        elif self.type == Employee.MANAGER:
            return 8000
        elif self.type == Employee.INTERN:
            return 2000
        raise ValueError('Unknown type')
```

**코드 — ✓ After — ABC + 하위 클래스 + Factory**

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def get_pay(self): ...

class Engineer(Employee):
    def get_pay(self): return 5000

class Manager(Employee):
    def get_pay(self): return 8000

class Intern(Employee):
    def get_pay(self): return 2000

def create_employee(t: str) -> Employee:
    return {'ENGINEER': Engineer, 'MANAGER': Manager,
            'INTERN': Intern}[t]()
```

### 슬라이드 262 — STEP 1 프롬프트 — 테스트 먼저 (회귀 안전망 확인)
<sub>부록 B · B.4  |  STEP 1 프롬프트</sub>

**▶ 프롬프트 — STEP 1**

```text
@docs/refactoring-plan.md 의 STEP 1 만 수행해줘.
- 부록 A 의 경계값 · 승인 테스트를 실행해 전체가 GREEN 인지 확인
- 빠진 경계(Backstage 11/10 · 6/5 · 1/0, quality 0/50)가 있으면 테스트만 추가
- 프로덕션 코드는 수정 금지
- 결과: 전체 테스트 수 · 통과 수 · 추가한 테스트 목록
```

**실행 명령 · 결과 — 터미널**

```text
실행 명령 (실제 결과 — 부록B 예제)
> python -m pytest -q                     # 전체 GREEN 확인 (시작점)
> python -m pytest -q tests/test_regression_b4.py   # 4 passed (추가한 회귀 테스트)
> git diff --stat gilded_rose.py        # 변경 없음 (프로덕션 코드 수정 금지)
> git add tests && git commit -m "test: 경계 보강"
```

### 슬라이드 263 — 테스트 먼저 — 회귀 테스트 ①
<sub>부록 B · B.4  |  STEP 1</sub>

**코드 — tests/test_regression_b4.py (1/2) — 프롬프트: 앞 장 262**

```python
# ① 일반 아이템 — 매일 quality -1, sellIn -1
def test_normal_item_degrades():
    items = [Item('+5 Dexterity Vest', 10, 20)]
    GildedRose(items).update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 19

# ② 판매일이 지나면 2배 감소
def test_normal_item_degrades_twice_after_sell_in():
    items = [Item('Normal', 0, 10)]
    GildedRose(items).update_quality()
    assert items[0].quality == 8
```

### 슬라이드 264 — 테스트 먼저 — 회귀 테스트 ②
<sub>부록 B · B.4  |  STEP 1</sub>

**코드 — tests/test_gilded_rose.py (2/2) — 프롬프트: 262**

```python
# ③ quality는 음수가 되지 않는다
def test_quality_never_negative():
    items = [Item('Normal', 5, 0)]
    GildedRose(items).update_quality()
    assert items[0].quality == 0

# ④ Aged Brie — 오래될수록 quality 증가
def test_aged_brie_increases_quality():
    items = [Item('Aged Brie', 5, 10)]
    GildedRose(items).update_quality()
    assert items[0].quality == 11

# ⑤ quality는 50을 넘지 않는다
def test_quality_never_more_than_50():
    items = [Item('Aged Brie', 5, 50)]
    GildedRose(items).update_quality()
    assert items[0].quality == 50

# ⑥ Sulfuras — sellIn·quality 변화 없음
def test_sulfuras_never_changes():
    items = [Item('Sulfuras, Hand of Ragnaros', 0, 80)]
    GildedRose(items).update_quality()
    assert (items[0].sell_in, items[0].quality) == (0, 80)
```

### 슬라이드 265 — 코드 정리 — 상수 추출
<sub>부록 B · B.5  |  STEP 2</sub>

**코드 — ✗ Before — 문자열 리터럴이 흩어짐**

```python
class GildedRose:
    def update_quality(self):
        if item.name != 'Aged Brie' and \
           item.name != 'Backstage passes...':
            if item.name != 'Sulfuras...':
                ...
```

**코드 — ✓ After — 상수로 추출 (오타 방지)**

```python
AGED_BRIE = 'Aged Brie'
BACKSTAGE_PASS = ('Backstage passes to a '
                  'TAFKAL80ETC concert')
SULFURAS = 'Sulfuras, Hand of Ragnaros'
MAX_QUALITY, MIN_QUALITY = 50, 0

def update_quality(self):
    if item.name != AGED_BRIE and \
       item.name != BACKSTAGE_PASS:
        if item.name != SULFURAS: ...
```

### 슬라이드 266 — 코드 정리 — 반복문과 중첩
<sub>부록 B · B.5  |  STEP 2</sub>

**코드 — gilded_rose.py — for-in으로 인덱스 제거**

```python
# ✗ Before — 인덱스로 접근
for i in range(len(self.items)):
    if self.items[i].quality > 0:
        self.items[i].quality -= 1

# ✓ After — 객체를 직접 순회 (같은 객체를 가리키므로 원본이 바뀐다)
for item in self.items:
    if item.quality > 0:
        item.quality -= 1
```

**코드 — 불필요한 중첩 걷어내기**

```python
# ✗ if item.quality < 50:
#        item.quality += 1
# ✓ item.quality = min(MAX_QUALITY, item.quality + 1)
```

### 슬라이드 267 — STEP 2 프롬프트 — 코드 정리 (상수 · 변수 · 불필요 코드)
<sub>부록 B · B.5  |  STEP 2 프롬프트</sub>

**▶ 프롬프트 — STEP 2**

```text
@docs/refactoring-plan.md 의 STEP 2 만 수행해줘. 동작은 바꾸지 마.
① 중복 조건 · 미사용 코드 제거  ② 인덱스 for → for item in self.items
한 가지씩 하고, 각각 pytest -q 를 실행해 결과를 보여줘.
메서드 추출 같은 구조 변경은 아직 하지 마. 테스트는 수정 금지.
```

### 슬라이드 268 — 조건 분리 — 부정 조건 반전 (Invert if)
<sub>부록 B · B.6  |  STEP 3</sub>

**코드 — ✗ Before — 이중 부정이라 읽기 어렵다**

```python
if item.name != AGED_BRIE and item.name != BACKSTAGE_PASS:
    if item.quality > 0:
        if item.name != SULFURAS: item.quality -= 1
else:  # Aged Brie / Backstage 로직
```

**코드 — ✓ After — 긍정 조건으로 먼저 갈라 놓는다**

```python
if item.name in (AGED_BRIE, BACKSTAGE_PASS):
    if item.quality < MAX_QUALITY: item.quality += 1
    # Backstage 추가 로직
elif item.name == SULFURAS:
    pass  # 아무것도 하지 않는다
else:
    if item.quality > MIN_QUALITY: item.quality -= 1
```

### 슬라이드 269 — 조건 분리 — elif 병합과 같은 타입 조건 합치기
<sub>부록 B · B.6  |  STEP 3</sub>

**코드 — else + if → elif 병합**

```python
# ✗ Before
else:
    if item.name == SULFURAS:
        pass  # 빈 블록
    else:
        item.quality -= 1

# ✓ After
elif item.name == SULFURAS:
    pass
else:
    if item.quality > 0: item.quality -= 1
```

**코드 — Aged Brie 조건 두 곳 → 한 곳**

```python
# ✓ After — sellIn 감소 '전'으로 모은다
if item.name == AGED_BRIE:
    if item.quality < MAX_QUALITY:
        item.quality += 1
    if item.sell_in < 1:      # 0 → 1
        if item.quality < MAX_QUALITY:
            item.quality += 1
```

### 슬라이드 270 — STEP 3 프롬프트 — 조건 분리 (Invert if · elif 병합)
<sub>부록 B · B.6  |  STEP 3 프롬프트</sub>

**▶ 프롬프트 — STEP 3**

```text
@docs/refactoring-plan.md 의 STEP 3 만 수행해줘.
부정 조건 반전(Invert if) · else + if → elif 병합 · 같은 타입 조건 합치기를 한 번에 하나씩.
적용 전에 ‘무엇을 어떻게 바꿀지’ 계획을 먼저 보여주고, 내가 승인하면 적용해줘.
조건의 의미(특히 sell_in < 0 경계)는 바뀌면 안 돼. 매 단계 pytest -q.
```

### 슬라이드 271 — 메서드 추출 — Before: 한 함수에 모든 타입
<sub>부록 B · B.7  |  STEP 4</sub>

**코드 — gilded_rose.py — 거대한 update_quality()**

```python
def update_quality(self):
    for item in self.items:
        if item.name == AGED_BRIE:
            if item.quality < MAX_QUALITY: item.quality += 1
            if item.sell_in < 1:
                if item.quality < MAX_QUALITY: item.quality += 1
        elif item.name == BACKSTAGE_PASS:
            ...  # Backstage 로직
        elif item.name == SULFURAS:
            pass
        else:
            if item.quality > 0: item.quality -= 1
            if item.sell_in < 1:
                if item.quality > 0: item.quality -= 1
        if item.name != SULFURAS: item.sell_in -= 1
```

### 슬라이드 272 — 메서드 추출 — After: 타입별 메서드
<sub>부록 B · B.7  |  STEP 4</sub>

**코드 — gilded_rose.py**

```python
def update_quality(self):
    for item in self.items:
        if   item.name == AGED_BRIE:      self._update_aged_brie(item)
        elif item.name == BACKSTAGE_PASS: self._update_backstage_pass(item)
        elif item.name == SULFURAS:       self._update_sulfuras(item)
        else:                             self._update_normal_item(item)
        self._update_sell_in(item)   # sellIn 감소를 분리

def _update_aged_brie(self, item):
    if item.quality < MAX_QUALITY: item.quality += 1
    if item.sell_in < 1 and item.quality < MAX_QUALITY: item.quality += 1

def _update_backstage_pass(self, item):
    if item.quality < MAX_QUALITY: item.quality += 1
    if item.sell_in < 11 and item.quality < MAX_QUALITY: item.quality += 1
    if item.sell_in < 6  and item.quality < MAX_QUALITY: item.quality += 1
    if item.sell_in < 1: item.quality = 0

def _update_sulfuras(self, item): pass   # 변화 없음

def _update_normal_item(self, item):
    if item.quality > 0: item.quality -= 1
    if item.sell_in < 1 and item.quality > 0: item.quality -= 1

def _update_sell_in(self, item):
    if item.name != SULFURAS: item.sell_in -= 1
```

### 슬라이드 273 — STEP 4 프롬프트 — 메서드 추출 (타입별 _update_*)
<sub>부록 B · B.7  |  STEP 4 프롬프트</sub>

**▶ 프롬프트 — STEP 4**

```text
@docs/refactoring-plan.md 의 STEP 4 만 수행해줘.
update_quality() 의 타입별 분기를 _update_normal · _update_aged_brie · _update_backstage · _update_sulfuras 와 _update_sell_in 으로 Extract Method 해줘.
반환값과 부수효과는 그대로, 호출 순서(quality → sell_in → 판매일 후 처리)도 그대로.
메서드 하나 추출할 때마다 pytest -q 를 실행해줘.
```

### 슬라이드 274 — 클래스 분리 ① — 타입마다 파일 하나
<sub>부록 B · B.8  |  STEP 5</sub>

**코드 — aged_brie_item.py — 새 파일**

```python
class AgedBrieItem:
    def __init__(self, item):
        self._item = item            # 원본 Item을 감싼다 (Item은 수정 금지)

    def update_quality(self):
        i = self._item
        if i.quality < MAX_QUALITY: i.quality += 1
        if i.sell_in < 1 and i.quality < MAX_QUALITY: i.quality += 1
```

### 슬라이드 275 — 클래스 분리 ② — 사용하는 쪽
<sub>부록 B · B.8  |  STEP 5</sub>

**코드 — backstage_pass_item.py**

```python
class BackstagePassItem:
    def __init__(self, item):
        self._item = item

    def update_quality(self):
        i = self._item
        MAX = MAX_QUALITY
        if i.quality < MAX: i.quality += 1
        if i.sell_in < 11 and i.quality < MAX: i.quality += 1
        if i.sell_in < 6  and i.quality < MAX: i.quality += 1
        if i.sell_in < 1: i.quality = 0
```

**코드 — gilded_rose.py — 사용부**

```python
def update_quality(self):
    for item in self.items:
        if item.name == AGED_BRIE:
            AgedBrieItem(item).update_quality()
        elif item.name == BACKSTAGE_PASS:
            BackstagePassItem(item).update_quality()
        elif item.name == SULFURAS:
            SulfurasItem(item).update_quality()
        else:
            NormalItem(item).update_quality()
        self._update_sell_in(item)
```

### 슬라이드 276 — STEP 5 프롬프트 — 클래스 분리 (타입마다 파일 하나)
<sub>부록 B · B.8  |  STEP 5 프롬프트</sub>

**▶ 프롬프트 — STEP 5**

```text
@docs/refactoring-plan.md 의 STEP 5 만 수행해줘.
각 _update_* 메서드를 AgedBrieItem · BackstagePassItem · SulfurasItem · NormalItem 클래스로 옮겨줘 (파일 하나씩).
Item 클래스는 수정 금지 — 각 클래스가 item 을 감싸도록(self._item).
GildedRose 는 타입에 맞는 클래스를 골라 호출만 하게. 클래스 하나 옮길 때마다 pytest -q.
```

### 슬라이드 277 — 추상화와 다형성 ① — 공통 부모 GildedRoseItem
<sub>부록 B · B.9  |  STEP 6</sub>

**코드 — gilded_rose_item.py — 추상 기반 클래스**

```python
from abc import ABC, abstractmethod

class GildedRoseItem(ABC):
    def __init__(self, item):
        self._item = item

    @abstractmethod
    def update_quality(self): ...   # 하위 클래스가 각자 구현 (다형성)
```

### 슬라이드 278 — 추상화와 다형성 ② — 각 클래스가 부모를 상속
<sub>부록 B · B.9  |  STEP 6</sub>

**코드 — *_item.py**

```python
class AgedBrieItem(GildedRoseItem):
    def update_quality(self):
        i = self._item
        if i.quality < MAX_QUALITY: i.quality += 1
        if i.sell_in < 1 and i.quality < MAX_QUALITY: i.quality += 1

class BackstagePassItem(GildedRoseItem):
    def update_quality(self): ...    # B.8과 같은 본문

class SulfurasItem(GildedRoseItem):
    def update_quality(self): pass   # 변화 없음

class NormalItem(GildedRoseItem):
    def update_quality(self):
        i = self._item
        if i.quality > 0: i.quality -= 1
        if i.sell_in < 1 and i.quality > 0: i.quality -= 1
```

### 슬라이드 279 — 추상화와 다형성 ③ — Factory로 분기를 한 곳에
<sub>부록 B · B.9  |  STEP 6</sub>

**코드 — gilded_rose.py**

```python
def create_item(item) -> GildedRoseItem:
    if   item.name == AGED_BRIE:      return AgedBrieItem(item)
    elif item.name == BACKSTAGE_PASS: return BackstagePassItem(item)
    elif item.name == SULFURAS:       return SulfurasItem(item)
    else:                             return NormalItem(item)

def update_quality(self):
    for item in self.items:
        gilded_item = create_item(item)   # Factory — 타입 판별은 여기 한 곳
        gilded_item.update_quality()      # 다형성
        self._update_sell_in(item)
```

### 슬라이드 281 — Template Method로 완성 ④ — 순서는 부모가, 세부는 자식이
<sub>부록 B · B.9  |  STEP 6</sub>

**코드 — gilded_rose_item.py — Template Method**

```python
class GildedRoseItem(ABC):
    def __init__(self, item):
        self._item = item

    def update(self):                # 템플릿 메서드: 순서를 고정
        self.update_quality()
        self.update_sell_in()

    @abstractmethod
    def update_quality(self): ...    # 필수 단계

    def update_sell_in(self):        # 기본 구현 (hook)
        self._item.sell_in -= 1

class SulfurasItem(GildedRoseItem):
    def update_quality(self): pass
    def update_sell_in(self): pass   # 필요한 타입만 재정의
```

**코드 — 파일**

```python
# GildedRose.update_quality()
for item in self.items:
    create_item(item).update()
```

### 슬라이드 282 — 변수명 통일 — Rename Symbol
<sub>부록 B · B.9  |  STEP 6</sub>

**코드 — ✗ Before — 타입마다 다른 변수명**

```python
if item.name == AGED_BRIE:
    agedBrieItem = AgedBrieItem(item)
    agedBrieItem.update_quality()
elif item.name == BACKSTAGE_PASS:
    backstageItem = BackstagePassItem(item)
    backstageItem.update_quality()
```

**코드 — ✓ After — 하나의 이름**

```python
for item in self.items:
    gilded_item = create_item(item)
    gilded_item.update_quality()
    self._update_sell_in(item)
```

### 슬라이드 283 — STEP 6 프롬프트 ① — 추상화와 다형성 + 템플릿 메서드
<sub>부록 B · B.9  |  STEP 6 프롬프트 ①</sub>

**▶ 프롬프트 — 추상화 · 템플릿 메서드**

```text
@docs/refactoring-plan.md 의 STEP 6 중 ‘추상화’만 수행해줘.
공통 부모 GildedRoseItem(ABC)을 만들고 네 클래스가 상속하게 해줘. 필수 단계 update_quality() 는 추상 메서드로.
update() 에서 ‘quality 갱신 → sell_in 감소’ 순서를 고정(Template Method)하고, Sulfuras 만 update_sell_in() 을 재정의해줘.
클래스 하나씩 pytest -q.
```

### 슬라이드 284 — STEP 6 프롬프트 ② — Factory 와 이름 통일
<sub>부록 B · B.9  |  STEP 6 프롬프트 ②</sub>

**▶ 프롬프트 — Factory**

```text
create_item(item) Factory 함수를 만들어 타입 분기를 한 곳에 모으고, GildedRose.update_quality() 는 create_item(item).update() 만 호출하게 해줘.
동작은 그대로. pytest -q 결과를 보여줘.
```

**▶ 프롬프트 — 이름 통일**

```text
변수명 i · item · _item 이 섞여 있어. Rename 으로만 통일해줘 (논리 변경 금지). 한 이름씩 바꾸고 pytest -q.
```

### 슬라이드 285 — STEP 7 프롬프트 — 새 기능 F&B (이번에는 TDD)
<sub>부록 B · B.10  |  STEP 7 프롬프트</sub>

**실행 명령 · 결과 — 터미널**

```text
실행 명령 (실제 결과 — 부록B 예제)
> python -m pytest -q tests/test_food_beverage.py    # GREEN : 3 passed
> python -m pytest -q                              # 20 passed (신규 + 기존)
> git add -A && git commit -m "feat: F&B (구조 변경과 분리)"
```

### 슬라이드 286 — 새 기능 추가 — Food & Beverage (F&B)
<sub>부록 B · B.10  |  STEP 7</sub>

**코드 — food_beverage_item.py — 새 파일 (기존 아이템 클래스는 수정 없음)**

```python
class FoodBeverageItem(GildedRoseItem):
    def update_quality(self):
        i = self._item
        amount = 4 if i.sell_in < 1 else 2       # 판매일 후 4, 전 2
        i.quality = max(MIN_QUALITY, i.quality - amount)
```

### 슬라이드 287 — Factory 연결과 테스트
<sub>부록 B · B.10  |  STEP 7</sub>

**코드 — gilded_rose.py — Factory에 한 줄 추가**

```python
def create_item(item) -> GildedRoseItem:
    if item.name == AGED_BRIE:
        return AgedBrieItem(item)
    if item.name == BACKSTAGE_PASS:
        return BackstagePassItem(item)
    if item.name == SULFURAS:
        return SulfurasItem(item)
    if '[F&B]' in item.name:
        return FoodBeverageItem(item)  # ← 추가
    return NormalItem(item)
```

**코드 — test_food_beverage.py — 먼저 작성 (RED)**

```python
def test_degrades_twice_as_normal():
    items = [Item('[F&B] Bread', 5, 20)]
    GildedRose(items).update_quality()
    assert items[0].quality == 18

def test_degrades_four_after_sell_in():
    items = [Item('[F&B] Milk', 0, 10)]
    GildedRose(items).update_quality()
    assert items[0].quality == 6

def test_quality_never_below_zero():
    items = [Item('[F&B] Water', 0, 1)]
    GildedRose(items).update_quality()
    assert items[0].quality == 0
```

### 슬라이드 288 — 추가 리팩터링 — 중복 제거와 변수 인라인
<sub>부록 B · B.11  |  STEP 8–10</sub>

**코드 — STEP 8–9 · 분기마다 반복되던 호출 → 한 곳**

```python
# ✗ Before
if item.name == AGED_BRIE:
    gi = AgedBrieItem(item)
    gi.update_quality()
elif item.name == BACKSTAGE_PASS:
    gi = BackstagePassItem(item)
    gi.update_quality()
# … 타입마다 같은 패턴
```

**코드 — STEP 10 · Inline Variable**

```python
# ✗ Before — 한 번 쓰고 버리는 임시 변수
gi = create_item(item)
gi.update_quality()
```

**코드 — 파일**

```python
create_item(item).update_quality()   # ✓ After
```

**코드 — 파일**

```python
# ✓ After — Extract Method
gi = create_item(item)
gi.update_quality()
```

### 슬라이드 289 — STEP 8–10 프롬프트 — 중복 제거와 변수 인라인
<sub>부록 B · B.11  |  STEP 8–10 프롬프트</sub>

**▶ 프롬프트 — 추가 리팩터링**

```text
@docs/refactoring-plan.md 의 STEP 8~10 을 순서대로, 한 단계씩만 수행해줘.
8) 분기마다 반복되던 호출을 한 곳으로  9) 한 번만 쓰는 임시 변수 인라인  10) 남은 중복 제거
각 단계마다 변경 계획 → 적용 → pytest -q 결과를 보고해줘. 동작 · 테스트는 바꾸지 마.
```

### 슬라이드 290 — Before vs After — 무엇이 달라졌나
<sub>부록 B · B.12</sub>

**코드 — ✗ Before — 레거시**

```python
def update_quality(self):
    for i in range(len(self.items)):
        if self.items[i].name != 'Aged Brie' \
           and self.items[i].name != 'Backstage...':
            ...  # 중첩이 계속된다
# 새 아이템? → if 블록 전체를 수정
# 테스트?   → 규칙이 얽혀 단위 테스트가 어렵다
```

**코드 — ✓ After — 리팩터링 결과**

```python
def update_quality(self):
    for item in self.items:
        create_item(item).update_quality()
        self._update_sell_in(item)

# 새 아이템? → 새 클래스 + Factory 한 줄
class ConjuredItem(GildedRoseItem): ...
```

### 슬라이드 291 — 검증 프롬프트 — 레거시와 결과를 전수 비교
<sub>부록 B · B.12  |  프롬프트</sub>

**▶ 프롬프트 — 레거시 대비 검증**

```text
legacy/gilded_rose_legacy.py 와 현재 gilded_rose.py 를 비교하는 tests/test_golden_vs_legacy.py 를 만들어줘.
- 아이템 4종(일반 · Aged Brie · Sulfuras · Backstage) × sell_in -2~20 × quality 0~50 × 30일
- [F&B] 는 제외(의도한 동작 변경)
- 다르면 처음 5건을 ‘입력 · 레거시 결과 · 새 결과’ 표로 보여줘
- 프로덕션 코드는 수정하지 마.
```

**실행 명령 · 결과 — 기대 결과 · 터미널**

```text
> pytest -q tests/test_golden_vs_legacy.py
.  [100%]
1 passed in 0.5s

# 차이가 있다면 (예)
mismatch #1: Backstage sell_in=0 q=20 → legacy 0 / new 3
```

### 슬라이드 293 — 최종 리뷰 프롬프트 — PR 설명과 함정 점검
<sub>부록 B · B.13  |  프롬프트</sub>

**▶ 프롬프트 — 최종 리뷰 (코드 수정 금지)**

```text
git diff main 을 읽고 PR 설명을 작성해줘. 코드는 수정하지 마.
구성: 변경 요약 · 단계별 커밋 목록 · 동작 불변의 근거(테스트 수 · 골든 · 레거시 비교) · 위험 · 남은 스멜
그다음 ‘리팩터링 함정 7가지’ 표로 점검해줘: 함정 | 해당 여부 | 근거 | 제안
```

**실행 명령 · 결과 — 기대 산출물 — PR 설명 (요약)**

```text
PR 설명
## 변경 요약
- update_quality() 를 타입별 클래스 + Factory 로 분리
## 동작 불변 근거
- 테스트 20 passed · 골든(30일) 동일 · 레거시 비교 동일
## 단계별 커밋
- refactor: 상수 · 조건 · 메서드 · 클래스 …
## 위험
- Item 은 수정하지 않음
## 남은 스멜
- Backstage 의 상한 검사 중복
```
