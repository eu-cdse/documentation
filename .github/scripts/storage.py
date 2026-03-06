"""
Atomic file writes and append-only run logging.
"""

from __future__ import annotations

import json
import os
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path

# Resolve project root relative to this file
_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

OUTPUT_DIR = _PROJECT_ROOT / "search_index"
OUTPUT_FILE = OUTPUT_DIR / "copernicus_docs.json"

# Minimum pages required to overwrite the output (safety threshold)
MIN_PAGES_THRESHOLD = 10


def ensure_dirs() -> None:
    """Create output/ and runs/ directories if they don't exist."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def atomic_write_json(data: list[dict], path: Path | None = None) -> int:
    """
    Write JSON atomically: temp file → fsync → rename.

    Returns the file size in bytes.
    """
    path = path or OUTPUT_FILE
    path.parent.mkdir(parents=True, exist_ok=True)

    content = json.dumps(data, indent=2, ensure_ascii=False)
    content_bytes = content.encode("utf-8")

    fd, tmp_path = tempfile.mkstemp(
        dir=str(path.parent), suffix=".tmp", prefix=".scraper_"
    )
    try:
        os.write(fd, content_bytes)
        os.fsync(fd)
        os.close(fd)
        os.replace(tmp_path, str(path))
    except BaseException:
        os.close(fd) if not os.get_inheritable(fd) else None  # noqa: already closed on success
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise

    return len(content_bytes)


def validate_output(pages: list[dict]) -> list[str]:
    """
    Validate basic sanity of the output data.
    Returns a list of error messages (empty = valid).
    """
    issues: list[str] = []
    if not pages:
        issues.append("Output is empty (no pages)")
        return issues

    required_keys = {"unique_id", "title", "url", "body"}
    for i, page in enumerate(pages):
        missing = required_keys - set(page.keys())
        if missing:
            issues.append(f"Page {i} missing keys: {missing}")
    return issues


def save_output(pages: list[dict]) -> int:
    """
    Validate and atomically write the output JSON.

    Returns the file size in bytes.
    Raises ValueError if validation fails critically.
    """
    ensure_dirs()

    issues = validate_output(pages)
    if issues:
        for issue in issues:
            print(f"  ⚠ {issue}")

    if len(pages) < MIN_PAGES_THRESHOLD:
        raise ValueError(
            f"Only {len(pages)} pages scraped (threshold: {MIN_PAGES_THRESHOLD}). "
            f"Refusing to overwrite output to avoid writing garbage."
        )

    return atomic_write_json(pages)


def generate_run_id() -> str:
    """Generate a short unique run ID."""
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "_" + uuid.uuid4().hex[:6]
