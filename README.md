# GenAI Multi‑Modal Research Assistant

An end‑to‑end Retrieval‑Augmented Generation assistant that ingests PDFs, web pages, and images—then answers questions over both text and visual content.

---

## 🚀 Current Progress (Phase 1)

- **Data Ingestion & Preprocessing**  
  - PDF loader (`src/ingestion/pdf_loader.py`)  
  - Web scraper (`src/ingestion/web_scraper.py`)  
  - Image captioning (`src/ingestion/image_caption.py`)  
- **Directory structure** and config scaffolding  
- **Automated tests** for each loader  
- **Output** saved under `data/processed/`

---

## 📅 Upcoming Phases

1. **Phase 2: Embeddings & Indexing**  
   - Turn text & captions into vectors (Sentence‑Transformers, CLIP)  
   - Build a FAISS index  
2. **Phase 3: RAG Orchestration & Guardrails**  
   - LangChain/LangGraph pipelines  
   - Safety middleware  
3. **Phase 4: Agentic Sub‑Flows & Evaluation**  
   - Summarizer, follow‑up question agents  
   - Benchmarking with held‑out Q&A  
4. **Phase 5: API & Front‑End**  
   - FastAPI backend  
   - Streamlit (or React) UI  
5. **Phase 6: Cloud Deployment & IaC**  
   - Docker + AWS Terraform  
   - GitHub Actions CI/CD

---

## 📂 Repo Structure

```plaintext
genai-multi-modal-research-assistant/
├── README.md
├── requirements.txt
├── config/
│   ├── settings.yaml
│   └── settings.py
├── data/
│   ├── raw/              # PDFs, HTML, images
│   └── processed/        # texts & captions
├── src/
│   ├── ingestion/
│   └── embeddings/       # (coming soon)
│   └── pipeline/         # (Phase 3)
│   └── agents/           # (Phase 4)
│   └── api/              # (Phase 5)
│   └── utils/
├── notebooks/            # demos
├── tests/                # unit tests
└── infra/                # Docker & Terraform (Phase 6)
