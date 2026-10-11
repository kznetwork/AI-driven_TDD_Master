import pytest

from validators import is_valid_email


@pytest.mark.parametrize("email, ok", [
    ("test@example.com", True),
    ("a.b+tag@mail.co.kr", True),
    ("invalid-email", False),
    ("no-domain@", False),
])
def test_email_format(email, ok):
    assert is_valid_email(email) is ok
