from rank_bm25 import BM25Okapi

class BM25Retriever:
    def __init__(self,chunks:list[dict[str,str]]):
        self.chunks=chunks
        tokenized = [chunk["text"].lower().split()for chunk in chunks]
        self.bm25 = BM25Okapi(tokenized)
    def search(self,query:str,k:int) -> list[str]:
        tokens=query.lower().split()
        scores = self.bm25.get_scores(tokens)
        ranked = sorted(range(len(scores)), key = lambda i:scores[i],reverse=True)
        return [self.chunks[i]["chunk_id"]for i in ranked[:k]]
    