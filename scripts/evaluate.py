import json
import sys
from pathlib import Path

from rag_eval.ingest import load_documents , chunk_document
from rag_eval.retrieval import BM25Retriever
from rag_eval.metrics import recall_at_k , mrr


chunk_size = int(sys.argv[1]) if len (sys.argv)>1 else 500
overlap = chunk_size//5
docs = load_documents(Path("data/docs"))
chunks = [c for d in docs for c in chunk_document(d,chunk_size,overlap)]
retriever = BM25Retriever(chunks)

with open ("data/eval_questions.json",encoding="utf-8") as f:
    questions = json.load(f)

recalls = []
mrrs=[]

for q in questions:
    chunks_ids = retriever.search(q["question"],10)
    files = [cid.split("#")[0]for cid in chunks_ids]
    files=list(dict.fromkeys(files))
    relevant = set(q["relevant"])
    recalls.append(recall_at_k(files,relevant,3))
    mrrs.append(mrr(files,relevant))

    print(q["question"])
    print(" top3:",files[:3],"expected:",q["relevant"])

print()
print(f"chunk_size={chunk_size} overlap={overlap} chunks={len(chunks)}")
print(f"recall@3={sum(recalls)/len(recalls):.2f}")
print(f"mrr={sum(mrrs)/len(mrrs):.2f}")