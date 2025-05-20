import re

def extract_components(query: str):
    document_match = re.search(r'from the (.*?) \((\d+)\) document', query)
    product_match = re.search(r'for product (.*?) under', query)
    field_match = re.search(r'Extract the (.*?) from', query)
    section_match = re.search(r'under (.*?) section', query)
    question_match = re.search(r'^(.*?) under', query, re.IGNORECASE)
    #section_match = re.search(r'under (\w+)', query)

    return {
        "document_type" : document_match.group(1) if document_match else None,
        "document_id" : document_match.group(2) if document_match else None,
        "product_code": product_match.group(1) if product_match else None,
        "field": field_match.group(1) if field_match else None,
        "section": section_match.group(1) if section_match else None,
        "question": question_match.group(1) if question_match else None
    }

