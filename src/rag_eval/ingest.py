from pathlib import Path
def load_documents(docs_dir: Path) ->list[dict[str,str]]:
    documents =[]
    for path in sorted(docs_dir.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        doc_id = path.relative_to(docs_dir).as_posix()
        documents.append({"id":doc_id, "text":text})
    return documents   

