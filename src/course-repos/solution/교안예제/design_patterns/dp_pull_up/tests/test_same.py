import after_mod
import before_mod


def test_developer_same_details():
    assert (after_mod.Developer("Kim", "Python").get_details()
            == before_mod.Developer("Kim", "Python").get_details()
            == "Kim (Developer, Language: Python)")


def test_manager_same_details():
    assert (after_mod.Manager("Lee", 5).get_details()
            == before_mod.Manager("Lee", 5).get_details()
            == "Lee (Manager, Team Size: 5)")
