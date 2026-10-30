def shipping_fee(order_amount):
    """배송비를 돌려준다.

    계약 (docs/계약표.md)
      CT-1  0 < order_amount < 30,000  -> 3,000
      CT-2  order_amount >= 30,000     -> 0 (무료)
      CT-3  order_amount <= 0          -> ValueError
    """
    raise NotImplementedError
