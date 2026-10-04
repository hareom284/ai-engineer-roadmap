# Learning notes

Detailed notes for the 90-day plan, organised by **topic**, not by day.

Interviewers ask "how did you choose your chunking strategy", never "what did you do on Day 16".
Notes filed by date are unfindable at the moment you need them, so everything here is filed by concept.

## Start here

**[DAILY-GUIDE.md](DAILY-GUIDE.md)** — all 90 days in order, with what to read, what to build step by step, and the test for whether you can move on. Open it each morning. It links to the topic file for that day.

The topic files are where understanding accumulates. The daily guide is the route through them.

## The three places things go

| File | What goes in it | When |
|---|---|---|
| `LEARNING.md` (repo root) | One line: what I did, what broke | Every day, 2 minutes |
| `notes/<phase>/<topic>.md` | The actual understanding | The day you touch that topic |
| `notes/debugging-log.md` | Anything that cost over an hour | Same day, while you remember |

Do not duplicate between them. The daily log proves you showed up. These files prove you learned.

## How to use a topic file

Every topic file is **pre-seeded with the questions that topic must answer**. Read those first,
before the docs. They tell you what to look for, which turns 45 minutes of reading into a search
rather than a skim.

Then, in order:

1. Skim the questions at the top. Do not answer yet.
2. Do the day's reading and building.
3. Write the **In my own words** paragraph. If it comes out as jargon, you have not understood it.
4. Tick off the questions you can now answer out loud in under two minutes, without notes.
5. Paste the smallest snippet that shows the idea. Type it, do not copy it.
6. Move **Status** from `not-started` to `learning` to `can-explain`.

A topic is only `can-explain` when every checkbox is ticked and you have said the answers aloud.
Being able to re-read your own note is not the same as being able to answer.

## Weekly, on Sunday

- Run `python3 notes/build_index.py` to refresh the table below.
- Any topic still `learning` after two weeks goes into next week's plan or gets consciously dropped.
- Promote the best debugging-log entries into `06-interview/interview-stories.md`.

## Interview prep is not a Phase 4 activity

`06-interview/concept-answers.md` holds the 25 questions the plan defers to Day 80.
Fill each one in as you finish the matching topic, while it is fresh. Arriving at Day 80 with
25 blank answers is the most likely way this plan fails at the last step.

---

## Index

<!-- INDEX:START -->

**5 of 46 topics at `can-explain`.**

| Day | Topic | Status |
|---|---|---|
| | **01-python-fastapi** | |
| 1 | [Python idioms for a PHP engineer](01-python-fastapi/python-idioms.md) | ✅ `can-explain` |
| 2 | [Pydantic v2](01-python-fastapi/pydantic.md) | ✅ `can-explain` |
| 3 | [async / await and the event loop](01-python-fastapi/async.md) | ✅ `can-explain` |
| 4 | [FastAPI core](01-python-fastapi/fastapi.md) | ✅ `can-explain` |
| 5 | [Docker + GitHub Actions](01-python-fastapi/docker-ci.md) | ✅ `can-explain` |
| 6 | [SQLAlchemy 2.0, Alembic, SSE](01-python-fastapi/sqlalchemy-alembic.md) |    `not-started` |
| 7 | [Project structure and settings](01-python-fastapi/project-structure.md) |    `not-started` |
| | **02-llm-apis** | |
| 8 | [Messages API basics](02-llm-apis/messages-api.md) |    `not-started` |
| 9 | [Streaming responses](02-llm-apis/streaming.md) |    `not-started` |
| 10 | [Tool calling and structured output](02-llm-apis/tool-calling.md) |    `not-started` |
| 11 | [Retries, backoff, timeouts, prompt caching](02-llm-apis/reliability.md) |    `not-started` |
| 12 | [Embeddings and similarity](02-llm-apis/embeddings.md) |    `not-started` |
| 13 | [pgvector and ANN indexes](02-llm-apis/pgvector.md) |    `not-started` |
| 14 | [Prompting patterns for grounded answers](02-llm-apis/prompting.md) |    `not-started` |
| | **03-rag** | |
| 15 | [Ingestion and metadata](03-rag/ingestion.md) |    `not-started` |
| 16 | [Chunking strategies](03-rag/chunking.md) |    `not-started` |
| 17 | [Hybrid search and RRF](03-rag/hybrid-search.md) |    `not-started` |
| 18 | [Re-ranking](03-rag/reranking.md) |    `not-started` |
| 19 | [Grounded answers with citations](03-rag/citations.md) |    `not-started` |
| 20 | [Deploying the RAG service](03-rag/deployment.md) |    `not-started` |
| 21 | [LangChain / LlamaIndex vs hand-rolled](03-rag/frameworks.md) |    `not-started` |
| 22 | [Golden datasets](03-rag/golden-datasets.md) |    `not-started` |
| 23 | [RAGAS metrics](03-rag/ragas.md) |    `not-started` |
| 24 | [LLM-as-judge](03-rag/llm-judge.md) |    `not-started` |
| 25 | [Langfuse tracing](03-rag/observability.md) |    `not-started` |
| 26–27 | [Retrieval tuning](03-rag/tuning.md) |    `not-started` |
| | **04-agents** | |
| 31 | [The tool-calling loop and ReAct](04-agents/agent-loop.md) |    `not-started` |
| 32 | [LangGraph state graphs](04-agents/langgraph.md) |    `not-started` |
| 33 | [Checkpointing and threads](04-agents/checkpointing.md) |    `not-started` |
| 35–43 | [Human-in-the-loop approvals](04-agents/hitl.md) |    `not-started` |
| 39 | [Tool design and least privilege](04-agents/tool-design.md) |    `not-started` |
| 41 | [Model Context Protocol](04-agents/mcp.md) |    `not-started` |
| 44 | [Prompt injection](04-agents/prompt-injection.md) |    `not-started` |
| 45 | [Input and output guardrails](04-agents/guardrails.md) |    `not-started` |
| 46 | [Agent memory](04-agents/memory.md) |    `not-started` |
| 47 | [Model routing and cost control](04-agents/model-routing.md) |    `not-started` |
| 49 | [Reliability and safety limits](04-agents/agent-reliability.md) |    `not-started` |
| 50 | [Agent evaluation](04-agents/agent-evals.md) |    `not-started` |
| | **05-extraction-aws** | |
| 62 | [Vision extraction](05-extraction-aws/vision-extraction.md) |    `not-started` |
| 63 | [Schema validation and retry loops](05-extraction-aws/validation-retry.md) |    `not-started` |
| 65–66 | [Field-level accuracy](05-extraction-aws/accuracy-metrics.md) |    `not-started` |
| 68 | [OCR fallback](05-extraction-aws/ocr-fallback.md) |    `not-started` |
| 69–70 | [AWS deployment](05-extraction-aws/aws-deploy.md) |    `not-started` |
| 71 | [Production observability](05-extraction-aws/prod-observability.md) |    `not-started` |
| 72 | [Bedrock and enterprise deployment](05-extraction-aws/bedrock.md) |    `not-started` |
| 72 | [Cost modeling](05-extraction-aws/cost-modeling.md) |    `not-started` |

<!-- INDEX:END -->
