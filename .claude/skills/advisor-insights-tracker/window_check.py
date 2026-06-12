#!/usr/bin/env python3
"""
Decide which meeting sessions fall inside the +/- 4 day window around the run date.

The window is INCLUSIVE on both ends: a session is included when
    run_date - 4 days  <=  session_date  <=  run_date + 4 days

Usage:
    # run date defaults to today (the machine's local date)
    python window_check.py --dates 2026-05-28,2026-06-04,2026-06-11

    # or pin the run date explicitly (e.g. to match the user's "I'm running this on 6/12")
    python window_check.py --run 2026-06-12 --dates 2026-05-28,2026-06-04,2026-06-11

Prints JSON: which dates are in/out, plus the window bounds.
Dates accepted as YYYY-MM-DD or M/D (M/D assumes the run date's year).
"""
import argparse
import datetime
import json
import sys

WINDOW_DAYS = 4


def parse_date(s, default_year):
    s = s.strip()
    for fmt in ("%Y-%m-%d", "%Y/%m/%d"):
        try:
            return datetime.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    # M/D form -> attach default year
    if "/" in s:
        m, d = s.split("/")[:2]
        return datetime.date(default_year, int(m), int(d))
    raise ValueError(f"Unrecognized date: {s!r}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", help="Run date YYYY-MM-DD (default: today)")
    ap.add_argument("--dates", required=True, help="Comma-separated session dates")
    ap.add_argument("--window", type=int, default=WINDOW_DAYS, help="+/- days (default 4)")
    args = ap.parse_args()

    run = (
        datetime.datetime.strptime(args.run, "%Y-%m-%d").date()
        if args.run
        else datetime.date.today()
    )
    lo = run - datetime.timedelta(days=args.window)
    hi = run + datetime.timedelta(days=args.window)

    included, excluded = [], []
    for raw in [x for x in args.dates.split(",") if x.strip()]:
        d = parse_date(raw, run.year)
        (included if lo <= d <= hi else excluded).append(
            {"input": raw.strip(), "date": d.isoformat()}
        )

    print(
        json.dumps(
            {
                "run_date": run.isoformat(),
                "window_start": lo.isoformat(),
                "window_end": hi.isoformat(),
                "included": included,
                "excluded": excluded,
            },
            indent=2,
        )
    )
    if not included:
        sys.exit(3)


if __name__ == "__main__":
    main()
