# async_tool

A command-line tool that processes a batch of tasks in three execution modes:
sequential, fully concurrent, and concurrency-limited.

---

## Requirements

Python 3.11 or newer. No third-party dependencies.

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

---

## CLI usage

```
python -m async_tool input.json [OPTIONS]
```

### Arguments

| Argument | Required | Default | Description |
|---|---|---|---|
| `input.json` | yes | — | Path to JSON file with task list |
| `--mode` | no | `sync` | Execution mode: `sync` \| `async` \| `limited` |
| `--limit N` | no | `5` | Max concurrent tasks (only for `--mode limited`) |
| `--continue-on-error` | no | off | Keep processing after failures |
| `--log-level LEVEL` | no | `WARNING` | `DEBUG` \| `INFO` \| `WARNING` \| `ERROR` |

---

## Input format

A JSON file containing a list of task objects:

```json
[
  {"id": 1, "delay": 1, "good": true},
  {"id": 2, "delay": 2, "good": false},
  {"id": 3, "delay": 1, "good": true}
]
```

Each task has:
- `id` — unique integer identifier
- `delay` — seconds to simulate I/O work
- `good` — `true` means success, `false` means failure

---

## Output format

Valid JSON printed to stdout, in input order:

```json
[
  {"id": 1, "status": "done"},
  {"id": 2, "status": "error", "message": "Task 2 failed"},
  {"id": 3, "status": "done"}
]
```

---

## Example commands

Sequential mode (one task at a time, stops on first error):
```bash
python -m async_tool input.json --mode sync --log-level INFO
```

Concurrent mode, continue past failures:
```bash
python -m async_tool input.json --mode async --continue-on-error --log-level INFO
```

Limited concurrency (max 3 at once), full debug output:
```bash
python -m async_tool input.json --mode limited --limit 3 --continue-on-error --log-level DEBUG
```

---

## Execution modes explained

| Mode | How it works | When to use |
|---|---|---|
| `sync` | Tasks run one after another (`await` in a loop) | Ordered side effects, simple debugging |
| `async` | All tasks start at once (`asyncio.gather`) | Maximum throughput, no ordering constraints |
| `limited` | Tasks share a `Semaphore` (`--limit N`) | Controlled throughput (API rate limits, etc.) |

