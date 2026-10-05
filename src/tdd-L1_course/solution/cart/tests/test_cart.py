import pytest
from cart import subtotal, apply_threshold_discount, final_total

def test_empty_cart_subtotal_is_zero():
    assert subtotal([]) == 0


def test_subtotal_sums_price_times_qty():
    items = [{"price": 12000, "qty": 3},
             {"price": 24000, "qty": 1}]
    assert subtotal(items) == 60000


@pytest.mark.parametrize("amount, expected", [
    (49999, 49999),   # 문턱 바로 아래: 할인 없음
    (50000, 45000),   # 문턱 정확히: 10% 할인
    (50001, 45000),   # 문턱 바로 위: 10% 할인 (원 단위 버림)
])
def test_threshold_discount_boundary(amount, expected):
    assert apply_threshold_discount(amount) == expected


def test_vip_gets_extra_5_percent_after_threshold():
    items = [{"price": 12000, "qty": 3},
             {"price": 24000, "qty": 1}]         # 합계 60,000
    # 60,000 → 54,000(문턱 10%) → 51,300(VIP 5%)
    assert final_total(items, is_vip=True) == 51300


def test_non_vip_gets_threshold_discount_only():
    items = [{"price": 25000, "qty": 2}]               # 50,000
    assert final_total(items) == 45000


SAMPLES = [
    [],
    [{"price": 1000, "qty": 1}],
    [{"price": 49999, "qty": 1}],
    [{"price": 25000, "qty": 2}],
    [{"price": 99000, "qty": 3}],
]


@pytest.mark.parametrize("items", SAMPLES)
@pytest.mark.parametrize("is_vip", [False, True])
def test_final_total_is_between_zero_and_subtotal(items, is_vip):
    total = final_total(items, is_vip)
    assert 0 <= total <= subtotal(items)


def test_negative_price_is_rejected():
    with pytest.raises(ValueError):
        subtotal([{"price": -1000, "qty": 1}])
