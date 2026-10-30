"""속성 테스트 — 입력은 hypothesis 가 만들고, 우리는 '항상 참인 성질'만 쓴다 (불변식)."""
from hypothesis import given, strategies as st
from cart import final_total, subtotal

ITEM = st.fixed_dictionaries({"price": st.integers(0, 1_000_000), "qty": st.integers(0, 20)})
BASKET = st.lists(ITEM, max_size=10)


@given(BASKET, st.booleans())
def test_total_is_between_zero_and_subtotal(items, is_vip):      # 0 <= 결제 <= 합계
    assert 0 <= final_total(items, is_vip) <= subtotal(items)


@given(BASKET)
def test_vip_never_pays_more_than_normal(items):                  # VIP <= 일반
    assert final_total(items, True) <= final_total(items, False)
