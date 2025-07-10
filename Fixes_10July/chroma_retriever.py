import chromadb
import json
from chromadb.config import Settings
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)


def connect_chromadb(host, port):
    return chromadb.HttpClient(
        host=host,
        port=port,
        settings=Settings(anonymized_telemetry=False)
    )

def get_collection(client, name):
    return client.get_collection(name=name)

def retrieve_documents(collection, embedding, filter_values, where_filter, where_document, max_results, full_document_search):
    results = None
    where = ""
    logging.info(f"full_document_search:{full_document_search}")
    logging.info(f"where document condition: {where_document}")
    if where_document !="":
        where_document = json.loads(where_document)

    if where_filter !="":
        try:
            where = json.loads(where_filter) if where_filter else ""
        except json.JSONDecodeError as e:
            print(f"[ChromaDB] Invalid where_filter JSON: {e}")
            where = ""


    if full_document_search=="Yes":
        logging.info("inside full document search full_document_search")
        # If full document search is enabled, we do not use embeddings
        if where!="" and where_document!="":
            results = collection.get(include=["documents", "metadatas"], where=where, where_document=where_document)
        elif where!="":
            results = collection.get(include=["documents", "metadatas"], where=where)
        elif where_document!="":
            results = collection.get(include=["documents", "metadatas"], where_document=where_document)
        else:
            results = collection.get(include=["documents", "metadatas"])
    else:
        logging.info("inside full document search else full_document_search")
        # Embedding-based similarity search
        if where!="" and  where_document!="":
            results = collection.query(
                query_embeddings=[embedding],
                n_results=max_results,
                include=["documents", "metadatas"],
                where=where,
                #where_document={"$contains": "packaging"}
                where_document= where_document
            )
        elif where!="":
            results = collection.query(
                query_embeddings=[embedding],
                n_results=max_results,
                include=["documents", "metadatas"],
                where=where,
            )
        elif where_document!="":
            results = collection.query(
                query_embeddings=[embedding],
                n_results=max_results,
                include=["documents", "metadatas"],
                where_document=where_document,
            )
        elif filter_values:
            results = collection.query(
                query_embeddings=[embedding],
                n_results=max_results,
                include=["documents", "metadatas"],
                where={"section": {"$in": filter_values}}
            )
        else:
            results = collection.query(
                query_embeddings=[embedding],
                n_results=max_results,
                include=["documents", "metadatas"]
            )

    return results
