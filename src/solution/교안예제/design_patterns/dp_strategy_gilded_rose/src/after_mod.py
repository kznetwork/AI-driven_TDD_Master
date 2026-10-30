from abc import ABC, abstractmethod


class Item:
    def __init__(self, name, sell_in, quality):
        self.name, self.sell_in, self.quality = name, sell_in, quality


class QualityUpdateStrategy(ABC):                # Strategy
    @abstractmethod
    def update(self, item): ...


class AgedBrieStrategy(QualityUpdateStrategy):
    def update(self, item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class SulfurasStrategy(QualityUpdateStrategy):
    def update(self, item):
        pass                                     # 아무 것도 안 함


class BackstageStrategy(QualityUpdateStrategy):
    def update(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0


class DefaultStrategy(QualityUpdateStrategy):
    def update(self, item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


STRATEGIES = {
    "Aged Brie": AgedBrieStrategy(),
    "Sulfuras": SulfurasStrategy(),
    "Backstage": BackstageStrategy(),
}
DEFAULT = DefaultStrategy()


def update_quality(items):                       # 전략만 호출 — 새 아이템은 클래스 + 등록 한 줄
    for item in items:
        STRATEGIES.get(item.name, DEFAULT).update(item)
