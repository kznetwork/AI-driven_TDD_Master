from stamp import now_ms


def test_now_ms():                     # ❌ 실행할 때마다 값이 다르다
    assert now_ms() == 1_700_000_000_000
