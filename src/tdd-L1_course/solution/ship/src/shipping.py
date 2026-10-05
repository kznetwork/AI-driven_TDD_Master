BASE_FEE = 3000
FREE_THRESHOLD = {"NORMAL": 30000, "GOLD": 20000}


def shipping_fee(order_amount, grade="NORMAL"):
    if order_amount <= 0:
        raise ValueError("주문 금액은 0보다 커야 합니다")
    if order_amount >= FREE_THRESHOLD[grade]:
        return 0
    return BASE_FEE
