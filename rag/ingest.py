import chromadb
from chromadb.config import Settings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from config import CHROMA_PATH, EMBEDDING_MODEL

def ingest_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    # ✅ Same settings as retriever.py
    chroma_client = chromadb.PersistentClient(
        path=CHROMA_PATH,
        settings=Settings(allow_reset=True)
    )

    db = Chroma(
        client=chroma_client,
        embedding_function=embedding_model
    )
    db.add_documents(chunks)

    return "✅ PDF ingested and indexed successfully."