import itertools

import pytest

from calc import add


def test_example():                          # Example — 특정 입력 하나
    assert add(2, 3) == 5


VALUES = [-7, 0, 1, 2.5, 10**6]


@pytest.mark.parametrize("a, b", list(itertools.product(VALUES, VALUES)))
def test_commutative(a, b):                  # Property — 허용된 모든 a, b
    assert add(a, b) == add(b, a)


@pytest.mark.parametrize("x", VALUES)
def test_zero_is_identity(x):                # Property — 항등원
    assert add(x, 0) == x
