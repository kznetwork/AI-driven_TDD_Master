import csv
import io
import json


def export(rows, kind):
    if kind == "json":
        return json.dumps(rows, ensure_ascii=False)
    if kind == "csv":
        buf = io.StringIO()
        csv.writer(buf, lineterminator="\n").writerows(rows)
        return buf.getvalue()
    raise ValueError(kind)
