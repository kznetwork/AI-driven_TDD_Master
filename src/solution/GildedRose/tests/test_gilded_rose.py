"""명세 테스트 — 기대값은 요구사항(docs/규칙표.md · docs/테스트케이스.md)에서 왔다."""
import pytest
from gilded_rose import GildedRose
from item import Item


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


# TC-04~06 · R-7 Backstage 경계 짝 (11/10 · 6/5 · 1/0) + 상한 50
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
