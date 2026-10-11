import pytest

import after_mod
import before_mod


@pytest.mark.parametrize("is_vip", [True, False])
@pytest.mark.parametrize("price", [0, 100, 12345])
def test_function_refactoring_same(price, is_vip):
    assert after_mod.calculate_discount(price, is_vip) == before_mod.calculate_discount(price, is_vip)


@pytest.mark.parametrize("is_vip", [True, False])
def test_restructuring_same(is_vip):
    b = before_mod.Order(10000, is_vip).discounted_price()
    a = after_mod.Order(10000, after_mod.Customer(is_vip)).discounted_price()
    assert a == b
