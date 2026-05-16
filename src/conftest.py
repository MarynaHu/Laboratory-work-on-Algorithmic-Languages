import json
from pathlib import Path
 
import pytest
 

TASKS_ALL_GOOD: list[dict[str, int | float | bool]] = [
    {"id": 1, "delay": 0.01, "good": True},
    {"id": 2, "delay": 0.01, "good": True},
    {"id": 3, "delay": 0.01, "good": True},
]
 
TASKS_WITH_FAILURE: list[dict[str, int | float | bool]] = [
    {"id": 1, "delay": 0.01, "good": True},
    {"id": 2, "delay": 0.01, "good": False},
    {"id": 3, "delay": 0.01, "good": True},
]
 
 
@pytest.fixture()
def input_all_good(tmp_path: Path) -> Path:
    """JSON file where every task succeeds."""
    f = tmp_path / "input_good.json"
    f.write_text(json.dumps(TASKS_ALL_GOOD), encoding="utf-8")
    return f
 
 
@pytest.fixture()
def input_with_failure(tmp_path: Path) -> Path:
    """JSON file that contains one failing task."""
    f = tmp_path / "input_fail.json"
    f.write_text(json.dumps(TASKS_WITH_FAILURE), encoding="utf-8")
    return f