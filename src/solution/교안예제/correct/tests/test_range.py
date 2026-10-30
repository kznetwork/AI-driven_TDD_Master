import pytest

from validators import is_valid_age


@pytest.mark.parametrize("age, ok", [
    (-1, False), (0, True),        # 하한 경계 양쪽
    (25, True),                    # 정상값
    (120, True), (121, False),     # 상한 경계 양쪽
])
def test_age_range(age, ok):
    assert is_valid_age(age) is ok
