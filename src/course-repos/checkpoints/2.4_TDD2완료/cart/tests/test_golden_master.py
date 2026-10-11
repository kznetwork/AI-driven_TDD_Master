"""골든 마스터 — 리팩터링 전에 final_total() 의 '지금 동작'을 통째로 고정한다.

장바구니 9종 × 일반/VIP = 18개 조합의 결과를 골든 파일에 저장해 두고, 리팩터링 뒤에도 똑같은지 비교한다.
골든 파일은 사람이 읽고 승인한 뒤에만 갱신한다.
    갱신:  UPDATE_GOLDEN=1 pytest tests/test_golden_master.py   (PowerShell: $env:UPDATE_GOLDEN=1)
"""
import json
import os
from pathlib import Path

import pytest

from cart import final_total

GOLDEN = Path(__file__).parent / "golden" / "cart.golden.json"

BASKETS = {
    "empty": [],
    "cheap": [{"price": 1000, "qty": 1}],
    "just_below": [{"price": 49999, "qty": 1}],
    "exactly_50000": [{"price": 25000, "qty": 2}],
    "just_above": [{"price": 50001, "qty": 1}],
    "sample_60000": [{"price": 12000, "qty": 3}, {"price": 24000, "qty": 1}],
    "large": [{"price": 99000, "qty": 3}],
    "zero_qty": [{"price": 10000, "qty": 0}],
    "negative_price": [{"price": -1000, "qty": 1}],
}


def capture(items, is_vip):
    try:
        return {"total": final_total(items, is_vip)}
    except ValueError:
        return {"error": "ValueError"}


def test_golden_master():
    actual = {f"{name}/{'vip' if vip else 'normal'}": capture(items, vip)
              for name, items in BASKETS.items() for vip in (False, True)}
    if os.environ.get("UPDATE_GOLDEN"):
        GOLDEN.parent.mkdir(exist_ok=True)
        GOLDEN.write_text(json.dumps(actual, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8")
    if not GOLDEN.exists():
        pytest.fail("골든 파일이 없다 — UPDATE_GOLDEN=1 로 만든 뒤 diff 를 읽고 승인한다")
    assert actual == json.loads(GOLDEN.read_text(encoding="utf-8"))
