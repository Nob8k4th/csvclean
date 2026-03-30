from csvclean.cleaner import Cleaner
from csvclean.loader import CSVLoader
from csvclean.writer import CSVWriter


def test_strip_strings():
    rows = [{"name": " Alice ", "city": " NY "}]
    assert Cleaner().strip_strings(rows) == [{"name": "Alice", "city": "NY"}]


def test_deduplicate():
    rows = [{"a": 1}, {"a": 1}, {"a": 2}]
    assert len(Cleaner().deduplicate(rows)) == 2


def test_remove_empty_rows():
    rows = [{"a": ""}, {"a": None}, {"a": 1}]
    assert Cleaner().remove_empty_rows(rows) == [{"a": 1}]


def test_normalize_columns_expected_underscore():
    rows = [{"Full Name": "Alice", "Zip Code": "10001"}]
    out = Cleaner().normalize_columns(rows)
    assert list(out[0].keys()) == ["full_name", "zip_code"]


def test_normalize_columns_single_key():
    rows = [{"My Col": 1}]
    out = Cleaner().normalize_columns(rows)
    assert "my_col" in out[0]


def test_writer_roundtrip(tmp_path):
    rows = [{"name": "A", "age": 1}, {"name": "B", "age": 2}]
    p = tmp_path / 'out.csv'
    CSVWriter().write(str(p), rows)
    loaded = CSVLoader().load(str(p))
    assert loaded[0]["name"] == "A"


def test_loader_int_float_date(tmp_path):
    p = tmp_path / 'types.csv'
    p.write_text('a,b,c\n1,1.5,2024-01-01\n', encoding='utf-8')
    row = CSVLoader().load(str(p))[0]
    assert row['a'] == 1 and row['b'] == 1.5 and str(row['c']) == '2024-01-01'
