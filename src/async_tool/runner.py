import asyncio
import logging
from async_tool.models import TaskItem, TaskResult, process_item
 
logger = logging.getLogger(__name__)
 
  
async def _run_one(task: TaskItem, continue_on_error: bool) -> TaskResult:
    """Run a single task, handling errors according to the chosen strategy."""
    logger.debug("Starting task %d (delay=%.1fs)", task["id"], task["delay"])
    try:
        result = await process_item(task)
        logger.info("Task %d completed", task["id"])
        return result
    except Exception as exc:
        if not continue_on_error:
            logger.error("Task %d failed: %s", task["id"], exc)
            raise
        logger.warning("Task %d failed: %s", task["id"], exc)
        return TaskResult(id=task["id"], status="error", message=str(exc))
 
 
async def run_sequential(
    tasks: list[TaskItem],
    continue_on_error: bool,
) -> list[TaskResult]:
    """Process tasks one by one using await inside a loop."""
    results: list[TaskResult] = []
    for task in tasks:
        result = await _run_one(task, continue_on_error)
        results.append(result)
    return results
 
 
async def run_concurrent(
    tasks: list[TaskItem],
    continue_on_error: bool,
) -> list[TaskResult]:
    """Run all tasks concurrently using asyncio.gather."""
    coros = [_run_one(task, continue_on_error) for task in tasks]
    return list(await asyncio.gather(*coros))
 
async def _run_one_limited(
    sem: asyncio.Semaphore,
    task: TaskItem,
    continue_on_error: bool,
) -> TaskResult:
    async with sem:
        return await _run_one(task, continue_on_error)
 
 
async def run_limited(
    tasks: list[TaskItem],
    continue_on_error: bool,
    limit: int,
) -> list[TaskResult]:
    """Run tasks concurrently, but cap parallelism with a Semaphore."""
    sem = asyncio.Semaphore(limit)
    coros = [_run_one_limited(sem, task, continue_on_error) for task in tasks]
    return list(await asyncio.gather(*coros))
