# async / await and the event loop

**Plan day:** Day 3 · **Status:** `can-explain`
_Status values: `not-started` → `learning` → `can-explain`. You are done when you can answer every question below out loud, without notes, in under two minutes each._

## In my own words
_One paragraph for a senior engineer who has never used this. No jargon you cannot define._

_(My own answers from the Day 3 session, 2026-09-28.)_

When I `await`, the loop goes and does other things while that task waits. The event loop is one thread, so a blocking call — one that never hands control back — takes down everything else with it: every other request queues behind it. `asyncio.gather` runs independent work together, but it is the wrong tool when the calls must be ordered (step 2 needs step 1's result), when a rate limit would be tripped, or when I need each result's errors separately (gather raises on the first failure unless `return_exceptions=True`). To call blocking code safely from async code, use `await asyncio.to_thread(fn, ...)`, which runs it on a worker thread and leaves the loop free.

## Must be able to answer
- [x] What actually happens when you `await`? What is the loop doing meanwhile?
- [x] Why does one blocking call inside an async endpoint hurt every other request?
- [x] `asyncio.gather` vs awaiting in sequence: when is gather wrong?
- [x] How do you call blocking/sync code from async code safely?

### The three ways to wait (measured, 10 tasks, no network)
| Code | 10 tasks | Use when |
|---|---|---|
| `time.sleep(1)` inside async | **10.04s** | never inside the loop |
| `await asyncio.to_thread(time.sleep, 1)` | **1.01s** | a blocking library I cannot change |
| `await asyncio.sleep(1)` | **1.00s** | a real async version exists |

FastAPI alternative: declare the endpoint as plain `def` instead of `async def` and FastAPI runs it in a threadpool.

## Gotchas / what bit me
_Anything that cost you more than fifteen minutes. These become interview stories._

- **A noisy benchmark hid the effect I was testing.** Over httpbin.org the `to_thread` version measured *slower* (20.1s) than the blocking one (13.6s), which is the opposite of the theory. The cause was the network, not the code: httpbin rate-limits, and sequential runs swung between 17.9s and 25.4s across runs — several seconds of noise against a 1-second signal. Re-running with the HTTP calls removed showed the real result: 10.04s vs 1.01s. **Lesson: when a benchmark disagrees with theory, suspect the measurement first; isolate the one thing being tested.**
- Calling `fetch_one(client, i)` does not start anything. A coroutine only runs when awaited (or wrapped in a task). `gather` is what starts them together.
- `asyncio.gather(*tasks)` needs the `*` — it takes separate arguments, not a list (like PHP's `...$args`).

## Minimal snippet
_The smallest code that demonstrates the idea. Typed by you, not pasted._

From `docuquery/scratch/08_async_fetch.py` — the same sleep, in and out of the loop:

```python
async def blocking_worker(client, i):
    response = await client.get(URL, timeout=30)
    time.sleep(1)                           # freezes the whole loop
    return response.status_code


async def safe_worker(client, i):
    response = await client.get(URL, timeout=30)
    await asyncio.to_thread(time.sleep, 1)  # loop stays free
    return response.status_code


tasks = [safe_worker(client, i) for i in range(N)]
results = await asyncio.gather(*tasks)      # coroutines only start here
```

Sequential vs concurrent over 10 real HTTP calls: **25.4s → 4.2s (6x)**.

## Sources I actually used
- `asyncio` docs: `gather`, `to_thread`, `sleep`
- `docuquery/scratch/08_async_fetch.py`
