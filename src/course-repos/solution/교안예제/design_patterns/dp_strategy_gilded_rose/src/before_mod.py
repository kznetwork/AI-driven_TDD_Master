class Item:
    def __init__(self, name, sell_in, quality):
        self.name, self.sell_in, self.quality = name, sell_in, quality


def update_quality(items):
    for item in items:
        if item.name == "Aged Brie":
            if item.quality < 50:
                item.quality += 1
            item.sell_in -= 1
            if item.sell_in < 0 and item.quality < 50:
                item.quality += 1
        elif item.name == "Sulfuras":
            pass
        elif item.name == "Backstage":
            if item.quality < 50:
                item.quality += 1
                if item.sell_in < 11 and item.quality < 50:
                    item.quality += 1
                if item.sell_in < 6 and item.quality < 50:
                    item.quality += 1
            item.sell_in -= 1
            if item.sell_in < 0:
                item.quality = 0
        else:
            if item.quality > 0:
                item.quality -= 1
            item.sell_in -= 1
            if item.sell_in < 0 and item.quality > 0:
                item.quality -= 1
