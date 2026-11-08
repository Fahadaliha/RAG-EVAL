def recall_at_k(retrieved: list[str], relevant:set[str],k:int) -> float:
    if not relevant:
        return 0

    top_k = retrieved[:k]
    hits = set(top_k) & relevant 

    return len(hits)/len(relevant)

def mrr(retrieved: list[str], relevant: set[str]) -> float:
    for rank, doc_id in enumerate(retrieved, start=1):
        if doc_id in relevant:
            return 1.0/rank
    return 0