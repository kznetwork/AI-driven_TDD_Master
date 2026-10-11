def can_ship(order):
    if order is None:
        return False
    if not order["paid"]:
        return False
    if not order["items"]:
        return False
    return bool(order["address"])
