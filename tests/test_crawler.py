import os
import shutil

from crawl_wiki import _extract_links, crawl


def test_extract_links_html_and_md():
    content = """
    <a href="page1.md">Page</a>
    [](page2.md)
    [text](page3.md#section)
    <a href="https://example.com/outside">out</a>
    """
    links = set(_extract_links(content))
    assert "page1.md" in links
    assert "page2.md" in links
    assert "page3.md#section" in links
    assert "https://example.com/outside" in links


def test_crawl_stops_after_max_pages(tmp_path, monkeypatch):
    html = '<a href="page2.md">Next</a>'

    def fake_fetch(url: str):
        return html

    monkeypatch.setattr("crawl_wiki._fetch", fake_fetch)
    output = tmp_path / "wiki"
    crawl("https://www.thelmbook.com/wiki/#!index.md", str(output), max_pages=1)
    saved = list(output.rglob("*.md"))
    assert len(saved) == 1
