import pytest
 
from async_tool.models import TaskItem, process_item
 
 
@pytest.mark.asyncio
async def test_success_returns_done_status() -> None:
    """A good task returns a result with status 'done'."""
    item = TaskItem(id=1, delay=0.0, good=True)
 
    result = await process_item(item)
 
    assert result["status"] == "done"
 

@pytest.mark.asyncio
async def test_failure_raises_value_error() -> None:
    """A bad task raises ValueError."""
    item = TaskItem(id=2, delay=0.0, good=False)
 
    with pytest.raises(ValueError):
        await process_item(item)
 
 
@pytest.mark.asyncio
async def test_failure_message_contains_task_id() -> None:
    """The ValueError message mentions the failing task's id."""
    item = TaskItem(id=42, delay=0.0, good=False)
 
    with pytest.raises(ValueError, match="42"):
        await process_item(item)
 

 
@pytest.mark.asyncio
async def test_result_contains_correct_id() -> None:
    """The returned dict contains the original task id."""
    item = TaskItem(id=7, delay=0.0, good=True)
 
    result = await process_item(item)
 
    assert result["id"] == 7
 
 
@pytest.mark.asyncio
async def test_result_has_no_extra_keys() -> None:
    """A successful result contains exactly 'id' and 'status'."""
    item = TaskItem(id=1, delay=0.0, good=True)
 
    result = await process_item(item)
 
    assert set(result.keys()) == {"id", "status"}
 

 
@pytest.mark.asyncio
@pytest.mark.parametrize("task_id", [1, 5, 100])
async def test_success_preserves_id(task_id: int) -> None:
    """The returned id always matches the input id."""
    item = TaskItem(id=task_id, delay=0.0, good=True)
 
    result = await process_item(item)
 
    assert result["id"] == task_id
    assert result["status"] == "done"