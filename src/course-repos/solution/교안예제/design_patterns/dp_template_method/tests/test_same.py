import after_mod
import before_mod

ROWS = [("노트북", 1200000), ("마우스", 50000)]
STOCK = [("노트북", 3), ("마우스", 40)]


def test_sales_report_same():
    assert after_mod.SalesReport().render(ROWS) == before_mod.sales_report(ROWS)


def test_inventory_report_same():
    assert after_mod.InventoryReport().render(STOCK) == before_mod.inventory_report(STOCK)


def test_report_text():
    assert after_mod.SalesReport().render(ROWS).splitlines()[-2] == "합계: 1,250,000원"
