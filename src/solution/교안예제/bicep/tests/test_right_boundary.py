import sys

from calculator import add


def test_right_result():                         # R: 결과가 맞는가
    assert add(5, 5) == 10


def test_boundary_large_int():                   # B: 경계 — 아주 큰 수
    big = sys.maxsize
    assert add(big, 1) == big + 1                # Python int 는 넘치지 않는다


def test_boundary_float():                       # B: 경계 — 실수 오차
    assert add(0.1, 0.2) != 0.3
    assert abs(add(0.1, 0.2) - 0.3) < 1e-9
