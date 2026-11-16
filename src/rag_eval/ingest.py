from pathlib import Path
def load_documents(docs_dir: Path) ->list[dict[str,str]]:
    documents =[]
    for path in sorted(docs_dir.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        doc_id = path.relative_to(docs_dir).as_posix()
        documents.append({"id":doc_id, "text":text})
    return documents   
def chunk_document(doc:dict[str,str],chunk_size:int, overlap:int)-> list[dict[str,str]]:
    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk_size")
    step = chunk_size - overlap
    text = doc["text"]
    chunks = []

    for start in range(0,len(text),step):
        piece = text[start:start+chunk_size].strip()
        if piece:
            chunks.append(
                {
                    "doc_id":doc["id"],
                    "chunk_id":f"{doc['id']}#{len(chunks)}",
                    "text":piece,

                }
            )
    return chunks
