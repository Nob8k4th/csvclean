import csv


class CSVWriter:
    def to_dict_list(self, rows):
        return list(rows)

    def write(self, path, rows):
        if not rows:
            return
        fieldnames = list(rows[0].keys())
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
