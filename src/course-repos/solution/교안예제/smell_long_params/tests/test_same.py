import after_mod
import before_mod


def test_same_behaviour():
    old = before_mod.create_user("Kim", "k@x.io", "010", "Main 1", "Seoul", "04524")
    addr = after_mod.Address("Main 1", "Seoul", "04524")
    assert after_mod.create_user("Kim", "k@x.io", "010", addr) == old
