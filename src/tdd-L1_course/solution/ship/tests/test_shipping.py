import pytest
from shipping import shipping_fee


def test_basic_fee_is_3000():
    assert shipping_fee(10000) == 3000


@pytest.mark.parametrize("amount, expected", [
    (29999, 3000),   # 기준 바로 아래
    (30000, 0),      # 기준 정확히: 무료
])
def test_free_shipping_boundary(amount, expected):
    assert shipping_fee(amount) == expected


@pytest.mark.parametrize("amount", [0, -1])
def test_non_positive_amount_raises(amount):
    with pytest.raises(ValueError):
        shipping_fee(amount)


@pytest.mark.parametrize("amount, expected", [
    (19999, 3000),
    (20000, 0),
])
def test_gold_free_shipping_boundary(amount, expected):
    assert shipping_fee(amount, grade="GOLD") == expected


def test_normal_member_keeps_30000_rule():
    assert shipping_fee(20000, grade="NORMAL") == 3000
