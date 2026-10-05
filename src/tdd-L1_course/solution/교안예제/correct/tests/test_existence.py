import pytest

from validators import is_valid_user


@pytest.mark.parametrize("user, ok", [
    ({"name": "Alice", "password": "pw123"}, True),
    ({"name": None, "password": "pw123"}, False),   # 값이 None
    ({"name": "", "password": "pw123"}, False),     # 빈 문자열
    ({"password": "pw123"}, False),                 # 키가 없음
])
def test_required_fields(user, ok):
    assert is_valid_user(user) is ok
