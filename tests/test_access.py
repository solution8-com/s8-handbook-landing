import asyncio
import os
from pathlib import Path

from playwright.async_api import async_playwright


URL = "https://www.thelmbook.com/wiki/#!index.md"


def _resolve_chromium_executable() -> str:
    env_path = os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE")
    if env_path and Path(env_path).exists():
        return env_path

    cache_dir = Path.home() / ".cache" / "ms-playwright"
    candidates = sorted(
        cache_dir.glob("chromium-*/chrome-linux/chrome"), reverse=True
    )
    if not candidates:
        raise FileNotFoundError("Chromium executable not found; run playwright install")
    return str(candidates[0])


async def _fetch_status(url: str) -> int:
    async with async_playwright() as p:
        chromium = p.chromium
        browser = await chromium.launch(
            headless=True, executable_path=_resolve_chromium_executable()
        )
        page = await browser.new_page()
        response = await page.goto(
            url, wait_until="domcontentloaded", timeout=20000
        )
        await browser.close()
        return response.status if response else 0


def test_playwright_can_access_wiki():
    status = asyncio.run(_fetch_status(URL))
    assert status == 200, "Playwright could not reach the wiki URL; check DNS/network"
