from rank_bm25 import BM25Okapi

class HybridSearch:
    def __init__(self, docs):
        self.docs = docs
        self.tokenized_docs = [doc.split() for doc in docs]
        self.bm25 = BM25Okapi(self.tokenized_docs)

    def search(self, query, n=3):
        n = min(n, len(self.docs))  # ✅ avoid crash if docs < n
        return self.bm25.get_top_n(
            query.split(),
            self.docs,
            n=n
        )