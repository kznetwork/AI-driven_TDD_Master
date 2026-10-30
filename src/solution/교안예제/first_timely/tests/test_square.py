import pytest

from mathx import square


@pytest.mark.parametrize("x, expected", [(5, 25), (0, 0), (-3, 9)])
def test_square(x, expected):          # 구현보다 먼저 쓴다
    assert square(x) == expected
