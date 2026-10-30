"""장바구니 불변식(C6)을 무작위 입력으로 — 그리고 '틀린 가정'을 반례로 잡는다."""
import pytest
from hypothesis import given, settings, strategies as st

from cart import apply_threshold_discount, final_total, subtotal

ITEM = st.fixed_dictionaries({"price": st.integers(0, 1_000_000), "qty": st.integers(0, 20)})
BASKET = st.lists(ITEM, max_size=10)


@given(BASKET, st.booleans())
def test_total_between_zero_and_subtotal(items, is_vip):      # C6 불변식
    assert 0 <= final_total(items, is_vip) <= subtotal(items)


@given(BASKET)
def test_vip_never_pays_more_than_regular(items):             # VIP 는 일반보다 더 내지 않는다
    assert final_total(items, True) <= final_total(items, False)


AMOUNT = st.integers(min_value=40_000, max_value=60_000)      # 경계(50,000) 근처로 좁힌 생성 범위


@given(AMOUNT, AMOUNT)
@pytest.mark.xfail(strict=True, reason="틀린 가정 — 문턱을 넘으면 오히려 싸진다 (사양: C3)")
def test_larger_subtotal_never_pays_less(a, b):               # '더 사면 더 낸다' — 이 가정은 거짓
    low, high = sorted((a, b))
    assert apply_threshold_discount(low) <= apply_threshold_discount(high)
