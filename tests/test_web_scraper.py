from pathlib import Path
from src.ingestion.web_scraper import load_html_files

def test_load_html_files(tmp_path):

    html = tmp_path / "sample.html"
    html.write_text(
        "<html><body>"
        "<p>Hello world.</p>"
        "<p>Second paragraph.</p>"
        "</body></html>",
        encoding="utf-8"
    )

    docs = load_html_files(str(tmp_path))

    assert len(docs) == 1
    doc = docs[0]
    assert "Hello world." in doc.page_content
    assert "Second paragraph." in doc.page_content
    assert doc.metadata["source"].endswith("sample.html")
