# Learning Log

One line per day: what I did, what broke, what I learned.

| Day | Date | Done | Broke / learned |
|---|---|---|---|
| 0 | 2026-09-09 | Setup: uv, Python 3.12, docuquery repo, .gitignore | |
| 1 | 2026-09-19 | Python idioms note → `can-explain`; 5 scratch scripts in docuquery; reviewed 5 roadmap videos (04-resource-reviews.md) | Planned 14 Sep, finished 19 Sep. Unsaved files ran as empty scripts. Hints are labels, not checks. |
| 2 | 2026-09-26 | Pydantic v2 note → `can-explain`; Invoice/LineItem models, field + model validators, 5 pytest tests green; plan switched to day numbers | Validators at column 0 are silently ignored — indentation is the code. Empty tests still pass. |
| 3 | 2026-09-28 | async/await note → `can-explain`; sequential vs gather vs blocking vs `to_thread` benchmark (25.4s → 4.2s) | httpbin noise reversed the result; isolated test showed 10.04s vs 1.01s. Coroutines don't start until awaited. |
| 4 | 2026-10-04 | FastAPI note → `can-explain`; /health, POST /documents, GET /documents/{id} with 404, Depends store, 5 TestClient tests (10 passing) | `=` vs `==` chained assignment broke a test; empty tests passed again; `.dict()` deprecated in Pydantic v2. |
