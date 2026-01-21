import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import deque
from typing import Iterable, Optional

from bs4 import BeautifulSoup


BASE_URL = "https://www.thelmbook.com/wiki/"
DEFAULT_START = "https://www.thelmbook.com/wiki/#!index.md"
USER_AGENT = "s8-handbook-landing-crawler/1.0"


def _canonicalize_link(raw_link: str, context_url: str):
    """Return (absolute_fetch_url, relative_path) for in-scope markdown links."""
    resolved = urllib.parse.urljoin(context_url, raw_link)
    parsed = urllib.parse.urlparse(resolved)

    # Reject external domains
    base_domain = urllib.parse.urlparse(BASE_URL).netloc
    if parsed.netloc and parsed.netloc != base_domain:
        return None

    # Handle hashbang links
    if parsed.fragment.startswith("!"):
        path = parsed.fragment[1:]
    else:
        path = parsed.path.lstrip("/")

    if not path.endswith(".md"):
        return None

    abs_url = urllib.parse.urljoin(BASE_URL, path)
    return abs_url, path


def _extract_links(content: str) -> Iterable[str]:
    """Extract markdown and HTML links from content."""
    links = set()

    # HTML links
    soup = BeautifulSoup(content, "html.parser")
    for tag in soup.find_all("a", href=True):
        links.add(tag["href"])

    # Markdown links
    md_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)", re.IGNORECASE)
    for match in md_pattern.finditer(content):
        links.add(match.group(1))

    return links


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req) as resp:  # nosec: B310 - external fetch is required
        return resp.read().decode("utf-8", errors="replace")


def crawl(
    start_url: str = DEFAULT_START,
    output_dir: str = "wiki",
    max_pages: Optional[int] = None,
):
    stack = deque([start_url])
    visited = set()
    os.makedirs(output_dir, exist_ok=True)

    while stack:
        current = stack.pop()
        canonical = _canonicalize_link(current, BASE_URL)
        if not canonical:
            continue

        fetch_url, rel_path = canonical
        if rel_path in visited:
            continue
        visited.add(rel_path)

        if max_pages is not None and len(visited) > max_pages:
            break

        try:
            content = _fetch(fetch_url)
        except (urllib.error.URLError, urllib.error.HTTPError) as exc:  # pragma: no cover - network errors
            print(f"Failed to fetch {fetch_url}: {exc}")
            continue

        dest_path = os.path.join(output_dir, rel_path)
        dir_name = os.path.dirname(dest_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(content)

        for raw_link in _extract_links(content):
            normalized = _canonicalize_link(raw_link, fetch_url)
            if normalized:
                _, next_rel = normalized
                if next_rel not in visited:
                    stack.append(raw_link)


if __name__ == "__main__":
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "wiki"
    start = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_START
    crawl(start, out_dir)
