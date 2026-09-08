# Why You're Getting Screened Out — Resume & Market Review (Sept 2026)

## TL;DR
- Rejections at screening come from two compounding causes: (1) a **positioning/credibility gap** — resume says "AI Builder" but shows only AI *coding tools* (Claude Code, Cursor, Copilot), no Python, no shipped LLM product, no RAG/agents/vector DB/evals; (2) a **visa/location filter** — Myanmar passport + Bangkok base means many Germany/EU/Singapore roles auto-filter before skills are read.
- Full-stack profile is solid but stacked on **PHP/Laravel + Vue**, a mid-tier lane in Germany/Singapore; it travels well in UAE and Thailand.
- Most realistic targets: **Thailand BOI/international companies, Dubai employer-sponsored roles, remote contractor roles for EU/US companies.**
- Highest-leverage fix: **build and ship 2–3 real LLM/RAG/agent projects** with GitHub + live demo + evals, learn Python + FastAPI, rewrite the resume single-column and honest.

## Key findings
1. **"AI Builder" is hurting.** Screeners distinguish "uses AI coding assistants" from "builds AI products." AI-engineer resumes that score well name a specific model version and at least one evaluation tool; ~72% of resumes list no evaluation tooling. The current resume has none of the AI-engineer vocabulary.
2. **No Python, no shipped LLM product.** Every posting surveyed requires production Python, LLM API integration, RAG with a named vector DB, agents/tool-calling, evals, FastAPI + Docker on a cloud. Fine-tuning is generally *not* required for application roles.
3. **Laravel/PHP is a lower-demand lane** for Germany/Singapore (TypeScript/Node, Java, Go, Python dominate) but common in UAE and Thailand.
4. **Visa filters:**
   - Germany Blue Card 2026: €50,700 standard / €45,934.20 for IT shortage occupations; degree must be in anabin or use the 3-years-IT-experience route.
   - Singapore EP: S$5,600/mo floor (S$6,000 from 2027) + COMPASS ≥40 points; likely ~30 points unless role is on the Shortage Occupation List or pays ~S$7,500+.
   - UAE: employer-sponsored permit is accessible; Golden Visa later at AED 30k basic salary.
   - Thailand: BOI Por.8/2568 — THB 75k/mo for engineers, THB 50k with a related degree; BOI companies streamline permits.
5. **Remote EU/US roles** are mostly location-restricted; contractor/freelance is the workable model.
6. **Credibility flags on the resume:** "200h/mo saved" and "99.9% uptime" from freelance work read as inflated; two-column layout with contact in header risks ATS parsing; "Hare Om." reads as an incomplete headline; education dates overlap first job; "Key Metrics" box reads as marketing.

## Requirements matrix (LLM/agent application roles)
| Requirement | Frequency | Now | After plan |
|---|---|---|---|
| Python (production, async) | ~100% | ✗ | ✓ |
| LLM APIs, prompt engineering, tool calling | ~100% | partial | ✓ |
| RAG + named vector DB | ~90% | ✗ | ✓ |
| Agents / LangGraph / LangChain / LlamaIndex | ~80% | ✗ | ✓ |
| Evaluation & testing frameworks | ~70% | ✗ | ✓ |
| Cloud (AWS/Azure/GCP) | ~80% | ✗ | ✓ (AWS) |
| FastAPI / Docker / CI/CD | ~70% | partial | ✓ |
| MCP / tool integration | ~30% | ✗ | ✓ |
| Structured extraction / IDP | ~30% | ✗ | ✓ |
| Observability, guardrails, HITL | ~40% | ✗ | ✓ |
| SWE fundamentals, production shipping | ~100% | ✓ | ✓ |
| CS degree | ~60% | ✓ | ✓ |
| "3+ yrs SWE incl. 1+ yr LLM" | common | 4+/0 | 4+/~0.3 |
| PyTorch / fine-tuning | ~30% (ML-flavored) | ✗ | skip |
| Thai language | some Bangkok enterprise | ✗ | skip |
| TypeScript/JS as a plus | ~40% | ✓ | ✓ |

## Market fit
- **Dubai:** typical bar "3+ yrs SWE, 1+ yr LLM, Python and/or TypeScript, LangChain/LlamaIndex, one vector DB, one cloud." Mid-level ~$8–9k/mo listed.
- **Remote-first Asia+Europe companies:** Python async + FastAPI + RAG in production + AWS + hands-on AI coding tools.
- **Bangkok FDE (Forward Deployed Engineer) roles:** Python + LLM orchestration + RAG + enterprise integration + stakeholder communication; sourced from senior full-stack engineers.
- **Avoid:** bank roles requiring PyTorch/fine-tuning, Senior/Lead/Platform titles, EU-only, Thai-fluency-required.

## Resume rewrite rules
- Single column, contact info in body, standard headings, no icons/sidebars/tables.
- Two versions: "AI Engineer — LLM Applications (RAG, Agents)" and "Full-Stack Engineer (Laravel/Vue · Python · AI)".
- Cut "AI Builder", "99.9% uptime", "200h/mo saved". Keep "8,000+ DAU" (employer-verified).
- Every AI bullet cites a project and a number; name model versions, vector store, eval scores.
- Summary template: *"Full-stack software engineer with 4+ years shipping production web apps (Laravel, Vue/Nuxt, GraphQL, PostgreSQL) — including an HR platform serving 8,000+ daily users. Now building LLM-powered features (RAG, agents) with Python, FastAPI, and the OpenAI/Anthropic APIs. Strong at owning products end-to-end from architecture to CI/CD deployment."*

## Application order
Thailand BOI/international → Dubai employer-sponsored → remote contractor (EU/US) → Germany Blue Card → Singapore (only if Shortage Occupation List or ~S$7,500+).

## Realistic expectations after the plan
- Thailand/Dubai: good odds of interviews; offers likely within 2–4 months of consistent applying (50–100 tailored applications).
- Remote contractor: moderate odds; Laravel + AI combo attractive to small teams.
- Germany/Singapore: low first-round odds; better after 6–12 months of AI work plus referrals.
- Biggest boosters: get one project used by real users; ship an LLM feature at the current employer.

## Caveats
Visa thresholds are 2025–2026 figures from official and law-firm sources; verify on MOM, anabin/ZAB, UAE ICP/GDRFA, and Thailand BOI before acting. COMPASS estimate depends on role, firm size, and degree authentication.
