import after_mod
import before_mod

ROWS = [["노트북", 1200000], ["마우스", 50000]]


def test_json_same():
    assert after_mod.JsonExporter().export(ROWS) == before_mod.export(ROWS, "json")


def test_csv_same():
    assert after_mod.CsvExporter().export(ROWS) == before_mod.export(ROWS, "csv")
    assert after_mod.CsvExporter().export(ROWS) == "노트북,1200000\n마우스,50000\n"
