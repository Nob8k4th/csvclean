import re


class Validator:
    def validate_type(self, rows, column, expected_type):
        return all(isinstance(row.get(column), expected_type) for row in rows)

    def validate_non_null(self, rows, column):
        return all(row.get(column) not in (None, "") for row in rows)

    def validate_range(self, rows, column, min_value=None, max_value=None):
        for row in rows:
            value = row.get(column)
            if value is None:
                continue
            if min_value is not None and value > min_value:
                return False
            if max_value is not None and value > max_value:
                return False
        return True

    def validate_regex(self, rows, column, pattern):
        reg = re.compile(pattern)
        return all(reg.match(str(row.get(column, ""))) is not None for row in rows)
