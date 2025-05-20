import logging
import sys

import os
import logging
from docx import Document
from langchain_community.document_loaders import PyPDFLoader
import pdfplumber
import fitz  # PyMuPDF
import base64
from langchain.schema import Document as LangChainDoc
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter, defaultdict

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

def is_multi_column_paragraph_page(page, min_word_threshold=30, min_cluster_distance=100, balance_threshold=0.25):
    words = page.extract_words()
    if len(words) < min_word_threshold:
        return False

    # Skip if text is mostly part of tables
    tables = page.extract_tables()
    table_word_count = sum(len(cell.split()) for table in tables for row in table for cell in row if cell)
    total_word_count = sum(len(w["text"].split()) for w in words)

    if table_word_count / (total_word_count + 1e-6) > 0.5:
        return False  # Table-heavy page, skip column logic

    # Proceed with x0 clustering
    x_positions = np.array([[word['x0']] for word in words])
    kmeans = KMeans(n_clusters=2, n_init=10, random_state=42)
    labels = kmeans.fit_predict(x_positions)
    cluster_sizes = Counter(labels)
    centers = sorted([center[0] for center in kmeans.cluster_centers_])

    balance = min(cluster_sizes.values()) / sum(cluster_sizes.values())
    center_distance = abs(centers[1] - centers[0])

    return balance > balance_threshold and center_distance > min_cluster_distance

def extract_pdf_text_tables_images(pdf_path):
    extracted_content = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            if "IFU_LABEL" in pdf_path and is_multi_column_paragraph_page(page):
                # Attempt 3-column split
                width = page.width
                height = page.height
                column_width = width / 3

                column_texts = []
                for i in range(3):
                    left = i * column_width
                    right = (i + 1) * column_width
                    column = page.within_bbox((left, 0, right, height))
                    col_text = column.extract_text() or ""
                    column_texts.append(col_text.strip())

                combined_text = "\n\n".join(f"[Column {i+1}]\n{txt}" for i, txt in enumerate(column_texts) if txt.strip())
            else:
                # Normal single-column extraction
                combined_text = page.extract_text() or ""

            # ----- Title/Section Chunking -----
            section_chunks = defaultdict(list)
            current_section = "Introduction"

            lines = combined_text.split('\n')
            for line in lines:
                # Simple heuristic for detecting titles/headers
                if len(line.strip()) < 80 and line.strip().istitle():
                    current_section = line.strip()
                    continue
                section_chunks[current_section].append(line.strip())

            for section_title, content_lines in section_chunks.items():
                if not content_lines:
                    continue
                section_text = f"[{section_title}]\n" + "\n".join(content_lines).strip()
                if section_text:
                    extracted_content.append({
                        "type": "section",
                        "section": section_title,
                        "page": page_num + 1,
                        "content": section_text
                    })


            # Extract tables from whole page
            tables = page.extract_tables()
            table_texts = []
            for table in tables:
                # Clean and flatten each table row
                cleaned_rows = []
                for row in table:
                    cleaned_row = [
                        (cell or "").replace("\n", " ").strip()  # flatten multi-line cells
                        for cell in row
                    ]
                    cleaned_rows.append(" | ".join(cleaned_row))  # join cells with pipe

                table_str = "\n".join(cleaned_rows)
                table_texts.append(table_str)

            if table_texts:
                combined_text += "\n\n[Tables]\n" + "\n\n".join(table_texts)

            if combined_text.strip():
                extracted_content.append({
                    "type": "text+table",
                    "page": page_num + 1,
                    "content": combined_text.strip()
                })

    # --- Extract images using PyMuPDF ---
    pdf_doc = fitz.open(pdf_path)
    for page_index in range(len(pdf_doc)):
        page = pdf_doc[page_index]
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = pdf_doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            b64_image = base64.b64encode(image_bytes).decode('utf-8')

            extracted_content.append({
                "type": "image",
                "page": page_index + 1,
                "format": image_ext,
                "content": f"[Image {img_index+1} on Page {page_index+1}]\n(base64): {b64_image[:100]}... (truncated)"
            })

    return extracted_content




def extract_docx_text_tables_images(docx_path):
    
    extracted_content = []    
    doc = Document(docx_path)

    # --- Extract text from paragraphs ---
    extracted_content = "\n".join([p.text for p in doc.paragraphs])

    # --- Extract tables ---
    rows_text = []
    for table_index, table in enumerate(doc.tables):
        for row in table.rows:
            row_text = " | ".join(cell.text.strip() for cell in row.cells)
            if row_text:
                rows_text.append(f"Table {table_index + 1}: {row_text}")

    # --- Extract embedded images ---
    image_data = []
    rels = doc.part._rels
    for rel in rels.values():
        if "image" in rel.target_ref:
            image_bytes = rel.target_part.blob
            image_ext = rel.target_part.content_type.split("/")[-1]  # e.g., 'jpeg', 'png'
            b64_image = base64.b64encode(image_bytes).decode('utf-8')
            image_data.append(f"[Word Image ({image_ext}) base64]: {b64_image[:100]}...")  # truncated preview

    # --- Combine extracted content ---
    if rows_text:
        extracted_content += "\n\n[TABLES]\n" + "\n".join(rows_text)
    if image_data:
        extracted_content += "\n\n[IMAGES]\n" + "\n".join(image_data)

    return extracted_content


def load_documents(folder_path):
    all_docs = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.startswith("~$"):
                continue

            full_path = os.path.join(root, file)
            full_text = ""
            logging.info(f"Processing file: {full_path}")

            # --- PDF files ---
            if file.lower().endswith(".pdf"):
                try:
                    # Extract text, tables and iamges from PDF
                    full_text = extract_pdf_text_tables_images(full_path)
                    #logging.info(f"Extracted content from PDF: {full_text}")
                    for entry in full_text:
                        all_docs.append(LangChainDoc(
                            page_content=entry["content"],
                            metadata={"source": full_path, "type": entry["type"], "page": entry["page"]}
                        ))
                    #logging.info(f"Extracted content from all PDF docs : {all_docs}")
                except Exception as e:
                    logging.error(f"Failed PDF: {full_path} - {e}")
                    continue

            # --- Word files ---
            elif file.lower().endswith((".doc", ".docx")):
                try:
                    # Extract text, tables and iamges from docx
                    full_text = extract_docx_text_tables_images(full_path)
                    #logging.info(f"Extracted content from Word: {full_text}")

                    all_docs.append(LangChainDoc(
                        page_content=full_text,
                        metadata={"source": full_path, "type": "docx"}
                    ))
                    #logging.info(f"Extracted content from all Word docs: {all_docs}")
                except Exception as e:
                    logging.error(f"Failed Word: {full_path} - {e}")
                    continue

            else:
                continue  # Skip unsupported files

    return all_docs


