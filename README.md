# lab12 — Testing an Async CLI Tool

Automated tests for `async_tool` from Lab 11.

---

## Requirements

Python 3.11 or newer.

```bash
pip install -r requirements.txt
```

---

## Run tests

```bash
pytest
```

With verbose output:
```bash
pytest -v
```

Run only unit tests:
```bash
pytest tests/test_process_item.py -v
```

Run only CLI tests:
```bash
pytest tests/test_cli.py -v
```

---

## Project structure

```
lab12/
├── pytest.ini
├── README.md
├── requirements.txt
├── src/
│   └── async_tool/        ← copied from Lab 11
├── tests/
│   ├── conftest.py        ← shared fixtures (tmp input files)
│   ├── test_process_item.py  ← unit tests (Part A)
│   └── test_cli.py           ← behavior tests (Part B)
└── report/
    └── answers.md
```

---

## Test overview

### Part A — Unit tests (`test_process_item.py`)

Tests call `process_item` directly via `await`:

| Test | What it checks |
|---|---|
| `test_success_returns_done_status` | good task → `status == "done"` |
| `test_failure_raises_value_error` | bad task → `ValueError` raised |
| `test_failure_message_contains_task_id` | error message includes the task id |
| `test_result_contains_id` | returned dict has correct `id` |
| `test_result_has_no_extra_keys` | result has exactly `id` and `status` |
| `test_success_preserves_id` | parametrized across multiple ids |

### Part B — CLI / Behavior tests (`test_cli.py`)

Tests run the tool as a subprocess via `subprocess.run`:

| Test | What it checks |
|---|---|
| `test_basic_execution_exits_zero` | valid input → exit 0 |
| `test_basic_execution_output_is_valid_json` | stdout is parseable JSON |
| `test_async_mode_exits_zero` | `--mode async` → exit 0 |
| `test_async_mode_all_tasks_done` | all results have `status == "done"` |
| `test_limited_mode_exits_zero` | `--mode limited` → exit 0 |
| `test_error_exits_nonzero_without_flag` | failure → non-zero exit |
| `test_error_without_flag_prints_nothing_to_stdout` | no JSON on hard failure |
| `test_continue_on_error_exits_zero` | flag present → exit 0 |
| `test_continue_on_error_failed_task_has_error_status` | failed task → `"status": "error"` |
| `test_continue_on_error_failed_task_has_message` | failed task has `"message"` key |
| `test_output_count_matches_input` | result count == input count |
| `test_output_order_preserved` | ids appear in input order |
| `test_all_modes_return_all_items` | parametrized across all 3 modes |
