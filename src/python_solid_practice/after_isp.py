from abc import ABC, abstractmethod


class Bird(ABC):
  @abstractmethod
  def sing(self):
    pass

  @abstractmethod
  def eat(self):
    pass


class FlyableBird(ABC):
  @abstractmethod
  def fly(self):
    pass


class Penguin(Bird):
  def sing(self):
    return "The penguin is singing."

  def eat(self):
    return "The penguin is eating."


class Eagle(Bird, FlyableBird):
  def sing(self):
    return "The eagle is singing."

  def eat(self):
    return "The eagle is eating."

  def fly(self):
    return "The eagle is flying."


def care_for_bird(bird):
  print(bird.sing())
  print(bird.eat())


def release_flying_bird(bird):
  print(bird.fly())


if __name__ == "__main__":
  penguin = Penguin()
  eagle = Eagle()

  care_for_bird(penguin)
  care_for_bird(eagle)
  release_flying_bird(eagle)
