import chromadb
from chromadb.config import Settings

def connect_chromadb(CHROMA_HOST, CHROMA_PORT):
    # Connect to ChromaDB
    chroma_client = chromadb.HttpClient(
        host=CHROMA_HOST,
        port=CHROMA_PORT,
        settings=Settings(anonymized_telemetry=False)
    )
    return chroma_client

def delete_collection(CHROMA_HOST, CHROMA_PORT, COLLECTION_NAME):
    # Connect to ChromaDB
    client = connect_chromadb(CHROMA_HOST, CHROMA_PORT)

    # Check if collection exists
    existing_collections = client.list_collections()
    existing_collection_names = [col.name for col in existing_collections]

    if COLLECTION_NAME in existing_collection_names:
        client.delete_collection(name=COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted.")
    else:
        print(f"Collection '{COLLECTION_NAME}' does not exist. Skipping deletion.")
