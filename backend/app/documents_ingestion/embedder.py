import requests
# Use Ollama to generate embeddings ---
def embed_texts(chunks, OLLAMA_URL, model):
    embeddings = []
    for text in chunks:
        res = requests.post(
            f"{OLLAMA_URL}/api/embeddings",
            json={"model": model, "prompt": text}
        )
        res.raise_for_status()
        embeddings.append(res.json()["embedding"])
    return embeddings

# Use Ollama to generate embeddings ---
def embed_section_texts(chunks, OLLAMA_URL, model):
    embeddings = []
    for chunk in chunks:
        text = chunk["content"]
        try:
            res = requests.post(
                f"{OLLAMA_URL}/api/embeddings",
                json={"model": model, "prompt": text}
            )
            res.raise_for_status()
            embeddings.append(res.json()["embedding"])
            
        except requests.RequestException as e:
            print(f"Failed to embed chunk for section: {chunk['section']}. Error: {e}")
    return embeddings
