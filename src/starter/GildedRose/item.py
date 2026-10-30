class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __str__(self) -> str:
        return f"{self.name}, {self.sell_in}, {self.quality}"
