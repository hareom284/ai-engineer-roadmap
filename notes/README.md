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

**0 of 46 topics at `can-explain`.**

| Day | Date | Topic | Status |
|---|---|---|---|
| | | **01-python-fastapi** | |
| 1 | Mon 14 Sep | [Python idioms for a PHP engineer](01-python-fastapi/python-idioms.md) |    `not-started` |
| 2 | Tue 15 Sep | [Pydantic v2](01-python-fastapi/pydantic.md) |    `not-started` |
| 3 | Wed 16 Sep | [async / await and the event loop](01-python-fastapi/async.md) |    `not-started` |
| 4 | Thu 17 Sep | [FastAPI core](01-python-fastapi/fastapi.md) |    `not-started` |
| 5 | Fri 18 Sep | [Docker + GitHub Actions](01-python-fastapi/docker-ci.md) |    `not-started` |
| 6 | Sat 19 Sep | [SQLAlchemy 2.0, Alembic, SSE](01-python-fastapi/sqlalchemy-alembic.md) |    `not-started` |
| 7 | Sun 20 Sep | [Project structure and settings](01-python-fastapi/project-structure.md) |    `not-started` |
| | | **02-llm-apis** | |
| 8 | Mon 21 Sep | [Messages API basics](02-llm-apis/messages-api.md) |    `not-started` |
| 9 | Tue 22 Sep | [Streaming responses](02-llm-apis/streaming.md) |    `not-started` |
| 10 | Wed 23 Sep | [Tool calling and structured output](02-llm-apis/tool-calling.md) |    `not-started` |
| 11 | Thu 24 Sep | [Retries, backoff, timeouts, prompt caching](02-llm-apis/reliability.md) |    `not-started` |
| 12 | Fri 25 Sep | [Embeddings and similarity](02-llm-apis/embeddings.md) |    `not-started` |
| 13 | Sat 26 Sep | [pgvector and ANN indexes](02-llm-apis/pgvector.md) |    `not-started` |
| 14 | Sun 27 Sep | [Prompting patterns for grounded answers](02-llm-apis/prompting.md) |    `not-started` |
| | | **03-rag** | |
| 15 | Mon 28 Sep | [Ingestion and metadata](03-rag/ingestion.md) |    `not-started` |
| 16 | Tue 29 Sep | [Chunking strategies](03-rag/chunking.md) |    `not-started` |
| 17 | Wed 30 Sep | [Hybrid search and RRF](03-rag/hybrid-search.md) |    `not-started` |
| 18 | Thu 1 Oct | [Re-ranking](03-rag/reranking.md) |    `not-started` |
| 19 | Fri 2 Oct | [Grounded answers with citations](03-rag/citations.md) |    `not-started` |
| 20 | Sat 3 Oct | [Deploying the RAG service](03-rag/deployment.md) |    `not-started` |
| 21 | Sun 4 Oct | [LangChain / LlamaIndex vs hand-rolled](03-rag/frameworks.md) |    `not-started` |
| 22 | Mon 5 Oct | [Golden datasets](03-rag/golden-datasets.md) |    `not-started` |
| 23 | Tue 6 Oct | [RAGAS metrics](03-rag/ragas.md) |    `not-started` |
| 24 | Wed 7 Oct | [LLM-as-judge](03-rag/llm-judge.md) |    `not-started` |
| 25 | Thu 8 Oct | [Langfuse tracing](03-rag/observability.md) |    `not-started` |
| 26–27 | Fri 9 Oct – Sat 10 Oct | [Retrieval tuning](03-rag/tuning.md) |    `not-started` |
| | | **04-agents** | |
| 31 | Wed 14 Oct | [The tool-calling loop and ReAct](04-agents/agent-loop.md) |    `not-started` |
| 32 | Thu 15 Oct | [LangGraph state graphs](04-agents/langgraph.md) |    `not-started` |
| 33 | Fri 16 Oct | [Checkpointing and threads](04-agents/checkpointing.md) |    `not-started` |
| 35–43 | Sun 18 Oct – Mon 26 Oct | [Human-in-the-loop approvals](04-agents/hitl.md) |    `not-started` |
| 39 | Thu 22 Oct | [Tool design and least privilege](04-agents/tool-design.md) |    `not-started` |
| 41 | Sat 24 Oct | [Model Context Protocol](04-agents/mcp.md) |    `not-started` |
| 44 | Tue 27 Oct | [Prompt injection](04-agents/prompt-injection.md) |    `not-started` |
| 45 | Wed 28 Oct | [Input and output guardrails](04-agents/guardrails.md) |    `not-started` |
| 46 | Thu 29 Oct | [Agent memory](04-agents/memory.md) |    `not-started` |
| 47 | Fri 30 Oct | [Model routing and cost control](04-agents/model-routing.md) |    `not-started` |
| 49 | Sun 1 Nov | [Reliability and safety limits](04-agents/agent-reliability.md) |    `not-started` |
| 50 | Mon 2 Nov | [Agent evaluation](04-agents/agent-evals.md) |    `not-started` |
| | | **05-extraction-aws** | |
| 62 | Tue 17 Nov | [Vision extraction](05-extraction-aws/vision-extraction.md) |    `not-started` |
| 63 | Wed 18 Nov | [Schema validation and retry loops](05-extraction-aws/validation-retry.md) |    `not-started` |
| 65–66 | Fri 20 Nov – Sat 21 Nov | [Field-level accuracy](05-extraction-aws/accuracy-metrics.md) |    `not-started` |
| 68 | Mon 23 Nov | [OCR fallback](05-extraction-aws/ocr-fallback.md) |    `not-started` |
| 69–70 | Tue 24 Nov – Wed 25 Nov | [AWS deployment](05-extraction-aws/aws-deploy.md) |    `not-started` |
| 71 | Thu 26 Nov | [Production observability](05-extraction-aws/prod-observability.md) |    `not-started` |
| 72 | Fri 27 Nov | [Bedrock and enterprise deployment](05-extraction-aws/bedrock.md) |    `not-started` |
| 72 | Fri 27 Nov | [Cost modeling](05-extraction-aws/cost-modeling.md) |    `not-started` |

<!-- INDEX:END -->
