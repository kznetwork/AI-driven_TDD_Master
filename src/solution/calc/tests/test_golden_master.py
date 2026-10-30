"""골든 마스터(특성화 테스트) — add() 의 '지금 동작'을 통째로 고정한다.

골든 파일은 '옳은 답'이 아니라 '현재 답'이다. 사람이 diff 를 읽고 승인한 뒤에만 갱신한다.
    갱신:  UPDATE_GOLDEN=1 pytest tests/test_golden_master.py   (PowerShell: $env:UPDATE_GOLDEN=1)
"""
import json
import os
from pathlib import Path

import pytest

from calculator import add

GOLDEN = Path(__file__).parent / "golden" / "add.golden.json"

INPUTS = [
    "", "   ", "0", "7",
    "1,2", "1;2", "1,2;3", "1,2,3,4", "10,20,30", " 4 , 5 ", "1;2,3;4",
    "-1", "-1,2,-3",
    "a,b", "1,,2", "1,2,",
]


def capture(text):
    try:
        return {"result": add(text)}
    except ValueError:
        return {"error": "ValueError"}


def test_golden_master():
    actual = {text: capture(text) for text in INPUTS}
    if os.environ.get("UPDATE_GOLDEN"):
        GOLDEN.parent.mkdir(exist_ok=True)
        GOLDEN.write_text(json.dumps(actual, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8")
    if not GOLDEN.exists():
        pytest.fail("골든 파일이 없다 — UPDATE_GOLDEN=1 로 만든 뒤 diff 를 읽고 승인한다")
    expected = json.loads(GOLDEN.read_text(encoding="utf-8"))
    assert actual == expected
