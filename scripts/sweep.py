#!/usr/bin/env python3
"""Auto-capture sweep.

Lists recent Devin sessions via the Devin API and prints draft capture-row
stubs for any session not yet referenced in data/engagements.csv. Output is a
draft for human/weekly-session review -- this script never writes to the CSV.

Usage:
    DEVIN_API_KEY=... python3 scripts/sweep.py [--days 14]

No dependencies beyond the Python 3 standard library.
"""

import argparse
import csv
import json
import os
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

API_BASE = "https://api.devin.ai/v1"
REPO_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = REPO_ROOT / "data" / "engagements.csv"


def api_get(path: str, api_key: str) -> dict:
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        headers={"Authorization": f"Bearer {api_key}"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def known_session_ids() -> set:
    ids = set()
    if not CSV_PATH.exists():
        return ids
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            for token in (row.get("sessions") or "").replace(";", " ").split():
                ids.add(token.rstrip("/").split("/")[-1])
    return ids


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=14,
                        help="look-back window in days (default 14)")
    args = parser.parse_args()

    api_key = os.environ.get("DEVIN_API_KEY")
    if not api_key:
        print("ERROR: DEVIN_API_KEY is not set. Create an API key in Devin "
              "Settings -> API and store it as a secret.", file=sys.stderr)
        return 1

    try:
        data = api_get("/sessions?limit=100", api_key)
    except Exception as exc:  # noqa: BLE001 - report any API failure plainly
        print(f"ERROR: Devin API request failed: {exc}", file=sys.stderr)
        return 1

    sessions = data.get("sessions", data if isinstance(data, list) else [])
    known = known_session_ids()
    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)

    drafts = []
    for s in sessions:
        sid = s.get("session_id", "")
        created = s.get("created_at", "")
        try:
            created_dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
        except ValueError:
            created_dt = None
        if created_dt and created_dt < cutoff:
            continue
        if sid.split("-")[-1] in known or sid in known:
            continue
        drafts.append({
            "session_id": sid,
            "created_at": created,
            "title": s.get("title") or (s.get("prompt") or "")[:120],
            "playbook_id": s.get("playbook_id") or "",
            "status": s.get("status_enum") or s.get("status") or "",
            "acus": s.get("acu_used") or "",
        })

    if not drafts:
        print(f"No uncaptured sessions in the last {args.days} days.")
        return 0

    print(f"# {len(drafts)} uncaptured session(s) in the last {args.days} "
          f"days -- draft capture stubs below.")
    print("# Review, group sessions belonging to the same engagement into one "
          "row, and leave `outcome` blank for a human to label.\n")
    for d in drafts:
        print(json.dumps(d, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
