from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import( HuggingFaceEmbeddings)
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
import os
CHROMA_PATH="database/chroma_db"
def ingest_pdf(pdf_path):
    loader=PyPDFLoader(pdf_path)
    documents=loader.load()
    splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks=splitter.split_documents(documents)
    embedding_model=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db=Chroma.from_documents(chunks, embedding_model, persist_directory=CHROMA_PATH)
    return "PDF ingested and indexed successfully."