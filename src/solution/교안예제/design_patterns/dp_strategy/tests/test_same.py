import pytest

import after_mod
import before_mod


@pytest.mark.parametrize("kind", ["percent", "fixed", "vip"])
@pytest.mark.parametrize("price", [1000, 5000, 20000])
def test_same_result(kind, price):
    assert after_mod.apply_discount(price, kind) == before_mod.apply_discount(price, kind)


def test_strategy_can_be_swapped_at_runtime():
    order = after_mod.Order(10000, after_mod.PercentageDiscount())
    assert order.total() == 9000
    order.strategy = after_mod.FixedDiscount()
    assert order.total() == 9000
    order.strategy = after_mod.VipDiscount()
    assert order.total() == 8500
