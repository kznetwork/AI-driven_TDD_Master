import pytest

from calc import add, divide


def test_add():
    assert add(2, 3) == 5


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
