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
    valid_chunks = []

    for chunk in chunks:
        text = chunk["content"]
        if not text.strip():
            continue  # skip completely empty content

        try:
            res = requests.post(
                f"{OLLAMA_URL}/api/embeddings",
                json={"model": model, "prompt": text}
            )
            res.raise_for_status()
            embedding = res.json().get("embedding")

            # ✅ Check if embedding is a non-empty list of floats
            if embedding and isinstance(embedding, list) and all(isinstance(x, float) for x in embedding):
                embeddings.append(embedding)
                valid_chunks.append(chunk)
            else:
                print(f"Invalid embedding for section: {chunk['section']}")

        except requests.RequestException as e:
            print(f"Failed to embed chunk for section: {chunk['section']}. Error: {e}")

    return embeddings, valid_chunks

