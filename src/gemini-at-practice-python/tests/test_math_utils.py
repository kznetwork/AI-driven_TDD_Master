import sys
import unittest

import pytest

from src.utils.math_utils import add, divide, multiply, power, subtract


def test_add_returns_sum_for_positive_numbers() -> None:
  assert add(10, 5) == 15


def test_add_returns_other_operand_when_left_operand_is_zero() -> None:
  assert add(0, 5) == 5


def test_add_returns_negative_sum_for_negative_numbers() -> None:
  assert add(-10, -5) == -15


def test_add_preserves_max_float_when_adding_zero() -> None:
  assert add(sys.float_info.max, 0.0) == sys.float_info.max


def test_subtract_returns_difference_for_positive_numbers() -> None:
  assert subtract(10, 5) == 5


def test_subtract_returns_same_value_when_subtracting_zero() -> None:
  assert subtract(5, 0) == 5


def test_subtract_returns_difference_for_negative_numbers() -> None:
  assert subtract(-10, -5) == -5


def test_subtract_preserves_negative_max_float_when_subtracting_zero() -> None:
  assert subtract(-sys.float_info.max, 0.0) == -sys.float_info.max


def test_multiply_returns_product_for_positive_numbers() -> None:
  assert multiply(10, 5) == 50


def test_multiply_returns_zero_when_left_operand_is_zero() -> None:
  assert multiply(0, -5) == 0


def test_multiply_returns_positive_product_for_negative_numbers() -> None:
  assert multiply(-10, -5) == 50


def test_multiply_preserves_max_float_when_multiplying_by_one() -> None:
  assert multiply(sys.float_info.max, 1.0) == sys.float_info.max


def test_divide_returns_quotient_for_positive_numbers() -> None:
  assert divide(10, 5) == 2.0


def test_divide_returns_zero_when_numerator_is_zero() -> None:
  assert divide(0, 5) == 0.0


def test_divide_returns_negative_quotient_for_negative_numerator() -> None:
  assert divide(-10, 5) == -2.0


def test_divide_returns_negative_quotient_for_negative_denominator() -> None:
  assert divide(10, -5) == -2.0


def test_divide_returns_one_for_equal_max_float_operands() -> None:
  assert divide(sys.float_info.max, sys.float_info.max) == 1.0


def test_divide_raises_value_error_for_integer_zero_denominator() -> None:
  with pytest.raises(ValueError, match=r"^Cannot divide by zero\.$"):
    divide(10, 0)


def test_divide_raises_value_error_for_float_zero_denominator() -> None:
  with pytest.raises(ValueError, match=r"^Cannot divide by zero\.$"):
    divide(10, 0.0)


def test_divide_raises_value_error_for_negative_zero_denominator() -> None:
  with pytest.raises(ValueError, match=r"^Cannot divide by zero\.$"):
    divide(10, -0.0)


class PowerTests(unittest.TestCase):
  def test_positive_integer_exponent(self) -> None:
    self.assertEqual(power(2, 3), 8)

  def test_negative_base_with_odd_exponent(self) -> None:
    self.assertEqual(power(-2, 3), -8)

  def test_fractional_exponent(self) -> None:
    self.assertAlmostEqual(power(9, 0.5), 3.0)

  def test_negative_exponent(self) -> None:
    self.assertAlmostEqual(power(2, -3), 0.125)

  def test_zero_exponent(self) -> None:
    self.assertEqual(power(7, 0), 1)

  def test_zero_to_zero_power(self) -> None:
    self.assertEqual(power(0, 0), 1)

  def test_zero_base_with_positive_exponent(self) -> None:
    self.assertEqual(power(0, 5), 0)

  def test_zero_base_with_negative_exponent_raises_error(self) -> None:
    with self.assertRaises(ZeroDivisionError):
      power(0, -1)

  def test_large_exponent(self) -> None:
    self.assertEqual(power(2, 100), 1267650600228229401496703205376)


if __name__ == "__main__":
  unittest.main()
