import chromadb
from chromadb.config import Settings

# CHROMA_HOST = "chromadb"
# CHROMA_PORT = "8000"
# COLLECTION_NAME = "rag_chunks"

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
    # Delete the collection
    client.delete_collection(name=COLLECTION_NAME)

# # List all collections in the database
# collections = client.list_collections()
# print("Available collections:", [col.name for col in collections])