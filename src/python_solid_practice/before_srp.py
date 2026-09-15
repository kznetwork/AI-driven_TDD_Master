class Guitar:
  def __init__(
    self,
    serial_number,
    price,
    builder,
    model,
    guitar_type,
    back_wood,
    top_wood,
  ):
    self.serial_number = serial_number
    self.price = price
    self.builder = builder
    self.model = model
    self.guitar_type = guitar_type
    self.back_wood = back_wood
    self.top_wood = top_wood

  def matches(self, builder, model, guitar_type, back_wood, top_wood):
    return (
      self.builder == builder
      and self.model == model
      and self.guitar_type == guitar_type
      and self.back_wood == back_wood
      and self.top_wood == top_wood
    )


if __name__ == "__main__":
  guitar = Guitar(
    serial_number="V95693",
    price=1499.95,
    builder="Fender",
    model="Stratocaster",
    guitar_type="Electric",
    back_wood="Alder",
    top_wood="Alder",
  )

  is_match = guitar.matches(
    builder="Fender",
    model="Stratocaster",
    guitar_type="Electric",
    back_wood="Alder",
    top_wood="Alder",
  )

  print(f"{guitar.serial_number}: {guitar.model}")
  print(f"Price: ${guitar.price:.2f}")
  print(f"Matches preferred guitar: {is_match}")
