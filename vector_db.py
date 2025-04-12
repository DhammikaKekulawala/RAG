import pandas as pd
from fastapi import FastAPI
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import pickle
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
import os

load_dotenv()

app = FastAPI()
embeddings = OpenAIEmbeddings()


@app.get("/load-pdf")
async def load_pdf():
    file_path = os.getenv("FILE_PATH")

    if not file_path or not os.path.exists(file_path):
        return {"error": "Invalid or missing FILE_PATH"}

    loader = PyPDFLoader(file_path)
    documents = loader.load()
    print(documents[0])

    return {"message": f"Loaded {len(documents)} pages {documents[0]}"}
