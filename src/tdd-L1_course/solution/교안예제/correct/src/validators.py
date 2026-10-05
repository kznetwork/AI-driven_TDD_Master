import re
from datetime import date

EMAIL = re.compile(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$")


def is_valid_email(email: str) -> bool:
    return bool(EMAIL.match(email))


def is_in_order(dates: list[date]) -> bool:
    return all(a <= b for a, b in zip(dates, dates[1:]))


def is_valid_age(age: int) -> bool:
    return 0 <= age <= 120


def is_valid_user(user: dict) -> bool:
    return bool(user.get("name")) and bool(user.get("password"))


def is_valid_name_list(names: list[str]) -> bool:
    return 1 <= len(names) <= 100
