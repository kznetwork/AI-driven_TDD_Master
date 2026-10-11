"""속성 테스트(Property-based) — 예제 하나가 아니라 '모든 입력'에서 성립하는 성질을 검증한다."""
import pytest
from hypothesis import given, strategies as st

from calculator import add

DELIMS = st.sampled_from([",", ";"])
NUMBERS = st.lists(st.integers(min_value=0, max_value=10**6), min_size=1, max_size=20)


@given(NUMBERS, st.data())
def test_sum_matches_for_any_delimiters(numbers, data):       # P1 합계 성질
    delims = [data.draw(DELIMS) for _ in numbers[1:]]
    text = str(numbers[0]) + "".join(d + str(n) for d, n in zip(delims, numbers[1:]))
    assert add(text) == sum(numbers)


@given(st.text(alphabet=" \t\n", max_size=10))
def test_blank_text_is_zero(text):                            # P2 공백만 → 0
    assert add(text) == 0


@given(NUMBERS, st.integers(min_value=1, max_value=10**6))
def test_any_negative_number_raises(numbers, negative):       # P3 음수가 하나라도 있으면 오류
    text = ",".join(map(str, numbers + [-negative]))
    with pytest.raises(ValueError):
        add(text)


@given(NUMBERS, st.randoms())
def test_order_does_not_matter(numbers, rnd):                 # P4 순서 무관
    shuffled = numbers[:]
    rnd.shuffle(shuffled)
    assert add(",".join(map(str, numbers))) == add(",".join(map(str, shuffled)))
