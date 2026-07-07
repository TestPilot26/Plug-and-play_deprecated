# Playbook: Engagement Triage

**When to run:** at the start of every new engagement, before any building.
Input: a client problem statement (pasted or summarized by the user).

## Procedure

1. Clone/pull the `engagement-os` repo. Read `data/engagements.csv`,
   `data/pattern-library.md`, and `data/schema.md`.
2. Normalize the problem statement: extract candidate tags from the controlled
   tag list and note key nouns/verbs (the "signals").
3. Match against history, in order of strength:
   a. **Pattern Library entries** whose signals overlap the statement.
   b. **Individual past engagements** with overlapping tags or semantically
      similar problem statements.
4. Produce a **starter kit** for the user, ranked and grounded:
   - Recommended playbooks and reusable components, each with *why* — which
     past engagements support it and their outcomes (e.g. "used in 3 similar
     engagements, 3/3 shipped-clean").
   - Knowledge folders to enable.
   - **Watch-outs**: recurring late-stage corrections from the `lessons` column
     of matched engagements — things to include in the spec up front.
   - **Effort estimate**: range of `human_hours` and `acus` from matched
     engagements, with the sample size stated.
5. Be honest about confidence:
   - Fewer than 2 matching engagements → say so explicitly and present matches
     as "possibly relevant history", not recommendations.
   - Never force-fit: if the statement doesn't match any pattern, say the
     library has nothing for it and recommend a from-scratch spec. Add the
     statement's tags anyway — this engagement becomes future training data.
6. Offer to turn the starter kit into a written spec with verifiable acceptance
   criteria, and to open the build session(s) from it.

## Rules

- Always show the evidence (engagement ids) behind every suggestion so the
  human can spot a bad match.
- Do not modify `data/` in this playbook — triage reads; retro writes.
