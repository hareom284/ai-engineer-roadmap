# System design practice

Day 81 asks for three 30-minute whiteboard designs. Use the same skeleton every time,
because interviewers score structure more than cleverness.

## The skeleton
1. **Clarify** — who uses it, how many, how fresh must answers be, what is the cost ceiling?
2. **Draw the happy path** — ingest, store, retrieve, generate, return.
3. **Name the storage** — what goes in Postgres, what goes in object storage, what is the index.
4. **Say how you would know it works** — eval set, metrics, what you would alert on.
5. **Guardrails** — authz, PII, injection, human approval for irreversible actions.
6. **Cost and latency** — per request and per month, and the biggest lever on each.
7. **What you would cut** if you had half the time.

Most candidates skip 4 and 6. That is where you win.

---

## Design 1 — internal-docs assistant for 5,000 employees
**Extra pressure:** permissions. Not everyone may see every document.

**Notes:**


## Design 2 — invoice intake for a bank
**Extra pressure:** auditability and error cost. A wrong number is worse than no number.

**Notes:**


## Design 3 — customer-support agent at scale
**Extra pressure:** irreversible actions and adversarial users.

**Notes:**

