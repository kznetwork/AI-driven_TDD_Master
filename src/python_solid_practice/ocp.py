from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
  @abstractmethod
  def calculate_area(self):
    pass


class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def calculate_area(self):
    return self.width * self.height


class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def calculate_area(self):
    return pi * self.radius ** 2


class Triangle(Shape):
  def __init__(self, base, height):
    self.base = base
    self.height = height

  def calculate_area(self):
    return self.base * self.height / 2


def total_area(shapes):
  return sum(shape.calculate_area() for shape in shapes)


if __name__ == "__main__":
  shapes = [
    Rectangle(width=4, height=5),
    Circle(radius=3),
    Triangle(base=6, height=4),
  ]

  for shape in shapes:
    print(f"{type(shape).__name__}: {shape.calculate_area():.2f}")

  print(f"Total: {total_area(shapes):.2f}")
