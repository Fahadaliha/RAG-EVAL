from pathlib import Path
from rag_eval.ingest import load_documents

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