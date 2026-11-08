# rag-eval

Question answering over technical documents: the system retrieves the most relevant passages and uses them to answer with measured evaluation of each design choice.

## Status

Done:

- Retrieval metrics: `recall_at_k` and `mrr`
- Unit tests for both metrics

Coming next:

- Document ingestion and chunking
- Keyword (BM25) and embedding-based retrieval
- Labeled evaluation set and experiments

## Run the tests

```bash
uv run pytest
```
