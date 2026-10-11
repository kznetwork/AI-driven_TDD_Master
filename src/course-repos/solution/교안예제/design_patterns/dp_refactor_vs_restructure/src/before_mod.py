def calculate_discount(price, is_vip):
    if is_vip:
        return price - (price * 10 // 100)
    else:
        return price - (price * 5 // 100)


class Order:
    def __init__(self, price, is_vip):
        self.price = price
        self.is_vip = is_vip

    def discounted_price(self):
        if self.is_vip:
            return self.price - (self.price * 10 // 100)
        else:
            return self.price - (self.price * 5 // 100)
