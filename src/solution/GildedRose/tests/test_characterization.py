"""특성화 테스트 — 명세에 없지만 '지금 이렇게 동작한다'를 그대로 고정한다 (docs/특성화.md).

기대값은 요구사항이 아니라 현재 코드를 실행해 얻은 값이다. 옳은지 그른지는 묻지 않는다.
실패하면 '동작이 바뀌었다'는 뜻이므로, 리팩터링 중이라면 방금 한 변경을 되돌린다.
"""
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
