import chromadb
from chromadb.config import Settings
import uuid

def connect_chromadb(CHROMA_HOST, CHROMA_PORT):
    # Connect to ChromaDB
    chroma_client = chromadb.HttpClient(
        host=CHROMA_HOST,
        port=CHROMA_PORT,
        settings=Settings(anonymized_telemetry=False)
    )
    return chroma_client

def create_collection(chroma_client, collection_name):
    # Create a collection in ChromaDB
    collection = chroma_client.get_or_create_collection(name=collection_name)
    return collection

def store_documents_in_chromadb(collection, chunks, embeddings, metas):
    # Store chunks in ChromaDB
    #upsert operation, which updates existing items, or adds them if they don't yet exist.
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        metadatas=metas,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )


def store_section_chunks_in_db(collection, chunks, embeddings):
    ids = [str(uuid.uuid4()) for _ in chunks]
    documents = [chunk["content"] for chunk in chunks]
    metadatas = [chunk["metadata"] for chunk in chunks]

    # Make sure lengths match
    assert len(ids) == len(documents) == len(metadatas) == len(embeddings)

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings
    )
 
def document_vectorize_by_section(CHROMA_HOST, CHROMA_PORT, COLLECTION_NAME, chunks,embeddings, batch_size=100):
    client = connect_chromadb(CHROMA_HOST, CHROMA_PORT)
    collection = create_collection(client, COLLECTION_NAME)
    total = len(chunks)
    for i in range(0, total, batch_size):
        batch_chunks = chunks[i:i+batch_size]
        batch_embeddings = embeddings[i:i+batch_size]
        store_section_chunks_in_db(collection, batch_chunks,batch_embeddings)
    
    return {
        "status": "success",
        "message": "Vectorized successfully."
    }


def document_vectorize(CHROMA_HOST, CHROMA_PORT, COLLECTION_NAME, chunks, embeddings, metas, batch_size=100):
    client = connect_chromadb(CHROMA_HOST, CHROMA_PORT)
    collection = create_collection(client, COLLECTION_NAME)
    total = len(chunks)
    for i in range(0, total, batch_size):
        batch_chunks = chunks[i:i+batch_size]
        batch_embeddings = embeddings[i:i+batch_size]
        batch_metas = metas[i:i+batch_size]
        store_documents_in_chromadb(collection, batch_chunks, batch_embeddings, batch_metas)
    
    return {
        "status": "success",
        "message": "Vectorized successfully."
    }