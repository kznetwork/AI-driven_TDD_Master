from gilded_rose import GildedRose
from item import Item


def test_conjured_degrades_twice_as_fast():          # TC-11 · R-8
    items = [Item('Conjured Mana Cake', 10, 20)]
    GildedRose(items).update_quality()
    assert items[0].quality == 18   # 레거시는 19 → 올바른 이유로 FAIL


def test_conjured_degrades_four_after_sell_date():   # TC-12 · R-8
    items = [Item('Conjured Mana Cake', 0, 10)]
    GildedRose(items).update_quality()
    assert items[0].quality == 6    # 레거시는 8 → FAIL


def test_conjured_quality_never_negative():          # TC-13 · R-8
    items = [Item('Conjured Mana Cake', 5, 1)]
    GildedRose(items).update_quality()
    assert items[0].quality == 0    # 레거시도 1-1=0 → 이미 PASS
