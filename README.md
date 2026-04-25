# Report tool

A simple command-line tool that parses a list of numbers, computes basic statistics, formats a plain-text report, and optionally saves it to disk.

---

## What it does

Given a comma- or semicolon-separated string of numbers, `report_tool`:

1. Parses the input into a list of floats.
2. Computes count, sum, minimum, maximum, and mean.
3. Formats a human-readable report (optionally with a sorted list).
4. Saves the report to a `.txt` file on demand.

---

## Requirements

Python 3.10 or newer. No third-party dependencies.

Install (if using a virtual environment):

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## How to run

### Run as a package

```bash
cd src
python -m report_tool
```

Prints a description of the tool, its public functions, usage instructions, and a live example.

### Run individual modules

Each module can be run directly to see its purpose and usage:

```bash
python -m report_tool.parser
python -m report_tool.analyzer
python -m report_tool.formatter
python -m report_tool.storage
```

---

## How to use in your own code

```python
from report_tool import parse_numbers, analyze, build_sorted_report, save_report, read_report

# 1. Parse input
numbers = parse_numbers("4, 8, 15, 16, 23, 42")

# 2. Analyze
stats = analyze(numbers)

# 3. Format
report = build_sorted_report(numbers, stats)
print(report)

# 4. Save and read back
path = save_report(report, "my_report")
content = read_report(path)
```

### Public API

| Function | Description |
|---|---|
| `parse_numbers(text)` | Parse a comma/semicolon-separated string into `list[float]` |
| `analyze(numbers)` | Return a dict with `count`, `sum`, `min`, `max`, `mean` |
| `build_report(stats)` | Format a statistics dict as a plain-text report |
| `build_sorted_report(numbers, stats)` | Same as above, with a sorted values line |
| `save_report(text, filename)` | Write report text to `<filename>.txt`; returns `Path` |
| `read_report(path)` | Read and return the contents of a saved report |
