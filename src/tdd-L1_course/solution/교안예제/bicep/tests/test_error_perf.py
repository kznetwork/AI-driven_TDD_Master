import time

import pytest

from calculator import divide, factorial


def test_error_divide_by_zero():                 # E: 오류 조건
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(10, 0)


def test_performance_factorial():                # P: 성능 한계
    start = time.perf_counter()
    factorial(10_000)
    elapsed = time.perf_counter() - start
    assert elapsed < 0.5                         # 0.5초 안에 끝나야 한다
