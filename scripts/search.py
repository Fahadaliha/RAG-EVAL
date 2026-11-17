import sys 
from pathlib import Path
from rag_eval.ingest import load_documents,chunk_document
from rag_eval.retrieval import BM25Retriever
query = sys.argv[1]
docs = load_documents(Path("data/docs"))
chunks = [c for d in docs for c in chunk_document(d,500,100)]
retriever= BM25Retriever(chunks)
for chunk_id in retriever.search(query,3):
    print(chunk_id)
    