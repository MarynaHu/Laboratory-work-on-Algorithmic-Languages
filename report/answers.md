# Answers

## 1. What is the difference between unit tests and behavior tests?

A **unit test** calls one function directly and checks its return value or side effects in isolation. It knows about the internal structure — function signatures, raised exceptions, returned types.

A **behavior test** (black-box test) treats the system as a closed box and interacts with it only through its public interface — in this case the CLI. It knows nothing about internal functions; it only checks what a real user would observe: exit code, stdout, and output format.

## 2. Why is subprocess used for CLI testing?

`subprocess.run` spawns a real OS process, which means the test exercises exactly the same entry path a user would: argument parsing, logging setup, `asyncio.run`, JSON serialization, and the exit code. Importing the module directly and calling `main()` would skip operating-system-level concerns (exit codes, stdout capture, process isolation) and create tight coupling to internal implementation details.

## 3. What happens if one async task fails without error handling?

In `asyncio.gather` (default `return_exceptions=False`), the first raised exception is propagated to the caller immediately. The other coroutines may still be running in the background but their results are discarded. Without a `try/except` in the CLI layer, the unhandled exception causes a traceback and a non-zero exit code with no JSON output.

## 4. When should you test internal functions vs full system behavior?

Test **internal functions** (unit tests) when:
- the logic is complex enough to need isolated verification (edge cases, error branches);
- the function is reused in many places;
- a bug there would be hard to pinpoint from a system-level failure alone.

Test **full system behavior** when:
- you want confidence the components work together correctly;
- you are checking user-visible contracts (exit codes, output format, ordering);
- the test should remain valid even if internal implementation changes.

Both levels are complementary, not alternatives.

## 5. What are the risks of time-based tests?

- **Flakiness on slow machines.** A threshold that passes locally may fail in CI where the CPU is shared or the system is under load.
- **False confidence.** A test that checks `async < sync` in wall time can pass even when async gives no real speedup, if the margin is small.
- **Coupled to delay values.** Tests become brittle when task delays are changed for unrelated reasons.
- **Non-determinism.** OS scheduling adds jitter that is outside the test's control.

Time-based checks are useful as rough sanity checks (e.g. async mode should finish in under 2× the longest single task), but must use generous thresholds and never be the primary correctness signal.
