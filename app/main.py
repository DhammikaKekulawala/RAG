from fastapi import FastAPI, File, UploadFile
from app.ingest import ingest_pdf
from app.rag import ask_question
from app.models.schemas import UploadResponse, QueryRequest, QueryResponse
from app.config import DOCUMENTS_DIR
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(
    title="RAG System API",
    description="A Retrieval-Augmented Generation API to ingest PDFs and answer questions using OpenAI.",
    version="1.0.0"
)

# Configure CORS (adjust allowed origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to specific origins for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload", response_model=UploadResponse, summary="Upload a PDF document")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(DOCUMENTS_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    # Ingest the PDF into the vector database
    ingest_pdf(file_path)
    return {"status": "ingested", "file": file.filename}

@app.post("/query", response_model=QueryResponse, summary="Query ingested documents with a natural language question")
async def query_pdf(data: QueryRequest):
    answer = ask_question(data.question)
    return {"answer": answer}
