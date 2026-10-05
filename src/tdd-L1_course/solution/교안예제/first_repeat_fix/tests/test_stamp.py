from stamp import now_ms


def fixed_clock():
    return 1_700_000_000.0


def test_now_ms_with_fixed_clock():
    assert now_ms(fixed_clock) == 1_700_000_000_000
