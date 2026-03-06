#!/usr/bin/env python3
"""
CLI entry point for the Copernicus documentation scraper.

Usage:
    python run.py scrape [--max-minutes 10]
"""

from __future__ import annotations

import argparse
import logging
import sys
import traceback

from crawl import crawl, DEFAULT_START_URL, DEFAULT_MAX_MINUTES
from storage import generate_run_id, save_output


def cmd_scrape(args: argparse.Namespace) -> None:
    """Run the BFS crawl and write output."""
    run_id = generate_run_id()
    logging.info("Starting run %s", run_id)

    try:
        result = crawl(
            start_url=args.start_url,
            max_minutes=args.max_minutes,
        )

        # Attempt to write output
        output_size = save_output(result.pages)

        print(f"\n✅  Run {run_id} complete")
        print(f"   Pages scraped : {len(result.pages)}")
        print(f"   Errors        : {len(result.errors)}")
        print(f"   Output size   : {output_size:,} bytes")
        print(f"   Elapsed       : {result.elapsed_seconds}s")

    except Exception as exc:
        error_msg = f"{type(exc).__name__}: {exc}"
        logging.error("Run %s failed: %s", run_id, error_msg)
        traceback.print_exc()
        print(f"\n❌  Run {run_id} failed: {error_msg}")
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Copernicus Documentation Scraper",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable debug logging"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- scrape ---
    sp_scrape = subparsers.add_parser("scrape", help="Run the BFS crawl")
    sp_scrape.add_argument(
        "--max-minutes",
        type=float,
        default=DEFAULT_MAX_MINUTES,
        help=f"Safety timeout in minutes (default: {DEFAULT_MAX_MINUTES})",
    )
    sp_scrape.add_argument(
        "--start-url",
        type=str,
        default=DEFAULT_START_URL,
        help=f"Starting URL for the crawl (default: {DEFAULT_START_URL})",
    )

    args = parser.parse_args()

    # Configure logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s  %(levelname)-8s  %(message)s",
        datefmt="%H:%M:%S",
    )

    if args.command == "scrape":
        cmd_scrape(args)
    else:
        logging.error("Unknown command: %s", args.command)
        sys.exit(1)


if __name__ == "__main__":
    main()
