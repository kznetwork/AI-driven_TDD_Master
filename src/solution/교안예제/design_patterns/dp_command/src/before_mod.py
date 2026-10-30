class Order:
    def __init__(self, items):
        self.items = items                       # [(이름, 가격, 수량), ...]

    def calculate_total_price(self):
        total = 0
        for _, price, qty in self.items:
            total += price * qty
        if total > 1000:
            total = total * 9 // 10              # 할인 적용
        return total
