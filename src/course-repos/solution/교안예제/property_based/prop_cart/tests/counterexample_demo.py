"""틀린 가정을 xfail 없이 돌려 hypothesis 가 찾아 주는 반례(falsifying example)를 눈으로 본다.

    python -m pytest tests/counterexample_demo.py -q
"""
from hypothesis import given, strategies as st

from cart import apply_threshold_discount

AMOUNT = st.integers(min_value=40_000, max_value=60_000)      # 경계(50,000) 근처로 좁힌 생성 범위


@given(AMOUNT, AMOUNT)
def test_larger_subtotal_never_pays_less(a, b):
    low, high = sorted((a, b))
    assert apply_threshold_discount(low) <= apply_threshold_discount(high)
