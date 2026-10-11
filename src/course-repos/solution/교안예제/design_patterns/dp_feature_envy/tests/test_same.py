import after_mod
import before_mod


def test_same_customer_info():
    b = before_mod.Customer("Kim", before_mod.Address("테헤란로 1", "서울", "06236"))
    a = after_mod.Customer("Kim", after_mod.Address("테헤란로 1", "서울", "06236"))
    assert after_mod.Invoice().customer_info(a) == before_mod.Invoice().customer_info(b) == "테헤란로 1, 서울 06236"
