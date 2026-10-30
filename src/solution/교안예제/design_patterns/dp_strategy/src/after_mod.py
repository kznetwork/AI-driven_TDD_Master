from abc import ABC, abstractmethod


class DiscountStrategy(ABC):                     # Strategy
    @abstractmethod
    def apply(self, price): ...


class PercentageDiscount(DiscountStrategy):      # 정률 10%
    def apply(self, price):
        return price * 90 // 100


class FixedDiscount(DiscountStrategy):           # 정액 1,000원
    def apply(self, price):
        return price - 1000


class VipDiscount(DiscountStrategy):             # VIP 15%
    def apply(self, price):
        return price * 85 // 100


class Order:                                     # Context — 전략을 주입받아 쓴다
    def __init__(self, price, strategy):
        self.price = price
        self.strategy = strategy

    def total(self):
        return self.strategy.apply(self.price)


STRATEGIES = {
    "percent": PercentageDiscount(),
    "fixed": FixedDiscount(),
    "vip": VipDiscount(),
}


def apply_discount(price, kind):
    return Order(price, STRATEGIES[kind]).total()
