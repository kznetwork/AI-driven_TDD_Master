def subtotal(items):
    for item in items:
        if item["price"] < 0 or item["qty"] < 0:
            raise ValueError("가격과 수량은 0 이상이어야 합니다")
    return sum(item["price"] * item["qty"] for item in items)


def apply_threshold_discount(amount):
    if amount >= 50000:
        return amount * 90 // 100
    return amount


def final_total(items, is_vip=False):
    amount = apply_threshold_discount(subtotal(items))
    if is_vip:
        amount = amount * 95 // 100
    return amount
