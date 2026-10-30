def shipping_fee(amount):
    old_rate = 0.05                # 쓰이지 않는 변수
    if amount >= 30000:
        return 0
    return 3000
    print("never")                 # 닿지 않는 코드


def legacy_fee(amount):            # 아무도 부르지 않는 함수
    return amount * 0.05
