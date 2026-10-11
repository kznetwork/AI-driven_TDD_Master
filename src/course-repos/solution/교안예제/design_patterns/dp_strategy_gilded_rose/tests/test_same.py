import itertools

import after_mod
import before_mod

NAMES = ["Normal", "Aged Brie", "Sulfuras", "Backstage"]


def run(mod, name, sell_in, quality, days=30):
    items = [mod.Item(name, sell_in, quality)]
    history = []
    for _ in range(days):
        mod.update_quality(items)
        history.append((items[0].sell_in, items[0].quality))
    return history


def test_same_for_30_days():
    for name, sell_in, quality in itertools.product(NAMES, [-1, 0, 1, 5, 6, 10, 11, 15], [0, 1, 20, 49, 50]):
        assert run(after_mod, name, sell_in, quality) == run(before_mod, name, sell_in, quality), (name, sell_in, quality)
