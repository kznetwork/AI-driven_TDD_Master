def apply_discount(price, kind):
    if kind == "percent":
        return price * 90 // 100
    if kind == "fixed":
        return price - 1000
    if kind == "vip":
        return price * 85 // 100
    raise ValueError(kind)
