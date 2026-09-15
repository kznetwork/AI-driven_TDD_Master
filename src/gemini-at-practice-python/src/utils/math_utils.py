import math


def add(a: float, b: float) -> float:
  return a + b
 
def subtract(a: float, b: float) -> float:
  return a - b
 
def multiply(a: float, b: float) -> float:
  return a * b
 
def divide(a: float, b: float) -> float:
  if b == 0:
    raise ValueError("Cannot divide by zero.")
  return a / b


def power(a: int | float, b: int | float) -> int | float:
  if isinstance(a, bool) or isinstance(b, bool):
    raise TypeError("Boolean arguments are not supported.")
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    raise TypeError("Arguments must be integers or floats.")
  if not math.isfinite(a) or not math.isfinite(b):
    raise ValueError("Arguments must be finite.")
  if a < 0 and not float(b).is_integer():
    raise ValueError("A negative base cannot have a fractional exponent.")

  return a ** b
