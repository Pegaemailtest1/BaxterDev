def questions_DesignValidation():
    QUESTION_TEMPLATES = {
        "Questions": [
            {
                "column": "29",
                "row": "13",
                "dictionary_element": "Date",
                "document_id": "BXU542980 Rev A_Design Validation Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id for product {product_code}.",
                        "prompt_template": "document_id_DesignValidation",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542980 Rev A_Design Validation Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the revision  for product {product_code}.",
                        "prompt_template": "revision_DesignValidation",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542980 Rev A_Design Validation Irrigation Sets\"}}, {\"type\": {\"$eq\": \"footer\"}}]}"
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_DesignValidation",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542980 Rev A_Design Validation Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}"
                    }
                ]
            },
            {
                "column": "29",
                "row": "14",
                "dictionary_element": "Date",
                "document_id": "BXU542980 Rev A_Design Validation Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id for product {product_code}.",
                        "prompt_template": "document_id_DesignValidation",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542980 Rev A_Design Validation Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the revision  for product {product_code}.",
                        "prompt_template": "revision_DesignValidation",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542980 Rev A_Design Validation Irrigation Sets\"}}, {\"type\": {\"$eq\": \"footer\"}}]}"
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_DesignValidation",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542980 Rev A_Design Validation Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}"
                    }
                ]
            },
            {
                "column": "29",
                "row": "15",
                "dictionary_element": "Date",
                "document_id": "BXU542980 Rev A_Design Validation Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id for product {product_code}.",
                        "prompt_template": "document_id_DesignValidation",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542980 Rev A_Design Validation Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the revision  for product {product_code}.",
                        "prompt_template": "revision_DesignValidation",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542980 Rev A_Design Validation Irrigation Sets\"}}, {\"type\": {\"$eq\": \"footer\"}}]}"
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_DesignValidation",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542980 Rev A_Design Validation Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}"
                    }
                ]
            },
            {
                "question": "Extract the intended purpose for product {product_code}",
                "column": "30",
                "row": "13",
                "dictionary_element": "Intended Use",
                "prompt_template": "intended_purpose_DesignValidation",
                "document_id": "BXU542980 Rev A_Design Validation Irrigation Sets"
            },
            {
                "question": "Extract the Indication for Use for product {product_code}.",
                "column": "30",
                "row": "14",
                "dictionary_element": "Indication for Use",
                "prompt_template": "indication_for_use_DesignValidation",
                "document_id": "BXU542980 Rev A_Design Validation Irrigation Sets"
            },
            {
                "question": "Extract the Contraindications for product {product_code}.",
                "column": "30",
                "row": "15",
                "dictionary_element": "Contraindications",
                "prompt_template": "contraindications_DesignValidation",
                "document_id": "BXU542980 Rev A_Design Validation Irrigation Sets"
            }
        ]
    }

    return QUESTION_TEMPLATES

