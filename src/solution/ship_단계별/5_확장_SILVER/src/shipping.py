from abc import ABC, abstractmethod

BASE_FEE = 3000


class ShippingPolicy(ABC):
    """등급별 배송비 규칙(전략). 새 등급 = 새 클래스 하나."""

    @abstractmethod
    def fee(self, order_amount):
        ...


class NormalPolicy(ShippingPolicy):
    def fee(self, order_amount):
        return 0 if order_amount >= 30000 else BASE_FEE


class GoldPolicy(ShippingPolicy):
    def fee(self, order_amount):
        return 0 if order_amount >= 20000 else BASE_FEE


class SilverPolicy(ShippingPolicy):               # ← 새 등급: 클래스 하나
    def fee(self, order_amount):
        return 0 if order_amount >= 25000 else BASE_FEE


POLICIES = {
    "NORMAL": NormalPolicy(),
    "GOLD": GoldPolicy(),
    "SILVER": SilverPolicy(),                      # ← 등록 한 줄
}


def shipping_fee(order_amount, grade="NORMAL"):    # ← 이 함수는 한 줄도 바뀌지 않았다
    if order_amount <= 0:
        raise ValueError("주문 금액은 0보다 커야 합니다")
    return POLICIES[grade].fee(order_amount)
