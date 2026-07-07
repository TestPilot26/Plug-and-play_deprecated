# Capture table schema (`engagements.csv`)

One row per engagement (or per major task within a large engagement). Rows are
drafted automatically by the sweep script / retro playbook; humans confirm.

| Column | Type | Notes |
|---|---|---|
| `id` | text | Short unique slug, e.g. `2026-07-acme-booking` |
| `date_started` | date | ISO format `YYYY-MM-DD` |
| `date_finished` | date | Blank while in progress |
| `client` | text | Client short name (or `internal`) |
| `problem_statement` | text | One-sentence summary. Summarize — never paste client documents verbatim. |
| `tags` | text | Semicolon-separated, from the controlled list below |
| `playbooks_used` | text | Semicolon-separated playbook names (blank = none) |
| `knowledge_used` | text | Knowledge folders/notes that mattered |
| `components_reused` | text | Repos/modules/templates forked or copied |
| `adhoc_functionality` | text | Functionality built from scratch (no playbook/component behind it), e.g. `stripe checkout; csv export`. **Feeds the playbook-candidate queue.** |
| `adhoc_procedures` | text | Procedures done manually, e.g. `render staging deploy; demo data seeding`. Also feeds the queue. |
| `sessions` | text | Devin session IDs/URLs involved |
| `acus` | number | Total ACUs across sessions (ACU = Devin's unit of work) |
| `human_hours` | number | Engineer hours, best estimate |
| `corrections` | number | Count of human correction messages / PR review rounds |
| `outcome` | enum | See rubric below |
| `lessons` | text | What had to be corrected; watch-outs for next time |
| `estimate_hours` | number | What was quoted/estimated up front (for quoting accuracy) |
| `sensitivity` | enum | `normal` or `confidential` (confidential rows are excluded from the dashboard and pattern library) |

## Outcome rubric (label consistently — the learning layer depends on it)

| Value | Criteria |
|---|---|
| `shipped-clean` | Delivered and accepted with ≤ 2 correction rounds; no post-delivery rework in the first 2 weeks. |
| `shipped-rework` | Delivered, but needed 3+ correction rounds OR post-delivery rework. |
| `abandoned` | Not delivered (scope change, client pause, dead end). Record why in `lessons`. |

One person owns label quality for the first ~15 rows; spot-check monthly after.

## Controlled tag list

Add new tags deliberately (edit this list in the same change that first uses
the tag). Starting set:

`client-portal` `scheduling` `payments` `notifications` `auth` `admin-dashboard`
`data-import-export` `reporting` `integration-api` `mobile` `content-management`
`internal-tooling` `automation` `migration`
