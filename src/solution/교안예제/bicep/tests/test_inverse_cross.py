import pytest

from calculator import add, subtract


def test_inverse():                              # I: 역관계로 확인
    result = add(5, 5)
    assert subtract(result, 5) == 5


@pytest.mark.parametrize("a, b", [(2, 3), (-1, 7), (0, 9)])
def test_cross_check(a, b):                      # C: 다른 방법과 비교
    assert add(a, b) == add(b, a) == sum([a, b])
