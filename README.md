# Engagement OS

A lightweight system for capturing, learning from, and reusing patterns across
client engagements built with Devin. It turns each engagement into structured
data, mines that data for repeatable patterns, and suggests "plug and play"
playbooks and components when a new client problem statement arrives.

> **Jargon guide (used throughout):**
> - **Playbook** — a reusable, step-by-step prompt stored in Devin that anyone
>   can attach to a session ("how we do a release", "how we scaffold a client app").
> - **Knowledge note** — a persistent fact Devin remembers across sessions.
> - **ACU** — Agent Compute Unit, Devin's unit of work/billing (roughly "how
>   much effort Devin spent").
> - **Scheduled session** — a Devin session that runs automatically on a timer,
>   like a weekly automated chore.

---

## What's in this repo

| Path | What it is |
|---|---|
| `data/engagements.csv` | The **capture table** — one row per engagement/task. The single source of truth. Editable in any spreadsheet app. |
| `data/schema.md` | Column definitions and the outcome-scoring rubric (fill this in consistently — it's what the learning layer learns from). |
| `data/pattern-library.md` | The **Pattern Library** — recognized recurring engagement shapes, each with a recommended starter kit. Updated by the weekly learn session. |
| `data/playbook-candidates.md` | The **suggestion queue** — ad-hoc functionality/procedures seen 2+ times, flagged for promotion to a playbook or component. Humans approve or dismiss. |
| `playbooks/retro.md` | The **Retro playbook** — run after each engagement to fill in a capture row (5 minutes, mostly automated). |
| `playbooks/triage.md` | The **Triage playbook** — run at the start of a new engagement: paste a problem statement, get a ranked starter kit. |
| `playbooks/weekly-learn.md` | The **Weekly Learn playbook** — for the scheduled session that sweeps recent Devin sessions, updates the table, mines patterns, and refreshes the dashboard. |
| `scripts/sweep.py` | Auto-capture: pulls recent sessions from the Devin API and drafts capture rows for human confirmation. |
| `scripts/dashboard.py` | Generates `docs/index.html` from the capture table — the living analytics dashboard. |
| `docs/index.html` | The generated dashboard (open in any browser; regenerate any time). |

## How the loop works

```
NEW ENGAGEMENT                       DURING                    AFTER
──────────────                       ──────                    ─────
Run Triage playbook          →   Build with Devin      →   Run Retro playbook
(problem statement in,           (playbooks +              (capture row filled,
 starter kit out)                 components from            candidates queued)
                                  the starter kit)
                                                                  │
        ┌─────────────────────────────────────────────────────────┘
        ▼
WEEKLY (automated)
Scheduled "Learn" session: sweeps Devin sessions via API → updates capture
table → clusters patterns → updates Pattern Library → flags playbook
candidates → regenerates dashboard → posts a short summary for human review.
```

Nothing is auto-applied: the system **drafts**, humans **approve**. Playbook
candidates only become real playbooks when a person promotes them.

---

## Target users

1. **Deployed/forward engineers** running client engagements with Devin — the
   primary users of Triage and Retro.
2. **Engagement leads / founders** — the dashboard's audience: reuse rate,
   effort per engagement type, playbook success rates, cost trends.
3. **Devin itself** — future sessions consume the Pattern Library and playbooks
   as structured context, which is the point: the system's outputs are inputs
   to the next engagement.

Not for: end clients (data contains cross-client commercial details — see
Risks), or teams with < ~5 engagements of history (see Cold Start).

## Expected ROI

The system converts one-off engineering effort into a compounding asset. Value
shows up in four places:

1. **Faster delivery (primary)** — each promoted playbook/component removes
   rework from every future engagement that matches its pattern. If a typical
   engagement is 40 engineer-hours and reuse removes even 15–25% on matching
   engagements, that's 6–10 hours saved per engagement.
2. **Fewer corrections** — captured watch-outs ("clients always ask for CSV
   export late") prevent expensive late-stage changes.
3. **Better quoting** — effort data per pattern type turns estimates from gut
   feel into evidence, reducing under-quoted (loss-making) engagements.
4. **Onboarding leverage** — a new engineer inherits the whole library on day
   one instead of relearning by trial and error.

**Break-even math:** setup is ~1–2 days of effort (mostly done — it's this
repo) plus ~10 minutes of human time per engagement (retro confirmation) and a
weekly automated session (a few ACUs). At any reasonable engineer cost, a
single engagement that reuses one solid playbook pays back months of running
cost. The real risk to ROI is not cost — it's *abandonment* (see Risks).

## Cost-to-return ratio

| Cost | Estimate |
|---|---|
| Initial build | Done (this repo) |
| Human time per engagement | ~10 min (confirm retro row, review suggestions) |
| Weekly learn session | ~2–5 ACUs/week |
| Playbook promotion (when a candidate is approved) | ~30 min human + 1 short Devin session |

| Return (per *matching* engagement) | Estimate |
|---|---|
| Delivery time saved via reuse | 10–25% of engagement effort |
| Avoided rework from watch-outs | 1–4 hours |
| Reduced ACU spend (Devin starts from a playbook, not a blank prompt) | 10–30% on matched tasks |

Ratio improves with volume: at < 5 engagements the system is roughly
break-even (it's just organized note-taking); at 15+ engagements with 2–3
promoted playbooks, returns dominate costs by an order of magnitude.

## Measuring impact in dollar terms

Measure against a **baseline window** (your first N engagements, before any
patterns are promoted). The dashboard computes the inputs; the formula:

```
Monthly $ impact =
    (hours saved via reuse        × engineer hourly cost)
  + (rework hours avoided         × engineer hourly cost)
  + (ACUs saved on matched tasks  × $/ACU)
  + (under-quote losses avoided)                 ← from quoting accuracy
  − (human time on retros/reviews × hourly cost)
  − (weekly session ACUs          × $/ACU)
  − (expected cost of risks, below)
```

**How each input is actually measured (no hand-waving):**
- *Hours saved via reuse:* compare `effort` (hours + ACUs) for engagements of
  the same pattern type before vs. after its playbook existed. This is the
  honest measure — same work shape, with and without the asset.
- *Rework avoided:* count of watch-outs applied per engagement × average
  historical cost of that class of correction (from the `lessons` column).
- *Quoting accuracy:* variance between estimated and actual effort, trending
  over time.
- *Risk cost (subtract, don't ignore):* expected cost of a **confidently wrong
  suggestion** (a mis-matched playbook that sends a build down the wrong path —
  budget the occasional half-day of unwinding), **stale playbook incidents**,
  and the **maintenance tax** if the sweep/dashboard breaks. If measured
  savings don't clearly exceed these within ~a quarter of normal engagement
  volume, simplify or stop — that finding is itself valuable.

Rule of thumb for early honesty: attribute savings **only** to engagements
where the triage suggestion was actually used, not to general productivity.

## Risks (and mitigations built into the design)

| Risk | Why it matters | Mitigation in this system |
|---|---|---|
| **Cold start** | With < ~10–15 engagements, "patterns" are noise. | Suggest layer stays advisory-only; dashboard shows sample sizes; pattern entries require ≥ 2–3 matching engagements. |
| **Overfitting to early wins** | First clients shape the library; client #5 gets force-fit. | Every suggestion shows *which* past engagements it's based on, so a human can spot a bad match. |
| **Confidently wrong suggestions** | Worse than no suggestion — sends builds down wrong paths. | Confidence labels (`n/n shipped cleanly`) + mandatory human review at triage. |
| **Playbook rot** | Tools and Devin change; old instructions mislead. | `last_successful_use` tracked per playbook; weekly session flags anything unused/failing for > 90 days. |
| **Goodhart's law** (metric becomes the target and stops measuring what you wanted) | Chasing "reuse rate" force-fits templates on novel problems. | Reuse rate is displayed as a health indicator, never a target; no per-person metrics. |
| **Inconsistent outcome labels** | Learning layer learns garbage from noisy human judgments. | 3-value rubric with written criteria in `data/schema.md`; one person owns label quality early on. |
| **Maintenance tax** | The learning system is itself software that can break. | Everything is CSV + markdown + two stdlib Python scripts. No database, no server, no dependencies. |
| **Client confidentiality** | Capture table holds cross-client problem statements and commercial detail. | Repo is private; schema marks a `sensitivity` column; anything client-confidential is summarized, never pasted verbatim. |
| **Abandonment** (the biggest one) | Learning loops die when retros feel like homework. | Retro is a 5-minute playbook where Devin pre-fills everything and the human only confirms. If retros are skipped 3 engagements running, the weekly session flags it. |

## Human behavioral changes required (deliberately minimal)

Only **three** habits, all lightweight, all high-leverage:

1. **Start every engagement with the Triage playbook** (2 minutes: paste the
   problem statement). Even when the library is empty — that's what builds it.
2. **End every engagement with the Retro playbook** (5 minutes: Devin drafts
   the capture row; you confirm the outcome label and add one lesson).
3. **Review the weekly summary** (5 minutes: approve/dismiss playbook
   candidates and pattern updates).

Everything else — sweeping sessions, clustering, dashboard refresh, candidate
detection — is automated. The quality bar is held by the rubric in
`data/schema.md` and by human approval gates, not by asking people to write
long documents.

## UI: what it is and why

Principle: **meet users where they already are**. No new app to log into.

1. **The dashboard** (`docs/index.html`) — a single static HTML file,
   regenerated by script, openable in any browser and hostable anywhere
   (GitHub Pages works). Shows: engagement funnel by pattern type, playbook
   leaderboard (uses × success rate × avg effort), reuse-rate trend,
   correction hotspots, effort/ACU per pattern type, and the candidate queue.
   Static-by-design: nothing to run, nothing to break, always inspectable.
2. **Playbooks as the interactive UI** — triage and retro happen *inside Devin
   sessions*, which is where the engineer already is. The "form" is a
   conversation.
3. **The CSV as the editing UI** — non-technical users can open the capture
   table in Google Sheets/Excel. No admin panel needed until volume demands it.

Deliberately **not** built (yet): a web app with auth, a database, real-time
charts. Each adds maintenance tax without adding learning-loop value at this
volume. The upgrade trigger is written down: when the CSV passes ~200 rows or
3+ people edit it concurrently, revisit.

## Best implementation practices

1. **Tag consistently from day one.** Tags (`scheduling`, `payments`,
   `client-portal`…) power matching before there's enough data for semantic
   clustering. Use the controlled tag list in `data/schema.md`; add new tags
   deliberately.
2. **Capture from day one; trust suggestions later.** Run retros immediately;
   treat triage output as a searchable memory until ~10–15 rows exist, then as
   a recommender.
3. **Summarize, don't paste, client material.** One-sentence problem
   statements; no client documents in the table.
4. **Promote conservatively.** A candidate becomes a playbook after 2–3
   appearances *and* one successful deliberate reuse. Draft playbooks live in
   `playbooks/` as markdown first; promote to Devin org playbooks once proven.
5. **Keep the weekly session boring.** It follows `playbooks/weekly-learn.md`
   exactly, changes only `data/` and `docs/`, and opens its changes as a
   pull request (a proposed change a human approves) — never direct commits.
6. **Review label quality monthly.** One person spot-checks outcome labels
   against the rubric until the team is calibrated.
7. **Write the retirement criteria now** (done — see risk table): if the
   system isn't paying for itself within a quarter of normal volume, simplify
   or stop.

## Setup

1. Create a Devin API key (Settings → API) and store it as the `DEVIN_API_KEY`
   secret in Devin (never in this repo).
2. Create the Retro and Triage playbooks in Devin from `playbooks/*.md`
   (or ask Devin to — the drafts here are the source of truth).
3. Set up the weekly scheduled session pointing at `playbooks/weekly-learn.md`.
4. Regenerate the dashboard any time: `python3 scripts/dashboard.py`
   (no dependencies beyond Python 3).
5. Optional: enable GitHub Pages on `docs/` so the dashboard has a URL.
