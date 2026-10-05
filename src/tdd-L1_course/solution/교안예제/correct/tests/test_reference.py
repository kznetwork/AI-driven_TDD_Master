from user_repo import UserRepository


def test_existing_user_is_found():
    repo = UserRepository({1: "Alice"})
    assert repo.find_by_id(1) == "Alice"


def test_missing_user_is_none():
    repo = UserRepository({1: "Alice"})
    assert repo.find_by_id(9999) is None
