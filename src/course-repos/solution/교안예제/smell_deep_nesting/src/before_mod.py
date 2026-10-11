def can_ship(order):
    if order is not None:
        if order["paid"]:
            if order["items"]:
                if order["address"]:
                    return True
    return False
