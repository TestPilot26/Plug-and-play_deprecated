# Health flags

Staleness and process-gap flags raised by the weekly learn session. Drafted for
human review — nothing here is acted on automatically.

## 2026-08-10

**Staleness (`Last validated` > 90 days, or uses correlating with `shipped-rework`)**
- Nothing over the 90-day line yet: the single pattern entry and all three playbooks date from
  2026-07-07 (34 days old).
- `playbooks/retro.md` and `playbooks/triage.md` are still unproven — `playbooks_used` is blank
  on every capture row five weeks after they were written. If they are not deliberately used on
  the next engagement they will age into staleness without ever having been validated.

**Process gaps (all carried over; none resolved this week)**
- Outcome labels still missing on both real rows (`2026-07-opsdeck`, `2026-07-engagement-os`),
  now ~5 weeks old. Confidence scoring in the pattern library stays blocked.
- Effort (`acus`, `human_hours`, `estimate_hours`) and `lessons` still blank on both rows —
  no quoting-accuracy or watch-out data can be computed.
- Neither engagement has a retro row of its own; both were sweep-drafted. Four weekly sessions
  in a row have flagged this, which meets the README's "retros skipped 3 engagements running"
  abandonment trigger.
- `example-2026-01-thisdeck` placeholder row still present and still counted by the dashboard.
- **Weekly output is still not landing:** PRs #3, #4 and #5 are all open and unreviewed. This
  PR carries all of their content forward and supersedes them; #3, #4 and #5 can be closed.
  Four weeks of drafts now sit in one review queue — the single highest-value human action is
  to review this PR and label the two outcome cells.

**Sweep coverage this week**
- 14- and 120-day sweeps found no new engagement sessions since 2026-08-03: the only sessions
  are the weekly-learn runs themselves (system chores, not engagements). No new rows drafted.

## 2026-08-03

**Staleness (`Last validated` > 90 days, or uses correlating with `shipped-rework`)**
- None yet on age: the single pattern entry and all three playbooks date from 2026-07-07 (27 days old).
- `playbooks/retro.md` and `playbooks/triage.md` remain unproven — `playbooks_used` is still
  blank on every capture row, four weeks after they were written.

**Process gaps (all carried over from 2026-07-27, none resolved)**
- Outcome labels still missing on both real rows (`2026-07-opsdeck`, `2026-07-engagement-os`),
  now ~4 weeks old. Confidence scoring stays blocked.
- Effort (`acus`, `human_hours`, `estimate_hours`) and `lessons` still blank on both rows.
- Neither engagement has a retro row of its own; both were sweep-drafted. Three weekly sessions
  in a row have now flagged this — the README's "abandonment" risk is materialising.
- `example-2026-01-thisdeck` placeholder row still present and still counted by the dashboard.
- **Weekly output is not landing:** PRs #3 (2026-07-13) and #4 (2026-07-27) are both still open
  and unreviewed, and the 2026-07-20 session left no PR at all. This PR carries forward and
  supersedes #3 and #4, which can be closed.

**Sweep coverage this week**
- 30-day sweep found no new engagement sessions: the only sessions since 2026-07-27 are the
  weekly-learn runs themselves (system chores, not engagements). No new rows drafted.

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
