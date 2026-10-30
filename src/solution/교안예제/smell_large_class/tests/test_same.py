from after_mod import Order, OrderCsv, OrderMail
import before_mod


def test_same_behaviour():
    items = [(1000, 2), (500, 3)]
    old, new = before_mod.Order(items), Order(items)
    assert old.total() == new.total() == 3500
    assert old.to_csv() == OrderCsv.render(new)
    assert old.email_body() == OrderMail.body(new)
