def total_after_tax(order_lines, tax_rate):
    subtotal = sum(price * qty for price, qty in order_lines)
    return subtotal * (1 - tax_rate)
