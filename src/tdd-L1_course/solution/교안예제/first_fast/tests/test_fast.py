from calculator import add
from user_db import UserDB


def test_add_is_fast():               # ✅ 순수 함수 — ms 단위
    assert add(5, 5) == 10


def test_name_with_real_db():         # ❌ 외부 연결 — 매번 1초
    db = UserDB()
    db.connect()
    assert db.get_name(1) == "Hello"
