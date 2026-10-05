class Order:
    def __init__(self, items):
        self.items = items

    def total(self):
        return sum(p * q for p, q in self.items)

    def to_csv(self):
        return "\n".join(f"{p},{q}" for p, q in self.items)

    def email_body(self):
        return f"주문 금액: {self.total()}원"
