import json
from pathlib import Path

from src.utils.math_utils import power


SNAPSHOT_PATH = Path(__file__).parent / "snapshots" / "power_results.json"
CASES = [
  ("positive_integer_exponent", 2, 3),
  ("negative_base_odd_exponent", -2, 3),
  ("negative_base_even_exponent", -2, 4),
  ("fractional_exponent", 9, 0.5),
  ("negative_exponent", 2, -3),
  ("negative_even_exponent", -2, -2),
  ("fractional_base", 1.5, 2),
  ("zero_exponent", 7, 0),
  ("zero_to_zero", 0, 0),
  ("zero_base_positive_exponent", 0, 5),
  ("large_integer_result", 2, 100),
  ("zero_base_negative_exponent", 0, -1),
  ("negative_base_fractional_exponent", -4, 0.5),
  ("non_finite_base", float("inf"), 2),
  ("boolean_base", True, 2),
]


def encode_scalar(value: object) -> dict[str, str]:
  if isinstance(value, bool):
    return {"type": "bool", "value": str(value).lower()}
  if isinstance(value, int):
    return {"type": "int", "value": str(value)}
  if isinstance(value, float):
    return {"type": "float", "value": value.hex()}
  raise TypeError(f"Unsupported snapshot value: {type(value).__name__}")


def capture_case(case_id: str, a: object, b: object) -> dict[str, object]:
  record = {
    "id": case_id,
    "input": {"a": encode_scalar(a), "b": encode_scalar(b)},
  }

  try:
    result = power(a, b)
  except Exception as error:
    record["outcome"] = {
      "kind": "exception",
      "type": type(error).__name__,
    }
  else:
    record["outcome"] = {
      "kind": "return",
      "result": encode_scalar(result),
    }

  return record


def test_power_matches_golden_master() -> None:
  expected = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
  actual = {
    "schema_version": 1,
    "cases": [capture_case(case_id, a, b) for case_id, a, b in CASES],
  }

  assert actual == expected
