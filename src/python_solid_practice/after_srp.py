class GuitarSpec:
  def __init__(self, builder, model, guitar_type, back_wood, top_wood):
    self.builder = builder
    self.model = model
    self.guitar_type = guitar_type
    self.back_wood = back_wood
    self.top_wood = top_wood

  def matches(self, other):
    return (
      self.builder == other.builder
      and self.model == other.model
      and self.guitar_type == other.guitar_type
      and self.back_wood == other.back_wood
      and self.top_wood == other.top_wood
    )


class Guitar:
  def __init__(self, serial_number, price, spec):
    self.serial_number = serial_number
    self.price = price
    self.spec = spec


if __name__ == "__main__":
  guitar = Guitar(
    serial_number="V95693",
    price=1499.95,
    spec=GuitarSpec(
      builder="Fender",
      model="Stratocaster",
      guitar_type="Electric",
      back_wood="Alder",
      top_wood="Alder",
    ),
  )
  preferred_spec = GuitarSpec(
    builder="Fender",
    model="Stratocaster",
    guitar_type="Electric",
    back_wood="Alder",
    top_wood="Alder",
  )

  print(f"{guitar.serial_number}: {guitar.spec.model}")
  print(f"Price: ${guitar.price:.2f}")
  print(f"Matches preferred guitar: {guitar.spec.matches(preferred_spec)}")
