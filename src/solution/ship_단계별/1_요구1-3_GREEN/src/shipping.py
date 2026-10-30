def shipping_fee(order_amount):
    if order_amount <= 0:
        raise ValueError("주문 금액은 0보다 커야 합니다")
    if order_amount >= 30000:
        return 0
    return 3000
