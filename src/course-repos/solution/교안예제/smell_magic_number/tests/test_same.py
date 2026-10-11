import pytest

import after_mod
import before_mod


@pytest.mark.parametrize('name', ['final_price'])
@pytest.mark.parametrize('args', [(p, g) for p in (49999, 50000) for g in (1, 2)])
def test_same_behaviour(name, args):
    assert getattr(before_mod, name)(*args) == getattr(after_mod, name)(*args)
