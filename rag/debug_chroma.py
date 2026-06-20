from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

CHROMA_PATH = "database/chroma_db"
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding)

total = db._collection.count()
print(f"Total chunks in DB: {total}")

all_docs = db._collection.get()
for i, text in enumerate(all_docs["documents"]):
    print(f"\n[Chunk {i+1}]:\n{text}")
    print("-" * 50)