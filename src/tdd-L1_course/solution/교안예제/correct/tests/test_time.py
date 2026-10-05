from api import timed_call


def test_response_time_with_fake_clock():
    ticks = iter([10.000, 10.250])     # 가짜 시계: 250ms 경과
    ms = timed_call(lambda: None, clock=lambda: next(ticks))
    assert ms == 250


def test_response_under_one_second():
    ms = timed_call(lambda: None)      # 진짜 시계 — 상한만 느슨하게
    assert ms < 1000
