import pytest

from counter import Counter


@pytest.fixture
def counter():                         # ✅ 테스트마다 새 객체
    return Counter()


def test_increment(counter):
    counter.increment()
    assert counter.value == 1


def test_decrement(counter):
    counter.decrement()
    assert counter.value == -1
