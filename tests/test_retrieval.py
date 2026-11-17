from rag_eval.retrieval import BM25Retriever
CHUNKS = [
    {"chunk_id":"a#0","text":"cats like to sleep all day"},
    {"chunk_id":"b#0","text":"databases store data in tables"},
    {"chunk_id":"c#0","text":"Messi is Greatest of All time"},

]

def test_bm25_search_ranks_matching_chunk_first():
    retriever = BM25Retriever(CHUNKS)
    results = retriever.search("databases tables",3)
    assert results[0] == "b#0"
def test_bm25_search_respects_k():
    retriever = BM25Retriever(CHUNKS)
    results = retriever.search("databases tables",2)
    assert len(results) ==2
