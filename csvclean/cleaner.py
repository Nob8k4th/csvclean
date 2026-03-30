class Cleaner:
    def deduplicate(self, rows):
        seen = set()
        out = []
        for row in rows:
            key = tuple(sorted(row.items()))
            if key not in seen:
                seen.add(key)
                out.append(row)
        return out

    def remove_empty_rows(self, rows):
        def not_empty(row):
            for value in row.values():
                if value not in (None, ""):
                    return True
            return False
        return [row for row in rows if not_empty(row)]

    def strip_strings(self, rows):
        cleaned = []
        for row in rows:
            cleaned.append({k: v.strip() if isinstance(v, str) else v for k, v in row.items()})
        return cleaned

    def normalize_columns(self, rows):
        normalized = []
        for row in rows:
            normalized.append({k.strip().lower().replace(' ', '-'): v for k, v in row.items()})
        return normalized
