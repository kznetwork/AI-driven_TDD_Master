def final_price(price, grade):
    if price >= 50000:
        price = price * 90 // 100
    if grade == 2:
        price = price * 95 // 100
    return price
