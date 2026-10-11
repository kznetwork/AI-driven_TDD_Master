counter = 0                            # ❌ 모듈 전역 — 테스트끼리 공유


def test_increment():
    global counter
    counter += 1
    assert counter == 1


def test_decrement():
    global counter
    counter -= 1
    assert counter == -1               # 혼자 돌리면 통과, 같이 돌리면 실패
