import pytest

import after_mod
import before_mod

CASES = [
    [],
    [("마우스", 500, 1)],
    [("노트북", 1200, 1), ("마우스", 50, 2)],
    [("키보드", 1000, 1)],
    [("키보드", 1001, 1)],
]


@pytest.mark.parametrize("items", CASES)
def test_same_total(items):
    assert after_mod.Order(items).calculate_total_price() == before_mod.Order(items).calculate_total_price()


def test_example_total():
    assert after_mod.Order([("노트북", 1200, 1), ("마우스", 50, 2)]).calculate_total_price() == 1170
