# Health flags

Staleness and process-gap flags raised by the weekly learn session. Drafted for
human review — nothing here is acted on automatically.

## 2026-07-27

**Staleness (`Last validated` > 90 days, or uses correlating with `shipped-rework`)**
- None. The only pattern entry and all three playbooks date from 2026-07-07 (20 days old).
- `playbooks/retro.md` and `playbooks/triage.md` have never been used: `playbooks_used`
  is blank on every capture row. Not stale yet, but unproven — worth deliberately
  using one on the next engagement.

**Process gaps**
- Outcome labels missing on both real rows (`2026-07-opsdeck`, `2026-07-engagement-os`),
  now ~3 weeks old. This blocks confidence scoring in the pattern library.
- Effort data (`acus`, `human_hours`, `estimate_hours`) and `lessons` blank on both
  real rows — no quoting-accuracy or watch-out data can be computed.
- Two engagements finished with no retro row of their own: both rows were drafted by
  the sweep, not by `playbooks/retro.md`. That is the "retros feel like homework"
  failure mode the README calls the biggest risk.
- `example-2026-01-thisdeck` placeholder row is still in the capture table and is
  counted by the dashboard. A human should replace or remove it (the weekly session
  does not delete rows).
- Prior weekly-learn PR (#3, 2026-07-13) is still open and unreviewed; the 2026-07-20
  weekly session left no PR at all. Weekly output is queuing up rather than landing.
- Five Devin sessions from 2026-07-05 (`tinyhttp` unit tests, Hono URL shortener,
  taxonomy blog page, architecture diagram, Express→Fastify migration guide) are
  uncaptured. They have no prompt, PRs or ACUs recorded and look like demo/eval runs,
  so no rows were drafted — confirm that read, or ask for rows next week.
