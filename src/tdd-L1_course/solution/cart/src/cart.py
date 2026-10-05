THRESHOLD = 50_000            # 문턱 할인 기준 금액 (이상)
THRESHOLD_PERCENT = 90        # 문턱 할인 후 남는 비율
VIP_PERCENT = 95              # VIP 추가 할인 후 남는 비율


def subtotal(items):
    for item in items:
        if item["price"] < 0 or item["qty"] < 0:
            raise ValueError("가격과 수량은 0 이상이어야 합니다")
    return sum(item["price"] * item["qty"] for item in items)


def _percent_of(amount, percent):
    return amount * percent // 100


def apply_threshold_discount(amount):
    if amount >= THRESHOLD:
        return _percent_of(amount, THRESHOLD_PERCENT)
    return amount


def final_total(items, is_vip=False):
    amount = apply_threshold_discount(subtotal(items))
    if is_vip:
        amount = _percent_of(amount, VIP_PERCENT)
    return amount
