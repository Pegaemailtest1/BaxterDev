def questions_CER():
    QUESTION_TEMPLATES = {
        "Questions": [
            {
                "column": "9",
                "row": "13",
                "dictionary_element": "Date",
                "document_id": "BXU601670_MDR_CER,A",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_CER",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU601670_MDR_CER,A\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_CER",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU601670_MDR_CER,A\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                
                    },
                    {
                        "question": "Extract the intended purpose for product {product_code}.",
                        "prompt_template": "section_number_CER"
                    }
                ]
            },
            {
                "column": "9",
                "row": "14",
                "dictionary_element": "Date",
                "document_id": "BXU601670_MDR_CER,A",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_CER",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU601670_MDR_CER,A\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_CER",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU601670_MDR_CER,A\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                
                    },
                    {
                        "question": "Extract the Indication for Use for product {product_code}.",
                        "prompt_template": "section_number_CER"
                    }
                ]
            },
            {
                "column": "9",
                "row": "15",
                "dictionary_element": "Date",
                "document_id": "BXU601670_MDR_CER,A",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_CER",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU601670_MDR_CER,A\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_CER",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU601670_MDR_CER,A\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                
                    },
                    {
                        "question": "Extract the Contraindications for product {product_code}.",
                        "prompt_template": "section_number_CER"
                    }
                ]
            },
            {
                "question": "Extract the intended purpose for product {product_code}",
                "column": "10",
                "row": "13",
                "dictionary_element": "Intended Use",
                "prompt_template": "intended_purpose_CER",
                "document_id": "BXU601670_MDR_CER,A"
            },
            {
                "question": "Extract the Indication for Use for product {product_code}.",
                "column": "10",
                "row": "14",
                "dictionary_element": "Indication for Use",
                "prompt_template": "indication_for_use_CER",
                "document_id": "BXU601670_MDR_CER,A"
            },
            {
                "question": "Extract the Contraindications for product {product_code}.",
                "column": "10",
                "row": "15",
                "dictionary_element": "Contraindications",
                "prompt_template": "contraindications_CER",
                "document_id": "BXU601670_MDR_CER,A"
            }
        ]
    }

    return QUESTION_TEMPLATES

