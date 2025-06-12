import cohere
import os
import numpy as np

co = cohere.Client(os.getenv("COHERE_API_KEY"))
text_path = "data/pradeep_info.txt"

def load_text_chunks():
    with open(text_path, "r", encoding="utf-8") as f:
        content = f.read()
    chunks = content.strip().split("\n\n")
    return chunks
    
def get_chunk_embeddings(chunks):
    response = co.embed(texts=chunks, model="embed-english-v3.0")
    return np.array(response.embeddings)

# Load once
CHUNKS = load_text_chunks()
CHUNK_EMBEDDINGS = get_chunk_embeddings(CHUNKS)]

def retrieve_context(query, top_k=3):
    query_vec = co.embed(texts=[query], model="embed-english-v3.0").embeddings[0]
    scores = np.dot(CHUNK_EMBEDDINGS, query_vec)
    top_indices = np.argsort(scores)[-top_k:][::-1]
    return "\n".join([CHUNKS[i] for i in top_indices])
