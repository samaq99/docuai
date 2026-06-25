# DocuAI

AI-powered document Q&A system for HR consultants. Upload employment contracts, policy documents, and German labour law PDFs — ask questions in plain English, receive answers with exact source citations.

Built for a German HR services firm via Devstride Solutions.

---

## Stack

- **Backend:** FastAPI, LangGraph, Qdrant, Langfuse
- **Frontend:** Next.js
- **Auth:** JWT (per-user document isolation)
- **Deployment:** Azure Container Apps (West Europe — EU data residency)
- **Evaluation:** RAGAS

## Key Design Decisions

- **Qdrant over Pinecone** — self-hosted on Azure, data never leaves EU jurisdiction (GDPR)
- **Langfuse over LangSmith** — Berlin-based, self-hostable, GDPR-compliant observability
- **Multilingual embeddings** — `paraphrase-multilingual-MiniLM-L12-v2` handles German documents + English queries
- **CrossEncoder reranking** — retrieve top-10, rerank to top-3 before passing to LLM

## Project Structure

```
app/
├── api/v1/routes/    # FastAPI route handlers
├── core/             # Config, JWT, dependencies
├── services/         # Ingestion, retrieval, agent logic
└── models/           # Pydantic request/response models
frontend/             # Next.js consultant interface
tests/                # pytest
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register` | Register a consultant account |
| POST | `/api/v1/auth/login` | Login, receive JWT |
| POST | `/api/v1/upload` | Upload a PDF document |
| POST | `/api/v1/ask` | Ask a question against your documents |
| GET | `/health` | Health check |

## Running Locally

```bash
# Start Qdrant
docker run -p 6333:6333 qdrant/qdrant

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env

# Start the API
uvicorn app.main:app --reload
```

---

*RAGAS evaluation scores documented in handover package.*
