DISCOUNT_THRESHOLD = 50_000
THRESHOLD_PERCENT = 90
VIP_PERCENT = 95
VIP = 2


def final_price(price, grade):
    if price >= DISCOUNT_THRESHOLD:
        price = price * THRESHOLD_PERCENT // 100
    if grade == VIP:
        price = price * VIP_PERCENT // 100
    return price
