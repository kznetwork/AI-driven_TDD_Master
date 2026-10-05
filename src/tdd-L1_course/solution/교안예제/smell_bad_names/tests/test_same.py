import after_mod
import before_mod


def test_same_behaviour():
    lines = [(1000, 2), (500, 3)]
    assert before_mod.calc(lines, 0.1) == after_mod.total_after_tax(lines, 0.1)
