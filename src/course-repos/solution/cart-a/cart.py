DISCOUNT_THRESHOLD = 50000
STANDARD_DISCOUNT_RATE = 0.1
VIP_DISCOUNT_RATE = 0.05


def _subtotal(items):
  for item in items:
    if item["price"] < 0:
      raise ValueError("price must not be negative")
    if item["qty"] < 1:
      raise ValueError("qty must be at least 1")

  return sum(item["price"] * item["qty"] for item in items)


def _apply_discounts(amount, is_vip):
  if amount >= DISCOUNT_THRESHOLD:
    amount *= 1 - STANDARD_DISCOUNT_RATE
  if is_vip:
    amount *= 1 - VIP_DISCOUNT_RATE
  return amount


def total(items, is_vip=False, coupon=0):
  amount = _apply_discounts(_subtotal(items), is_vip)
  return int(max(0, amount - coupon))


def summary(items, is_vip=False):
  subtotal = _subtotal(items)
  final_total = int(_apply_discounts(subtotal, is_vip))
  return {
    "subtotal": subtotal,
    "discount": subtotal - final_total,
    "total": final_total,
  }
