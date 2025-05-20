import chromadb
import requests
from chromadb.config import Settings
import logging
import sys
import json
from .generate_prompt import test_prompt_template
from .extract_components import extract_components

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

def connect_chromadb(CHROMA_HOST, CHROMA_PORT):
    # Connect to ChromaDB
    chroma_client = chromadb.HttpClient(
        host=CHROMA_HOST,
        port=CHROMA_PORT,
        settings=Settings(anonymized_telemetry=False)
    )
    return chroma_client

def get_chromadb_collection(chroma_client, collection_name):
    # Retrieve an existing collection
    collection = chroma_client.get_collection(name=collection_name)
    return collection

# Function to get embeddings from Ollama (mxbai)
def embed_with_ollama(query, OLLAMA_URL, EMBED_MODEL):
    response = requests.post(
        f"{OLLAMA_URL}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": query}
    )
    response.raise_for_status()
    return response.json()["embedding"]

# Function to get LLM answer from Ollama (llama3)
def ask_llama3(prompt, OLLAMA_URL, FM_MODEL,temperature, max_tokens):
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={"model": FM_MODEL, "prompt": prompt, "temperature": temperature, "num_predict": max_tokens}
    )
    response.raise_for_status()
    
    full_response = ""
    for line in response.iter_lines(decode_unicode=True):
        if line:
            data = json.loads(line)
            full_response += data.get("response", "")
    
    return full_response

def retrieve_collection_data_prompt(CHROMA_HOST, CHROMA_PORT, COLLECTION_NAME, EMBED_MODEL, prompt_query, query_text, max_results, FM_MODEL, OLLAMA_URL,temperature, max_tokens):
    # Step 1: Connect to ChromaDB and get collection
    client = connect_chromadb(CHROMA_HOST, CHROMA_PORT)
    collection = get_chromadb_collection(client, COLLECTION_NAME)

    #logging.info(f"Connected to ChromaDB and retrieved collection: {COLLECTION_NAME}")

    # Step 2: Embed the query with mxbai
    query_embedding = embed_with_ollama(query_text, OLLAMA_URL, EMBED_MODEL)

    
    #logging.info(f"Query embedding generated successfully: {query_embedding}")
    
    # Step 3: Query ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=max_results,
        include=["documents", "metadatas","data","distances"]
    )
    
    #logging.info(f"Query results: {results}")

    # Step 4: Retrieve documents and metadata
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    #logging.info(f"Documents: {documents}")
    #logging.info(f"Metadatas: {metadatas}")

    # Step 5: Define filters from extracted_components
    extracted_components = extract_components(query_text)
    target_product = extracted_components.get("product_code")
    #logging.info(f"Target product: {target_product}")
    target_doc_type = extracted_components.get("document_type")
    #logging.info(f"Target document type: {target_doc_type}")


    # Step 6: Filter based on metadata match
    if target_product is not None and target_doc_type is not None:
        filtered_chunks = [
            doc for doc, meta in zip(documents, metadatas)
            if target_product in (meta.get("source", "") or "") and target_doc_type in (meta.get("source", "") or "")
        ]
    else:
        filtered_chunks = documents

    # Step 7: Combine into final context
    context = "\n\n".join(filtered_chunks)

    #logging.info(f"Filtered Query results: {filtered_chunks}")
    #logging.info(f"context: {context}")
    prompt = test_prompt_template(context, prompt_query)
    logging.info(f"Prompt generated successfully: {prompt}")

    # Step 4: Get answer from llama3
    llama_response = ask_llama3(prompt, OLLAMA_URL, FM_MODEL,temperature, max_tokens)
    
    logging.info(f"Llama response generated successfully: {llama_response}")

    return llama_response
