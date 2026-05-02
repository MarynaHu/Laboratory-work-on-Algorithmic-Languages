# report_tool

A command-line interface (CLI) tool that reads a list of numbers from a file, computes basic statistics, formats the report, and saves it to disk with execution logging.

---

## What it does

Given an input text file containing comma-, space-, or semicolon-separated numbers, `report_tool`:
1. Reads the data from the file.
2. Parses the input into a list of floats.
3. Computes count, sum, minimum, maximum, and mean.
4. Formats the report into human-readable text or structured JSON.
5. Saves the report to an output file.
6. Logs the execution process at a user-defined verbosity level.

---

## Requirements

Python 3.10 or newer. No third-party dependencies.
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
---

## CLI Arguments
```
python -m report_tool \
    --input   FILE    input file containing numbers (comma/semicolon-separated)
    --out     FILE    output file for the report
    --format  text|json   output format (default: text)
    --log-level DEBUG|INFO|WARNING|ERROR   logging verbosity (default: INFO)
```
---

## How to run (CLI Examples)
If you not in folder src
```bash
cd src
```
Example 1: Generating a human-readable text report with standard logging

```bash
python -m report_tool --input data.txt --out report.txt --format text --log-level INFO
```

Example 2: Generating a JSON report for downstream systems, suppressing standard info logs

```bash
python -m report_tool --input data.txt --out report.json --format json --log-level WARNING
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
from report_tool import parse_numbers, analyze, build_json_report, save_report, read_file

# 1. Read and parse input
raw_text = read_file("data.txt")
numbers = parse_numbers(raw_text)

# 2. Analyze
stats = analyze(numbers)

# 3. Format
report = build_json_report(stats)

# 4. Save
path = save_report(report, "output.json")
```

### Public API

| Function | Description |
|---|---|
| `parse_numbers(text)` | Parse a comma/semicolon-separated string into `list[float]` |
| `analyze(numbers)` | Return a dict with `count`, `sum`, `min`, `max`, `mean` |
| `build_report(stats)` | Format a statistics dict as a plain-text report |
| `build_sorted_report(numbers, stats)` | Same as above, with a sorted values line |
| `build_json_report(stats)` | Format a statistics dict into a JSON string |
| `save_report(text, filename)` | Safely write text to the specified file path; returns Path |
| `read_file(filepath)` | Read and return the contents of a file |
