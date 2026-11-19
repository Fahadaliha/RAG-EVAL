import re
from rank_bm25 import BM25Okapi
from nltk.stem import PorterStemmer

STOPWORDS = {"how", "do", "i", "a", "an", "the", "to", "is", "of", "in", "my", "what", "can", "we", "you"}
STEMMER = PorterStemmer()
def tokenize(text:str) -> list[str]:
    tokens = re.findall(r"[a-z0-9_]+",text.lower())
    return[STEMMER.stem(t) for t in tokens if t not in STOPWORDS]

class BM25Retriever:
    def __init__(self,chunks:list[dict[str,str]]):
        self.chunks=chunks
        tokenized = [tokenize(chunk["text"])for chunk in chunks]
        self.bm25 = BM25Okapi(tokenized)
    def search(self,query:str,k:int) -> list[str]:
        tokens=tokenize(query)
        scores = self.bm25.get_scores(tokens)
        ranked = sorted(range(len(scores)), key = lambda i:scores[i],reverse=True)
        return [self.chunks[i]["chunk_id"]for i in ranked[:k]]
    