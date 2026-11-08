from rag_eval.metrics import recall_at_k , mrr

def test_recall_at_k():
    assert recall_at_k(["a","b","c"],{"a","c"},k=2) ==0.5

def test_mrr():
    assert mrr(["x","y","a"],{"a"}) == 1/3



