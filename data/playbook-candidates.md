# Playbook candidate queue

Ad-hoc functionality or procedures observed in **2+ engagements** get flagged
here by the weekly learn session (mined from the `adhoc_functionality` and
`adhoc_procedures` columns). This works like Devin's knowledge-note
suggestions: the system drafts, a human decides.

For each candidate, a reviewer picks one:
- **Promote to playbook** — if it's a *procedure* (steps to follow). Draft it in
  `playbooks/`, prove it once on a real engagement, then create it as a Devin
  org playbook.
- **Promote to component** — if it's *code* (a module/template worth a repo).
- **Dismiss** — note why, so it isn't re-suggested.

| Candidate | Type | Seen in (engagement ids) | Times seen | Status | Decision notes |
|---|---|---|---|---|---|
| _empty — populated by the weekly learn session_ | | | | | |

## Sweep log

**2026-08-24** — no change. No new engagement rows again this week, so the
ad-hoc columns are unchanged and nothing reached the 2+ threshold. Queue stays
empty; the deploy-procedure near-miss noted below is unchanged. Seven weeks with
no new capture rows: the blocker remains capture, not mining.

**2026-08-17** — no change. No new engagement rows again this week, so the
ad-hoc columns are unchanged and nothing reached the 2+ threshold. Queue stays
empty; the deploy-procedure near-miss noted below is unchanged. Six weeks with
no new capture rows means the queue cannot fill — the blocker is capture, not
mining.

**2026-08-10** — no change. The sweep found no new engagement sessions, so the
ad-hoc columns are identical to last week and no item reached the 2+ threshold.
Queue remains empty; the deploy-procedure near-miss noted below is unchanged.

**2026-08-03** — no change. No new engagement rows this week, so the ad-hoc
columns are unchanged and nothing reached the 2+ threshold. The `vercel deploy
setup` / `GitHub Pages deploy` near-miss below still stands at one real
occurrence.

**2026-07-27** — no candidate met the 2+ threshold. Every ad-hoc item across the
capture table so far appears exactly once (the `example-2026-01-thisdeck`
placeholder row is excluded from mining). Nearest near-miss, for a human to
judge: `vercel deploy setup` (placeholder row) and `GitHub Pages deploy`
(`2026-07-engagement-os`) are both "publish a static/front-end artefact"
procedures — one real occurrence, so not suggested.
