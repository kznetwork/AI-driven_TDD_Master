import pytest
from calculator import add


def test_empty_string_returns_zero():
    assert add("") == 0


def test_single_number_returns_itself():
    assert add("7") == 7


def test_two_numbers_separated_by_comma():
    assert add("1,2") == 3


def test_many_numbers():
    assert add("1,2,3,4") == 10


def test_semicolon_is_also_a_delimiter():
    assert add("1;2") == 3


def test_mixed_delimiters():
    assert add("1,2;3") == 6


def test_negative_numbers_raise_error():
    message = "음수는 허용하지 않습니다: -1, -3"
    with pytest.raises(ValueError, match=message):
        add("-1,2,-3")


# def test_whitespace_only_returns_zero():
#     assert add("   ") == 0
