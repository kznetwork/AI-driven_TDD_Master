import csv
import io
import json
from abc import ABC, abstractmethod


class Formatter(ABC):                            # Product
    @abstractmethod
    def format(self, rows): ...


class JsonFormatter(Formatter):                  # ConcreteProduct
    def format(self, rows):
        return json.dumps(rows, ensure_ascii=False)


class CsvFormatter(Formatter):                   # ConcreteProduct
    def format(self, rows):
        buf = io.StringIO()
        csv.writer(buf, lineterminator="\n").writerows(rows)
        return buf.getvalue()


class Exporter(ABC):                             # Creator
    def export(self, rows):                      # 어떤 Formatter 인지 모르고 사용만 한다
        return self.create_formatter().format(rows)

    @abstractmethod
    def create_formatter(self) -> Formatter: ... # 팩토리 메서드


class JsonExporter(Exporter):                    # ConcreteCreator
    def create_formatter(self):
        return JsonFormatter()


class CsvExporter(Exporter):
    def create_formatter(self):
        return CsvFormatter()
