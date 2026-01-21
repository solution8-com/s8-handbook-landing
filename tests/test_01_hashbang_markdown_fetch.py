import asyncio
from pathlib import Path

from bs4 import BeautifulSoup
from playwright.async_api import async_playwright


URL = "https://www.thelmbook.com/wiki/#!index.md"
TIMEOUT_MS = 30000
MIN_CONTENT_LEN = 2000
MIN_HEADINGS = 2
MIN_LINKS = 10


def _html_to_markdownish(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    lines = []
    for tag in soup.find_all(["h1", "h2", "h3", "p", "li", "a"]):
        text = tag.get_text(strip=True)
        if not text:
            continue
        if tag.name in ("h1", "h2"):
            prefix = "# " if tag.name == "h1" else "## "
            lines.append(f"{prefix}{text}")
        elif tag.name == "a":
            href = tag.get("href", "")
            lines.append(f"[{text}]({href})" if href else text)
        else:
            lines.append(text)
    # Fallback to full text if structured capture is too small
    joined = "\n".join(lines)
    if len(joined) < MIN_CONTENT_LEN:
        return soup.get_text("\n", strip=True)
    return joined


def _extract_links(html: str):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "#!" in href or href.endswith(".md"):
            links.append(href)
    return links


async def _fetch_markdown_and_links():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(ignore_https_errors=True)
        page = await context.new_page()
        response = await page.goto(
            URL, wait_until="networkidle", timeout=TIMEOUT_MS
        )
        html = await page.content()
        current_url = page.url
        await context.close()
        await browser.close()
        return response, current_url, html


def test_hashbang_markdown_fetch():
    response, current_url, html = asyncio.run(_fetch_markdown_and_links())
    status = response.status if response else 0
    content = _html_to_markdownish(html)
    links = _extract_links(html)
    heading_count = content.count("\n#")

    diagnostics = (
        f"page.url: {current_url}\n"
        f"status: {status}\n"
        f"content_len: {len(content)}\n"
        f"headings: {heading_count}\n"
        f"links_found: {len(links)}\n"
        f"content_preview:\n{content[:500]}\n"
        f"link_samples: {links[:10]}"
    )

    assert "#!index.md" in current_url or "index.md" in current_url, diagnostics
    assert status in (200, 301, 302), diagnostics
    assert len(content) > MIN_CONTENT_LEN, diagnostics
    assert heading_count >= MIN_HEADINGS, diagnostics
    assert len(links) >= MIN_LINKS, diagnostics
