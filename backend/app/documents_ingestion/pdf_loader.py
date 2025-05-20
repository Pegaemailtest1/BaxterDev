import logging
import sys

import logging
import pdfplumber
import fitz  # PyMuPDF
import base64

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

def extract_pdf_text_tables_images(pdf_path):
    extracted_content = []
    
    # --- Extract text and tables using pdfplumber ---
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            page_text = page.extract_text() or ""
            tables = page.extract_tables()

            table_texts = []
            for table in tables:
                table_str = "\n".join([" | ".join(cell or "" for cell in row) for row in table])
                table_texts.append(table_str)

            combined_text = page_text.strip()
            if table_texts:
                combined_text += "\n\n[Tables]\n" + "\n\n".join(table_texts)

            if combined_text:
                extracted_content.append({
                    "type": "text+table",
                    "page": page_num + 1,
                    "content": combined_text
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