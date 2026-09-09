# Daily study guide — Day 1 to Day 90

The plan file (`03-90-day-daily-plan.md`) says *what* each day is. This says *how*.

For every day: what to read, what to build step by step, and the test for whether you can move on.
Each day names its note file in `notes/`. Open that file first and read its questions before you read any docs.

**Format:** `[45]` = 45 minutes learning, `[75]` = 75 minutes building. Long-block days say so.
**Rule:** if a day overruns, cut the build scope, not the "Done when" test.

---

## PHASE 1 — PYTHON + RAG (Days 1–30) — DocuQuery

### Day 1 — Mon 14 Sep — Python idioms
**Note:** `01-python-fastapi/python-idioms.md`

**Learn [45]** — Do not read a beginner tutorial. Read only for the deltas from PHP: snake_case naming, `None` vs null, truthiness of empty collections, f-strings, and why `is` is not `==`.

**Build [75]** — Five scripts in `docuquery/scratch/`, run each with `uv run python <name>.py`:
1. `file_io.py` — open a text file in a `with` block, count non-empty lines, write a summary file.
2. `comprehensions.py` — from a list of dicts, produce a filtered list and a keyed dict. No `append` anywhere.
3. `models.py` — a `@dataclass Order` with typed fields. Deliberately assign a string to the int field. Print it.
4. `parse.py` — `json.loads` a nested JSON string, reach a deep value, then catch the `KeyError` on a missing one.
5. `fetch.py` — `httpx.get("https://httpbin.org/json")`, print the status code and one field.

**Done when:** all five run, and you can say out loud why script 3 did not raise an error.
**Commit:** `chore: python setup + practice scripts`

### Day 2 — Tue 15 Sep — Pydantic v2
**Note:** `01-python-fastapi/pydantic.md`

**Learn [45]** — Pydantic docs: `BaseModel`, field types, `field_validator`, `model_validator`, `model_validate`, `model_dump`. This is yesterday's unenforced-annotations problem being solved.

**Build [75]**
1. `Invoice` with a nested `LineItem` list, `Decimal` money fields, and a date.
2. A `field_validator` rejecting a negative quantity.
3. A `model_validator` checking that line items sum to the total.
4. Five pytest tests: two valid cases, three that must raise `ValidationError`.
5. Print `Invoice.model_json_schema()` and keep the output. You will need it on Day 10.

**Done when:** `uv run pytest` is green and you can explain the difference between a field and a model validator.
**Commit:** `feat: pydantic models + tests`

### Day 3 — Wed 16 Sep — async / await
**Note:** `01-python-fastapi/async.md`

**Learn [45]** — The event loop, `async def`, `await`, `asyncio.gather`, `httpx.AsyncClient`. Key idea: concurrency here is cooperative and single-threaded. Nothing overlaps unless you await it together.

**Build [75]**
1. `fetch_sequential()` — await ten requests one after another, time it.
2. `fetch_concurrent()` — the same ten via `asyncio.gather`, time it.
3. Print both timings and the ratio.
4. Now add `time.sleep(1)` inside the concurrent version and re-time it. Understand why the gain disappears.

**Done when:** concurrent beats sequential by roughly the expected factor, and you can explain what step 4 proved.
**Commit:** `feat: async fetch benchmark`

### Day 4 — Thu 17 Sep — FastAPI core
**Note:** `01-python-fastapi/fastapi.md`

**Learn [45]** — FastAPI tutorial: path and query parameters, request bodies as models, `response_model`, and `Depends`. Treat `Depends` as the service container.

**Build [75]**
1. `POST /documents` taking a Pydantic body, returning a created model.
2. `GET /documents/{id}` returning 404 via `HTTPException` when missing.
3. `GET /health` returning a fixed payload.
4. An in-memory dict store injected with `Depends`.
5. Tests with `TestClient`, including one that overrides the store dependency with a fake.

**Done when:** tests pass, `/docs` renders your schema, and you have overridden a dependency in a test.
**Commit:** `feat: fastapi skeleton + tests`

### Day 5 — Fri 18 Sep — Docker + CI
**Note:** `01-python-fastapi/docker-ci.md`

**Learn [30]** — Multi-stage Dockerfiles and layer caching. The rule: copy the lockfile and install dependencies *before* copying source, so code edits do not bust the dependency layer.

**Build [90]**
1. Multi-stage Dockerfile using `uv`, non-root user, `EXPOSE 8000`.
2. `docker-compose.yml` with the API and a Postgres 16 service.
3. `docker compose up` and hit `/health` from the host.
4. `.github/workflows/ci.yml` running `ruff check` then `pytest` on push.
5. Push and watch it go green.

**Done when:** the Actions check is green on GitHub and the container serves `/health`.
**Commit:** `ci: docker + github actions`

### Day 6 — Sat 19 Sep — Postgres, Alembic, SSE (long block, 3–4h)
**Note:** `01-python-fastapi/sqlalchemy-alembic.md`

**Learn [45]** — SQLAlchemy 2.0 or SQLModel basics and the session lifecycle. Alembic is Laravel migrations.

**Build [rest]**
1. Define the `Document` table.
2. `alembic init`, autogenerate the first migration, read the generated file before running it.
3. `alembic upgrade head` against the compose Postgres.
4. Replace the in-memory store with a session-per-request dependency.
5. Add `GET /stream` returning a `StreamingResponse` that yields a fake token every 100ms in SSE format.
6. Watch it stream in the browser, token by token.

**Done when:** data survives `docker compose restart`, and the stream renders progressively rather than all at once.
**Commit:** `feat: postgres persistence + sse streaming`

### Day 7 — Sun 20 Sep — Consolidation (3h)
**Note:** `01-python-fastapi/project-structure.md`

No new topics. Make the week's code look like something you would hand to a colleague.
1. Split into `routers/`, `services/`, `models/`, `db/`.
2. Move all config to `pydantic-settings` reading from `.env`. Commit a `.env.example`, never the `.env`.
3. Write the "ten things Python does differently from PHP" list in your note file.
4. Three easy LeetCode problems in Python, arrays and strings.
5. Fill in the week's topic notes and run `python3 notes/build_index.py`.

**Done when:** five topic files from this week are at `learning` or better.
**Commit:** `refactor: project structure`

### Day 8 — Mon 21 Sep — Messages API
**Note:** `02-llm-apis/messages-api.md`

**Learn [45]** — Anthropic Messages API: message roles, the system prompt, `max_tokens`, `temperature`, and the usage block on the response. Find the current per-token prices for the model you pick.

**Build [75]**
1. `POST /chat` taking a prompt, calling Claude with a fixed system prompt.
2. Read `usage.input_tokens` and `usage.output_tokens` off the response.
3. Compute cost in USD from a price constant and store prompt, response, both token counts and cost in a `llm_calls` table.
4. Make ten calls of different lengths and query the table for total spend.

**Done when:** you can run one SQL query that tells you what today cost you.
**Commit:** `feat: /chat with token + cost logging`

### Day 9 — Tue 22 Sep — Streaming
**Note:** `02-llm-apis/streaming.md`

**Learn [30]** — The streaming event sequence and how to accumulate text deltas into a final message.

**Build [90]**
1. Convert `/chat` to stream, forwarding deltas over SSE.
2. A single static HTML page with a text box that renders the stream as it arrives.
3. Capture the final usage numbers *after* the stream completes and log them as on Day 8.
4. Kill the API mid-stream and see what the browser does. Handle it.

**Done when:** text appears progressively, and cost logging still works for streamed calls.
**Commit:** `feat: streaming chat`

### Day 10 — Wed 23 Sep — Tool calling and structured output
**Note:** `02-llm-apis/tool-calling.md`

**Learn [45]** — Tool use docs, and `model_json_schema()` from Day 2. This is the single most important day of week 2. Every later project depends on reliable structured output.

**Build [75]**
1. Define `Person{name, email, company}` in Pydantic.
2. Pass its JSON schema as a tool definition.
3. Endpoint takes free text, returns a validated `Person`.
4. On `ValidationError`, retry once with the error message fed back into the conversation.
5. Feed it deliberately bad input (no email present) and see what it does.

**Done when:** a malformed first attempt recovers on the retry, and you have a log line proving it happened.
**Commit:** `feat: structured extraction via tool calling`

### Day 11 — Thu 24 Sep — Reliability
**Note:** `02-llm-apis/reliability.md`

**Learn [30]** — Which errors are retryable (429, 5xx, timeouts) and which are not (400, 401). Exponential backoff with jitter. What prompt caching caches and what invalidates it.

**Build [90]**
1. An `LLMClient` wrapper class. All calls go through it from now on.
2. `tenacity` retry with exponential backoff and jitter, retrying only on the right exception types.
3. An explicit request timeout.
4. Prompt caching on the long system prompt.
5. Tests with a mocked client: one asserting a retry happened, one asserting a 400 did *not* retry.

**Done when:** tests pass without a single real API call.
**Commit:** `feat: llm client wrapper with retries + caching`

### Day 12 — Fri 25 Sep — Embeddings
**Note:** `02-llm-apis/embeddings.md`

**Learn [45]** — What an embedding is, why cosine similarity is meaningful, and how chunk size cuts both ways. Read the pgvector README today, before you need it tomorrow.

**Build [75]**
1. Twenty sentences: five clearly about one topic, five about another, ten deliberately ambiguous.
2. Embed with `text-embedding-3-small`.
3. Compute and print the 20x20 cosine similarity matrix.
4. Repeat with `bge-m3` via `sentence-transformers`.
5. Write down one pair the hosted model ranked differently from the open one.

**Done when:** you can point at the matrix and explain one surprising result.
**Commit:** `feat: embedding experiments`

### Day 13 — Sat 26 Sep — pgvector (long block, 3–4h)
**Note:** `02-llm-apis/pgvector.md`

**Build**
1. `CREATE EXTENSION vector` in your compose Postgres, via an Alembic migration.
2. A `chunks` table: text, embedding `vector(1536)`, source path, start line, end line.
3. Clone the FastAPI repo somewhere local.
4. Ingest its markdown with a naive recursive splitter, embed, and insert.
5. Add an HNSW index. Time one query before and after adding it.
6. `POST /search` returning top-k by cosine distance with source metadata.

**Done when:** a search for "dependency injection" returns plausible FastAPI docs chunks, and you recorded the before/after index timing.
**Commit:** `feat: pgvector ingestion + vector search`

### Day 14 — Sun 27 Sep — Prompting patterns (3h)
**Note:** `02-llm-apis/prompting.md`

**Learn [60]** — Few-shot vs instructions, output schemas, and the grounded-answer pattern: answer only from the provided context, and say "I don't know" otherwise.

**Build [60]**
1. Write the DocuQuery answer prompt. Context chunks go in delimited blocks with their path and line range.
2. Require citations in a strict `[path:line]` format.
3. Test it three ways: a question the context answers, one it does not, and one where the context is subtly wrong.
4. Iterate until case two reliably refuses.

Then three LeetCode problems on hash maps.
**Done when:** the refusal case refuses five times out of five.
**Commit:** `feat: answer prompt v1`

### Day 15 — Mon 28 Sep — Ingestion with metadata
**Note:** `03-rag/ingestion.md`

**Build**
1. Ingest the FastAPI repo's `docs/` markdown *and* its `.py` source.
2. Store per chunk: path, start line, end line, and type (doc or code).
3. Make re-ingestion idempotent. Use a content hash so a second run does not duplicate rows.
4. Verify: run the ingest twice, confirm the row count is unchanged.

**Done when:** the second ingest adds zero rows and line numbers point at the right source lines.
**Commit:** `feat: ingest docs + source with line metadata`

### Day 16 — Tue 29 Sep — Code-aware chunking
**Note:** `03-rag/chunking.md`

**Learn [30]** — Recursive, heading-based, and AST-based chunking, and what each one preserves.

**Build [90]**
1. Heading-based splitter for markdown, keeping the heading trail on each chunk.
2. AST-based splitter for Python using the `ast` module, one chunk per function or class, keeping the real line numbers.
3. Print a comparison: chunk count, mean size, and max size for naive vs smart.
4. Re-ingest with the new splitters.

**Done when:** you have the comparison table in your note file.
**Commit:** `feat: code-aware chunking`

### Day 17 — Wed 30 Sep — Hybrid search
**Note:** `03-rag/hybrid-search.md`

**Learn [30]** — BM25, and Postgres `tsvector` full-text search. Vectors find paraphrase; keywords find exact identifiers. A code search needs both.

**Build [90]**
1. Add a `tsvector` column and GIN index, or use `rank_bm25` in Python.
2. Keyword search returning top-20.
3. Fuse the two rankings with Reciprocal Rank Fusion.
4. Find one query where keyword wins outright (an exact function name) and one where vector wins (a conceptual question). Record both.

**Done when:** you have those two concrete example queries written down.
**Commit:** `feat: hybrid search (RRF)`

### Day 18 — Thu 1 Oct — Re-ranking
**Note:** `03-rag/reranking.md`

**Learn [30]** — Bi-encoder vs cross-encoder. The cross-encoder reads query and document together, which is why it is better and why it cannot be pre-computed.

**Build [90]**
1. Retrieve top-20 from hybrid search.
2. Rerank with Cohere Rerank or a local `bge-reranker`, take top-5.
3. Log which retrieval stage produced each surviving chunk.
4. Measure added latency per query.

**Done when:** you can state the latency cost of reranking in milliseconds.
**Commit:** `feat: reranking`

### Day 19 — Fri 2 Oct — End-to-end answers
**Note:** `03-rag/citations.md`

**Build**
1. Wire retrieve, rerank, prompt, and stream into one endpoint.
2. Parse `[path:line]` citations out of the answer.
3. Validate every citation against the chunks actually retrieved. Drop any the model invented.
4. Render citations as GitHub blob URLs with the line anchor.

**Done when:** clicking a citation lands on the right line on GitHub, and an invented citation gets dropped rather than shown.
**Commit:** `feat: end-to-end RAG answers with citations`

### Day 20 — Sat 3 Oct — UI and deploy (long block, 4h)
**Note:** `03-rag/deployment.md`

**Build**
1. Minimal chat UI in Vue or plain HTML: question box, streamed answer, clickable citations.
2. A "with RAG / without RAG" toggle. This is what sells the project in ten seconds.
3. Supabase Postgres with pgvector, run migrations, re-ingest.
4. Deploy the API. Set secrets as environment variables.
5. Open the live URL in a private window and use it as a stranger would.

**Done when:** first click works with no login, no cold-start wait, and no console errors.
**Commit:** `feat: web ui + deploy`

### Day 21 — Sun 4 Oct — Framework comparison (3h)
**Note:** `03-rag/frameworks.md`

**Build [90]** — Rebuild only the retrieval step with LlamaIndex or LangChain, in a separate module, behind the same interface. Keep both. Then write, specifically: what it abstracted, what you can no longer see, and how many lines it saved.

Three LeetCode problems.
**Done when:** the "what the framework hides" note is written and both paths still work.
**Commit:** `docs: framework comparison`

### Day 22 — Mon 5 Oct — Golden dataset
**Note:** `03-rag/golden-datasets.md`

This day is usually underestimated. If it overruns, take it into the evening; do not shorten it.

**Build** — 50 questions in `evals/golden.jsonl`, each with question, reference answer, and expected source files. Mix deliberately:
- 20 factual, answerable from one chunk
- 15 how-to, needing two or more chunks
- 10 not in the docs, where the correct answer is a refusal
- 5 ambiguous or badly worded, like real users write

**Done when:** the file has 50 lines and the refusal cases are genuinely unanswerable from the corpus.
**Commit:** `test: golden eval set`

### Day 23 — Tue 6 Oct — RAGAS baseline
**Note:** `03-rag/ragas.md`

**Learn [30]** — Define all four metrics precisely: faithfulness, answer relevancy, context precision, context recall. Know which one moves when retrieval breaks and which when generation breaks.

**Build [90]**
1. An eval runner reading the golden file and running the live pipeline.
2. Score with RAGAS.
3. Save to `evals/results/baseline.json` with a timestamp and the config used.
4. Never overwrite a results file. Every run is a new one.

**Done when:** you have four baseline numbers and can say which is weakest.
**Commit:** `test: ragas baseline`

### Day 24 — Wed 7 Oct — LLM judge and refusal accuracy
**Note:** `03-rag/llm-judge.md`

**Build**
1. A judge scoring answer correctness 1 to 5 against the reference, with a rubric in the prompt.
2. Refusal accuracy over the 10 unanswerable questions: how often did it correctly decline?
3. Hand-grade 10 answers yourself and compare to the judge. Record the disagreement rate.

**Done when:** you know your judge's disagreement rate with your own grading. Without that number the judge is decoration.
**Commit:** `test: llm judge + refusal metrics`

### Day 25 — Thu 8 Oct — Langfuse
**Note:** `03-rag/observability.md`

**Learn [30]** — Traces and spans, and what to attach to each.

**Build [90]**
1. Wrap each pipeline stage in a span: retrieve, rerank, generate.
2. Attach retrieved chunk ids, token counts, cost and latency.
3. Tag eval runs so they are filterable separately from real traffic.
4. Deliberately break retrieval, run one query, and find the fault in the Langfuse UI.

**Done when:** you found a bug you planted using only the trace view.
**Commit:** `feat: langfuse tracing`

### Day 26 — Fri 9 Oct — Tuning round 1
**Note:** `03-rag/tuning.md`

Change one variable at a time. Six runs:
| Run | Chunk size | Top-k | Rerank |
|---|---|---|---|
| 1 | small | 5 | no |
| 2 | small | 5 | yes |
| 3 | small | 10 | yes |
| 4 | large | 5 | yes |
| 5 | large | 10 | yes |
| 6 | best of above, tweaked | | |

**Done when:** a table in your note file shows all six with their four RAGAS scores, and you can name the winner.
**Commit:** `test: tuning round 1 results`

### Day 27 — Sat 10 Oct — Tuning round 2 (long block, 4h)
**Note:** `03-rag/tuning.md`

1. Add query rewriting, either HyDE or multi-query. Measure it against the Day 26 winner.
2. Cache repeated identical queries.
3. Take the five worst failures from the eval run, diagnose each one, and fix what you can.
4. Re-run the full eval.

**Done when:** you can say which single change moved the numbers most, with the delta.
**Commit:** `feat: query rewriting + fixes`

### Day 28 — Sun 11 Oct — README (3h)
1. Two-line problem statement at the very top.
2. Numbers table, baseline against final, all four metrics plus latency and cost per query.
3. Architecture diagram in Mermaid.
4. "What failed and what I changed", with the three real failures.
5. Stack list naming exact model versions and the vector store.
6. Three LeetCode problems.

**Done when:** a stranger reading only the first screen knows what it does and how well.
**Commit:** `docs: README v1`

### Day 29 — Mon 12 Oct — Demo and hardening
1. Record 90 seconds: problem, one query, citations, the RAG toggle, the eval table.
2. Rate limiting on the public endpoint so the demo cannot drain your API budget.
3. Click through the live URL on your phone.
4. Fix every first-click bug you find.

**Commit:** `chore: demo + rate limiting`

### Day 30 — Tue 13 Oct — Blog post and Phase 1 checkpoint
Draft and publish: "Building a RAG system over the FastAPI codebase: what the evals taught me." Lead with the numbers table, be honest about what failed. Post to LinkedIn with the demo link.

**Checkpoint:** live URL, repo with tests and evals, blog post published. Fill in `projects/docuquery.md` completely today, while every number is fresh.

---

## PHASE 2 — AGENTS (Days 31–60) — SupportPilot

### Day 31 — Wed 14 Oct — The agent loop, by hand
**Note:** `04-agents/agent-loop.md`

**Learn [60]** — Read Anthropic's "Building Effective Agents". The most valuable idea in it is that most problems are workflows, not agents. Write ten bullets, and make at least three of them about when *not* to use an agent.

**Build [60]** — A bare loop in plain Python, no framework:
1. Two tools: calculator and current time, each a normal function with a JSON schema.
2. Loop: call the model, if it requests a tool then run it and append the result, else return.
3. Hard cap of five iterations.
4. Print every step so you can watch it think.
5. Give it a question needing both tools in sequence.

**Done when:** you can draw the loop on paper from memory.
**Commit:** `feat: raw agent loop`

### Day 32 — Thu 15 Oct — LangGraph
**Note:** `04-agents/langgraph.md`

**Learn [45]** — `StateGraph`, nodes, edges, conditional edges, and how state is merged between nodes.

**Build [75]** — Rebuild yesterday's loop as a graph. Keep yesterday's version. Then answer in your note file: what did the graph give you that the while loop did not?

**Done when:** both implementations pass the same test prompt and you can name the real difference.
**Commit:** `feat: langgraph agent loop`

### Day 33 — Fri 16 Oct — Checkpointing
**Note:** `04-agents/checkpointing.md`

**Learn [30]** — Checkpointers and threads.

**Build [90]**
1. Wire the Postgres checkpointer.
2. Run a conversation, stop the process entirely, restart, and resume by thread id.
3. Inspect the checkpoint rows in Postgres and see exactly what was stored.

**Done when:** a conversation survives a full process restart, and you can describe what is in a checkpoint row.
**Commit:** `feat: checkpointing`

### Day 34 — Sat 17 Oct — Three-tool agent (long block, 4h)
1. Tools: web search via Tavily, calculator, and `ask_docuquery` calling your live Project 1 endpoint.
2. **Add a local fallback for `ask_docuquery`** so this day is not blocked if Project 1 is down. The plan does not mention this and it is a real dependency risk.
3. Langfuse tracing on every node.
4. Ten test prompts. Record which tool it chose for each and whether that was right.

**Done when:** you have a ten-row table of prompt against tool chosen, and at least one wrong choice you can explain.
**Commit:** `feat: 3-tool agent with tracing`

### Day 35 — Sun 18 Oct — Human in the loop (3h)
**Note:** `04-agents/hitl.md`

**Build [90]** — An `interrupt` before a tool marked dangerous. The graph pauses, a CLI prompt asks you, and the graph resumes with your decision. Test rejecting as well as approving.

**Notes [30]** — Five real examples from your past jobs where an agent would have been the wrong choice and a plain workflow was right. These are interview gold.

Three LeetCode problems.
**Commit:** `feat: hitl interrupt`

### Day 36 — Mon 19 Oct — Schema
New repo `supportpilot`. Tables: customers, orders, order_items, shipments, refunds, tickets, ticket_messages, audit_log. The audit log matters more than it looks; it is what makes the money-moving tools defensible in an interview.
**Done when:** the Alembic migration runs clean on an empty database.
**Commit:** `feat: schema`

### Day 37 — Tue 20 Oct — Seed data
50 customers, 200 orders, 40 tickets. The ticket mix is the whole value of this project, so build it deliberately:
- 15 easy, "where is my order"
- 10 refund requests, some above the $50 threshold
- 8 ambiguous, where the right move is to ask or escalate
- 7 adversarial: prompt injection, abuse, and out-of-scope requests

Write the expected correct action for each ticket now, in the seed file. That is your eval label set, and writing it later biases it.
**Done when:** all 40 tickets have an expected action recorded.
**Commit:** `feat: seed data`

### Day 38 — Wed 21 Oct — Backend API
Plain FastAPI CRUD over orders, shipments, refunds, tickets, with tests. No AI today. This is the boring day that makes the rest possible.
**Commit:** `feat: support backend api`

### Day 39 — Thu 22 Oct — Tools with scopes
**Note:** `04-agents/tool-design.md`

Five tools: `lookup_order`, `get_shipping_status`, `issue_refund`, `escalate`, `draft_reply`. For each: a Pydantic argument schema, a docstring the model will actually read, and an audit log row on every call.

The `$50` refund cap goes in the function body, not the prompt. Write a test that calls `issue_refund` with `$500` directly and asserts it is rejected. That test is the point of the whole day.
**Done when:** the cap holds even when the tool is called directly, bypassing the model.
**Commit:** `feat: agent tools`

### Day 40 — Fri 23 Oct — Agent graph v0
Nodes: classify_ticket, gather_context, decide, act or escalate, draft_reply. The system prompt carries the support policy. Run it on five tickets and read every trace.
**Done when:** five tickets produce five plausible drafts, and you have read the full trace of each.
**Commit:** `feat: agent graph v0`

### Day 41 — Sat 24 Oct — MCP server (long block, 4h)
**Note:** `04-agents/mcp.md`

**Learn [45]** — MCP Python SDK quickstart. Understand what it adds over just calling your functions: a standard protocol so any client can discover and call them.

**Build [rest]**
1. Expose the five tools over stdio.
2. Connect from Claude Desktop or Claude Code.
3. Resolve a real ticket through the MCP connection.
4. Record a GIF. This goes in the README and it is disproportionately impressive.

**Done when:** the GIF exists and shows a ticket being resolved end to end.
**Commit:** `feat: mcp server`

### Day 42 — Sun 25 Oct — Baseline run (3h)
Run all 40 tickets. Save every output. Grade by hand: correct action, correct escalation, reply quality 1 to 5. Do not skip the hand-grading; it is what teaches you the failure modes.

Three LeetCode problems.
**Done when:** you have a 40-row baseline table and a first impression of where it fails.
**Commit:** `test: baseline run`

### Day 43 — Mon 26 Oct — Approvals
Refund over $50 triggers `interrupt`, writes a pending row, and waits. An `/approvals` page lists them with approve and reject buttons. Approving resumes the graph.
**Done when:** an over-threshold refund pauses, survives an API restart while pending, and completes after you approve it in the UI.
**Commit:** `feat: approval workflow`

### Day 44 — Tue 27 Oct — Prompt injection
**Note:** `04-agents/prompt-injection.md`

**Learn [30]** — Indirect injection specifically: the attack arrives inside data your tools return, not in the user's message.

**Build [90]**
1. Wrap all tool output in delimiters, framed explicitly as data and not instructions.
2. Add a classifier step over incoming ticket text.
3. Run the seven adversarial tickets and record which defenses stopped which attack.
4. Then try to beat your own defenses. Write down anything that still gets through.

**Done when:** you have an honest list of what still works against you. Claiming full protection here fails interviews.
**Commit:** `feat: injection defenses`

### Day 45 — Wed 28 Oct — Output guardrails
**Note:** `04-agents/guardrails.md`

Regex for emails, phone numbers and card numbers, plus an LLM tone check on every draft. On failure, block and regenerate once. Redact PII before it reaches Langfuse.
**Done when:** a deliberately rude draft is caught and regenerated, and no PII appears in a trace.
**Commit:** `feat: output guardrails`

### Day 46 — Thu 29 Oct — Memory
**Note:** `04-agents/memory.md`

Thread state per ticket for the short term. A rolling customer history summary in Postgres for the long term, injected into context. Test on a customer with three previous tickets.
**Done when:** the agent references a prior interaction correctly without the full history in context.
**Commit:** `feat: customer memory`

### Day 47 — Fri 30 Oct — Model routing
**Note:** `04-agents/model-routing.md`

A cheap model for classification, a strong one for decisions. Add a confidence field to the structured output and escalate to the strong model below a threshold. Then measure: did total cost per ticket actually fall, or did you just double the calls? Report the real number either way.
**Done when:** you have before and after cost per ticket.
**Commit:** `feat: model routing`

### Day 48 — Sat 31 Oct — UI and deploy (long block, 4h)
Inbox list, per-ticket agent trace, approve and reject, and the audit log view. Deploy API and database. Check the live URL cold.
**Commit:** `feat: ui + deploy`

### Day 49 — Sun 1 Nov — Reliability (3h)
**Note:** `04-agents/agent-reliability.md`

Timeouts, max iterations, retries, rate limiting, and idempotency on `issue_refund` via an idempotency key. Write the test that calls the refund twice with the same key and asserts one refund.

Three LeetCode problems.
**Done when:** the double-refund test passes.
**Commit:** `feat: reliability`

### Day 50 — Mon 2 Nov — Eval harness
**Note:** `04-agents/agent-evals.md`

A script over all 40 tickets computing: task success rate, escalation precision and recall, mean steps, cost per ticket, and p50 and p95 latency. Escalation precision and recall matter separately, because over-escalating and under-escalating fail in opposite directions.
**Done when:** one command prints all six numbers.
**Commit:** `test: agent eval harness`

### Day 51 — Tue 3 Nov — Failure catalogue
Group every failure: wrong tool, hallucinated order id, blocked over-refund, injection succeeded, wrong escalation. Count each. Fix the top three.
**Done when:** the catalogue has counts, not adjectives.
**Commit:** `fix: top failure modes`

### Day 52 — Wed 4 Nov — Re-run
Re-run the harness. Produce the before and after table. If a number got worse, keep it in the table and explain it. That honesty reads as senior.
**Commit:** `test: v1 results`

### Day 53 — Thu 5 Nov — Security section and diagrams
Write "Security and failure modes" in the README: what an attacker can try, what stops them, and what you know is still open. Add the LangGraph state diagram and a sequence diagram of an approval.
**Commit:** `docs: security + diagrams`

### Day 54 — Fri 6 Nov — README and video
Full README with the numbers table, plus the 90-second demo. Show the approval interrupt on camera; it is the most distinctive thing in the project.
**Commit:** `docs: README v1`

### Day 55 — Sat 7 Nov — Blog post (3h)
"Building a bounded support agent: approvals, guardrails, and what the evals showed." Publish and post.

### Day 56 — Sun 8 Nov — Interview practice (3h)
Record yourself, two minutes each, no notes: RAG pipeline, hybrid search, reranking, agent versus workflow, human in the loop, prompt injection. Play it back. The parts where you waffle are the topic files to reopen.

Three LeetCode problems.

### Days 57–60 — Mon 9 Nov to Thu 12 Nov — Buffer
Finish anything that slipped. If genuinely on track: Langfuse dashboards, a cost-per-resolved-ticket chart, and start one LeetCode medium daily.

**Phase 2 checkpoint:** two live projects, an MCP server, two blog posts.

### Rest weekend — Fri 13 to Sun 15 Nov
The only scheduled break. Take it. Phase 3 is the most tedious stretch of the plan and you should not start it tired.

---

## PHASE 3 — EXTRACTION + AWS (Days 61–75) — ExtractIQ

### Day 61 — Mon 16 Nov — Schema and dataset
New repo `extractiq`.

1. The `Invoice` Pydantic schema: vendor, invoice number, date, due date, currency, line items, subtotal, tax, total. Money as `Decimal`, never float.
2. Reconciliation validators: line items sum to subtotal, subtotal plus tax equals total, within a small tolerance.
3. Start gathering 60 invoices: public datasets, 15 you generate with varied layouts, 5 scanned or blurry, 5 Thai or Burmese.

Gathering will take longer than the schema. If you only finish 30 today, that is fine; keep collecting in the background all week.
**Commit:** `feat: schema + dataset`

### Day 62 — Tue 17 Nov — Vision extraction
**Note:** `05-extraction-aws/vision-extraction.md`

**Learn [30]** — Vision input: PDF and image handling, and how page resolution drives token cost.

**Build [90]**
1. PDF to images with `pdf2image`.
2. Send a page to Claude with the Day 61 schema as a tool.
3. Run it on five documents and read every output against the source by eye.
4. Try one page at two different resolutions and compare both accuracy and cost.

**Done when:** five documents extract, and you know what resolution costs you.
**Commit:** `feat: vision extraction v0`

### Day 63 — Wed 18 Nov — Validation and retry
**Note:** `05-extraction-aws/validation-retry.md`

1. Run the reconciliation validators on every extraction.
2. On failure, retry with the specific validation errors in the prompt. Maximum two retries.
3. After the final failure, mark the document for human review rather than storing a wrong answer.
4. Log how often retry rescued a document. If it is near zero, the retry is not worth its cost and you should say so.

**Done when:** you have the retry rescue rate as a number.
**Commit:** `feat: validate + retry`

### Day 64 — Thu 19 Nov — Async pipeline
Upload endpoint, background task, status endpoint. Store the raw model response alongside the parsed result, plus tokens, cost and a confidence value. Keeping the raw response is what lets you debug an extraction three weeks later.
**Commit:** `feat: async pipeline`

### Day 65 — Fri 20 Nov — Labeling
**Note:** `05-extraction-aws/accuracy-metrics.md`

Hand-label 50 documents into ground-truth JSON. This is the single most tedious day in the plan and the one that makes the project credible. Nobody else's portfolio has real labels.

**Realistic estimate: five hours, not two.** Move it to a weekend block if your Friday is short. Label without looking at model output, otherwise you will anchor to it.
**Done when:** 50 ground-truth files exist and none were copied from a model response.
**Commit:** `test: ground truth labels`

### Day 66 — Sat 21 Nov — Accuracy report (long block, 4h)
1. Per-field exact match.
2. Per-field normalized match, ignoring whitespace and number formatting. Report both, because the gap between them tells you how much is a formatting problem rather than a reading problem.
3. Line-item F1, since count and order can both be wrong.
4. Document-level "every field correct" percentage. This will be much lower than per-field accuracy and that is the honest headline.
5. Run the whole thing across two models. Table it with cost and latency.

**Done when:** the README table shows both models across all four metrics.
**Commit:** `test: accuracy report`

### Day 67 — Sun 22 Nov — Dashboard (3h)
Upload, processing status, extracted fields with confidence, and low-confidence fields flagged for review. The review flag is the product idea: nobody trusts blind extraction.

Three LeetCode problems.
**Commit:** `feat: dashboard`

### Day 68 — Mon 23 Nov — Improvements
**Note:** `05-extraction-aws/ocr-fallback.md`

Take the worst failures from Day 66 and fix them: unusual layouts, multi-page invoices, Thai text. Add a Tesseract OCR fallback for scans. Re-run the full report and keep both sets of numbers.
**Done when:** the before and after table exists, including anything that got worse.
**Commit:** `feat: improvements + rerun`

### Day 69 — Tue 24 Nov — AWS foundations
**Note:** `05-extraction-aws/aws-deploy.md`

**Learn [60]** — Account, IAM user with least privilege, ECR, App Runner or ECS Fargate, RDS. **Set a billing alarm today, before you deploy anything.** App Runner has no free tier and RDS free tier only lasts twelve months on a new account.

**Build [60]** — Build the image and push it to ECR.
**Commit:** `ci: ecr push`

### Day 70 — Wed 25 Nov — Deploy
RDS Postgres, App Runner service pulling from ECR, secrets in Secrets Manager or Parameter Store, S3 for uploads with a private bucket policy. Confirm the service reads its secrets at runtime rather than baking them into the image.
**Done when:** the live AWS URL processes an uploaded invoice end to end.
**Commit:** `infra: aws deploy`

### Day 71 — Thu 26 Nov — Production hygiene
**Note:** `05-extraction-aws/prod-observability.md`

Sentry, structured JSON logs with a request id, a `/health` that checks the database but never checks a third-party API, and a CloudWatch alarm on 5xx. Decide explicitly what would page a human and what is dashboard-only.
**Commit:** `feat: observability`

### Day 72 — Fri 27 Nov — Bedrock and cost
**Notes:** `05-extraction-aws/bedrock.md`, `05-extraction-aws/cost-modeling.md`

**Learn [60]** — Read the Bedrock and Azure OpenAI docs, then actually run one extraction through Bedrock so you can say you have used it. Understand why enterprises want it: data residency, existing cloud contracts, and no new vendor review.

**Build [60]** — Cost per 1,000 documents at each model, broken down so the dominant term is visible. Add it to the README.
**Commit:** `docs: bedrock + cost model`

### Day 73 — Sat 28 Nov — README and video (long block, 4h)
Accuracy table, infra diagram, cost table, an explicit limitations section, and "what failed". The limitations section is what makes a skeptical reader trust the rest. Then the 90-second video.
**Commit:** `docs: README v1`

### Day 74 — Sun 29 Nov — Blog post (3h)
"Invoice extraction with LLMs: measuring field-level accuracy across two models." Lead with the document-level number, not the flattering per-field one.

Three LeetCode problems.

### Day 75 — Mon 30 Nov — Consolidate
Either redeploy Projects 1 and 2 to AWS, or add an AWS section to their READMEs explaining how you would. Then open all three live URLs cold and fix anything that does not work on the first click.

**Phase 3 checkpoint:** three live projects, three blog posts, AWS on the resume.

---

## PHASE 4 — PORTFOLIO AND APPLICATIONS (Days 76–90)

These days are execution, not learning, so the detail below is thinner on purpose. The work is real but it does not need study notes.

### Day 76 — Tue 1 Dec — GitHub profile
Profile README with all three projects: one screenshot, one live link, and one number each. Pin the three repos. Archive or add a README to old repos, because recruiters do look.

### Day 77 — Wed 2 Dec — Resume, AI version
Single column, contact details in the body, no icons or sidebars or tables, because parsers mangle them. Title: "AI Engineer — LLM Applications (RAG, Agents)". Every AI bullet cites a project and a number, and names model versions, the vector store, and eval scores. Cut "AI Builder", "99.9% uptime" and "200h/mo saved". Keep "8,000+ DAU" because an employer can verify it.

### Day 78 — Thu 3 Dec — Resume, full-stack version, plus ATS check
Second version headed "Full-Stack Engineer (Laravel/Vue · Python · AI)". Run both through a free ATS parser and fix anything that comes out garbled.

### Day 79 — Fri 4 Dec — LinkedIn and site
Headline, About, Featured with the three demos, and a projects page on your own site.

### Day 80 — Sat 5 Dec — Interview prep, concepts (long block, 4h)
Open `notes/06-interview/concept-answers.md`. If you have been filling it in weekly as intended, today is a review rather than a scramble. Any question still blank goes back to its topic file.

### Day 81 — Sun 6 Dec — Interview prep, system design (3h)
Three 30-minute whiteboard designs from `notes/06-interview/system-design.md`. Time yourself strictly. Always cover evals and cost, because most candidates do not.

### Day 82 — Mon 7 Dec — Coding practice
Two hours of LeetCode mediums in Python: arrays, hash maps, two pointers. Timed.

### Day 83 — Tue 8 Dec — Target list
60 companies in a spreadsheet: 20 Thailand, 20 Dubai and Abu Dhabi, 15 remote-first, 5 Germany. Columns: role, link, which project matches, visa note, status, date applied.

### Day 84 — Wed 9 Dec — Applications, batch 1
Ten tailored applications. Each gets the right resume version and a three-line note linking the single most relevant project. Answer visa and location questions honestly; being filtered early is cheaper than being filtered at offer stage.

### Day 85 — Thu 10 Dec — Mock interview 1
Sixty minutes: behavioural plus three technical questions. Note the weak answers and fix them tomorrow.

### Day 86 — Fri 11 Dec — Applications, batch 2
Ten more. Then message five people at target companies with a short, specific note referencing one project and one number.

### Day 87 — Sat 12 Dec — Referrals and the FDE angle (long block, 4h)
Contact recruiters posting Forward Deployed Engineer and AI Engineer roles in Bangkok, Singapore and Dubai. Publish a LinkedIn article comparing the eval results across your three projects; that comparison is something almost no other candidate can write.

### Day 88 — Sun 13 Dec — Mock interview 2 (3h)
System design mock, plus three mediums.

### Day 89 — Mon 14 Dec — Applications, batch 3
Ten more. Review which roles replied and adjust the resume wording toward what is working.

### Day 90 — Tue 15 Dec — Retrospective
What worked, response rate per market, and your weakest interview topic. Then plan the next 30 days: ten applications a week, one LeetCode a day, and pick one project to get real users. Offer DocuQuery to an open-source maintainer or ExtractIQ to a small business.

---

## The thing this guide cannot do for you

Your own market review says that after 90 days you will have roughly 0.3 years of LLM experience against a bar that commonly asks for one. Three portfolio projects narrow that gap but do not close it.

The one thing that does close it is shipping an LLM feature at your current job, because employer-verified experience outranks any side project. The plan mentions this once, in a habits list. Treat it as a fourth project: find the opportunity during Phase 1, propose it during Phase 2, and ship it before Day 90.
