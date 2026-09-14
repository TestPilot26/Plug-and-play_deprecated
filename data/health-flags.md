# Health flags

Staleness and process-gap flags raised by the weekly learn session. Drafted for
human review — nothing here is acted on automatically.

## 2026-09-14

**Staleness (`Last validated` > 90 days, or uses correlating with `shipped-rework`)**
- Nothing past the 90-day line yet. All three playbooks date from 2026-07-07 (69 days old) and
  cross the rot threshold on 2026-10-05 — three weeks away. The pattern entry's `Last validated`
  moved to 2026-09-11 with this week's new row, so it is no longer on the clock.
- `playbooks/retro.md` and `playbooks/triage.md` are still unproven: `playbooks_used` is blank on
  every row, including this week's new one (the engagement started ad hoc, without Triage).

**Process gaps**
- **New:** `2026-09-exec-inbox-triage-sheet` finished with no retro row — drafted by the sweep.
  That makes three engagements in a row without a retro, and the row has gaps only a human can
  fill: `client` is `tbd-external`, `outcome`/`estimate_hours`/`acus` blank, `sensitivity`
  defaulted to `normal` (client is a named executive's inbox — confirm this is not `confidential`).
- Outcome labels still missing on `2026-07-opsdeck` and `2026-07-engagement-os` (~10 weeks old),
  plus the new row. Confidence scoring stays 0/3 by default, not by evidence.
- `example-2026-01-thisdeck` placeholder row still present and still counted by the dashboard.
- **Weekly output is still not landing:** PRs #3–#10 are all open. This PR carries their content
  forward and supersedes all eight; #3–#10 can be closed. Merging this one plus labelling three
  `outcome` cells unblocks everything else.
- The weekly-learn sessions keep surfacing as "uncaptured" in every sweep (ten now). Still a
  candidate `sweep.py` filter (script change — out of scope here).

**Sweep coverage this week**
- 14-day sweep found 4 uncaptured sessions: three weekly-learn runs (system chores, no rows) and
  one real engagement (`devin-0f6d1aff…`, 2026-09-11, Google Apps Script simplification) → one
  row drafted. First new engagement captured since 2026-07-07.
- The five 2026-07-05 demo/eval-looking sessions remain uncaptured and unconfirmed (seventh week).

## 2026-09-07

**Staleness (`Last validated` > 90 days, or uses correlating with `shipped-rework`)**
- Still nothing past the 90-day line: the single pattern entry and all three playbooks date from
  2026-07-07 (62 days old). They cross the rot threshold on 2026-10-05 — four weeks away.
- `playbooks/retro.md` and `playbooks/triage.md` remain unproven: `playbooks_used` is blank on
  every capture row nine weeks after they were written. Unless one is deliberately used before
  2026-10-05 they will be flagged stale having never been validated once.

**Process gaps (all carried over; none resolved this week)**
- Outcome labels still missing on both real rows (`2026-07-opsdeck`, `2026-07-engagement-os`),
  now ~9 weeks old. Confidence scoring in the pattern library stays blocked.
- Effort (`acus`, `human_hours`, `estimate_hours`) and `lessons` still blank on both rows — no
  quoting-accuracy or watch-out data can be computed.
- Neither engagement has a retro row of its own; both were sweep-drafted. Eight weekly sessions
  running have flagged this, far past the README's "retros skipped 3 engagements running"
  abandonment trigger.
- `example-2026-01-thisdeck` placeholder row still present and still counted by the dashboard.
- **Weekly output is still not landing:** PRs #3–#9 are all open and unreviewed. This PR carries
  their content forward and supersedes all seven; #3–#9 can be closed. Eight weeks of drafts now
  sit in one review queue. Two human actions unblock everything else: label the two `outcome`
  cells, then merge this PR.
- No engagement work has been captured since 2026-07-07 (nine weeks). Either engagement activity
  has stopped, or it is happening outside Devin sessions where the sweep cannot see it. Flagged
  for the fourth week — the second case means the capture table is silently incomplete.
- The weekly-learn sessions themselves surface in every sweep as "uncaptured" (nine of them now).
  They are system chores, not engagements, so no rows are drafted — but a human may want to
  decide whether `sweep.py` should filter out sessions started from the Weekly Learn playbook so
  the sweep output stays readable (a script change, so out of scope for this session).

**Sweep coverage this week**
- 14- and 120-day sweeps found no new engagement sessions since 2026-08-31: the only sessions in
  the window are the weekly-learn runs themselves. No new rows drafted.
- The five 2026-07-05 sessions (`tinyhttp` unit tests, Hono URL shortener, taxonomy blog page,
  architecture diagram, Express→Fastify migration guide) remain uncaptured and still read as
  demo/eval runs. Flagged for the sixth week; a human should confirm that read or ask for rows.

## 2026-08-31

**Staleness (`Last validated` > 90 days, or uses correlating with `shipped-rework`)**
- Still nothing past the 90-day line: the single pattern entry and all three playbooks date from
  2026-07-07 (55 days old). They cross the rot threshold on 2026-10-05 — five weeks away.
- `playbooks/retro.md` and `playbooks/triage.md` remain unproven: `playbooks_used` is blank on
  every capture row eight weeks after they were written. Unless one is deliberately used before
  2026-10-05 they will be flagged stale having never been validated once.

**Process gaps (all carried over; none resolved this week)**
- Outcome labels still missing on both real rows (`2026-07-opsdeck`, `2026-07-engagement-os`),
  now ~8 weeks old. Confidence scoring in the pattern library stays blocked.
- Effort (`acus`, `human_hours`, `estimate_hours`) and `lessons` still blank on both rows — no
  quoting-accuracy or watch-out data can be computed.
- Neither engagement has a retro row of its own; both were sweep-drafted. Seven weekly sessions
  running have flagged this, far past the README's "retros skipped 3 engagements running"
  abandonment trigger.
- `example-2026-01-thisdeck` placeholder row still present and still counted by the dashboard.
- **Weekly output is still not landing:** PRs #3, #4, #5, #6, #7 and #8 are all open and
  unreviewed. This PR carries their content forward and supersedes all six; #3–#8 can be closed.
  Seven weeks of drafts now sit in one review queue. Two human actions unblock everything else:
  label the two `outcome` cells, then merge this PR.
- No engagement work has been captured since 2026-07-07 (eight weeks). Either engagement activity
  has stopped, or it is happening outside Devin sessions where the sweep cannot see it. Flagged
  for the third week — the second case means the capture table is silently incomplete.

**Sweep coverage this week**
- 14- and 120-day sweeps found no new engagement sessions since 2026-08-24: the only sessions in
  the window are the weekly-learn runs themselves (system chores, not engagements). No new rows
  drafted.
- The five 2026-07-05 sessions (`tinyhttp` unit tests, Hono URL shortener, taxonomy blog page,
  architecture diagram, Express→Fastify migration guide) remain uncaptured and still read as
  demo/eval runs. Flagged for the fifth week; a human should confirm that read or ask for rows.

## 2026-08-24

**Staleness (`Last validated` > 90 days, or uses correlating with `shipped-rework`)**
- Nothing past the 90-day line yet: the single pattern entry and all three playbooks date from
  2026-07-07 (48 days old). They cross the rot threshold on 2026-10-05.
- `playbooks/retro.md` and `playbooks/triage.md` are still unproven — `playbooks_used` is blank
  on every capture row seven weeks after they were written. Nothing has been validated since
  they were created, so they are on track to go stale without ever being used once.

**Process gaps (all carried over; none resolved this week)**
- Outcome labels still missing on both real rows (`2026-07-opsdeck`, `2026-07-engagement-os`),
  now ~7 weeks old. Confidence scoring in the pattern library stays blocked.
- Effort (`acus`, `human_hours`, `estimate_hours`) and `lessons` still blank on both rows — no
  quoting-accuracy or watch-out data can be computed.
- Neither engagement has a retro row of its own; both were sweep-drafted. Six weekly sessions
  running have flagged this, well past the README's "retros skipped 3 engagements running"
  abandonment trigger.
- `example-2026-01-thisdeck` placeholder row still present and still counted by the dashboard.
- **Weekly output is still not landing:** PRs #3, #4, #5, #6 and #7 are all open and unreviewed.
  This PR carries their content forward and supersedes all five; #3–#7 can be closed. Six weeks
  of drafts now sit in one review queue. Two human actions unblock everything else: label the
  two `outcome` cells, then merge this PR.
- No engagement work has been captured since 2026-07-07 (seven weeks). Either engagement
  activity has stopped, or it is happening outside Devin sessions where the sweep cannot see it.
  Flagged for the second week — worth confirming which, since the second case means the capture
  table is silently incomplete.

**Sweep coverage this week**
- 14- and 90-day sweeps found no new engagement sessions since 2026-08-17: the only sessions in
  the window are the weekly-learn runs themselves (system chores, not engagements). No new rows
  drafted.
- The five 2026-07-05 sessions (`tinyhttp` unit tests, Hono URL shortener, taxonomy blog page,
  architecture diagram, Express→Fastify migration guide) remain uncaptured and still read as
  demo/eval runs. Flagged for the fourth week; a human should confirm that read or ask for rows.

## 2026-08-17

**Staleness (`Last validated` > 90 days, or uses correlating with `shipped-rework`)**
- Still nothing past the 90-day line: the single pattern entry and all three playbooks date from
  2026-07-07 (41 days old). Half-way to the rot threshold with nothing validated in between.
- `playbooks/retro.md` and `playbooks/triage.md` remain unproven — `playbooks_used` is blank on
  every capture row six weeks after they were written. On current trend they will cross 90 days
  (2026-10-05) never having been used once, which is rot by default rather than by decay.

**Process gaps (all carried over; none resolved this week)**
- Outcome labels still missing on both real rows (`2026-07-opsdeck`, `2026-07-engagement-os`),
  now ~6 weeks old. Confidence scoring in the pattern library stays blocked.
- Effort (`acus`, `human_hours`, `estimate_hours`) and `lessons` still blank on both rows — no
  quoting-accuracy or watch-out data can be computed.
- Neither engagement has a retro row of its own; both were sweep-drafted. Five weekly sessions
  in a row have flagged this, well past the README's "retros skipped 3 engagements running"
  abandonment trigger.
- `example-2026-01-thisdeck` placeholder row still present and still counted by the dashboard.
- **Weekly output is still not landing:** PRs #3, #4, #5 and #6 are all open and unreviewed.
  This PR carries their content forward and supersedes all four; #3–#6 can be closed. Five
  weeks of drafts now sit in one review queue. Two human actions unblock everything else:
  label the two `outcome` cells, then merge this PR.
- No engagement work at all has been captured since 2026-07-07 (six weeks). Either engagement
  activity has stopped, or it is happening outside Devin sessions and the sweep cannot see it —
  worth confirming which, since the second case means the capture table is silently incomplete.

**Sweep coverage this week**
- 14- and 60-day sweeps found no new engagement sessions since 2026-08-10: the only sessions in
  the window are the weekly-learn runs themselves (system chores, not engagements). No new rows
  drafted.
- The five 2026-07-05 sessions (`tinyhttp` unit tests, Hono URL shortener, taxonomy blog page,
  architecture diagram, Express→Fastify migration guide) remain uncaptured and still read as
  demo/eval runs. Flagged for the third week; a human should confirm that read or ask for rows.

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
