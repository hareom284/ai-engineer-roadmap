# FastAPI core

**Plan day:** Day 4 · **Status:** `can-explain`
_Status values: `not-started` → `learning` → `can-explain`. You are done when you can answer every question below out loud, without notes, in under two minutes each._

## In my own words
_One paragraph for a senior engineer who has never used this. No jargon you cannot define._

_(My own answers from the Day 4 session, 2026-10-04.)_

`Depends` lets tests swap a fake store: the endpoint asks for what it needs and the caller decides what to hand it, so a test injects a fake without touching the app — on Day 6 the same hook swaps a real DB session for a test one. `response_model` shapes the **output**: it serialises (a `datetime` goes out as `"2026-09-30T02:45:09.781888Z"`), filters anything not declared in the model so internal fields cannot leak, and generates `/docs`. Request validation is separate — it comes from the type hint on the body (`payload: DocumentIn`), and a body that does not match gets a **422** from FastAPI before my function runs. A **404** is my own decision: the request was valid, the id simply does not exist, so I raise `HTTPException(404)`.

## Must be able to answer
- [x] How does dependency injection work, and how do you override a dependency in a test?
- [x] What does `response_model` actually do to your output?
- [x] `def` vs `async def` endpoints: which runs on a threadpool and why does that matter?
- [x] Where do validation errors come from and what status code do they produce?

### Who decides what
| Thing | Decided by | Status |
|---|---|---|
| Body doesn't match the schema | FastAPI + Pydantic, before my code | 422 |
| Id not in the store | my code, `HTTPException` | 404 |
| What fields go out | `response_model=` | — |
| Which store the endpoint gets | `Depends(get_store)`, overridable | — |

### `def` vs `async def`
| | Runs on | A blocking call inside |
|---|---|---|
| `def` (what I used) | threadpool | safe — only that thread waits |
| `async def` | the event loop | freezes every other request (Day 3: 10.04s vs 1.01s) |

## Gotchas / what bit me
_Anything that cost you more than fifteen minutes. These become interview stories._

- **`=` instead of `==` in a test.** I wrote `data = response.json()['title'] = "Fake"`, which Python read as a chained assignment, so `data` became the string `"Fake"` and the next line failed with `TypeError: string indices must be integers`. PHP would have warned about assignment in a condition; Python treats `a = b = x` as a normal feature, so there is no warning — the error appears later and looks unrelated.
- **Empty tests pass.** `pytest` reported "10 passed" while five of those functions contained only `# TODO` comments. Second time this has caught me (Day 2 was the first). A test is not finished until I have seen it fail.
- **Pydantic v1 names in v2 code.** `document.dict()` still runs but raises `PydanticDeprecatedSince20`; the v2 name is `model_dump()`. Most tutorials online are still v1.
- Warnings are a library saying "this works, but not forever". `StarletteDeprecationWarning: install httpx2 instead` — fixed with `uv add --dev httpx2`, test-only so it goes in the dev group.
- Naming a variable `id` shadows the built-in `id()`. Use `doc_id`.

## Minimal snippet
_The smallest code that demonstrates the idea. Typed by you, not pasted._

From `docuquery/src/docuquery/api.py` and `tests/test_api.py`:

```python
@app.get("/documents/{doc_id}", response_model=DocumentOut)
def read_document(doc_id: str, store: InMemoryStore = Depends(get_store)) -> DocumentOut:
    document = store.get(doc_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document
```

Swapping the dependency in a test — the reason `Depends` exists:

```python
def test_dependency_override():
    fake_store = InMemoryStore()
    app.dependency_overrides[get_store] = lambda: fake_store
    try:
        created = client.post("/documents", json={"title": "Fake", "body": "x"}).json()
        assert fake_store.get(created["id"]) is not None   # it really used the fake
    finally:
        app.dependency_overrides.clear()
```

Observed: `POST /documents` → 201, unknown id → 404, `{"title": ""}` → 422 *"String should have at least 1 character"*.

## Sources I actually used
- FastAPI docs: request body, path parameters, `response_model`, `Depends`, `TestClient`
- `docuquery/src/docuquery/api.py`, `docuquery/tests/test_api.py`
