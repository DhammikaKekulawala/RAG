from langchain.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings  # Updated import
from langchain.vectorstores import Chroma
from app.config import CHROMA_DIR

def ingest_pdf(file_path: str):
    # Load the PDF file
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    
    # Create an embedding model (using a model from sentence-transformers)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Create a vector store database and persist it
    vectordb = Chroma.from_documents(documents, embeddings, persist_directory=CHROMA_DIR)
    vectordb.persist()
    return {"status": "ingested", "file": file_path}
