def add(numbers: str) -> int:
  if numbers == "":
    return 0
  values = [int(number) for number in numbers.replace(";", ",").split(",")]
  negatives = [str(value) for value in values if value < 0]
  if negatives:
    raise ValueError(f"음수는 허용하지 않습니다: {', '.join(negatives)}")
  return sum(values)
