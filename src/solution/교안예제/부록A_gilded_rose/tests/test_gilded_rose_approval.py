from approvaltests import verify
from gilded_rose import GildedRose, Item

def make_items():
    return [
        Item('+5 Dexterity Vest', 10, 20),
        Item('Aged Brie', 2, 0),
        Item('Elixir of the Mongoose', 5, 7),
        Item('Sulfuras, Hand of Ragnaros', 0, 80),
        Item('Sulfuras, Hand of Ragnaros', -1, 80),
        Item('Backstage passes to a TAFKAL80ETC concert', 15, 20),
    ]

def simulate_30_days(items):
    gr, lines = GildedRose(items), []
    for day in range(31):
        lines.append(f'-------- day {day} --------')
        lines += [f'{i.name}, {i.sell_in}, {i.quality}' for i in gr.items]
        if day < 30:
            gr.update_quality()
    return '\n'.join(lines)

def test_thirty_day_simulation():
    verify(simulate_30_days(make_items()))
