import logging
import sys
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
from pydantic import BaseModel

from documents_ingestion.load_documents import load_documents
from documents_ingestion.chunker import split_documents, create_chunks_and_metas, split_by_sections, generate_all_chunks
from documents_ingestion.embedder import embed_texts, embed_section_texts
from documents_ingestion.vectorizer import document_vectorize, document_vectorize_by_section
from documents_ingestion.move_files_to_archive import move_files_to_archive
from documents_ingestion.remove_empty_folders import remove_empty_folders
from documents_ingestion.delete_collection import delete_collection
from retrieval.retrieve_content import retrieve_collection_data
from retrieval.generate_output_template import generate_output_template
from retrieval.retrieve_content_prompt import retrieve_collection_data_prompt

from utils import load_constants
config = load_constants()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

# --- Configuration ---
OLLAMA_URL = config["embedding"]["ollama_url"]
EMBED_MODEL = config["embedding"]["embed_model"]

CHROMA_HOST = config["storage"]["chroma_host"]
CHROMA_PORT = config["storage"]["chroma_port"]
COLLECTION_NAME = config["storage"]["collection_name"]
CHUNK_SIZE = config["storage"]["chunk_size"]
CHUNK_OVERLAP = config["storage"]["chunk_overlap"]

FM_MODEL = config["llm"]["fm_model"]
MAX_RESULTS = config["llm"]["max_results"]
TEMPERATURE = config["llm"]["temperature"]
MAX_TOKENS = config["llm"]["max_tokens"]

UPLOAD_FOLDER = config["data"]["upload_folder"]
ARCHIVE_FOLDER = config["data"]["archive_folder"]
INPUT_TEMPLATE_FOLDER = config["data"]["input_template_folder"]
DOWNLOAD_TEMPLATE_FOLDER = config["data"]["download_template_folder"]

# Set LangSmith env variables
langsmith_config = config.get("langsmith", {})
if langsmith_config.get("enable_tracing"):
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = langsmith_config["api_key"]
    os.environ["LANGCHAIN_ENDPOINT"] = langsmith_config["endpoint"]
    os.environ["LANGCHAIN_PROJECT"] = langsmith_config["project"]
    
# --- FastAPI app ---

class Message(BaseModel):
    message: str

class FolderPathRequest(BaseModel):
    folder_path: str

class UserQuery(BaseModel):
    user_query: str

class PromptQuery(BaseModel):
    prompt_query: str
    user_query: str

app = FastAPI()

@app.get("/")
def read_root():  
     
    return {"message": "Welcome to the RAG API"}

# Ollama API or model call
def get_ollama_response(message: str) -> str:
    # Replace with actual Ollama API call or logic
    response = f"Simulated Ollama response to: {message}"
    return response

@app.post("/get_response")
def get_response(message: Message):
    response = get_ollama_response(message.message)
    return {"response": response}


@app.post("/vectorization")
def file_vectorization(request: FolderPathRequest):
    folder_path = request.folder_path
    logging.info(f"folder_path:{folder_path}")
    
    delete_collection(CHROMA_HOST, CHROMA_PORT, COLLECTION_NAME)
    #logging.info(f"Collection deleted successfully")
    
    documents = load_documents(folder_path)    
    #logging.info(f"Documents loaded successfully: {documents}")

    chunks = generate_all_chunks(documents)
    #logging.info(f"Split documents successfully:{chunks}")

    embeddings = embed_section_texts(chunks, OLLAMA_URL, EMBED_MODEL)
    #logging.info(f"embedding successfully")

    vectorize_response = document_vectorize_by_section(CHROMA_HOST, CHROMA_PORT, COLLECTION_NAME, chunks, embeddings)
    logging.info(f"vectorization successfully: {vectorize_response}")

    # move files to destination folder
    move_files_to_archive(UPLOAD_FOLDER, ARCHIVE_FOLDER)

    # Remove empty folder
    remove_empty_folders(UPLOAD_FOLDER)
   
    return vectorize_response

@app.post("/retrieval")
def retrieval_content_from_chromadb(request: UserQuery):
    user_query = request.user_query
    logging.info(f"User query: {user_query}")

    llama_response =retrieve_collection_data(
        CHROMA_HOST,
        CHROMA_PORT,
        COLLECTION_NAME,
        EMBED_MODEL,
        user_query,
        max_results=MAX_RESULTS,
        FM_MODEL=FM_MODEL,
        OLLAMA_URL=OLLAMA_URL,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )

    logging.info(f"llama_response: {llama_response}")

    return {"response": llama_response}


@app.post("/prompt")
def retrieval_content_from_chromadb_prompt(request: PromptQuery):
    prompt_query = request.prompt_query
    user_query = request.user_query
    logging.info(f"Prompt query: {prompt_query}")

    llama_response =retrieve_collection_data_prompt(
        CHROMA_HOST,
        CHROMA_PORT,
        COLLECTION_NAME,
        EMBED_MODEL,
        prompt_query,
        user_query,
        max_results=MAX_RESULTS,
        FM_MODEL=FM_MODEL,
        OLLAMA_URL=OLLAMA_URL,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )

    logging.info(f"llama_response: {llama_response}")

    return {"response": llama_response}

@app.get("/download/{filename}")
def download_file(filename: str):

    logging.info(f"Download started")
    input_file_path = os.path.join(INPUT_TEMPLATE_FOLDER, filename)
    #Generate output template
    os.makedirs(os.path.dirname(DOWNLOAD_TEMPLATE_FOLDER), exist_ok=True)
    file_path = os.path.join(DOWNLOAD_TEMPLATE_FOLDER, filename)
    generate_output_template(input_file_path, file_path, OLLAMA_URL, EMBED_MODEL,CHROMA_HOST,CHROMA_PORT,COLLECTION_NAME,FM_MODEL,MAX_RESULTS,TEMPERATURE, MAX_TOKENS)
    #file_path = os.path.join(INPUT_TEMPLATE_FOLDER, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, filename=filename, media_type='application/octet-stream')
    return {"error": "File not found"}