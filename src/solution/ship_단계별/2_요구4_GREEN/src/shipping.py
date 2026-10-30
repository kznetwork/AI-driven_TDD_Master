BASE_FEE = 3000


def shipping_fee(order_amount, grade="NORMAL"):
    if order_amount <= 0:
        raise ValueError("주문 금액은 0보다 커야 합니다")
    if grade == "GOLD":
        if order_amount >= 20000:
            return 0
    elif order_amount >= 30000:
        return 0
    return BASE_FEE
