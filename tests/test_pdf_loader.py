import os
from src.ingestion.pdf_loader import load_pdfs

def test_load_pdfs(tmp_path):
    pdf_file = tmp_path / "dummy.pdf"
    pdf_file.write_bytes(b"%PDF-1.4\n%%EOF")  
    docs = load_pdfs(str(tmp_path))
    assert len(docs) >= 1
