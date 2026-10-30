from constants import CONJURED, AGED_BRIE, BACKSTAGE_PASS, SULFURAS, MAX_QUALITY, MIN_QUALITY
from item import Item


def _degrade(item, amount):
    item.quality = max(MIN_QUALITY, item.quality - amount)


def _upgrade(item, amount):
    item.quality = min(MAX_QUALITY, item.quality + amount)


class GildedRose:
    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == CONJURED:
                _degrade(item, 2 if item.sell_in > 0 else 4)
                item.sell_in -= 1
                continue
            if (item.name != AGED_BRIE
                    and item.name != BACKSTAGE_PASS):
                if item.quality > MIN_QUALITY:
                    if item.name != SULFURAS:
                        item.quality = item.quality - 1
            else:
                if item.quality < MAX_QUALITY:
                    item.quality = item.quality + 1

                    if item.name == BACKSTAGE_PASS:
                        if item.sell_in < 11:
                            if item.quality < MAX_QUALITY:
                                item.quality = item.quality + 1

                        if item.sell_in < 6:
                            if item.quality < MAX_QUALITY:
                                item.quality = item.quality + 1

            if item.name != SULFURAS:
                item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                if item.name != AGED_BRIE:
                    if item.name != BACKSTAGE_PASS:
                        if item.quality > MIN_QUALITY:
                            if item.name != SULFURAS:
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < MAX_QUALITY:
                        item.quality = item.quality + 1
