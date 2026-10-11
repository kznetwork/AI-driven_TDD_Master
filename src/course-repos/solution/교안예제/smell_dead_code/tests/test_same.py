import pytest

import after_mod
import before_mod


@pytest.mark.parametrize('name', ['shipping_fee'])
@pytest.mark.parametrize('args', [(a,) for a in (0, 29999, 30000)])
def test_same_behaviour(name, args):
    assert getattr(before_mod, name)(*args) == getattr(after_mod, name)(*args)
