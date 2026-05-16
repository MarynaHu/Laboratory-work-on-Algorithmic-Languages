import argparse
import asyncio
import json
import logging
import sys
from collections.abc import Sequence
from pathlib import Path
 
from async_tool.models import TaskItem, TaskResult
from async_tool.runner import run_sequential, run_concurrent, run_limited
 
logger = logging.getLogger(__name__)
 
 
# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------
 
def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="async_tool",
        description="Process a batch of async tasks in different execution modes.",
    )
    p.add_argument(
        "input",
        metavar="input.json",
        help="Path to a JSON file containing a list of task objects.",
    )
    p.add_argument(
        "--mode",
        choices=["sync", "async", "limited"],
        default="sync",
        help="Execution mode: sync (default) | async | limited.",
    )
    p.add_argument(
        "--limit",
        type=int,
        default=5,
        metavar="N",
        help="Max concurrent tasks for --mode limited (default: 5).",
    )
    p.add_argument(
        "--continue-on-error",
        action="store_true",
        default=False,
        help="Keep processing after a task failure instead of stopping.",
    )
    p.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="WARNING",
        metavar="LEVEL",
        dest="log_level",
        help="Logging verbosity (default: WARNING).",
    )
    return p
 
 
# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
 
def configure_logging(level_name: str) -> None:
    level = getattr(logging, level_name.upper(), logging.WARNING)
    logging.basicConfig(
        level=level,
        format="%(levelname)s %(name)s: %(message)s",
        stream=sys.stderr,
    )
 
 
# ---------------------------------------------------------------------------
# Input loading
# ---------------------------------------------------------------------------
 
def load_tasks(path: str) -> list[TaskItem]:
    raw: object = json.loads(Path(path).read_bytes())
    if not isinstance(raw, list):
        raise ValueError("Input JSON must be a list of task objects.")
    tasks: list[TaskItem] = []
    for item in raw:
        if not isinstance(item, dict):
            raise ValueError(f"Each task must be a JSON object, got: {type(item)}")
        tasks.append(
            TaskItem(
                id=int(item["id"]),
                delay=float(item["delay"]),
                good=bool(item["good"]),
            )
        )
    return tasks
 
 
# ---------------------------------------------------------------------------
# Async orchestration
# ---------------------------------------------------------------------------
 
async def _run(
    tasks: list[TaskItem],
    mode: str,
    continue_on_error: bool,
    limit: int,
) -> list[TaskResult]:
    logger.info(
        "Running %d task(s) in %s mode (continue_on_error=%s)",
        len(tasks),
        mode,
        continue_on_error,
    )
    if mode == "sync":
        return await run_sequential(tasks, continue_on_error)
    if mode == "async":
        return await run_concurrent(tasks, continue_on_error)
    # limited
    logger.info("Semaphore limit: %d", limit)
    return await run_limited(tasks, continue_on_error, limit)
 
 
# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
 
def main(argv: Sequence[str] | None = None) -> None:
    parser = build_arg_parser()
    ns = parser.parse_args(argv)
 
    configure_logging(ns.log_level)
 
    logger.debug(
        "Args: input=%s mode=%s limit=%d continue_on_error=%s log_level=%s",
        ns.input, ns.mode, ns.limit, ns.continue_on_error, ns.log_level,
    )
 
    try:
        tasks = load_tasks(ns.input)
        logger.info("Loaded %d task(s) from %s", len(tasks), ns.input)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Error loading input: {exc}", file=sys.stderr)
        sys.exit(1)
 
    try:
        results: list[TaskResult] = asyncio.run(
            _run(tasks, ns.mode, ns.continue_on_error, ns.limit)
        )
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
 
    print(json.dumps([dict(r) for r in results], indent=2))