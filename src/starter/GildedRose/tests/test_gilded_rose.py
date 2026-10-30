import unittest

from gilded_rose import GildedRose
from item import Item


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        app = GildedRose(items)
        app.update_quality()
        self.assertEqual("fixme", app.items[0].name)


if __name__ == "__main__":
    unittest.main()
