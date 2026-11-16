from pathlib import Path
import pytest 
from rag_eval.ingest import load_documents,chunk_document

def test_load_documents(tmp_path:Path):
    (tmp_path / "b.md").write_text("second",encoding="utf-8")
    (tmp_path / "a.md").write_text("first",encoding="utf-8")

    sub = tmp_path /"sub"
    sub.mkdir()
    (sub/"c.md").write_text("third",encoding="utf-8")
    (tmp_path / "notes.txt").write_text("ignore me", encoding='utf=8')
    docs = load_documents(tmp_path)
    assert [d["id"] for d in docs] == ["a.md","b.md","sub/c.md"]
    assert docs[0]["text"]=="first"

def test_chunk_document():
    doc = {"id":"d.md","text":"abcdefghij"}
    chunks = chunk_document(doc,4,1)
    assert[c["text"] for c in chunks]==["abcd","defg","ghij","j"]
    assert[c["chunk_id"]for c in chunks]==["d.md#0","d.md#1","d.md#2","d.md#3"]
def test_chunk_document_bad_overlap():
    doc={"id":"d.md","text":"abcdefghij"}
    with pytest.raises(ValueError):
        chunk_document(doc,4,4)


