class TotalPriceCalculator:                      # Command — 계산(작업)을 객체로
    def __init__(self, order):
        self.order = order

    def execute(self):
        total = self._subtotal()
        return self._apply_discount(total)

    def _subtotal(self):
        return sum(price * qty for _, price, qty in self.order.items)

    def _apply_discount(self, total):
        return total * 9 // 10 if total > 1000 else total


class Order:                                     # Invoker — 호출만 한다
    def __init__(self, items):
        self.items = items

    def calculate_total_price(self):
        return TotalPriceCalculator(self).execute()
