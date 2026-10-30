def checkout(items, is_vip):
    total = 0
    for it in items:
        if it["qty"] < 1:
            raise ValueError("qty")
        total += it["price"] * it["qty"]
    if total >= 50000:
        total = total * 0.9
    if is_vip:
        total = total * 0.95
    receipt = f"합계 {int(total):,}원"
    return int(total), receipt
