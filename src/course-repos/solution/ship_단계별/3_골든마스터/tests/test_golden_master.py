"""골든 마스터 — 리팩터링 전에 shipping_fee() 의 '지금 동작'을 통째로 고정한다.

등급 2종 × 금액 10종 = 20개 조합. 골든 파일은 사람이 읽고 승인한 뒤에만 갱신한다.
    갱신:  UPDATE_GOLDEN=1 pytest tests/test_golden_master.py   (PowerShell: $env:UPDATE_GOLDEN=1)
"""
import json
import os
from pathlib import Path

import pytest

from shipping import shipping_fee

GOLDEN = Path(__file__).parent / "golden" / "shipping.golden.json"

GRADES = ["NORMAL", "GOLD"]
AMOUNTS = [-1, 0, 1, 10000, 19999, 20000, 29999, 30000, 30001, 100000]


def capture(amount, grade):
    try:
        return {"fee": shipping_fee(amount, grade=grade)}
    except ValueError:
        return {"error": "ValueError"}


def test_golden_master():
    """TC-09 · INV-1 · 모든 등급 × 금액 조합의 결과가 리팩터링 전후 같다"""
    actual = {f"{grade}/{amount}": capture(amount, grade) for grade in GRADES for amount in AMOUNTS}
    if os.environ.get("UPDATE_GOLDEN"):
        GOLDEN.parent.mkdir(exist_ok=True)
        GOLDEN.write_text(json.dumps(actual, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8")
    if not GOLDEN.exists():
        pytest.fail("골든 파일이 없다 — UPDATE_GOLDEN=1 로 만든 뒤 diff 를 읽고 승인한다")
    assert actual == json.loads(GOLDEN.read_text(encoding="utf-8"))
