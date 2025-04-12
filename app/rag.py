from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from app.config import CHROMA_DIR, OPENAI_API_KEY

def ask_question(query: str):
    # Setup the embedding model and vector store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
    
    # Use OpenAI as the LLM
    llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.7)
    
    # Build the RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())
    answer = qa_chain.run(query)
    return answer
