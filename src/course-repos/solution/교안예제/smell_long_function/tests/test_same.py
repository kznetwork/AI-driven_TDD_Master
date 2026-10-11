import pytest

import after_mod
import before_mod


@pytest.mark.parametrize('name', ['checkout'])
@pytest.mark.parametrize('args', [([{'price': 30000, 'qty': 2}], v) for v in (True, False)] + [([{'price': 100, 'qty': 1}], False)])
def test_same_behaviour(name, args):
    assert getattr(before_mod, name)(*args) == getattr(after_mod, name)(*args)
