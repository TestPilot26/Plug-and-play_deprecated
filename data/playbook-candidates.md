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

**2026-10-26** — no change. The sweep still did not run (paused — see
`data/health-flags.md`), so no new rows and the ad-hoc columns match
2026-09-14. Nothing reached the 2+ threshold; the deploy-procedure near-miss
still waits on a human call.

**2026-10-19** — no change. The sweep still did not run (paused — see
`data/health-flags.md`), so no new rows and the ad-hoc columns match
2026-09-14. Nothing reached the 2+ threshold; the deploy-procedure near-miss
still waits on a human call.

**2026-10-12** — no change. The sweep still did not run (paused — see
`data/health-flags.md`), so no new rows and the ad-hoc columns match
2026-09-14. Nothing reached the 2+ threshold; the deploy-procedure near-miss
still waits on a human call.

**2026-10-05** — no change. The sweep did not run (script paused — see
`data/health-flags.md`), so no new rows; the ad-hoc columns match 2026-09-14
and nothing reached the 2+ threshold. The deploy-procedure near-miss below is
unchanged and still waits on a human call.

**2026-09-14** — no candidate met the 2+ threshold, but the table finally grew:
one new row (`2026-09-exec-inbox-triage-sheet`). Its ad-hoc items are all
first occurrences. Near-misses for a human to judge (each is one real
occurrence plus a loose match, so not suggested):
- *Publish/deploy a built artefact by hand* — `paste-into-Apps-Script deploy`
  (new row) joins `GitHub Pages deploy` (`2026-07-engagement-os`) and `vercel
  deploy setup` (placeholder row). Three different targets, same shape: a
  "ship the thing to where it runs" procedure with no playbook behind it. If a
  human reads these as one procedure, it qualifies (2 real occurrences).
- *Third-party permission / API-key setup* — `Drive/Gmail permission scope fix`
  (new row) vs. `create client GitHub repo` (`2026-07-opsdeck`). Weak match.

**2026-09-07** — no change. No new engagement rows again this week, so the
ad-hoc columns are unchanged and nothing reached the 2+ threshold. Queue stays
empty; the deploy-procedure near-miss noted below is unchanged. Nine weeks with
no new capture rows: the blocker remains capture, not mining.

**2026-08-31** — no change. No new engagement rows again this week, so the
ad-hoc columns are unchanged and nothing reached the 2+ threshold. Queue stays
empty; the deploy-procedure near-miss noted below is unchanged. Eight weeks with
no new capture rows: the blocker remains capture, not mining.

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
