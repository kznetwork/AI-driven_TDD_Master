"""승인 테스트(골든 마스터) — 6종 아이템 × 30일의 '현재 동작'을 파일로 고정한다."""
from approvaltests import verify
from gilded_rose import GildedRose
from item import Item


def make_items():
    return [
        Item('+5 Dexterity Vest', 10, 20),
        Item('Aged Brie', 2, 0),
        Item('Elixir of the Mongoose', 5, 7),
        Item('Sulfuras, Hand of Ragnaros', 0, 80),
        Item('Sulfuras, Hand of Ragnaros', -1, 80),
        Item('Backstage passes to a TAFKAL80ETC concert', 15, 20),
        # Conjured는 넣지 않는다 — 곧 동작을 바꿀 대상
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
    # 처음에는 approved 파일이 없어 반드시 FAIL
    # → received 파일을 읽고 사람이 승인해야 보호막이 완성된다
    verify(simulate_30_days(make_items()))


def test_simulation_is_deterministic():
    # 같은 입력으로 두 번 돌려 결과가 같은지 (결정성)
    assert simulate_30_days(make_items()) == simulate_30_days(make_items())
