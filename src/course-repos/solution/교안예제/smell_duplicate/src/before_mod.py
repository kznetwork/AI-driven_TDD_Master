def vip_price(price):
    if price >= 50000:
        return int(price * 0.9 * 0.95)
    return int(price * 0.95)


def normal_price(price):
    if price >= 50000:
        return int(price * 0.9)
    return int(price)
