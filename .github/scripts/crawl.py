"""
BFS link-driven crawl of Copernicus documentation.
"""

from __future__ import annotations

import logging
import time
from collections import deque
from dataclasses import dataclass, field
from datetime import datetime, timezone

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from extract import extract_links, extract_page
from normalize import ALLOWED_HOST, normalize_url

logger = logging.getLogger(__name__)

DEFAULT_START_URL = f"https://{ALLOWED_HOST}/"

# Crawl tunables
REQUEST_TIMEOUT = 30  # seconds per request
RATE_LIMIT_DELAY = 0.25  # seconds between requests (politeness)
DEFAULT_MAX_MINUTES = 10  # safety cap on total runtime


@dataclass
class CrawlResult:
    """Aggregated result of a full crawl run."""

    pages: list[dict] = field(default_factory=list)
    errors: list[dict] = field(default_factory=list)
    started_at: str = ""
    finished_at: str = ""
    total_urls_seen: int = 0
    elapsed_seconds: float = 0.0


def _decode_html_response(resp: requests.Response) -> str:
    """
    Decode response body as UTF-8 first to avoid mojibake (e.g. â...â).
    Falls back to declared/apparent encoding if UTF-8 is not valid.
    """
    raw = resp.content
    try:
        return raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        fallback_encoding = resp.encoding or resp.apparent_encoding or "latin-1"
        logger.warning(
            "Non-UTF-8 page at %s; decoding with fallback encoding: %s",
            resp.url,
            fallback_encoding,
        )
        return raw.decode(fallback_encoding, errors="replace")


def _build_session() -> requests.Session:
    """Build a requests Session with retry policy."""
    session = requests.Session()
    retries = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update(
        {
            "User-Agent": "CopernicusDocsScraper/1.0 (+https://github.com/eu-cdse/documentation)",
            "Accept-Charset": "utf-8",
        }
    )
    return session


def crawl(
    start_url: str = DEFAULT_START_URL,
    max_minutes: float = DEFAULT_MAX_MINUTES,
) -> CrawlResult:
    """
    BFS crawl starting from *start_url*.

    Follows all same-host HTML links until the queue is exhausted or
    *max_minutes* elapses (safety net).
    """
    result = CrawlResult()
    result.started_at = datetime.now(timezone.utc).isoformat()

    session = _build_session()
    queue: deque[str] = deque()
    visited: set[str] = set()

    # Seed the queue
    seed = normalize_url(start_url)
    if not seed:
        raise ValueError(f"Invalid start URL: {start_url}")
    queue.append(seed)
    visited.add(seed)

    deadline = time.monotonic() + max_minutes * 60

    while queue:
        # Safety: respect max runtime
        if time.monotonic() > deadline:
            logger.warning(
                "Max runtime of %.1f minutes reached – stopping crawl.", max_minutes
            )
            break

        url = queue.popleft()
        logger.info(
            "Crawling [%d done, %d queued]: %s", len(result.pages), len(queue), url
        )

        try:
            resp = session.get(url, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()

            # Skip non-HTML responses
            content_type = resp.headers.get("Content-Type", "")
            if "html" not in content_type.lower():
                logger.debug("Skipping non-HTML content-type: %s", content_type)
                continue

            html = _decode_html_response(resp)

            # Extract page data
            page_data = extract_page(html, url)
            result.pages.append(page_data)

            # Discover links
            raw_links = extract_links(html, url)
            for href in raw_links:
                normalized = normalize_url(href, base_url=url)
                if normalized and normalized not in visited:
                    visited.add(normalized)
                    queue.append(normalized)

        except requests.RequestException as exc:
            logger.error("Failed to fetch %s: %s", url, exc)
            result.errors.append({"url": url, "error": str(exc)})

        # Politeness delay
        time.sleep(RATE_LIMIT_DELAY)

    result.total_urls_seen = len(visited)
    result.finished_at = datetime.now(timezone.utc).isoformat()
    result.elapsed_seconds = round(
        (
            datetime.fromisoformat(result.finished_at)
            - datetime.fromisoformat(result.started_at)
        ).total_seconds(),
        2,
    )

    # Sort pages deterministically by URL for stable output
    result.pages.sort(key=lambda p: p["url"])

    logger.info(
        "Crawl complete: %d pages extracted, %d errors, %.1fs elapsed",
        len(result.pages),
        len(result.errors),
        result.elapsed_seconds,
    )
    return result
