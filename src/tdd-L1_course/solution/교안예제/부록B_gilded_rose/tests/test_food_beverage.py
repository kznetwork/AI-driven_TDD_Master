from gilded_rose import GildedRose, Item

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
