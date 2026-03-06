"""
URL normalization and unique_id generation.
"""

import re
from urllib.parse import urlparse, urldefrag, urljoin

# Extensions we consider crawlable (HTML/doc pages)
_CRAWLABLE_EXTENSIONS = {".html", ".htm", ""}

ALLOWED_HOST = "documentation.dataspace.copernicus.eu"


def normalize_url(url: str, base_url: str | None = None) -> str | None:
    """
    Normalize a URL for dedup / crawl eligibility.

    Returns the cleaned absolute URL (no fragment), or None if it should
    be skipped (off-host, non-HTML, mailto, etc.).
    """
    # Resolve relative URLs
    if base_url:
        url = urljoin(base_url, url)

    # Strip fragment
    url, _ = urldefrag(url)

    parsed = urlparse(url)

    # Must be http(s)
    if parsed.scheme not in ("http", "https"):
        return None

    # Must stay on the allowed host
    if parsed.hostname != ALLOWED_HOST:
        return None

    # Check extension
    path_lower = parsed.path.lower()

    # Get extension from path
    dot_pos = path_lower.rfind(".")
    ext = path_lower[dot_pos:] if dot_pos != -1 else ""

    if ext and ext not in _CRAWLABLE_EXTENSIONS:
        return None

    # Rebuild clean URL (strip trailing whitespace, keep query for completeness)
    return url.strip()


def url_to_unique_id(url: str) -> str:
    """
    Derive a stable slug from the URL path.

    Examples:
        AnnualReports.html  → annual_reports
        Home.html           → home
        APIs/SentinelHub/Process.html → apis_sentinelhub_process
    """
    parsed = urlparse(url)
    path = parsed.path.strip("/")

    # Remove .html / .htm extension
    path = re.sub(r"\.html?$", "", path, flags=re.IGNORECASE)

    if not path:
        return "index"

    # Replace path separators with underscores
    slug = path.replace("/", "_")

    # Insert underscore before uppercase letters (CamelCase → Camel_Case)
    slug = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", slug)

    # Replace any non-alphanumeric characters with underscores
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", slug)

    # Lowercase and collapse multiple underscores
    slug = re.sub(r"_+", "_", slug.lower()).strip("_")

    return slug or "index"


def clean_whitespace(text: str) -> str:
    """
    Remove all newlines and collapse whitespace to single spaces.
    """
    # Replace newlines with space
    text = text.replace("\n", " ").replace("\r", " ")
    # Collapse all whitespace runs to a single space
    text = re.sub(r"\s+", " ", text)
    return text.strip()
