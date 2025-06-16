import re

def extract_components(context, query: str):
    # Match patterns like: "from the ABC (123) document"
    document_match = re.search(r'from the (.*?)\s+\((.*?)\)\s+document', query, re.IGNORECASE)
    
    # Match pattern like: "listed in the BXU601670_MDR_CER,A document"
    fallback_doc_match = re.search(r'listed in the\s+([\w,\-\.]+)\s+document', query, re.IGNORECASE)

    # Match product code if present
    product_match = re.search(r'for product\s+([\w\-]+)', query, re.IGNORECASE)
    
    # Match pattern like: "Extract the XYZ from ..." or "Extract all XYZ listed in ..."
    field_match = re.search(r'Extract(?: all)?\s+(.*?)\s+(?:from|listed in)', query, re.IGNORECASE)

    return {
        "document_type" : document_match.group(1) if document_match else None,
        "document_id" : (
            document_match.group(2) if document_match 
            else fallback_doc_match.group(1) if fallback_doc_match 
            else None
        ),
        "product_code": product_match.group(1) if product_match else None,
        "field": field_match.group(1) if field_match else None,
        "context": context,
        "query": query
    }


def extract_components_bulk(context: str, query: str):
    product_match = re.search(r'for product (\w+)', query)

    # Match "Extract the ... for"
    field_match = re.search(r'Extract the (.*?) for', query, re.IGNORECASE)

    # Capitalize each word to match expected title casing like "Intended Purpose"
    field = field_match.group(1).strip() if field_match else None
    target_section_title = field.title() if field else None

    return {
        "product_code": product_match.group(1) if product_match else None,
        "field": field,
        "target_section_title": target_section_title,
        "context": context,
        "query": query
    }
