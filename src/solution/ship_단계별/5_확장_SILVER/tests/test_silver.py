import pytest
from shipping import shipping_fee


@pytest.mark.parametrize("amount, expected", [
    (24999, 3000),
    (25000, 0),
])
def test_silver_free_shipping_boundary(amount, expected):
    assert shipping_fee(amount, grade="SILVER") == expected
