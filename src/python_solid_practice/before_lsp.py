class Bird:
  def eat(self):
    return "The bird is eating."

  def fly(self):
    return "The bird is flying."


class Sparrow(Bird):
  def fly(self):
    return "The sparrow is flying."


class Ostrich(Bird):
  def fly(self):
    raise RuntimeError("Ostriches cannot fly.")


def make_bird_fly(bird):
  print(bird.fly())


if __name__ == "__main__":
  make_bird_fly(Sparrow())

  try:
    make_bird_fly(Ostrich())
  except RuntimeError as error:
    print(f"LSP violation: {error}")
