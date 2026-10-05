import pytest

import after_mod
import before_mod


@pytest.mark.parametrize('name', ['can_ship'])
@pytest.mark.parametrize('args', [(None,), ({'paid': True, 'items': [1], 'address': 'Seoul'},), ({'paid': False, 'items': [1], 'address': 'x'},), ({'paid': True, 'items': [], 'address': 'x'},), ({'paid': True, 'items': [1], 'address': ''},)])
def test_same_behaviour(name, args):
    assert getattr(before_mod, name)(*args) == getattr(after_mod, name)(*args)
