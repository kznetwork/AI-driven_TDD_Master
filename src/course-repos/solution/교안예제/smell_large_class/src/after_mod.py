class Order:                       # 계산만 책임진다
    def __init__(self, items):
        self.items = items

    def total(self):
        return sum(p * q for p, q in self.items)


class OrderCsv:                    # 내보내기 책임
    @staticmethod
    def render(order):
        return "\n".join(f"{p},{q}" for p, q in order.items)


class OrderMail:                   # 알림 책임
    @staticmethod
    def body(order):
        return f"주문 금액: {order.total()}원"
