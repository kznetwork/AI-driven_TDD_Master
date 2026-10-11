def calculate_discount(price, is_vip):          # 리팩토링 — 중복 제거 (한 함수 안)
    rate = 10 if is_vip else 5
    return price - (price * rate // 100)


class Customer:                                 # 리스트럭처링 — 책임을 Customer 에게
    def __init__(self, is_vip):
        self.is_vip = is_vip

    def get_discount(self, price):
        rate = 10 if self.is_vip else 5
        return price - (price * rate // 100)


class Order:
    def __init__(self, price, customer):
        self.price = price
        self.customer = customer

    def discounted_price(self):
        return self.customer.get_discount(self.price)
