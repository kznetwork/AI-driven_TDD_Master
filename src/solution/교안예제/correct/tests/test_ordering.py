from datetime import date

from validators import is_in_order


def test_dates_in_order():
    assert is_in_order([date(2024, 1, 1), date(2024, 12, 31)])


def test_dates_out_of_order():
    assert not is_in_order([date(2024, 12, 31), date(2024, 1, 1)])


def test_sorted_keeps_order():
    dates = [date(2024, 5, 1), date(2024, 1, 1), date(2024, 3, 1)]
    assert is_in_order(sorted(dates))
