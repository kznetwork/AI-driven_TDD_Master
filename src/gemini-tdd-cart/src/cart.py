def subtotal(items):
  return sum(item["price"] * item["qty"] for item in items)


def apply_threshold_discount(amount):
  if amount >= 50000:
    return round(amount * 0.9)
  return amount


def final_total(items, is_vip=False):
  amount = apply_threshold_discount(subtotal(items))
  if is_vip:
    return round(amount * 0.95)
  return amount
