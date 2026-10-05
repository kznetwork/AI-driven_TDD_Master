from abc import ABC, abstractmethod

from constants import MAX_QUALITY, MIN_QUALITY


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


class AgedBrieItem(GildedRoseItem):
    def update_quality(self):
        i = self._item
        if i.quality < MAX_QUALITY: i.quality += 1
        if i.sell_in < 1 and i.quality < MAX_QUALITY: i.quality += 1


class BackstagePassItem(GildedRoseItem):
    def update_quality(self):
        i = self._item
        MAX = MAX_QUALITY
        if i.quality < MAX: i.quality += 1
        if i.sell_in < 11 and i.quality < MAX: i.quality += 1
        if i.sell_in < 6  and i.quality < MAX: i.quality += 1
        if i.sell_in < 1: i.quality = 0


class SulfurasItem(GildedRoseItem):
    def update_quality(self): pass
    def update_sell_in(self): pass   # 필요한 타입만 재정의


class NormalItem(GildedRoseItem):
    def update_quality(self):
        i = self._item
        if i.quality > 0: i.quality -= 1
        if i.sell_in < 1 and i.quality > 0: i.quality -= 1


class FoodBeverageItem(GildedRoseItem):
    def update_quality(self):
        i = self._item
        amount = 4 if i.sell_in < 1 else 2       # 판매일 후 4, 전 2
        i.quality = max(MIN_QUALITY, i.quality - amount)
