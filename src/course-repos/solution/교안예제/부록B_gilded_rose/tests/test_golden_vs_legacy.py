import importlib.util, io, sys, contextlib, pathlib
LEGACY = pathlib.Path(__file__).resolve().parent.parent / "legacy" / "gilded_rose_legacy.py"

def _run(mod_items, mod_gr, days=30):
    items = [mod_items("+5 Dexterity Vest", 10, 20), mod_items("Aged Brie", 2, 0), mod_items("Elixir of the Mongoose", 5, 7),
             mod_items("Sulfuras, Hand of Ragnaros", 0, 80), mod_items("Sulfuras, Hand of Ragnaros", -1, 80),
             mod_items("Backstage passes to a TAFKAL80ETC concert", 15, 20), mod_items("Backstage passes to a TAFKAL80ETC concert", 10, 49),
             mod_items("Backstage passes to a TAFKAL80ETC concert", 5, 49), mod_items("Conjured Mana Cake", 3, 6)]
    out = []
    for _ in range(days):
        out.append([repr(i) for i in items]); mod_gr(items).update_quality()
    return out

def test_same_as_legacy_for_30_days():
    spec = importlib.util.spec_from_file_location("legacy_gr", LEGACY); legacy = importlib.util.module_from_spec(spec); spec.loader.exec_module(legacy)
    import gilded_rose as new
    assert _run(legacy.Item, legacy.GildedRose) == _run(new.Item, new.GildedRose)
