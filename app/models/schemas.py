from pydantic import BaseModel

class UploadResponse(BaseModel):
    status: str
    file: str

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
