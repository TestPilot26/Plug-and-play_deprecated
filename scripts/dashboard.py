#!/usr/bin/env python3
"""Generate the static analytics dashboard from data/engagements.csv.

Usage:
    python3 scripts/dashboard.py

Writes docs/index.html. No dependencies beyond the Python 3 standard
library -- open the output in any browser.
"""

import csv
import html
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = REPO_ROOT / "data" / "engagements.csv"
OUT_PATH = REPO_ROOT / "docs" / "index.html"

OUTCOME_LABELS = {
    "shipped-clean": ("Shipped clean", "#2e7d32"),
    "shipped-rework": ("Shipped w/ rework", "#f9a825"),
    "abandoned": ("Abandoned", "#c62828"),
    "": ("Unlabeled", "#9e9e9e"),
}


def load_rows():
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return [r for r in rows if (r.get("sensitivity") or "normal") != "confidential"]


def split_multi(value):
    return [v.strip() for v in (value or "").split(";") if v.strip()]


def num(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def bar(count, total, color):
    pct = 0 if total == 0 else round(100 * count / total)
    return (f'<div class="bar"><div class="fill" '
            f'style="width:{pct}%;background:{color}"></div>'
            f'<span>{count} ({pct}%)</span></div>')


def table(headers, rows_html):
    head = "".join(f"<th>{h}</th>" for h in headers)
    return f'<table><tr>{head}</tr>{"".join(rows_html)}</table>'


def build(rows):
    total = len(rows)
    outcomes = Counter((r.get("outcome") or "").strip() for r in rows)
    reuse_rows = [r for r in rows if split_multi(r.get("playbooks_used"))
                  or split_multi(r.get("components_reused"))]

    # Playbook leaderboard
    pb_stats = defaultdict(lambda: {"uses": 0, "clean": 0, "hours": 0.0, "acus": 0.0})
    for r in rows:
        for pb in split_multi(r.get("playbooks_used")):
            s = pb_stats[pb]
            s["uses"] += 1
            s["clean"] += r.get("outcome") == "shipped-clean"
            s["hours"] += num(r.get("human_hours"))
            s["acus"] += num(r.get("acus"))

    # Tag effort profile
    tag_stats = defaultdict(lambda: {"n": 0, "hours": 0.0, "acus": 0.0})
    for r in rows:
        for t in split_multi(r.get("tags")):
            s = tag_stats[t]
            s["n"] += 1
            s["hours"] += num(r.get("human_hours"))
            s["acus"] += num(r.get("acus"))

    # Candidate hotspots: ad-hoc items seen 2+ times
    adhoc = Counter()
    for r in rows:
        for item in split_multi(r.get("adhoc_functionality")) + split_multi(r.get("adhoc_procedures")):
            adhoc[item.lower()] += 1
    hotspots = [(k, v) for k, v in adhoc.most_common() if v >= 2]

    # Quoting accuracy
    quoted = [(r["id"], num(r.get("estimate_hours")), num(r.get("human_hours")))
              for r in rows if num(r.get("estimate_hours")) > 0 and num(r.get("human_hours")) > 0]

    sections = []
    sections.append(
        "<h2>Engagement outcomes</h2>"
        + "".join(
            f'<div class="row"><label>{html.escape(OUTCOME_LABELS.get(k, (k, "#607d8b"))[0])}</label>'
            + bar(v, total, OUTCOME_LABELS.get(k, (k, "#607d8b"))[1]) + "</div>"
            for k, v in outcomes.most_common())
        + f"<p class='note'>{total} engagement(s) total (confidential rows excluded).</p>")

    reuse_pct = 0 if total == 0 else round(100 * len(reuse_rows) / total)
    sections.append(
        "<h2>Reuse rate</h2>"
        f"<p class='big'>{reuse_pct}%</p>"
        "<p class='note'>Share of engagements using at least one playbook or reused "
        "component. Health indicator, not a target (see README: Goodhart risk).</p>")

    if pb_stats:
        sections.append("<h2>Playbook leaderboard</h2>" + table(
            ["Playbook", "Uses", "Shipped clean", "Avg hours", "Avg ACUs"],
            [f"<tr><td>{html.escape(pb)}</td><td>{s['uses']}</td>"
             f"<td>{s['clean']}/{s['uses']}</td>"
             f"<td>{s['hours']/s['uses']:.1f}</td><td>{s['acus']/s['uses']:.1f}</td></tr>"
             for pb, s in sorted(pb_stats.items(), key=lambda kv: -kv[1]["uses"])]))
    else:
        sections.append("<h2>Playbook leaderboard</h2><p class='note'>No playbook "
                        "usage recorded yet.</p>")

    if tag_stats:
        sections.append("<h2>Effort by pattern type (tags)</h2>" + table(
            ["Tag", "Engagements", "Avg hours", "Avg ACUs"],
            [f"<tr><td>{html.escape(t)}</td><td>{s['n']}</td>"
             f"<td>{s['hours']/s['n']:.1f}</td><td>{s['acus']/s['n']:.1f}</td></tr>"
             for t, s in sorted(tag_stats.items(), key=lambda kv: -kv[1]["n"])]))

    if hotspots:
        sections.append(
            "<h2>Playbook candidates (ad-hoc work seen 2+ times)</h2>" + table(
                ["Ad-hoc functionality / procedure", "Times seen"],
                [f"<tr><td>{html.escape(k)}</td><td>{v}</td></tr>" for k, v in hotspots])
            + "<p class='note'>Review these in data/playbook-candidates.md — "
              "promote to a playbook/component or dismiss.</p>")
    else:
        sections.append("<h2>Playbook candidates</h2><p class='note'>No repeated "
                        "ad-hoc work detected yet (needs 2+ occurrences).</p>")

    if quoted:
        sections.append("<h2>Quoting accuracy</h2>" + table(
            ["Engagement", "Estimated hrs", "Actual hrs", "Variance"],
            [f"<tr><td>{html.escape(i)}</td><td>{e:.0f}</td><td>{a:.0f}</td>"
             f"<td>{'+' if a >= e else ''}{(a - e):.0f} ({(a - e) / e * 100:+.0f}%)</td></tr>"
             for i, e, a in quoted]))

    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    body = "".join(f"<section>{s}</section>" for s in sections)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Engagement OS dashboard</title>
<style>
 body{{font-family:system-ui,sans-serif;max-width:860px;margin:2rem auto;padding:0 1rem;color:#222}}
 h1{{font-size:1.5rem}} h2{{font-size:1.1rem;margin-top:0;border-bottom:1px solid #eee;padding-bottom:.4rem}}
 section{{background:#fafafa;border:1px solid #e5e5e5;border-radius:8px;padding:1rem 1.2rem;margin:1rem 0}}
 table{{border-collapse:collapse;width:100%}} td,th{{text-align:left;padding:.35rem .6rem;border-bottom:1px solid #eee;font-size:.9rem}}
 .row{{display:flex;align-items:center;gap:.6rem;margin:.3rem 0}} .row label{{width:10rem;font-size:.85rem}}
 .bar{{flex:1;background:#eee;border-radius:4px;position:relative;height:1.3rem}}
 .fill{{height:100%;border-radius:4px}}
 .bar span{{position:absolute;left:.5rem;top:0;font-size:.75rem;line-height:1.3rem}}
 .big{{font-size:2.2rem;font-weight:700;margin:.2rem 0}}
 .note{{color:#777;font-size:.8rem}}
</style></head><body>
<h1>Engagement OS — living dashboard</h1>
<p class="note"><a href="about.html">About: the thinking behind this system</a></p>
<p class="note">Generated {generated} from data/engagements.csv. Regenerate with
<code>python3 scripts/dashboard.py</code>.</p>
{body}
</body></html>
"""


def main():
    rows = load_rows()
    OUT_PATH.parent.mkdir(exist_ok=True)
    OUT_PATH.write_text(build(rows), encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({len(rows)} row(s)).")


if __name__ == "__main__":
    main()
