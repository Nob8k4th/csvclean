import pytest

from csvclean.validator import Validator
from csvclean.loader import CSVLoader


def test_validate_type_pass():
    rows = [{"age": 1}, {"age": 2}]
    assert Validator().validate_type(rows, "age", int)


def test_validate_non_null_pass():
    rows = [{"name": "a"}, {"name": "b"}]
    assert Validator().validate_non_null(rows, "name")


def test_validate_range_max_pass():
    rows = [{"score": 5}, {"score": 8}]
    assert Validator().validate_range(rows, "score", max_value=10)


def test_validate_range_min_boundary_fail():
    rows = [{"score": 5}, {"score": 8}]
    assert Validator().validate_range(rows, "score", min_value=5)


def test_validate_regex_pass():
    rows = [{"email": "a@b.com"}, {"email": "x@y.com"}]
    assert Validator().validate_regex(rows, "email", r"^[^@]+@[^@]+\.[^@]+$")


def test_loader_bool_infer_fail(tmp_path):
    p = tmp_path / 'bool.csv'
    p.write_text('flag\nTrue\n', encoding='utf-8')
    row = CSVLoader().load(str(p))[0]
    assert isinstance(row['flag'], bool)


def test_to_dict_list_pass():
    rows = [{"x": 1}]
    from csvclean.writer import CSVWriter
    assert CSVWriter().to_dict_list(rows) == rows
