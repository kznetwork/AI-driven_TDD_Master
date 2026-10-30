import pytest
from shipping import shipping_fee

# 테스트 플랜: docs/테스트플랜.md — 본문은 TODO. 하나씩 채우며 RED → GREEN.


def test_basic_fee_is_3000():
    """TC-01 · CT-1 · 기본 배송비 3,000원"""
    pytest.skip("TODO TC-01")


@pytest.mark.parametrize("amount, expected", [
    (29999, 3000),   # TC-02 기준 바로 아래
    (30000, 0),      # TC-03 기준 정확히
])
def test_free_shipping_boundary(amount, expected):
    """TC-02·03 · CT-2 · 무료 배송 경계는 짝으로"""
    pytest.skip("TODO TC-02, TC-03")


@pytest.mark.parametrize("amount", [0, -1])
def test_non_positive_amount_raises(amount):
    """TC-04·05 · CT-3 · 0 이하는 ValueError"""
    pytest.skip("TODO TC-04, TC-05")
