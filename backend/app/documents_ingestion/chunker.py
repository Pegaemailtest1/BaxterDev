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
    
    # Robust regex to match all section types
    section_pattern = re.compile(
        r'(?P<header>'
        r'^\d+(?:\.\d+)*\s+[^\n]+|'                            # e.g., 5, 5.1, 2.3.4 Title
        r'^\[[^\]]+\]:?|'
        r'^[A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,4}$|'              # Title Case: "Directions for Use"
        r'^[A-Z ]{3,}$|'                                      # ALL CAPS: "WARNINGS"
        r'^[A-Z][a-zA-Z\s]{2,50}:\s*'                         # Mixed-case ending in colon: "Intended Users:"
        r')',
        re.MULTILINE
    )


    matches = list(section_pattern.finditer(text))

    # 🔁 If no section headers are matched, return entire content as one chunk
    if not matches:
        if text.strip():
            chunks.append({
                "section": metadata.get("section", "unknown"),
                "content": text.strip(),
                "metadata": metadata
            })
        return chunks

    for i, match in enumerate(matches):
        start = match.start()
        end = match.end()
        header = match.group("header").strip()
        next_start = matches[i + 1].start() if i + 1 < len(matches) else len(text)

        content = text[end:next_start].strip()

        # Normalize header
        if header.startswith("[") and header.endswith("]") or header.endswith("]:"):
            header = header.strip("[]:").strip()

        if content:
            chunks.append({
                "section": header,
                "content": content,
                "metadata": {
                    **metadata,
                    "section": header
                }
            })

    return chunks


def generate_all_chunks(documents):
    all_chunks = []
    for doc in documents:
        text = doc.page_content
        metadata = doc.metadata
        section = metadata.get("section", "").strip()
        # If the document already has a section (like from header-date/image OCR), preserve it
        if section:
            all_chunks.append({
                "section": section,
                "content": text,
                "metadata": metadata
            })
        else:
            # Default: try to split by sections
            section_chunks = split_by_sections(text, metadata)
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
