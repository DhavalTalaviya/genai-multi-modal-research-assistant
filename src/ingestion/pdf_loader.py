from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from config.settings import pdf_dir

def load_pdfs(pdf_dir: str):
    """
    Load all PDFs in pdf_dir into a list of Document objects.
    """
    docs = []
    for pdf_path in Path(pdf_dir).glob("*.pdf"):
        loader = PyPDFLoader(str(pdf_path))
        docs.extend(loader.load())
    return docs

if __name__ == "__main__":
    from config.settings import pdf_dir, processed_text_dir
    from pathlib import Path

    # Load all pages
    documents = load_pdfs(pdf_dir)
    print(f"Loaded {len(documents)} pages from PDFs in '{pdf_dir}'.")

    # Ensure output dir exists
    Path(processed_text_dir).mkdir(parents=True, exist_ok=True)

    # Write each page to a separate .txt file
    for doc in documents:
        # metadata.source is the PDF path, metadata.page has page number
        src_path = Path(doc.metadata["source"])
        stem     = src_path.stem
        page_no  = doc.metadata.get("page", "0")
        out_file = Path(processed_text_dir) / f"{stem}_page{page_no}.txt"
        out_file.write_text(doc.page_content, encoding="utf-8")

    print(f"Saved text files to '{processed_text_dir}'.")