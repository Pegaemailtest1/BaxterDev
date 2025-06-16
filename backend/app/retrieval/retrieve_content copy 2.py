import chromadb
import requests
from chromadb.config import Settings
import logging
import sys
import json
from .generate_prompt import select_prompt_template
from .extract_components import extract_components

import base64
import re
from PIL import Image, ImageDraw
from io import BytesIO
import pytesseract

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

client = Client()
try:
    projects = list(client.list_projects())
    logging.info(f"LangSmith client connected. First project: {projects[0].name if projects else 'No projects found'}")
except Exception as e:
    logging.error(f"LangSmith client connection failed: {e}")

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

def extract_text_from_base64_image(base64_data):
    try:
        image_bytes = base64.b64decode(base64_data)
        image = Image.open(BytesIO(image_bytes)).convert("L")
        image = image.resize((image.width * 2, image.height * 2))
        return pytesseract.image_to_string(image).strip()
    except Exception as e:
        logging.error(f"Failed to OCR image: {e}")
        return ""

def extract_image_base64(document_text):
    match = re.search(r'\(base64\):\s*([A-Za-z0-9+/=]+)', document_text)
    return match.group(1) if match else None

def extract_issued_effective_dates(text):
    issued = re.search(r"Issued Date[:\-]?\s*(\d{2}/\d{2}/\d{4})", text, re.IGNORECASE)
    effective = re.search(r"Effective Date[:\-]?\s*(\d{2}/\d{2}/\d{4})", text, re.IGNORECASE)
    return {
        "issued_date": issued.group(1) if issued else None,
        "effective_date": effective.group(1) if effective else None
    }

def ocr_from_vector_path(vector_path, width=600, height=200, scale=1):
    img = Image.new("L", (width, height), color=255)
    draw = ImageDraw.Draw(img)
    pattern = re.compile(r"M(\d+),(\d+)h1v1h-1z")
    for match in pattern.finditer(vector_path):
        x, y = int(match.group(1)) * scale, int(match.group(2)) * scale
        draw.rectangle([x, y, x + scale - 1, y + scale - 1], fill=0)
    return pytesseract.image_to_string(img).strip()

def retrieve_collection_data(CHROMA_HOST, CHROMA_PORT, COLLECTION_NAME, EMBED_MODEL, query_text, max_results, FM_MODEL, OLLAMA_URL, temperature, max_tokens):
    client = connect_chromadb(CHROMA_HOST, CHROMA_PORT)
    collection = get_chromadb_collection(client, COLLECTION_NAME)

    extracted_components = extract_components(query_text)
    collection_filter = extracted_components.get("section")
    question = extracted_components.get("question")
    field = extracted_components.get("field")
    #logging.info(f"field: {field}")
    question_text = question + "." if question else query_text

    query_embedding = embed_with_ollama(question_text, OLLAMA_URL, EMBED_MODEL)

    filter_values = collection_filter if isinstance(collection_filter, list) else [collection_filter] if collection_filter else None
    target_doc_id = extracted_components.get("document_id")
    logging.info(f"Target document id: {target_doc_id}")

    # Filter by section if provided
    meta_filter = {}
    if field:
        meta_filter["section"] = {"$contains": field}
    if target_doc_id:
        meta_filter["source"] = {"$contains": target_doc_id}

    # Perform query
    if meta_filter:
        results = collection.query(
            query_texts=[question_text],
            n_results=max_results,
            where_document=meta_filter,
            include=["documents", "metadatas"]
        )
    else:
        results = collection.query(
            query_texts=[question_text],
            n_results=max_results,
            include=["documents", "metadatas"]
        )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]


    logging.info(f"documents:{documents}")
    logging.info(f"metadatas:{metadatas}")
    

    # Step 6: Filter based on metadata match
    filtered_chunks = []
    if target_doc_id:
        for doc, meta in zip(documents, metadatas):
            source = meta.get("source", "")
            filename = os.path.basename(source)
            if target_doc_id in filename:
                #logging.info(f"Matched document: {filename}")
                filtered_chunks.append(doc)
                logging.info(f"Filtered docs: {doc}")
    else:
        filtered_chunks = documents

    logging.info(f"Filtered chunks: {filtered_chunks}")
    # Step 7: Combine into final context
    context = "\n\n".join(
        str(chunk).strip() for chunk in filtered_chunks if str(chunk).strip()
    )

    #logging.info(f"Filtered Query results: {filtered_chunks}")
    logging.info(f"context: {context}")

    prompt = select_prompt_template(context, query_text)
    llama_response = ask_llama3(prompt, OLLAMA_URL, FM_MODEL, temperature, max_tokens)

    return llama_response
