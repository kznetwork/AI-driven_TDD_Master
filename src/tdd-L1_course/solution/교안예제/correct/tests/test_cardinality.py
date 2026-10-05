import pytest

from validators import is_valid_name_list


@pytest.mark.parametrize("count, ok", [
    (0, False), (1, True),          # 0 · 1 · 다수
    (2, True),
    (100, True), (101, False),      # 최대 경계 양쪽
])
def test_name_list_size(count, ok):
    assert is_valid_name_list(["x"] * count) is ok
