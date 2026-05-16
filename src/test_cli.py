"""test_cli.py — behavior tests for the async_tool CLI."""

import json
import subprocess
import sys
from pathlib import Path
 
import pytest
 
SRC_DIR: Path = Path(__file__).parent.parent / "src"
 
 
def run_cli(*args: str, input_file: Path, timeout: int = 15) -> subprocess.CompletedProcess[str]:
    """Run the CLI tool and return the completed process."""
    return subprocess.run(
        [sys.executable, "-m", "async_tool", str(input_file), *args],
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd=str(SRC_DIR),
    )
 
  
def test_basic_execution_exits_zero(input_all_good: Path) -> None:
    proc = run_cli(input_file=input_all_good)
 
    assert proc.returncode == 0
 
 
def test_basic_execution_output_is_valid_json(input_all_good: Path) -> None:
    proc = run_cli(input_file=input_all_good)
 
    result = json.loads(proc.stdout)
    assert isinstance(result, list)
 
 
def test_async_mode_exits_zero(input_all_good: Path) -> None:
    proc = run_cli("--mode", "async", input_file=input_all_good)
 
    assert proc.returncode == 0
 
 
def test_async_mode_all_tasks_done(input_all_good: Path) -> None:
    proc = run_cli("--mode", "async", input_file=input_all_good)
 
    result = json.loads(proc.stdout)
    assert all(item["status"] == "done" for item in result)
 
 
def test_limited_mode_exits_zero(input_all_good: Path) -> None:
    proc = run_cli("--mode", "limited", "--limit", "2", input_file=input_all_good)
 
    assert proc.returncode == 0
 

def test_error_exits_nonzero_without_flag(input_with_failure: Path) -> None:
    proc = run_cli(input_file=input_with_failure)
 
    assert proc.returncode != 0
 
 
def test_error_without_flag_no_stdout(input_with_failure: Path) -> None:
    proc = run_cli(input_file=input_with_failure)
 
    assert proc.stdout.strip() == ""
 
 

def test_continue_on_error_exits_zero(input_with_failure: Path) -> None:
    proc = run_cli("--continue-on-error", input_file=input_with_failure)
 
    assert proc.returncode == 0
 
 
def test_continue_on_error_failed_task_has_error_status(input_with_failure: Path) -> None:
    proc = run_cli("--continue-on-error", input_file=input_with_failure)
 
    result = json.loads(proc.stdout)
    failed = [item for item in result if item["id"] == 2]
    assert len(failed) == 1
    assert failed[0]["status"] == "error"
 
 
def test_continue_on_error_failed_task_has_message(input_with_failure: Path) -> None:
    proc = run_cli("--continue-on-error", input_file=input_with_failure)
 
    result = json.loads(proc.stdout)
    failed = next(item for item in result if item["id"] == 2)
    assert "message" in failed
    assert failed["message"] != ""
 
 

def test_output_count_matches_input(input_with_failure: Path) -> None:
    proc = run_cli("--continue-on-error", input_file=input_with_failure)
 
    result = json.loads(proc.stdout)
    assert len(result) == 3
 
 
def test_output_order_preserved(input_with_failure: Path) -> None:
    proc = run_cli("--continue-on-error", input_file=input_with_failure)
 
    result = json.loads(proc.stdout)
    assert [item["id"] for item in result] == [1, 2, 3]
 
 

@pytest.mark.parametrize("mode", ["sync", "async", "limited"])
def test_all_modes_return_all_items(mode: str, input_all_good: Path) -> None:
    proc = run_cli("--mode", mode, input_file=input_all_good)
 
    result = json.loads(proc.stdout)
    assert len(result) == 3