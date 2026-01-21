import asyncio
import os
from pathlib import Path

from playwright.async_api import async_playwright


URL = "https://www.thelmbook.com/wiki/"


def _resolve_chromium_executable() -> str:
    env_path = os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE")
    if env_path and Path(env_path).exists():
        return env_path

    cache_dir = Path.home() / ".cache" / "ms-playwright"
    candidates = sorted(
        list(cache_dir.glob("chromium-*/chrome-linux/chrome"))
        + list(cache_dir.glob("chromium-*/chrome-linux64/chrome")),
        reverse=True,
    )
    if not candidates:
        raise FileNotFoundError("Chromium executable not found; run playwright install")
    return str(candidates[0])


async def _fetch_status_and_text(url: str):
    async with async_playwright() as p:
        chromium = p.chromium
        browser = await chromium.launch(
            headless=True, executable_path=_resolve_chromium_executable()
        )
        context = await browser.new_context(ignore_https_errors=True)
        page = await context.new_page()
        response = await page.goto(
            url, wait_until="networkidle", timeout=20000
        )
        text = await page.content()
        await context.close()
        await browser.close()
        status = response.status if response else 0
        return status, text or ""


def test_playwright_can_access_wiki():
    status, body = asyncio.run(_fetch_status_and_text(URL))
    assert status in (200, 301, 302), f"Unexpected status {status}"
    markers = ["wiki", "thelm"]
    assert any(m in body.lower() for m in markers), (
        "Page content did not include expected markers; "
        "body indicates potential JS-required splash"
    )
