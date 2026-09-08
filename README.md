# AI Engineer Roadmap — 90 Days

Started: 2026-09-09
Goal: become a credible candidate for LLM/agent application engineer roles (RAG, agents, LLM integration) by shipping three evaluated, deployed projects.

## Documents
1. [Market requirements & resume rules](01-resume-market-review.md) — what AI-engineer postings actually ask for
2. [3-month plan](02-3-month-plan.md) — weekly overview
3. [90-day daily plan](03-90-day-daily-plan.md) — day-by-day tasks
4. [Learning log](LEARNING.md) — one line per day
5. [Weekly reviews](reviews/) — one file per week, from [the template](reviews/TEMPLATE.md)

## Projects
| Project | What | Repo | Live | Status |
|---|---|---|---|---|
| [DocuQuery](projects/docuquery.md) | RAG over a codebase/docs with citations + evals | – | – | Not started |
| [SupportPilot](projects/supportpilot.md) | Customer-support agent with tools, approvals, guardrails | – | – | Not started |
| [ExtractIQ](projects/extractiq.md) | Invoice → structured data extraction with accuracy report | – | – | Not started |

## Progress
### Phase 1 — Python + RAG (Days 1–30)
- [ ] Week 1 — Python + FastAPI (Days 1–7)
- [ ] Week 2 — LLM API fluency (Days 8–14)
- [ ] Week 3 — DocuQuery v0 (Days 15–21)
- [ ] Week 4 — DocuQuery v1: evals + ship (Days 22–30)
- [ ] Checkpoint: live URL, evals table, blog post #1

### Phase 2 — Agents (Days 31–60)
- [ ] Week 5 — Agent fundamentals (Days 31–35)
- [ ] Week 6 — SupportPilot v0 + MCP server (Days 36–42)
- [ ] Week 7 — Approvals, guardrails, memory (Days 43–49)
- [ ] Week 8 — Agent evals + writeup (Days 50–56)
- [ ] Buffer (Days 57–60)
- [ ] Checkpoint: two live projects, MCP server, blog post #2

### Phase 3 — Extraction + AWS (Days 61–75)
- [ ] ExtractIQ pipeline + labels (Days 61–65)
- [ ] Accuracy report + improvements (Days 66–68)
- [ ] AWS deploy + observability (Days 69–72)
- [ ] README, video, blog post #3 (Days 73–75)
- [ ] Checkpoint: three live projects, AWS on resume

### Phase 4 — Portfolio + applications (Days 76–90)
- [ ] GitHub profile + resumes (Days 76–78)
- [ ] LinkedIn + site (Day 79)
- [ ] Interview prep (Days 80–82)
- [ ] Target list + 30 applications (Days 83–89)
- [ ] Retrospective (Day 90)

## How I use this repo
- **Daily:** one commit, prefixed `day-NN:`, plus a row in `LEARNING.md`.
- **Weekly:** one GitHub Issue per week with the day checkboxes; closed Sunday with a file in `reviews/`.
- **Projects:** code lives in its own repo (linked above); this repo holds notes, eval numbers, and interview stories.

## Rules
1. Commit every day.
2. Learn max 45 min, build min 75 min.
3. Never skip: golden datasets, eval tables, READMEs, deploys, blog posts.
