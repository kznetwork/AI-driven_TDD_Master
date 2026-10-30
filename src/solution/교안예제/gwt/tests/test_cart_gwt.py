"""Given-When-Then 스타일 pytest — 같은 시나리오를 .feature 와 1:1 로 대응시킨다."""
import pytest

from cart import final_total


def test_given_vip_over_threshold_when_checkout_then_both_discounts():
    # Given — 합계 60,000원 장바구니 + VIP 고객
    items = [{"price": 12000, "qty": 3}, {"price": 24000, "qty": 1}]
    is_vip = True
    # When — 결제 금액을 계산하면
    total = final_total(items, is_vip)
    # Then — 문턱 10% 뒤 VIP 5% 가 차례로 적용된다 (60,000 → 54,000 → 51,300)
    assert total == 51300


@pytest.mark.parametrize("subtotal, expected", [      # Examples
    (49999, 49999),
    (50000, 45000),
    (50001, 45000),
])
def test_given_regular_when_checkout_then_boundary_discount(subtotal, expected):
    items = [{"price": subtotal, "qty": 1}]           # Given
    total = final_total(items)                        # When
    assert total == expected                          # Then


# 단계를 함수로 뽑으면 .feature 문장과 더 닮는다
def given_basket(*prices):
    return [{"price": p, "qty": 1} for p in prices]


def when_checkout(items, vip=False):
    return final_total(items, vip)


def then_total_is(actual, expected):
    assert actual == expected


def test_empty_basket_costs_zero():
    basket = given_basket()
    total = when_checkout(basket)
    then_total_is(total, 0)
