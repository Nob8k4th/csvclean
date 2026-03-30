# csvclean

`csvclean` 提供一套从 CSV 读取、字段清洗、规则校验到写回文件的基础流水线。

## 主要组件

- `CSVLoader`：读取 CSV 并尝试做基础类型推断
- `Cleaner`：去重、去空行、字符串裁剪、列名规范化
- `Validator`：非空、类型、范围、正则等校验
- `CSVWriter`：将字典列表写回 CSV

## 快速使用

```bash
pip install -e .
```

```python
from csvclean import CSVLoader, Cleaner, Validator, CSVWriter

rows = CSVLoader().load("input.csv")
cleaner = Cleaner()
rows = cleaner.strip_strings(rows)
rows = cleaner.remove_empty_rows(rows)
rows = cleaner.deduplicate(rows)

validator = Validator()
ok = validator.validate_non_null(rows, "name")
print("name 列非空:", ok)

CSVWriter().write("output.csv", rows)
```

## 测试

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
pytest tests/ -v --tb=short --json-report --json-report-file=test_results.json
```
