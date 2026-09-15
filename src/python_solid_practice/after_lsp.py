from abc import ABC, abstractmethod


class Bird:
  def eat(self):
    return f"The {type(self).__name__.lower()} is eating."


class Flyable(ABC):
  @abstractmethod
  def fly(self):
    pass


class Sparrow(Bird, Flyable):
  def fly(self):
    return "The sparrow is flying."


class Ostrich(Bird):
  pass


def feed_bird(bird):
  print(bird.eat())


def make_fly(flyable):
  print(flyable.fly())


if __name__ == "__main__":
  sparrow = Sparrow()
  ostrich = Ostrich()

  feed_bird(sparrow)
  feed_bird(ostrich)
  make_fly(sparrow)
