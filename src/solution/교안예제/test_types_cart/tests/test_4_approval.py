"""승인(골든 마스터) 테스트 — 출력 전체를 파일로 고정한다. 처음 실행은 FAIL, 사람이 읽고 승인해야 완성된다."""
from approvaltests import verify
from cart import final_total

BASKETS = {
    "empty": [],
    "just_below": [{"price": 49999, "qty": 1}],
    "exactly_50000": [{"price": 25000, "qty": 2}],
    "sample_60000": [{"price": 12000, "qty": 3}, {"price": 24000, "qty": 1}],
}


def render():
    lines = []
    for name, items in BASKETS.items():
        for vip in (False, True):
            lines.append(f"{name:14s} vip={vip!s:5s} -> {final_total(items, vip)}")
    return "\n".join(lines)


def test_final_total_table():
    verify(render())
