import csv
from datetime import date


class CSVLoader:
    def infer_type(self, value: str):
        if value is None:
            return None
        value = value.strip()
        if value == "":
            return ""
        if value in {"True", "False"}:
            return value
        if value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
            return int(value)
        try:
            return float(value)
        except ValueError:
            pass
        try:
            return date.fromisoformat(value)
        except ValueError:
            pass
        lower = value.lower()
        if lower in {"true", "false"}:
            return lower == "true"
        return value

    def load(self, path: str):
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [
                {k: self.infer_type(v) for k, v in row.items()} for row in reader
            ]
