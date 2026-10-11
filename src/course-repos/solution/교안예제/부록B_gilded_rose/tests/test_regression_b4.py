from gilded_rose import GildedRose, Item

def test_normal_item_degrades():
    items = [Item('+5 Dexterity Vest', 10, 20)]
    GildedRose(items).update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 19

def test_normal_item_degrades_twice_after_sell_in():
    items = [Item('Normal', 0, 10)]
    GildedRose(items).update_quality()
    assert items[0].quality == 8

def test_aged_brie_increases_quality():
    items = [Item('Aged Brie', 5, 10)]
    GildedRose(items).update_quality()
    assert items[0].quality == 11

def test_sulfuras_never_changes():
    items = [Item('Sulfuras, Hand of Ragnaros', 0, 80)]
    GildedRose(items).update_quality()
    assert (items[0].sell_in, items[0].quality) == (0, 80)
