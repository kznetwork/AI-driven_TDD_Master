# -*- coding: utf-8 -*-
from constants import AGED_BRIE, BACKSTAGE_PASS, SULFURAS
from gilded_rose_item import (AgedBrieItem, BackstagePassItem, FoodBeverageItem,
                              GildedRoseItem, NormalItem, SulfurasItem)


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


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            create_item(item).update()

    def _update_sell_in(self, item):
        if item.name != SULFURAS: item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
