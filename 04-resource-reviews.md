# Resource Reviews

Every video, course or "roadmap" I find goes here **before** it changes the plan.
The question is never "is this good?" — it is "does this help *my* target role in *my* 90 days?"

Target role (from [01-resume-market-review.md](01-resume-market-review.md)): **LLM / agent application engineer** — RAG, agents, LLM APIs, evals, FastAPI, cloud. Not ML research, not model training.

---

## Review 1 — five short roadmap videos (2026-09-18)

Source: five social-media videos saved to Downloads. Reviewed from the audio transcript and the on-screen slides.

### What each video says

**Video 1 — "Become an AI Engineer: one week roadmap"** (one course per day)

| Day | Course shown on screen | Length |
|---|---|---|
| Mon | Python for Data Science — Full Course (freeCodeCamp) | 12h 20m |
| Tue–Wed | Machine Learning for Everybody (freeCodeCamp, Kylie Ying) | 3h 54m |
| Thu | FastAPI Crash Course | — |
| Fri | Learn LLMs with HuggingFace — Essential Course | 15 lessons |
| Sat | Learn RAG From Scratch — Python AI Tutorial from a LangChain Engineer (freeCodeCamp) | 2h 33m |
| Sun | AI Agents Full Course 2026: Master Agentic AI (Codex, Claude Code, Antigravity) | 2h 13m |
| + | Docker Tutorial for Beginners [Full Course in 3 Hours] | 2h 46m |

**Video 2 — "AI engineer at a big tech company: the exact roadmap I would follow"** (3 months, in order)
1. Python — basics only. *"If you already know it, skip it. Don't waste a week learning syntax."*
2. Machine-learning fundamentals — one course (the name was unclear in the audio; most likely Andrew Ng's). *"Stop searching for the perfect course."*
3. Deep learning — neural networks, loss functions, how training works. *"This is where most people quit."*
4. LLMs, prompt engineering, RAG, agents. *"You cannot skip to here. Everyone who tries ends up back at step 2."*

**Video 3 — "90 days: from laid off to $3K/month with Claude"** (6.5 min)
Not a learning roadmap. It is a plan for a small paid product:
week 1 ask Claude which of your skills people pay for → week 2 build one tiny tool in a weekend → week 3 message 10 people who complained about the problem and offer it for $29 (3+ yes = build, 0 = kill the idea) → weeks 4–8 ship one small feature every 3 days → weeks 9–12 raise prices using testimonials.

**Video 4 — "How I'd become an AI engineer"** (6 steps)
1. Foundations: Python, SQL, NumPy, Pandas, Git/GitHub, APIs
2. Machine learning: statistics, probability, regression, classification, clustering, scikit-learn, model evaluation, feature engineering
3. Deep learning: neural networks, backpropagation, ANN, CNN, RNN, LSTM, transformers
4. Generative AI: LLMs, prompt engineering, embeddings, vector databases, LangChain, RAG, LLM APIs, semantic search
5. AI agents: tool calling, agentic workflows, memory, multi-agent systems, MCP, orchestration
6. **Stop watching tutorials and build**: RAG chatbot, research assistant, multi-agent system, document Q&A, support agent, coding assistant. Put code on GitHub, deploy it, write about it, apply.

**Video 5 — "1 week roadmap to become AI engineer"** (music only, courses on screen)
Complete Python for AI & ML (5h 42m) → Math for ML/AI (8h 20m) → Machine Learning Full Course part 1 (4h 14m) → Deep Learning Full Course (4h 25m) → NLP Full Course (1h 58m) → Generative AI Full Course 2026 (4h 01m) → Agentic AI Complete Course (40 videos).

### My verdict

**1. The "one week" titles are not real.** Video 5 is about 30 hours of video before the 40-video agent playlist. Video 1 is over 25 hours. Watching is not learning — you would finish the week able to *recognise* words, not *build* anything. This is exactly the failure mode my plan's rule 2 exists to stop (learn max 45 min, build min 75 min).

**2. Four of five videos end with "comment and I'll DM you the plan".** They are designed for engagement first. That does not make them wrong, but it means the order and the "you must" claims were not written for my situation.

**3. The big disagreement: do I need ML + deep learning first?**
Videos 2, 4 and 5 say yes (Python → ML → deep learning → LLMs). Video 1 and my plan say no (Python → LLM APIs → RAG → agents).

My answer: **keep my plan's order, add a small concept backfill.** Reasons:
- My target postings ask for PyTorch / fine-tuning in only ~30% of roles, and those are the ML-flavoured roles I already decided to avoid ([market review](01-resume-market-review.md)).
- These videos describe the path to an *ML engineer* (someone who trains models). I am aiming to be an engineer who *builds products on top of* models. Different job, different foundation.
- Adding ML + deep learning properly would take 4–6 weeks. That would push my first shipped project from Day 30 to about Day 70.

But video 2 has a real point: in interviews I will be asked *what an embedding is*, *what a transformer does*, *why temperature changes output*. I must be able to explain those in plain words. That needs a few hours of concepts — not a month of math. See "Concept backfill" below.

**4. Things all five agree with my plan on** — this is reassuring:
- Python is the base (Week 1).
- LLM APIs, prompting, embeddings, vector DB, RAG (Weeks 2–4).
- Tool calling, agents, memory, MCP (Weeks 5–8).
- Video 4 step 6 is my whole plan in one sentence: build, GitHub, deploy, write about it, apply.

**5. Two ideas worth taking:**
- From video 2: *"Python basics only. If you already know it, skip it."* I already program professionally. Learn only the differences from PHP, then build. Do not restart Python from a 12-hour course.
- From video 3: **real users beat imaginary users.** Before Day 30, send the DocuQuery demo link to 3–5 developers and ask them to try one real question. Their confusion is better README material than my guesses. (I am *not* adopting the business/income part — the income numbers are the creator's claims, not evidence.)

### What I changed because of this review

| Change | Where |
|---|---|
| Added "RAG From Scratch" (freeCodeCamp) as an optional reference for Week 3 | [DAILY-GUIDE Day 15](notes/DAILY-GUIDE.md) |
| Added the Docker course as an optional reference — not to watch start to finish | [DAILY-GUIDE Day 5](notes/DAILY-GUIDE.md) |
| Added "Concept backfill" (below) to the buffer days | [DAILY-GUIDE Days 57–60](notes/DAILY-GUIDE.md) |
| Added a "Videos — reference only" list | [02-3-month-plan.md](02-3-month-plan.md) |
| Did **not** add ML / deep learning / math weeks | — see verdict 3 |

### Concept backfill (optional, ~4–6 hours total)

Goal: explain each of these in two minutes, in plain words. Not math, not training models.

- [ ] What a neural network does, and what "training" and a "loss function" mean
- [ ] What a token is, and why models have a context limit
- [ ] What a transformer and "attention" do, at a high level
- [ ] What an embedding is, and why similar meanings end up close together (I also meet this on Day 12)
- [ ] Why temperature changes the output
- [ ] Precision vs recall (I also meet this on Day 23 and in ExtractIQ)

Suggested resource (my suggestion, not from the videos): **3Blue1Brown's "Neural networks" YouTube series** — short, visual, and its later chapters cover transformers and attention. Watch one chapter at a time, then write the answer into [notes/06-interview/concept-answers.md](notes/06-interview/concept-answers.md).

When: the Days 57–60 buffer, or any weekend where I am on schedule. **Never** instead of a build day.

### Courses shown in the videos that I am skipping, and why

| Course | Why skip |
|---|---|
| Python for Data Science (12h), Complete Python for AI & ML (5h 42m), Python in 4 hours | I already program. Week 1 teaches only the PHP → Python differences. |
| Math for ML/AI (8h 20m), ML full courses, Deep Learning full course, NLP full course | Path to ML engineer, not my target role. Concept backfill covers what interviews ask. |
| Generative AI / Agentic AI full courses (4h+, 40 videos) | My plan covers the same topics by *building* them, using official docs. |
| AI Agents Full Course 2026 (Codex / Claude Code / Antigravity) | This is about *using* coding agents, not *building* agents. I use Claude Code every day already. |
| Learn LLMs with HuggingFace | Useful for open-source models; my projects use hosted APIs. Maybe after Day 90. |

---

## How to review the next resource (template)

1. **What does it claim?** One line.
2. **Who is it for?** ML engineer, or LLM application engineer?
3. **How long, honestly?** Add up the hours.
4. **Does my plan already cover it?** Check the daily guide.
5. **Decision:** skip · reference only (use when stuck on that day) · replace an existing resource.
6. **Rule:** a new resource can replace a resource. It cannot add a day.
