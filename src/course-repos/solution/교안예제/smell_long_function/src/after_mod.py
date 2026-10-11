def subtotal(items):
    if any(it["qty"] < 1 for it in items):
        raise ValueError("qty")
    return sum(it["price"] * it["qty"] for it in items)


def apply_discounts(amount, is_vip):
    if amount >= 50000:
        amount *= 0.9
    return amount * 0.95 if is_vip else amount


def checkout(items, is_vip):
    total = int(apply_discounts(subtotal(items), is_vip))
    return total, f"합계 {total:,}원"
