"""파라미터 테스트 — 같은 규칙(문턱 할인)을 입력만 바꿔 한 함수로 쓴다. 기대값은 예시 표(C3 · C4)에서 온다."""
import pytest
from cart import final_total


@pytest.mark.parametrize("price, qty, is_vip, expected", [
    (49999, 1, False, 49999),    # C3 문턱 바로 아래: 할인 없음
    (50000, 1, False, 45000),    # C3 문턱 정확히: 10% 할인
    (50001, 1, False, 45000),    # C3 + C5 원 미만 버림
    (60000, 1, True, 51300),     # C4 60,000 → 54,000 → 51,300
])
def test_final_total_examples(price, qty, is_vip, expected):
    assert final_total([{"price": price, "qty": qty}], is_vip) == expected
