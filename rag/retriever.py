import chromadb
from chromadb.config import Settings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from rag.hybrid_search import HybridSearch
from config import CHROMA_PATH, EMBEDDING_MODEL

embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

# ✅ allow_reset=True so admin can delete PDFs
chroma_client = chromadb.PersistentClient(
    path=CHROMA_PATH,
    settings=Settings(allow_reset=True)
)

db = Chroma(
    client=chroma_client,
    embedding_function=embedding
)

retriever = db.as_retriever(search_kwargs={"k": 5})

QUERY_EXPANSION = {
    "minimum deposit"  : "minimum fixed deposit amount opening balance",
    "maximum deposit"  : "maximum fixed deposit amount limit",
    "interest rate"    : "interest rate fixed deposit savings account",
    "loan"             : "loan eligibility amount interest repayment",
    "account opening"  : "account opening requirements documents minimum balance",
}

def expand_query(query: str) -> str:
    query_lower = query.lower()
    for key, expansion in QUERY_EXPANSION.items():
        if key in query_lower:
            return f"{query} {expansion}"
    return query

def get_context(query: str) -> str:
    expanded = expand_query(query)
    docs = retriever.invoke(expanded)
    semantic_texts = [doc.page_content for doc in docs]

    if semantic_texts:
        hybrid = HybridSearch(semantic_texts)
        reranked = hybrid.search(expanded)
        context = "\n\n".join(reranked)
    else:
        context = "\n\n".join(semantic_texts)

    return context