import after_mod
import before_mod


def test_same_total():
    b = [before_mod.Book(100, "1234"), before_mod.Fruit("Banana", 10, 2)]
    a = [after_mod.Book(100, "1234"), after_mod.Fruit("Banana", 10, 2)]
    assert after_mod.total_cost(a) == before_mod.total_cost(b) == 120


def test_new_operation_without_touching_elements():
    items = [after_mod.Book(100, "1234"), after_mod.Fruit("Banana", 10, 2)]
    labels = [item.accept(after_mod.LabelVisitor()) for item in items]
    assert labels == ["Book ISBN: 1234", "Fruit: Banana"]
