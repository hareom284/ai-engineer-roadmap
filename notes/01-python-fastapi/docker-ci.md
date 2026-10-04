# Docker + GitHub Actions

**Plan day:** Day 5 · **Status:** `learning`
_Status values: `not-started` → `learning` → `can-explain`. You are done when you can answer every question below out loud, without notes, in under two minutes each._

## In my own words
_One paragraph for a senior engineer who has never used this. No jargon you cannot define._

_(Written during the Day 5 session, 2026-10-04. Answer the three questions out loud before moving this to `can-explain`.)_

A multi-stage build uses one image to **build** (it needs `uv`, compilers, caches) and a second clean image to **run** (it gets only the finished `.venv` and `src/`). The runtime image stays small — 275MB here — and ships no build tools for an attacker to use. Layer order is what makes rebuilds fast: `COPY pyproject.toml uv.lock README.md ./` and `uv sync` come **before** `COPY src/`, because dependencies change rarely and source changes constantly; put source first and every one-character edit re-downloads every package. CI runs the same two commands I run locally — `ruff check .` then `pytest -q`, lint first because it fails in seconds — and both block the merge.

## Must be able to answer
- [ ] Why multi-stage, and what belongs in each stage?
- [ ] How do you order Dockerfile steps so dependency layers stay cached?
- [ ] What should CI block a push on, and what should only warn?

### Checks that prove it works
| Check | Command | Expected |
|---|---|---|
| image builds | `docker build -t docuquery .` | no error |
| serves traffic | `curl localhost:8000/health` | `{"status":"ok"}` |
| not root | `docker run --rm docuquery whoami` | `appuser` |
| API + DB together | `docker compose up --build`, `docker compose ps` | 2 services, `db` healthy |
| CI will pass | `uv run ruff check . && uv run pytest -q` | clean, 10 passed |

## Gotchas / what bit me
_Anything that cost you more than fifteen minutes. These become interview stories._

- **The container only has what you `COPY` in.** The build failed with ``failed to open file `/app/README.md` `` even though README.md was sitting in the project. `pyproject.toml` has `readme = "README.md"`, so the packaging step needs it — but the Dockerfile only copied `pyproject.toml` and `uv.lock`. My Mac's files are not the build context.
- **YAML indentation is structure, like Python.** Steps indented 8 spaces instead of 6 gave `expected <block end>, but found '-'`, then `run:` at 10 instead of 8 gave `mapping values are not allowed here`. Check before pushing: `python -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))"`.
- **A linter is advice, not law — decide per warning.** `ASYNC251 Async functions should not call time.sleep` was correct but the code was a deliberate experiment → `# noqa: ASYNC251` *with a reason*. `B008 Do not perform function call in argument defaults` was a false positive for FastAPI → rewrote it the modern way with `Annotated` instead of silencing the rule.
- **`.env` was untracked and not in `.gitignore`**, so `git add .` would have committed it. Mine was empty, but from Day 8 it holds an API key. Added `.env` to `.gitignore` plus a committed `.env.example`. A secret committed once lives in git history forever.
- Inside a container, bind to `0.0.0.0`, not `127.0.0.1` — otherwise the port mapping reaches nothing. Inside a compose network, the DB hostname is the **service name** (`db`), not `localhost`.

## Minimal snippet
_The smallest code that demonstrates the idea. Typed by you, not pasted._

The caching rule — dependencies before source:

```dockerfile
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder
WORKDIR /app
COPY pyproject.toml uv.lock README.md ./      # rarely changes -> layer stays cached
RUN uv sync --locked --no-dev --no-install-project
COPY src/ ./src/                              # changes constantly -> last
RUN uv sync --locked --no-dev

FROM python:3.12-slim-bookworm AS runtime     # clean image: no uv, no build tools
RUN useradd --create-home --uid 1000 appuser
COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv
COPY --from=builder --chown=appuser:appuser /app/src /app/src
ENV PATH="/app/.venv/bin:$PATH"
USER appuser
CMD ["uvicorn", "docuquery.api:app", "--host", "0.0.0.0", "--port", "8000"]
```

`--locked` fails if `uv.lock` disagrees with `pyproject.toml` — like `composer install`, never a silent upgrade.

FastAPI dependency without the B008 warning:

```python
StoreDep = Annotated[InMemoryStore, Depends(get_store)]

def read_document(doc_id: str, store: StoreDep) -> DocumentOut: ...
```

## Sources I actually used
- uv Docker integration guide; Docker multi-stage build docs
- GitHub Actions workflow syntax; `astral-sh/setup-uv`
- `docuquery/Dockerfile`, `compose.yaml`, `.github/workflows/ci.yml`
