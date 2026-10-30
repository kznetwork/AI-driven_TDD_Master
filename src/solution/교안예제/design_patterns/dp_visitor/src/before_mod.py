class Book:
    def __init__(self, price, isbn):
        self.price, self.isbn = price, isbn


class Fruit:
    def __init__(self, name, price_per_kg, weight):
        self.name, self.price_per_kg, self.weight = name, price_per_kg, weight


def total_cost(items):
    total = 0
    for item in items:
        if isinstance(item, Book):               # 종류마다 if — 연산이 늘 때마다 여기를 고친다
            total += item.price
        elif isinstance(item, Fruit):
            total += item.price_per_kg * item.weight
    return total
