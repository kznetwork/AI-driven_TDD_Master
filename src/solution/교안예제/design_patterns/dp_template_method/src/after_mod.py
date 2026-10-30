from abc import ABC, abstractmethod


class Report(ABC):
    title = ""

    def render(self, rows):                      # 템플릿 메서드 — 알고리즘의 뼈대
        lines = ["=== 보고서 ===", f"제목: {self.title}"]
        lines += [self.format_row(name, value) for name, value in rows]
        lines.append(self.format_total(rows))
        lines.append("=== 끝 ===")
        return "\n".join(lines)

    @abstractmethod
    def format_row(self, name, value): ...       # 단계 — 하위 클래스가 구현

    @abstractmethod
    def format_total(self, rows): ...


class SalesReport(Report):
    title = "매출"

    def format_row(self, name, value):
        return f"- {name}: {value:,}원"

    def format_total(self, rows):
        return f"합계: {sum(v for _, v in rows):,}원"


class InventoryReport(Report):
    title = "재고"

    def format_row(self, name, value):
        return f"- {name}: {value}개"

    def format_total(self, rows):
        return f"합계: {sum(v for _, v in rows)}개"
