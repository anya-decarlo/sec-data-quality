"""Command-line interface.

  python -m sec_data_quality sample              # synthetic data, no network
  python -m sec_data_quality fetch AAPL MSFT     # cache EDGAR payloads
  python -m sec_data_quality run --tickers AAPL MSFT
  python -m sec_data_quality run --offline       # whatever is already cached
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from .edgar import DEFAULT_USER_AGENT, fetch_companyfacts
from .pipeline import DEFAULT_METRICS, run
from .sample_data import write_sample

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
SAMPLE_DIR = ROOT / "data" / "sample"
OUT_DIR = ROOT / "outputs"


def _user_agent() -> str:
    return os.environ.get("SEC_USER_AGENT", DEFAULT_USER_AGENT)


def cmd_sample(args) -> int:
    path = write_sample(SAMPLE_DIR if not args.raw_dir else Path(args.raw_dir))
    print(f"sample payload written: {path}")
    stats = run([path], Path(args.out_dir), metrics=None)
    _print_stats(stats)
    return 0


def cmd_fetch(args) -> int:
    for t in args.tickers:
        path = fetch_companyfacts(t, Path(args.raw_dir), _user_agent())
        print(f"cached {t}: {path}")
    return 0


def cmd_run(args) -> int:
    raw_dir = Path(args.raw_dir)
    files: list[Path] = []
    if args.offline:
        files = sorted(raw_dir.glob("CIK*.json"))
        files = [f for f in files if "company_tickers" not in f.name]
        if not files:
            print("no cached payloads; run `fetch` first", file=sys.stderr)
            return 1
    else:
        for t in args.tickers:
            files.append(fetch_companyfacts(t, raw_dir, _user_agent()))
    metrics = None if args.all_tags else (args.metrics or DEFAULT_METRICS)
    stats = run(files, Path(args.out_dir), metrics)
    _print_stats(stats)
    return 0


def _print_stats(stats: dict) -> None:
    print(
        f"done: {stats['facts']:,} facts, {stats['findings']:,} findings, "
        f"{stats['recon_rows']:,} reconciliation rows -> {stats['out_dir']}"
    )


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        prog="sec_data_quality",
        description="DQ checks + reconciliation over SEC EDGAR XBRL facts",
    )
    p.add_argument("--raw-dir", default=str(RAW_DIR))
    p.add_argument("--out-dir", default=str(OUT_DIR))
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("sample", help="run the pipeline on synthetic data")

    f = sub.add_parser("fetch", help="download and cache companyfacts")
    f.add_argument("tickers", nargs="+")

    r = sub.add_parser("run", help="fetch (or reuse cache) and run checks")
    r.add_argument("--tickers", nargs="+", default=["AAPL", "MSFT"])
    r.add_argument("--metrics", nargs="*", default=None)
    r.add_argument("--all-tags", action="store_true",
                   help="run over every tag, not just the focus metrics")
    r.add_argument("--offline", action="store_true",
                   help="use whatever is cached, do not hit the network")

    args = p.parse_args(argv)
    return {"sample": cmd_sample, "fetch": cmd_fetch, "run": cmd_run}[args.cmd](args)
