# 90-Day AI Engineer Plan — Day by Day

**Commitment:** 2 hours every weekday, 3–4 hours Saturday and Sunday (~16 hrs/week, ~200 hrs total).
**Dates:** Day 1 = Mon 2026-09-14 · Day 90 = Tue 2026-12-15. Every day header carries its real date. One rest weekend falls between Day 60 and Day 61 (Fri 13 – Sun 15 Nov), so the plan spans 93 calendar days.
**Projects:** DocuQuery (RAG, Days 1–30) · SupportPilot (agent, Days 31–60) · ExtractIQ (extraction, Days 61–75) · Portfolio + applications (Days 76–90).
**Daily rules:**
1. Every day ends with a git commit (even a note in `LEARNING.md`).
2. Learn max 45 min, build min 75 min. Reading without building is the failure mode.
3. Keep a `LEARNING.md` in each repo — one line per day: what you did, what broke.
4. Use Claude Code to accelerate, but type the core logic yourself the first time so you can explain it in interviews.
5. If you fall behind, cut scope, not days. Ship something smaller on schedule.

Timebox notation: **[45/75]** = 45 min learn, 75 min build.

---

## PHASE 1 — PYTHON + RAG (Days 1–30) — Project: DocuQuery

### Week 1 — Python for a Laravel engineer + FastAPI

**Day 1 (Mon 14 Sep)** — Setup
- Install `uv`, Python 3.12, VS Code/Cursor Python extension. Create repo `docuquery`.
- [45] Skim Python basics with a "Laravel → Python" lens: virtual envs = composer, `pyproject.toml` = composer.json, `pytest` = PHPUnit.
- [75] Write 5 small scripts: file I/O, dict/list comprehension, a class with a dataclass, JSON parse, HTTP call with `httpx`.
- Commit: `chore: python setup + practice scripts`

**Day 2 (Tue 15 Sep)** — Type hints, Pydantic v2
- [45] Pydantic v2 docs: BaseModel, validators, `model_validate`, `model_dump`.
- [75] Model an "Invoice" and a "Ticket" with nested models, custom validator, and 5 pytest tests.
- Commit: `feat: pydantic models + tests`

**Day 3 (Wed 16 Sep)** — async/await
- [45] Async in Python: event loop, `asyncio.gather`, `httpx.AsyncClient`. Compare to Laravel queues/jobs mentally.
- [75] Write a script that fetches 10 URLs concurrently vs sequentially and prints timing.
- Commit: `feat: async fetch benchmark`

**Day 4 (Thu 17 Sep)** — FastAPI core
- [45] FastAPI tutorial: path/query params, request bodies, response models, dependency injection.
- [75] Build `POST /documents`, `GET /documents/{id}`, `GET /health` with in-memory store, Pydantic models, and pytest via `TestClient`.
- Commit: `feat: fastapi skeleton + tests`

**Day 5 (Fri 18 Sep)** — Docker + CI
- [30] Review FastAPI Dockerfile best practices (multi-stage, `uv`).
- [90] Dockerfile, `docker-compose.yml` with Postgres, GitHub Actions running `pytest` + `ruff` on push.
- Commit: `ci: docker + github actions`

**Day 6 (Sat 19 Sep, 3–4h)** — Postgres + SQLAlchemy/SQLModel + Alembic
- [45] SQLModel or SQLAlchemy 2.0 basics; Alembic = Laravel migrations.
- [Rest] Replace in-memory store with Postgres; add migration; add streaming endpoint (`StreamingResponse`, SSE) that streams a fake token stream.
- Commit: `feat: postgres persistence + sse streaming`

**Day 7 (Sun 20 Sep, 3h)** — Consolidation
- Write `LEARNING.md` summary of week 1: 10 things Python does differently from PHP.
- Refactor: routers folder, services folder, settings via `pydantic-settings`.
- 30 min: solve 3 easy LeetCode problems in Python (arrays/strings). Do this every Sunday from now on.
- Commit: `refactor: project structure`

### Week 2 — LLM API fluency

**Day 8 (Mon 21 Sep)** — First calls
- [45] Anthropic docs: Messages API, system prompts, max_tokens, temperature. OpenAI equivalents.
- [75] `POST /chat` endpoint calling Claude with a system prompt; log input/output tokens and computed cost per call to Postgres.
- Commit: `feat: /chat with token + cost logging`

**Day 9 (Tue 22 Sep)** — Streaming
- [30] Streaming docs (Anthropic `stream=True`, event types).
- [90] Stream Claude output to the client via SSE; tiny HTML page that renders it.
- Commit: `feat: streaming chat`

**Day 10 (Wed 23 Sep)** — Tool calling / structured output
- [45] Anthropic tool use docs; JSON schema from Pydantic (`model_json_schema()`).
- [75] Endpoint: given free text, extract a Pydantic `Person{name,email,company}` via tool calling; retry once on validation failure with the error fed back.
- Commit: `feat: structured extraction via tool calling`

**Day 11 (Thu 24 Sep)** — Robustness
- [30] Rate limits, retries, backoff (`tenacity`), timeouts, prompt caching.
- [90] Add retry/backoff wrapper, timeouts, prompt caching on the system prompt; write tests with a mocked client.
- Commit: `feat: llm client wrapper with retries + caching`

**Day 12 (Fri 25 Sep)** — Embeddings
- [45] What embeddings are; cosine similarity; chunk-size trade-offs. Read the pgvector README.
- [75] Script: embed 20 sentences with `text-embedding-3-small` and `bge-m3` (via `sentence-transformers`), compute similarity matrix, eyeball results.
- Commit: `feat: embedding experiments`

**Day 13 (Sat 26 Sep, 3–4h)** — pgvector
- Enable pgvector in Postgres; `chunks` table with `vector(1536)` column + HNSW index.
- Ingest a markdown folder (start with FastAPI docs cloned from GitHub): chunk with a simple recursive splitter, embed, store.
- Endpoint `POST /search` returning top-k by cosine distance.
- Commit: `feat: pgvector ingestion + vector search`

**Day 14 (Sun 27 Sep, 3h)** — Prompting patterns + LeetCode
- [60] Few-shot, output schemas, refusal handling, "answer only from context, say I don't know" pattern.
- [60] Write the DocuQuery answer prompt with citation format `[file:line]`.
- [30] 3 LeetCode easy/medium (hash maps).
- Commit: `feat: answer prompt v1`

### Week 3 — DocuQuery v0: real RAG pipeline

**Day 15 (Mon 28 Sep)** — Data source
- Decide the target repo (recommend: FastAPI repo — docs + source, English, well-known to interviewers).
- Ingest both `docs/` markdown and `.py` source; store metadata: path, start_line, end_line, type (doc/code).
- Commit: `feat: ingest docs + source with line metadata`

**Day 16 (Tue 29 Sep)** — Code-aware chunking
- [30] Read about chunking strategies (recursive, by heading, by AST for code).
- [90] Implement heading-based chunking for markdown and function/class-level chunking for Python (use `ast`). Compare chunk count and avg size.
- Commit: `feat: code-aware chunking`

**Day 17 (Wed 30 Sep)** — Hybrid search
- [30] BM25 basics; Postgres full-text search (`tsvector`) or `rank_bm25`.
- [90] Add keyword search; combine with vector search via Reciprocal Rank Fusion.
- Commit: `feat: hybrid search (RRF)`

**Day 18 (Thu 1 Oct)** — Re-ranking
- [30] Cross-encoder re-rankers; Cohere Rerank API (free trial) or `bge-reranker`.
- [90] Retrieve top-20 hybrid → re-rank → top-5 to the LLM. Log which stage each final chunk came from.
- Commit: `feat: reranking`

**Day 19 (Fri 2 Oct)** — End-to-end answer with citations
- Wire retrieve → prompt → stream answer with `[path:line]` citations; make citations links to GitHub blob URLs.
- Commit: `feat: end-to-end RAG answers with citations`

**Day 20 (Sat 3 Oct, 4h)** — UI
- Minimal Vue (you know it) or plain HTML/HTMX chat UI: question box, streamed answer, clickable citations, "with RAG / without RAG" toggle.
- Deploy DB to Supabase (pgvector enabled), API to Railway/Render.
- Commit: `feat: web ui + deploy`

**Day 21 (Sun 4 Oct, 3h)** — Framework comparison + LeetCode
- [90] Rebuild the retrieval step using LlamaIndex (or LangChain) in a separate module; note what it abstracts and what you lose.
- [30] LeetCode ×3.
- [30] `LEARNING.md`: "What the framework hides" note.
- Commit: `docs: framework comparison`

### Week 4 — DocuQuery v1: evals, observability, ship

**Day 22 (Mon 5 Oct)** — Golden dataset
- Write 50 questions about FastAPI with reference answers + expected source files. Mix: factual, how-to, "not in docs" (should refuse).
- Store as `evals/golden.jsonl`.
- Commit: `test: golden eval set`

**Day 23 (Tue 6 Oct)** — RAGAS baseline
- [30] RAGAS docs: faithfulness, answer relevancy, context precision, context recall.
- [90] Eval runner script; run baseline; save `evals/results/baseline.json`.
- Commit: `test: ragas baseline`

**Day 24 (Wed 7 Oct)** — LLM-as-judge + refusal test
- Judge script scoring correctness 1–5 against reference; refusal accuracy on the "not in docs" set.
- Commit: `test: llm judge + refusal metrics`

**Day 25 (Thu 8 Oct)** — Langfuse
- [30] Langfuse quickstart (cloud free tier).
- [90] Trace every request: retrieval spans, rerank span, generation span, tokens, cost, latency. Tag eval runs.
- Commit: `feat: langfuse tracing`

**Day 26 (Fri 9 Oct)** — Tuning round 1
- Experiment: chunk size ×2 variants, top-k 5 vs 10, with/without rerank. Re-run evals. Record in a table.
- Commit: `test: tuning round 1 results`

**Day 27 (Sat 10 Oct, 4h)** — Tuning round 2 + hardening
- Try query rewriting (HyDE or multi-query); measure. Add caching for repeated queries. Fix worst 5 failures from evals.
- Commit: `feat: query rewriting + fixes`

**Day 28 (Sun 11 Oct, 3h)** — README + diagram
- README: 2-line problem statement, numbers table (baseline vs final), architecture diagram (Mermaid or Excalidraw), stack, cost/query, "what failed and what I changed", "next steps".
- LeetCode ×3.
- Commit: `docs: README v1`

**Day 29 (Mon 12 Oct)** — Demo video + polish
- Record a 90-second demo (Loom/OBS). Fix any first-click bugs on the live URL. Add rate limiting so the demo can't be abused.
- Commit: `chore: demo + rate limiting`

**Day 30 (Tue 13 Oct)** — Blog post draft + LinkedIn
- Draft post: "Building a RAG system over the FastAPI codebase: what the evals taught me." Publish (dev.to or your site). LinkedIn post with demo link.
- **Phase 1 checkpoint:** live URL, repo with tests + evals, blog post.

---

## PHASE 2 — AGENTS (Days 31–60) — Project: SupportPilot

### Week 5 — Agent fundamentals

**Day 31 (Wed 14 Oct)** — Concepts
- [60] Read: tool-calling loop, ReAct, "workflows vs agents" (Anthropic's Building Effective Agents post). Write 10 bullet notes.
- [60] Hand-write a bare tool-calling loop in Python (no framework): LLM → tool call → result → LLM, max 5 iterations, with two tools (calculator, current time).
- Commit: `feat: raw agent loop`

**Day 32 (Thu 15 Oct)** — LangGraph basics
- [45] LangGraph tutorial: StateGraph, nodes, edges, conditional edges.
- [75] Rebuild yesterday's loop as a LangGraph graph.
- Commit: `feat: langgraph agent loop`

**Day 33 (Fri 16 Oct)** — Checkpoints + memory
- [30] LangGraph checkpointers (Postgres), threads.
- [90] Add Postgres checkpointer; resume a conversation by thread id.
- Commit: `feat: checkpointing`

**Day 34 (Sat 17 Oct, 4h)** — 3-tool agent + tracing
- Tools: web search (Tavily free tier), calculator, `ask_docuquery` (calls Project 1). Langfuse tracing on every node.
- Write 10 test prompts; record which tools it chose.
- Commit: `feat: 3-tool agent with tracing`

**Day 35 (Sun 18 Oct, 3h)** — Human-in-the-loop + LeetCode
- [90] LangGraph `interrupt` before a "dangerous" tool; approve via a CLI prompt, then resume.
- [30] LeetCode ×3.
- [30] Notes: when NOT to use an agent (write 5 real examples from your past jobs).
- Commit: `feat: hitl interrupt`

### Week 6 — SupportPilot v0: backend + tools

**Day 36 (Mon 19 Oct)** — Domain + schema
- New repo `supportpilot`. Design tables: customers, orders, order_items, shipments, refunds, tickets, ticket_messages, audit_log. Alembic migration.
- Commit: `feat: schema`

**Day 37 (Tue 20 Oct)** — Seed data
- Seed 50 customers, 200 orders, 40 tickets. Ticket mix: 15 easy (where's my order), 10 refund requests (some over threshold), 8 ambiguous, 7 adversarial (prompt injection, angry, out-of-scope).
- Commit: `feat: seed data`

**Day 38 (Wed 21 Oct)** — Backend API
- FastAPI endpoints for orders, shipments, refunds, tickets. Tests.
- Commit: `feat: support backend api`

**Day 39 (Thu 22 Oct)** — Tools with scopes
- Tools: `lookup_order`, `get_shipping_status`, `issue_refund` (hard max $50 enforced in code, not prompt), `escalate`, `draft_reply`. Each tool: Pydantic schema, docstring, audit log entry.
- Commit: `feat: agent tools`

**Day 40 (Fri 23 Oct)** — Agent graph v0
- Graph: classify_ticket → gather_context → decide → act/escalate → draft_reply. System prompt with policy. Run on 5 tickets.
- Commit: `feat: agent graph v0`

**Day 41 (Sat 24 Oct, 4h)** — MCP server
- [45] MCP Python SDK quickstart.
- [Rest] Expose the 5 tools as an MCP server (stdio). Connect from Claude Desktop or Claude Code; record a GIF of Claude resolving a ticket.
- Commit: `feat: mcp server`

**Day 42 (Sun 25 Oct, 3h)** — Run all 40 + LeetCode
- Run the agent over all 40 tickets; save outputs. Manually grade: correct action? correct escalation? reply quality 1–5. This is your baseline.
- LeetCode ×3.
- Commit: `test: baseline run`

### Week 7 — SupportPilot v1: approvals, guardrails, memory

**Day 43 (Mon 26 Oct)** — Approval flow
- Refund > $50 → `interrupt` → pending approval row → simple approval UI (`/approvals` page, approve/reject) → resume graph.
- Commit: `feat: approval workflow`

**Day 44 (Tue 27 Oct)** — Prompt injection defenses
- [30] Read on indirect prompt injection via tool results.
- [90] Wrap tool outputs in delimiters + "data, not instructions" framing; add an injection classifier step; test with the 7 adversarial tickets.
- Commit: `feat: injection defenses`

**Day 45 (Wed 28 Oct)** — Output guardrails
- Tone/PII check on drafts (regex for emails/cards + LLM tone check); block and regenerate on failure. PII redaction in Langfuse logs.
- Commit: `feat: output guardrails`

**Day 46 (Thu 29 Oct)** — Memory
- Short-term: thread state per ticket. Long-term: customer history summary stored in Postgres, injected into context. Test on a repeat customer.
- Commit: `feat: customer memory`

**Day 47 (Fri 30 Oct)** — Model routing
- Cheap model (Haiku/mini) for classification, strong model for decisions; confidence field in structured output; escalate to strong model when low.
- Commit: `feat: model routing`

**Day 48 (Sat 31 Oct, 4h)** — UI + deploy
- Inbox UI: tickets list, agent trace per ticket, approve/reject, audit log. Deploy API + DB. 
- Commit: `feat: ui + deploy`

**Day 49 (Sun 1 Nov, 3h)** — Reliability + LeetCode
- Timeouts, max iterations, retries, idempotency on `issue_refund`, rate limiting. LeetCode ×3.
- Commit: `feat: reliability`

### Week 8 — Agent evals + writeup

**Day 50 (Mon 2 Nov)** — Eval harness
- Script runs all 40 tickets, compares to expected action/escalation labels, computes: task success %, escalation precision/recall, avg steps, cost/ticket, p50/p95 latency.
- Commit: `test: agent eval harness`

**Day 51 (Tue 3 Nov)** — Failure catalogue
- Group failures into categories (wrong tool, hallucinated order id, over-refund attempt blocked, injection success/fail). Fix top 3.
- Commit: `fix: top failure modes`

**Day 52 (Wed 4 Nov)** — Re-run + table
- Re-run evals; produce before/after table. 
- Commit: `test: v1 results`

**Day 53 (Thu 5 Nov)** — Security section + diagram
- Write "Security & failure modes" README section; LangGraph state diagram; sequence diagram of an approval.
- Commit: `docs: security + diagrams`

**Day 54 (Fri 6 Nov)** — README + video
- Full README with numbers table; 90-second demo video.
- Commit: `docs: README v1`

**Day 55 (Sat 7 Nov, 3h)** — Blog post
- "Building a bounded support agent: approvals, guardrails, and what the evals showed." Publish + LinkedIn.

**Day 56 (Sun 8 Nov, 3h)** — Interview practice #1
- Explain out loud (record yourself): RAG pipeline, hybrid search, reranking, agent vs workflow, HITL, prompt injection. 2 min each.
- LeetCode ×3.

**Days 57–60 (Mon 9 – Thu 12 Nov)** — Buffer / catch-up
- Use these 4 days to finish anything slipped in Phases 1–2. If on track: add Langfuse dashboards, add a "cost per resolved ticket" chart to SupportPilot UI, and start Python LeetCode mediums daily (1/day).
- **Phase 2 checkpoint:** two live projects, MCP server, two blog posts.

**Fri 13 – Sun 15 Nov — rest weekend (no day number).**
The only scheduled break in the plan. Phase 3 resumes on Monday. If Phases 1–2 slipped, this is the last slack before ExtractIQ.

---

## PHASE 3 — EXTRACTION + AWS (Days 61–75) — Project: ExtractIQ

**Day 61 (Mon 16 Nov)** — Scope + data
- New repo `extractiq`. Schema: `Invoice{vendor, invoice_no, date, due_date, currency, line_items[{desc, qty, unit_price, total}], subtotal, tax, total}` with reconciliation validators.
- Gather 60 invoices: public datasets (e.g. Hugging Face invoice sets), plus generate 15 with varied layouts, 5 scanned/blurry, 5 Thai/Burmese. 
- Commit: `feat: schema + dataset`

**Day 62 (Tue 17 Nov)** — Vision extraction
- [30] Anthropic vision docs (PDF/image input).
- [90] Pipeline: PDF → images (`pdf2image`) → Claude with tool-calling into the schema. Run on 5 docs.
- Commit: `feat: vision extraction v0`

**Day 63 (Wed 18 Nov)** — Validation + retry loop
- Validators: totals reconcile within tolerance, dates parse, currency ISO. On failure, retry with the validation errors in the prompt (max 2).
- Commit: `feat: validate + retry`

**Day 64 (Thu 19 Nov)** — Pipeline + storage
- Upload endpoint → background task → Postgres → status endpoint. Store raw response, parsed result, confidence, tokens, cost.
- Commit: `feat: async pipeline`

**Day 65 (Fri 20 Nov)** — Labeling
- Hand-label 50 documents (ground truth JSON). Tedious but this is what makes the project credible.
- Commit: `test: ground truth labels`

**Day 66 (Sat 21 Nov, 4h)** — Accuracy report
- Script: per-field exact match + normalized match (whitespace/number formatting), line-item F1, document-level "all fields correct" %. Compare two models (e.g. Sonnet vs Haiku, or Claude vs GPT). Table in README.
- Commit: `test: accuracy report`

**Day 67 (Sun 22 Nov, 3h)** — Dashboard + LeetCode
- Simple dashboard: upload, processing status, extracted fields with confidence, flag low-confidence for review. LeetCode ×3.
- Commit: `feat: dashboard`

**Day 68 (Mon 23 Nov)** — Improve
- Fix top failures (layouts, multi-page, Thai text). Add OCR fallback (Tesseract) for scans. Re-run report.
- Commit: `feat: improvements + rerun`

**Day 69 (Tue 24 Nov)** — AWS foundations
- [60] AWS account, IAM user, ECR, App Runner (or ECS Fargate) concepts; RDS Postgres.
- [60] Push image to ECR.
- Commit: `ci: ecr push`

**Day 70 (Wed 25 Nov)** — Deploy to AWS
- RDS Postgres (pgvector-capable), App Runner service, secrets in Parameter Store/Secrets Manager, S3 for uploads.
- Commit: `infra: aws deploy`

**Day 71 (Thu 26 Nov)** — Production hygiene
- Sentry, structured JSON logs, `/health`, CloudWatch alarms on 5xx. Langfuse for LLM calls.
- Commit: `feat: observability`

**Day 72 (Fri 27 Nov)** — Bedrock awareness
- [60] Read Bedrock + Azure OpenAI docs; run one extraction via Bedrock to say you've used it.
- [60] Cost model: cost per 1,000 documents at each model; add to README.
- Commit: `docs: bedrock + cost model`

**Day 73 (Sat 28 Nov, 4h)** — README + diagram + video
- README with accuracy table, infra diagram, cost table, limitations, "what failed". 90-second video.
- Commit: `docs: README v1`

**Day 74 (Sun 29 Nov, 3h)** — Blog post #3 + LeetCode
- "Invoice extraction with LLMs: measuring field-level accuracy across two models." Publish + LinkedIn.

**Day 75 (Mon 30 Nov)** — Redeploy Projects 1 & 2 to AWS (optional) or add AWS section to their READMEs; make sure all three live URLs work first-click.
- **Phase 3 checkpoint:** three live projects, three blog posts, AWS on the resume.

---

## PHASE 4 — PORTFOLIO, RESUME, INTERVIEWS, APPLICATIONS (Days 76–90)

**Day 76 (Tue 1 Dec)** — GitHub profile
- Profile README with the three projects (screenshots, live links, numbers). Pin repos. Clean up old repos (archive or add READMEs).

**Day 77 (Wed 2 Dec)** — Resume: AI Engineer version
- Single column, contact in body. Title: "AI Engineer — LLM Applications (RAG, Agents)". New summary. Projects section with a numbers line each. Skills grouped: AI/LLM · Backend · Frontend · Cloud/Infra. Cut "AI Builder", "99.9% uptime", "200h/mo".

**Day 78 (Thu 3 Dec)** — Resume: Full-Stack (AI) version + ATS check
- Second version headed "Full-Stack Engineer (Laravel/Vue · Python · AI)". Run both through a free ATS parser (e.g. Jobscan trial) and fix parsing issues.

**Day 79 (Fri 4 Dec)** — LinkedIn + site
- Headline, About, Featured (3 posts + demos), Projects section. Update hareom284.com with a projects page.

**Day 80 (Sat 5 Dec, 4h)** — Interview prep: concepts
- Write answers (bullet form) to 25 questions: RAG failure modes, chunking, hybrid search, reranking, evals design, hallucination measurement, agent vs workflow, HITL, prompt injection, structured outputs, cost/latency optimization, fine-tune vs RAG vs prompt, when not to use AI, MCP, observability.

**Day 81 (Sun 6 Dec, 3h)** — Interview prep: system design
- Whiteboard 3 designs, 30 min each: internal-docs assistant for 5,000 employees; invoice intake for a bank; customer-support agent at scale. Include evals, cost, guardrails.

**Day 82 (Mon 7 Dec)** — Python coding practice
- 2h LeetCode mediums in Python (arrays, hash maps, two pointers). Time yourself.

**Day 83 (Tue 8 Dec)** — Target list
- Build a spreadsheet of 60 target companies/roles: 20 Thailand (BOI/international, FDE roles), 20 Dubai/Abu Dhabi, 15 remote-first (Asia+EU), 5 Germany. Columns: role, link, matching project, visa note, status.

**Day 84 (Wed 9 Dec)** — Applications batch 1
- 10 tailored applications. Each: matching resume version, 3-line note linking the most relevant project, answer screening questions honestly about visa/location.

**Day 85 (Thu 10 Dec)** — Mock interview #1
- 60 min mock with a friend/ChatGPT/Claude voice: behavioral + 3 technical questions. Note weak answers, fix tomorrow.

**Day 86 (Fri 11 Dec)** — Applications batch 2 + follow-ups
- 10 more applications. Message 5 people at target companies on LinkedIn with a specific, short note referencing a project.

**Day 87 (Sat 12 Dec, 4h)** — Referral push + FDE angle
- Find recruiters posting FDE/AI Engineer roles in Bangkok/Singapore/Dubai; send tailored notes. Post a LinkedIn article comparing your three projects' eval results.

**Day 88 (Sun 13 Dec, 3h)** — Mock interview #2 + LeetCode
- System design mock + 3 mediums.

**Day 89 (Mon 14 Dec)** — Applications batch 3
- 10 applications. Review responses; adjust resume wording based on which roles reply.

**Day 90 (Tue 15 Dec)** — Retrospective + next 30 days
- Write: what worked, response rate per market, weakest interview topic. Plan the next 30 days: keep 10 applications/week, 1 LeetCode/day, and pick ONE project to get real users (offer DocuQuery to an open-source maintainer, or ExtractIQ to a small business).

---

## Ongoing habits (all 90 days)
- Daily commit. Daily `LEARNING.md` line.
- Sundays: 3 LeetCode problems in Python (mediums from Day 57).
- Weekly LinkedIn progress post (Sunday, 10 min) — public proof compounds.
- Keep a running "interview stories" file: every bug that took >1 hour is a future STAR answer.
- At work: look for one place to ship an LLM feature at Leap Technology. Employer-verified AI work beats all side projects.

## If you fall behind
- Week 1–2 slip → skip framework comparison (Day 21) and query rewriting (Day 27).
- Week 6–7 slip → skip model routing (Day 47) and memory (Day 46).
- Week 9–10 slip → skip Bedrock (Day 72); deploy only ExtractIQ to AWS.
- Never skip: golden datasets, eval tables, READMEs, deploys, the three blog posts.
