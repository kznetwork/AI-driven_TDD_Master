from abc import ABC, abstractmethod


class Bird(ABC):
  @abstractmethod
  def sing(self):
    pass

  @abstractmethod
  def eat(self):
    pass

  @abstractmethod
  def fly(self):
    pass


class Penguin(Bird):
  def sing(self):
    return "The penguin is singing."

  def eat(self):
    return "The penguin is eating."

  def fly(self):
    raise NotImplementedError("Penguins cannot fly.")


class Eagle(Bird):
  def sing(self):
    return "The eagle is singing."

  def eat(self):
    return "The eagle is eating."

  def fly(self):
    return "The eagle is flying."


if __name__ == "__main__":
  penguin = Penguin()

  print(penguin.sing())
  print(penguin.eat())

  try:
    print(penguin.fly())
  except NotImplementedError as error:
    print(f"ISP violation: {error}")
