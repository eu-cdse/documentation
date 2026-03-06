"""
Page content extraction: <main> → plain text body + title.
"""

from __future__ import annotations

from bs4 import BeautifulSoup, Tag

from normalize import clean_whitespace, url_to_unique_id


def extract_page(html: str, url: str) -> dict:
    """
    Extract structured data from a single HTML page.

    Returns a dict with keys: unique_id, title, url, body.
    """
    soup = BeautifulSoup(html, "html.parser")

    # --- body text ---
    main_tag: Tag | None = soup.find("main")
    container = main_tag if main_tag else soup.find("body")

    if container:
        body_raw = container.get_text(separator=" ", strip=True)
    else:
        body_raw = soup.get_text(separator=" ", strip=True)

    body = clean_whitespace(body_raw)

    # --- title ---
    title = _extract_title(soup, main_tag)

    # --- unique_id ---
    unique_id = url_to_unique_id(url)

    return {
        "unique_id": unique_id,
        "title": title,
        "url": url,
        "body": body,
    }


def extract_links(html: str, base_url: str) -> list[str]:
    """
    Return all raw href values from anchor tags in the page.
    Normalization / filtering happens upstream in normalize.py.
    """
    soup = BeautifulSoup(html, "html.parser")
    hrefs: list[str] = []
    for a in soup.find_all("a", href=True):
        hrefs.append(a["href"])
    return hrefs


# ------------------------------------------------------------------
# Internal helpers
# ------------------------------------------------------------------

def _extract_title(soup: BeautifulSoup, main_tag: Tag | None) -> str:
    """
    Prefer first <h1> inside <main>, else fall back to <title>.
    """
    if main_tag:
        h1 = main_tag.find("h1")
        if h1:
            return clean_whitespace(h1.get_text())

    # Fall back: any <h1> on the page
    h1 = soup.find("h1")
    if h1:
        return clean_whitespace(h1.get_text())

    # Fall back: <title> tag
    title_tag = soup.find("title")
    if title_tag:
        return clean_whitespace(title_tag.get_text())

    return ""
