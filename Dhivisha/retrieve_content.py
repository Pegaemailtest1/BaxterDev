from rag_pipeline.retriever.chroma_retriever import connect_chromadb, get_collection, retrieve_documents
from .generate_prompt import select_prompt_template
from .extract_components import extract_components
from config.config_loader import ConfigLoader
import logging
import sys
 
config_loader = ConfigLoader()
 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
 
 
def retrieve_content(config, query_text):
    embedder = config["embedder"]
    llm = config["llm"]
    chroma_host = config["chroma_host"]
    chroma_port = config["chroma_port"]
    collection_name = config["collection"]
    max_results = config.get("max_results", 5)
    where_filter = config.get("where_filter", "")
    full_document_search = config.get("full_document_search", False)
    temperature = config["temperature"]
    max_tokens = config["max_tokens"]
 
    # Step 1: Connect to ChromaDB and get collection
    client = connect_chromadb(chroma_host, chroma_port)
    collection = get_collection(client, collection_name)
 
    # Step 2: Extract structured query components
    extracted = extract_components(query_text)
    question = extracted.get("question")
    field = extracted.get("field")
    target_doc_id = extracted.get("document_id")
    filter_values = extracted.get("section")
    if not isinstance(filter_values, list) and filter_values:
        filter_values = [filter_values]
 
    # Step 3: Embed the query
    question_text = f"{question}." if question else query_text
    embedding = embedder.embed(question_text)
 
    # Step 4: Build dynamic filters
    meta_filter = {}
    if field:
        meta_filter["section"] = {"$contains": field}
    if target_doc_id:
        meta_filter["source"] = {"$contains": target_doc_id}
 
    where_filter = "{\"$and\": [{\"document_id\": {\"$eq\": \"RMC4916_0719004306_IFU_LABEL\"}}, {\"page\": {\"$eq\": 1}}]}"   
   
    #where_filter = "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU535425 Rev D_User Needs\"}}, {\"type\": {\"$eq\": \"section-table\"}}]}"
   
    #where_filter = "{\"document_id\": {\"$eq\": \"BXU601670_MDR_CER,A\"}}"
    full_document_search = "false"
    
    max_results = 100
    # Step 5: Retrieve documents
    results = retrieve_documents(collection, embedding, filter_values, where_filter, max_results, full_document_search)
    documents = results.get("documents", [[]])
    metadatas = results.get("metadatas", [[]])
 
    #logging.info(f"documents retrievedfrom chromadb: {documents}")
    logging.info(f"metadatas retrieved from chromadb: {metadatas}")
    # Step 6: Create prompt from context
    context = "\n\n".join(str(doc).strip() for doc in documents if str(doc).strip())
    #logging.info(f"context retrieved from chromadb: {context}")
    prompt = select_prompt_template(context, question_text)
 
    logging.info(f"Generated prompt: {prompt}")
    # Step 7: Generate response
    #return llm.generate(prompt, context, question_text, temperature, max_tokens)
    return "test"
 