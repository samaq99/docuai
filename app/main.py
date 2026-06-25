from fastapi import FastAPI
from app.api.v1.routes import upload, ask, auth

app = FastAPI(
    title="DocuAI",
    description="AI-powered document Q&A for HR consultants",
    version="1.0.0",
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(upload.router, prefix="/api/v1", tags=["documents"])
app.include_router(ask.router, prefix="/api/v1", tags=["q&a"])


@app.get("/health")
def health():
    return {"status": "ok"}
