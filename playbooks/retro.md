# Playbook: Engagement Retro

**When to run:** at the end of every engagement (or major task). Target: 5
minutes of human time.

**Inputs the user provides:** the engagement-os repo, the engagement's Devin
session links (or rough dates so you can find them), and the client short name.

## Procedure

1. Clone/pull the `engagement-os` repo. Read `data/schema.md` for the column
   definitions, outcome rubric, and controlled tag list.
2. Gather evidence automatically before asking the user anything:
   - Inspect the engagement's Devin sessions (prompts, playbooks attached,
     correction messages, PRs, ACU usage).
   - From the sessions, draft: `problem_statement` (one sentence, summarized —
     never paste client documents), `tags` (controlled list only),
     `playbooks_used`, `knowledge_used`, `components_reused`, `sessions`,
     `acus`, `corrections`.
   - Draft `adhoc_functionality` and `adhoc_procedures`: functionality built
     and procedures followed that had **no playbook or reused component behind
     them**. Be specific ("stripe checkout flow", "render staging deploy") —
     these feed the playbook-candidate queue.
3. Present the drafted row to the user and ask **only** for what you cannot
   infer: the `outcome` label (offer the rubric's three options),
   `human_hours`, `estimate_hours`, and one `lessons` sentence.
4. Append the confirmed row to `data/engagements.csv`. Set `sensitivity` to
   `confidential` if the user indicates the client details are sensitive.
5. Regenerate the dashboard: `python3 scripts/dashboard.py`.
6. Open a pull request with the new row and regenerated dashboard. Title:
   `retro: <engagement id>`.

## Rules

- Never invent an outcome label — the human always chooses it.
- If the user has skipped retros for 2+ finished engagements, note that in the
  PR description so the gap is visible.
