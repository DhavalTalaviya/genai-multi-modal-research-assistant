from pathlib import Path
from bs4 import BeautifulSoup
from langchain.schema import Document
from config.settings import html_dir, processed_text_dir

def load_html_files(html_dir: str) -> list[Document]:
    """
    Parse all local HTML files in html_dir into a list of Documents.
    """
    docs = []
    for html_path in Path(html_dir).glob("*.html"):
        content = html_path.read_text(encoding="utf-8")
        soup = BeautifulSoup(content, "html.parser")
        # Extract only non‑empty <p> text
        paras = [p.get_text().strip() for p in soup.find_all("p") if p.get_text().strip()]
        text = "\n\n".join(paras)
        docs.append(Document(page_content=text, metadata={"source": str(html_path)}))
    return docs

if __name__ == "__main__":
    # load & save
    docs = load_html_files(html_dir)
    print(f"Loaded {len(docs)} HTML files from '{html_dir}'.")
    Path(processed_text_dir).mkdir(parents=True, exist_ok=True)
    for doc in docs:
        src = Path(doc.metadata["source"])
        out = Path(processed_text_dir) / f"{src.stem}.txt"
        out.write_text(doc.page_content, encoding="utf-8")
    print(f"Saved scraped texts to '{processed_text_dir}'.")
