from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document as LangChainDoc
import re
import logging
import sys
# from transformers import AutoTokenizer, AutoModel, pipeline
# import torch
import os


# MODEL_NAME = os.getenv("MODEL_NAME")
# HF_TOKEN = os.getenv("HF_TOKEN")

# tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HF_TOKEN)
# model = AutoModel.from_pretrained(MODEL_NAME)
# lang_detect = pipeline("text-classification", model=model, tokenizer=tokenizer)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)


# Split documents using RecursiveCharacterTextSplitter ---
def split_documents(documents, chunk_size, chunk_overlap):
    # Split documents using RecursiveCharacterTextSplitter ---
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, length_function=len)
    split_docs = splitter.split_documents(documents)
    return split_docs


# Create chunks and metadata ---
def create_chunks_and_metas(split_docs):
    chunks = []
    metas = []
    for doc in split_docs:
        chunks.append(doc.page_content)
        metas.append({"source": doc.metadata["source"]})
    return chunks, metas


def split_by_sections(text, metadata):
    chunks = []
    buffer = []
    current_section = None

    # Match both [Header] and [Header]:
    section_splits = re.split(r'(\[.*?\]:?)', text)

    for i, part in enumerate(section_splits):
        part = part.strip()
        if not part:
            continue

        # Detect headers like [Title] or [Title]:
        if re.match(r'^\[.*?\]:?$', part):
            #logging.debug(f"Matched header part: '{part}'")

            # Flush previous section
            if current_section and buffer:
                #logging.info(f"Appending section: {current_section}")
                chunks.append({
                    "section": current_section,
                    "content": "\n".join(buffer).strip(),
                    "metadata": {
                        **metadata,
                        "section": current_section
                    }
                })
                buffer = []

            # Clean and assign the new section header
            current_section = part.strip().lstrip("[").rstrip("]:").strip()
            #logging.debug(f"Current section set to: '{current_section}'")

        else:
            # Add content to buffer
            buffer.append(part)

    # Final flush
    if current_section and buffer:
        #logging.info(f"Appending final section: {current_section}")
        chunks.append({
            "section": current_section,
            "content": "\n".join(buffer).strip(),
            "metadata": {
                        **metadata,
                        "section": current_section
                    }
        })

    #logging.info(f"Total chunks created: {len(chunks)}")
    return chunks

def generate_all_chunks(documents):
    all_chunks = []
    for doc in documents:
        text = doc.page_content
        logging.debug(f"text: '{text}'")
        # eng_section_text = detect_language(text)
        # logging.debug(f"eng_section_text: '{eng_section_text}'")
        metadata = doc.metadata
        section_chunks  = split_by_sections(text, metadata)  # pass only the string
        all_chunks.extend(section_chunks)
    return all_chunks

# def detect_language(text, max_chars=1000):
#     sample_text = text[:max_chars]
#     try:
#         lang = lang_detect(sample_text)[0]['label']
#         if lang == 'en':
#             return text
#     except Exception as e:
#         logging.error(f"Language detection failed: {e}")
#     return ""
