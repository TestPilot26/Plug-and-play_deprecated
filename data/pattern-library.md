# Pattern Library

Recognized recurring engagement shapes. Maintained by the weekly learn session;
changes arrive as pull requests for human review. A pattern requires **at least
2–3 matching engagements** before it earns an entry — below that, it's noise.

Entry template:

```
## Pattern: <name>
- Signals: <keywords/tags in the problem statement that indicate this pattern>
- Recommended starter kit:
  - Playbooks: <...>
  - Components: <...>
  - Knowledge folders: <...>
- Confidence: <n>/<m> matching engagements shipped cleanly (list ids)
- Typical effort: <hours> human / <acus> ACUs (range)
- Watch-outs: <recurring late-stage corrections to handle up front>
- Last validated: <date of most recent successful use>
```

_Last swept: 2026-10-05 (no new rows — sweep paused; entry below unchanged since 2026-09-14)._

## Pattern: Internal ops/admin tooling prototype
- Signals: tags `internal-tooling` + (`admin-dashboard` | `automation` | `reporting` | `integration-api`); problem statements about an internal console/tool/script for a team's own operations rather than an end-client-facing product
- Recommended starter kit:
  - Playbooks: none proven yet (no engagement in this cluster used one)
  - Components: none proven yet — the sweep/dashboard scripts in this repo are the only reusable artefacts so far
  - Knowledge folders: none recorded
- Confidence: 0/3 matching engagements shipped cleanly — **outcomes not yet labelled** (`2026-07-opsdeck`, `2026-07-engagement-os`, `2026-09-exec-inbox-triage-sheet`)
- Typical effort: ~1.5 human hours / ACUs unknown (only `2026-09-exec-inbox-triage-sheet` has effort data; 9 correction messages in one session)
- Watch-outs: (draft, from one row's `lessons`) platform run-time limits (Apps Script 6-minute cap), stale third-party AI model names, and OAuth permission scopes caused most late corrections; all three engagements also built permission/role or data-governance behaviour from scratch
- Last validated: 2026-09-11 (most recent use — not yet a labelled *successful* use)
- ⚠ low confidence — entry is a 3-row cluster with no outcome labels and effort data on one row only. Treat as a placeholder for shape recognition; do not use it to justify a starter kit until the rows are labelled at retro.
