import pytest

import after_mod
import before_mod


@pytest.mark.parametrize('name', ['vip_price', 'normal_price'])
@pytest.mark.parametrize('args', [(p,) for p in (0, 49999, 50000, 60000)])
def test_same_behaviour(name, args):
    assert getattr(before_mod, name)(*args) == getattr(after_mod, name)(*args)
