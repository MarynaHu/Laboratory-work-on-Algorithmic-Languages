# Answers
 
## 1. Why does `await` inside a loop lead to sequential execution?
 
`await` suspends the current coroutine and gives control back to the event loop **only until that one awaitable finishes**. Inside a `for` loop, the next iteration does not start until the previous `await` returns, so tasks run one after another regardless of how long each one takes. There is never more than one task in flight at any moment.
 
## 2. How does `asyncio.gather` change behavior?
 
`asyncio.gather` schedules **all coroutines at the same time** before awaiting any of them. The event loop interleaves their execution whenever one suspends (e.g. at `await asyncio.sleep`). Total wall-clock time approaches the duration of the single longest task rather than the sum of all tasks. Tasks are still run on a single thread — it is concurrency, not parallelism.
 
## 3. What happens if one task fails in async mode without `--continue-on-error`?
 
`asyncio.gather` (with the default `return_exceptions=False`) re-raises the first exception it receives. The caller gets that exception immediately. Other coroutines that were already scheduled may continue running in the background, but their results are discarded. The CLI catches the exception, prints an error to stderr, and exits with a non-zero code.
 
## 4. Why is a semaphore needed?
 
`asyncio.gather` starts every coroutine at once. If the task list is large this can overwhelm a remote API, a database connection pool, or simply consume too much memory. A `Semaphore(N)` acts as a counter: each coroutine must acquire it before doing real work and releases it when done, so at most `N` tasks run concurrently at any moment. This gives controlled throughput without changing the logical concurrency model.
 
## 5. When should async NOT be used?
 
- **CPU-bound work.** `asyncio` is cooperative and single-threaded; heavy computation blocks the event loop and gives no speedup. Use `multiprocessing` or `concurrent.futures.ProcessPoolExecutor` instead.
- **Blocking I/O calls.** Any call to a synchronous library (`time.sleep`, `requests.get`, standard file I/O in a tight loop) blocks the entire event loop. All other coroutines freeze until it returns.
- **Simple sequential scripts.** If there is nothing to overlap — one task, or tasks with hard ordering constraints — async adds boilerplate with no benefit.
- **When the codebase is not async-ready.** Mixing sync and async code requires adapters (`run_in_executor`, etc.) and increases complexity without a clear payoff.