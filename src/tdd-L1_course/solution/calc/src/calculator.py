import re

DELIMITERS = r"[,;]"


def add(numbers: str) -> int:
    if not numbers.strip():
        return 0
    values = _parse(numbers)
    _reject_negatives(values)
    return sum(values)


def _parse(numbers: str) -> list[int]:
    return [int(n) for n in re.split(DELIMITERS, numbers)]


def _reject_negatives(values: list[int]) -> None:
    negatives = [v for v in values if v < 0]
    if negatives:
        listed = ", ".join(map(str, negatives))
        raise ValueError(f"음수는 허용하지 않습니다: {listed}")
