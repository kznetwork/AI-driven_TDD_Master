def threshold(price):
    return price * 0.9 if price >= 50000 else price


def vip_price(price):
    return int(threshold(price) * 0.95)


def normal_price(price):
    return int(threshold(price))
