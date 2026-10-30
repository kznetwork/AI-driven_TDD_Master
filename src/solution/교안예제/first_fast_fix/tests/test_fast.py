from user_service import greeting


class FakeDB:                          # 메모리 대역 — 연결이 없다
    def get_name(self, user_id):
        return {1: "Hello"}[user_id]


def test_greeting_with_fake_db():
    assert greeting(FakeDB(), 1) == "Hello!"
