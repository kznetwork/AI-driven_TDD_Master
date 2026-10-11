import pytest
from shipping import shipping_fee


def test_basic_fee_is_3000():
    """TC-01 · CT-1"""
    assert shipping_fee(10000) == 3000


@pytest.mark.parametrize("amount, expected", [
    (29999, 3000),   # TC-02 기준 바로 아래
    (30000, 0),      # TC-03 기준 정확히: 무료
])
def test_free_shipping_boundary(amount, expected):
    """TC-02·03 · CT-2"""
    assert shipping_fee(amount) == expected


@pytest.mark.parametrize("amount", [0, -1])
def test_non_positive_amount_raises(amount):
    """TC-04·05 · CT-3"""
    with pytest.raises(ValueError):
        shipping_fee(amount)


@pytest.mark.parametrize("amount, expected", [
    (19999, 3000),   # TC-06 GOLD 기준 바로 아래
    (20000, 0),      # TC-07 GOLD 기준 정확히
])
def test_gold_free_shipping_boundary(amount, expected):
    """TC-06·07 · CT-4"""
    assert shipping_fee(amount, grade="GOLD") == expected


def test_normal_member_keeps_30000_rule():
    """TC-08 · CT-5 · 회귀: 일반 회원 기준은 그대로"""
    assert shipping_fee(20000, grade="NORMAL") == 3000
