import os
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")
index_path = "pradeep_index.faiss"
text_path = "data/pradeep_info.txt"

def load_text_chunks():
    with open(text_path, "r", encoding="utf-8") as f:
        content = f.read()
    chunks = content.strip().split("\n\n")
    return chunks

def build_index(chunks):
    embeddings = model.encode(chunks)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype('float32'))
    faiss.write_index(index, index_path)
    return index, chunks

def load_rag():
    chunks = load_text_chunks()
    if os.path.exists(index_path):
        index = faiss.read_index(index_path)
    else:
        index, _ = build_index(chunks)
    return index, chunks

def retrieve_context(query, index, chunks, top_k=3):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec).astype('float32'), top_k)
    return "\n".join([chunks[i] for i in I[0]])
