import chromadb
import requests
from chromadb.config import Settings
import logging
import sys
import json
from .generate_prompt import bulk_prompt_template
from .extract_components import extract_components

from utils import load_constants
import os
from langsmith import Client

config = load_constants()

OpenAI_FM_MODEL = config["openai"]["api_key"]
OpenAI_Model = config["openai"]["model"]
OpenAI_base_url = config["openai"]["base_url"]

# Set LangSmith env variables
langsmith_config = config.get("langsmith", {})
if langsmith_config.get("enable_tracing"):
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = langsmith_config["api_key"]
    os.environ["LANGCHAIN_ENDPOINT"] = langsmith_config["endpoint"]
    os.environ["LANGCHAIN_PROJECT"] = langsmith_config["project"]

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

# client = Client()
# try:
#     projects = list(client.list_projects())
#     logging.info(f"LangSmith client connected. First project: {projects[0].name if projects else 'No projects found'}")
# except Exception as e:
#     logging.error(f"LangSmith client connection failed: {e}")

def connect_chromadb(CHROMA_HOST, CHROMA_PORT):
    chroma_client = chromadb.HttpClient(
        host=CHROMA_HOST,
        port=CHROMA_PORT,
        settings=Settings(anonymized_telemetry=False)
    )
    return chroma_client

def get_chromadb_collection(chroma_client, collection_name):
    return chroma_client.get_collection(name=collection_name)

def embed_with_ollama(query, OLLAMA_URL, EMBED_MODEL):
    response = requests.post(
        f"{OLLAMA_URL}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": query}
    )
    response.raise_for_status()
    return response.json()["embedding"]

def ask_llama3(prompt, OLLAMA_URL, FM_MODEL, temperature, max_tokens):
    if '"response": ["No Trace"]' in prompt or '"response": "No Trace"' in prompt:
        return '{"response": ["No Trace"]}'

    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={"model": FM_MODEL, "prompt": prompt, "temperature": temperature, "num_predict": max_tokens}
    )
    if response.status_code == 404:
        raise Exception(f"Endpoint not found at {OLLAMA_URL}/api/generate")

    response.raise_for_status()
    full_response = ""
    for line in response.iter_lines(decode_unicode=True):
        if line:
            data = json.loads(line)
            full_response += data.get("response", "")

    return full_response

def retrieve_collection_data_template(CHROMA_HOST, CHROMA_PORT, COLLECTION_NAME, EMBED_MODEL, query_text, document_id, prompt_template, full_document_search, where_filter, max_results, FM_MODEL, OLLAMA_URL, temperature, max_tokens):
    client = connect_chromadb(CHROMA_HOST, CHROMA_PORT)
    collection = get_chromadb_collection(client, COLLECTION_NAME)

    extracted_components = extract_components(query_text)
    collection_filter = extracted_components.get("section")
    question = extracted_components.get("question")
    question_text = question + "." if question else query_text

    query_embedding = embed_with_ollama(question_text, OLLAMA_URL, EMBED_MODEL)

    filter_values = collection_filter if isinstance(collection_filter, list) else [collection_filter] if collection_filter else None

    if full_document_search:
        if where_filter:
            where_filter = json.loads(where_filter)
            results = collection.get(
                include=["documents", "metadatas"],
                where=where_filter
            )
        else:
            results = collection.get(
            include=["documents", "metadatas"]
    )
    elif filter_values:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=max_results,
            include=["documents", "metadatas"],
            where={"section": {"$in": filter_values}}
        )
    else:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=max_results,
            include=["documents", "metadatas"]
        )

    documents = results.get("documents", [[]])
    metadatas = results.get("metadatas", [[]])
    logging.info(f"documents:{documents}")
    logging.info(f"metadatas:{metadatas}")
    #target_doc_id = extracted_components.get("document_id")

    context = "\n\n".join(
        str(chunk).strip() for chunk in documents if str(chunk).strip()
    )
    prompt = bulk_prompt_template(context, query_text, prompt_template)
    llama_response = ask_llama3(prompt, OLLAMA_URL, FM_MODEL, temperature, max_tokens)
    logging.info(f"LLama response: {llama_response}")

    return llama_response
