# Playbook: Weekly Learn (scheduled session)

**When to run:** automatically, weekly. Changes only `data/` and `docs/`,
delivered as a single pull request — never direct commits.

## Procedure

1. Clone/pull the `engagement-os` repo.
2. **Sweep** — run `python3 scripts/sweep.py` (requires the `DEVIN_API_KEY`
   secret). It lists recent Devin sessions and drafts capture-row stubs for any
   engagement work missing from `data/engagements.csv`. Review its output and
   add drafted rows with `outcome` left blank (a human labels outcomes in the
   next retro or PR review — never guess them).
3. **Mine candidates** — scan `adhoc_functionality` and `adhoc_procedures`
   across all rows. Anything appearing in 2+ engagements and not already in
   `data/playbook-candidates.md` gets appended to the queue table with status
   `suggested`, listing the supporting engagement ids.
4. **Update the Pattern Library** — cluster engagements by tags and
   problem-statement similarity. For clusters of 2–3+:
   - Create/update the pattern entry per the template, computing confidence
     (`n/m shipped-clean`), typical effort ranges, and watch-outs from
     `lessons`.
   - Never create an entry from a single engagement.
5. **Flag rot** — any playbook or pattern whose `Last validated` is > 90 days
   old, or whose recent uses correlate with `shipped-rework`, gets a
   `⚠ stale — review` marker.
6. **Flag process gaps** — if 2+ engagements finished without a retro row, or
   outcome labels are missing on old rows, note it.
7. **Regenerate the dashboard** — `python3 scripts/dashboard.py`.
8. Open one pull request containing all changes. The description is the weekly
   summary: new rows drafted, candidates suggested, patterns updated, staleness
   and process-gap flags. Keep it under ~15 lines.

## Rules

- Draft, never decide: no promoting candidates, no assigning outcome labels,
  no deleting rows.
- Exclude `sensitivity=confidential` rows from the pattern library and
  dashboard.
- If the sweep script fails (e.g. missing API key), still do steps 3–8 from
  existing data and flag the failure in the PR.
