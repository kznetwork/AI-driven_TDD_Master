from abc import ABC, abstractmethod


class Book:                                      # Element — 데이터는 그대로
    def __init__(self, price, isbn):
        self.price, self.isbn = price, isbn

    def accept(self, visitor):
        return visitor.visit_book(self)


class Fruit:
    def __init__(self, name, price_per_kg, weight):
        self.name, self.price_per_kg, self.weight = name, price_per_kg, weight

    def accept(self, visitor):
        return visitor.visit_fruit(self)


class ShoppingCartVisitor(ABC):                  # Visitor — 연산을 따로 모은다
    @abstractmethod
    def visit_book(self, book): ...

    @abstractmethod
    def visit_fruit(self, fruit): ...


class CostVisitor(ShoppingCartVisitor):          # ConcreteVisitor ① 가격 계산
    def visit_book(self, book):
        return book.price

    def visit_fruit(self, fruit):
        return fruit.price_per_kg * fruit.weight


class LabelVisitor(ShoppingCartVisitor):         # ConcreteVisitor ② 라벨 — 데이터 클래스는 그대로
    def visit_book(self, book):
        return f"Book ISBN: {book.isbn}"

    def visit_fruit(self, fruit):
        return f"Fruit: {fruit.name}"


def total_cost(items):
    visitor = CostVisitor()
    return sum(item.accept(visitor) for item in items)
