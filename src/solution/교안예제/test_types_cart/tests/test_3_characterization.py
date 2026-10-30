"""특성화 테스트 — 명세에 없는 입력에서 '지금 코드가 하는 일'을 그대로 기록한다. 옳은지는 묻지 않는다.

기대값은 요구사항이 아니라 코드를 실행해서 얻은 값이다. 실패하면 동작이 바뀐 것이다.
"""
import pytest
from cart import final_total


def test_float_price_returns_float():                  # 사양에 소수 가격이 없다 — 현재는 float 로 돌려준다
    assert final_total([{"price": 50000.5, "qty": 1}]) == 45000.0


def test_vip_below_threshold_gets_only_vip_discount():  # 40,000 · VIP → 38,000
    assert final_total([{"price": 40000, "qty": 1}], is_vip=True) == 38000


def test_missing_qty_raises_key_error():                # 오류 종류가 ValueError 가 아니라 KeyError 다
    with pytest.raises(KeyError):
        final_total([{"price": 1000}])
