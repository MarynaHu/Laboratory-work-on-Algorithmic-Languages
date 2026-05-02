# Lab 10 — Refactoring into a CLI Tool

## 1. What was added
- **CLI Interface:** Added `argparse` to `__main__.py` to handle command-line flags (`--input`, `--out`, `--format`, `--log-level`).
- **File Input/Output:** Updated the `storage.py` module to accurately read raw strings from an input file and write reports to an explicit output path using `pathlib`.
- **JSON Output:** Added the `build_json_report` function to the `formatter.py` module, utilizing Python's built-in `json` library to produce structured dictionaries.
- **Logging:** Replaced basic prints with the `logging` module. Execution steps are now logged securely with varying severity, isolating application output from diagnostic information.

## 2. How the tool changed
The tool evolved from a static, **demo-style execution** to a **real CLI-based usage** program. Previously, running the package simply executed hardcoded variables (like `text = "4, 8, 15, 16, 23, 42"`) and printed the result directly to the terminal. Now, the `__main__.py` dynamically acts as an orchestrator: it parses user arguments, routes the file reading through `storage.py`, passes data down the analysis pipeline, formats it based on user preference, and safely writes the file to the disk without altering the pure business logic inside the submodules. 

## 3. Why these changes matter
- **CLI improves usability and automation:** Hardcoded data is useless in production. Allowing file paths to be passed as arguments means this script can be executed by cron jobs, CI/CD pipelines, or other shell scripts automatically.
- **JSON is useful for machine-readable output:** Plain text is good for human eyes, but terrible for automated systems. JSON allows the analysis output of this tool to be easily parsed and consumed by frontend dashboards, databases, or other Python services downstream.
- **Logging improves debugging and transparency:** Standard `print()` statements mix diagnostic info with actual program output, causing chaos in data pipelines. The `logging` module separates the concerns, sending logs to `stderr` with timestamps, while allowing the user to squelch noise by setting `--log-level WARNING` when everything is running smoothly.
