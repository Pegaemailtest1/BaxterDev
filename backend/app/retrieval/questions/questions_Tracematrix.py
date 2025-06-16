def questions_Tracematrix():
    QUESTION_TEMPLATES = {
        "Questions": [
            {
                "column": "31",
                "row": "13",
                "dictionary_element": "Date",
                "document_id": "BXU542284 Rev F_Verification Trace Matrix Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id for product {product_code}.",
                        "prompt_template": "document_id_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542284 Rev F_Verification Trace Matrix Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the revision  for product {product_code}.",
                        "prompt_template": "revision_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542284 Rev F_Verification Trace Matrix Irrigation Sets\"}}, {\"type\": {\"$eq\": \"footer\"}}]}"
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542284 Rev F_Verification Trace Matrix Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}"
                    }
                ]
            },
            {
                "column": "31",
                "row": "14",
                "dictionary_element": "Date",
                "document_id": "BXU542284 Rev F_Verification Trace Matrix Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id for product {product_code}.",
                        "prompt_template": "document_id_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542284 Rev F_Verification Trace Matrix Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the revision  for product {product_code}.",
                        "prompt_template": "revision_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542284 Rev F_Verification Trace Matrix Irrigation Sets\"}}, {\"type\": {\"$eq\": \"footer\"}}]}"
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542284 Rev F_Verification Trace Matrix Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}"
                    }
                ]
            },
            {
                "column": "31",
                "row": "15",
                "dictionary_element": "Date",
                "document_id": "BXU542284 Rev F_Verification Trace Matrix Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id for product {product_code}.",
                        "prompt_template": "document_id_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542284 Rev F_Verification Trace Matrix Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the revision  for product {product_code}.",
                        "prompt_template": "revision_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542284 Rev F_Verification Trace Matrix Irrigation Sets\"}}, {\"type\": {\"$eq\": \"footer\"}}]}"
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU542284 Rev F_Verification Trace Matrix Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}"
                    }
                ]
            },
            {
                "question": "Extract the intended purpose for product {product_code}",
                "column": "32",
                "row": "13",
                "dictionary_element": "Intended Use",
                "prompt_template": "intended_purpose_Tracematrix",
                "document_id": "BXU542284 Rev F_Verification Trace Matrix Irrigation Sets"
            },
            {
                "question": "Extract the Indication for Use for product {product_code}.",
                "column": "32",
                "row": "14",
                "dictionary_element": "Indication for Use",
                "prompt_template": "indication_for_use_Tracematrix",
                "document_id": "BXU542284 Rev F_Verification Trace Matrix Irrigation Sets"
            },
            {
                "question": "Extract the Contraindications for product {product_code}.",
                "column": "32",
                "row": "15",
                "dictionary_element": "Contraindications",
                "prompt_template": "contraindications_Tracematrix",
                "document_id": "BXU542284 Rev F_Verification Trace Matrix Irrigation Sets"
            },
            #second document
            {
                "column": "33",
                "row": "13",
                "dictionary_element": "Date",
                "document_id": "BXU517502 Rev A_Labeling Trace Matrix_Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id for product {product_code}.",
                        "prompt_template": "document_id_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU517502 Rev A_Labeling Trace Matrix_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the revision  for product {product_code}.",
                        "prompt_template": "revision_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU517502 Rev A_Labeling Trace Matrix_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"footer\"}}]}"
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU517502 Rev A_Labeling Trace Matrix_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}"
                    }
                ]
            },
            {
                "column": "33",
                "row": "14",
                "dictionary_element": "Date",
                "document_id": "BXU517502 Rev A_Labeling Trace Matrix_Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id for product {product_code}.",
                        "prompt_template": "document_id_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU517502 Rev A_Labeling Trace Matrix_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the revision  for product {product_code}.",
                        "prompt_template": "revision_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU517502 Rev A_Labeling Trace Matrix_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"footer\"}}]}"
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU517502 Rev A_Labeling Trace Matrix_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}"
                    }
                ]
            },
            {
                "column": "33",
                "row": "15",
                "dictionary_element": "Date",
                "document_id": "BXU517502 Rev A_Labeling Trace Matrix_Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id for product {product_code}.",
                        "prompt_template": "document_id_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU517502 Rev A_Labeling Trace Matrix_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the revision  for product {product_code}.",
                        "prompt_template": "revision_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU517502 Rev A_Labeling Trace Matrix_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"footer\"}}]}"
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Tracematrix",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU517502 Rev A_Labeling Trace Matrix_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}"
                    }
                ]
            },
            {
                "question": "Extract the intended purpose for product {product_code}",
                "column": "34",
                "row": "13",
                "dictionary_element": "Intended Use",
                "prompt_template": "intended_purpose_Tracematrix",
                "document_id": "BXU517502 Rev A_Labeling Trace Matrix_Irrigation Sets"
            },
            {
                "question": "Extract the Indication for Use for product {product_code}.",
                "column": "34",
                "row": "14",
                "dictionary_element": "Indication for Use",
                "prompt_template": "indication_for_use_Tracematrix",
                "document_id": "BXU517502 Rev A_Labeling Trace Matrix_Irrigation Sets"
            },
            {
                "question": "Extract the Contraindications for product {product_code}.",
                "column": "34",
                "row": "15",
                "dictionary_element": "Contraindications",
                "prompt_template": "contraindications_Tracematrix",
                "document_id": "BXU517502 Rev A_Labeling Trace Matrix_Irrigation Sets"
            }
        ]
    }

    return QUESTION_TEMPLATES

