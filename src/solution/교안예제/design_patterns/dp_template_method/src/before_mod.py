def sales_report(rows):
    lines = ["=== 보고서 ===", "제목: 매출"]
    for name, amount in rows:
        lines.append(f"- {name}: {amount:,}원")
    lines.append(f"합계: {sum(a for _, a in rows):,}원")
    lines.append("=== 끝 ===")
    return "\n".join(lines)


def inventory_report(rows):
    lines = ["=== 보고서 ===", "제목: 재고"]
    for name, qty in rows:
        lines.append(f"- {name}: {qty}개")
    lines.append(f"합계: {sum(q for _, q in rows)}개")
    lines.append("=== 끝 ===")
    return "\n".join(lines)
