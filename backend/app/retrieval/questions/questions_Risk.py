def questions_Risk():
    QUESTION_TEMPLATES = {
        "Questions": [
            {
                "column": "17",
                "row": "13",
                "dictionary_element": "Date",
                "document_id": "1266804_Rev B_RMP Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1266804_Rev B_RMP Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1266804_Rev B_RMP Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the intended purpose section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "column": "17",
                "row": "14",
                "dictionary_element": "Date",
                "document_id": "1266804_Rev B_RMP Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1266804_Rev B_RMP Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1266804_Rev B_RMP Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the Indication for Use section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "column": "17",
                "row": "15",
                "dictionary_element": "Date",
                "document_id": "1266804_Rev B_RMP Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1266804_Rev B_RMP Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1266804_Rev B_RMP Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the Contraindications section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "question": "Extract the intended purpose for product {product_code}",
                "column": "18",
                "row": "13",
                "dictionary_element": "Intended Use",
                "prompt_template": "intended_purpose_Risk",
                "document_id": "1266804_Rev B_RMP Irrigation Sets"
            },
            {
                "question": "Extract the Indication for Use for product {product_code}.",
                "column": "18",
                "row": "14",
                "dictionary_element": "Indication for Use",
                "prompt_template": "indication_for_use_Risk",
                "document_id": "1266804_Rev B_RMP Irrigation Sets"
            },
            {
                "question": "Extract the Contraindications for product {product_code}.",
                "column": "18",
                "row": "15",
                "dictionary_element": "Contraindications",
                "prompt_template": "contraindications_Risk",
                "document_id": "1266804_Rev B_RMP Irrigation Sets"
            },
            #second document set
            {
                "column": "19",
                "row": "13",
                "dictionary_element": "Date",
                "document_id": "1239908 Rev J_DFMEA_Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1239908 Rev J_DFMEA_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1239908 Rev J_DFMEA_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the intended purpose section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "column": "19",
                "row": "14",
                "dictionary_element": "Date",
                "document_id": "1239908 Rev J_DFMEA_Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1239908 Rev J_DFMEA_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1239908 Rev J_DFMEA_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the Indication for Use section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "column": "19",
                "row": "15",
                "dictionary_element": "Date",
                "document_id": "1239908 Rev J_DFMEA_Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1239908 Rev J_DFMEA_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1239908 Rev J_DFMEA_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the Contraindications section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "question": "Extract the intended purpose for product {product_code}",
                "column": "20",
                "row": "13",
                "dictionary_element": "Intended Use",
                "prompt_template": "intended_purpose_Risk",
                "document_id": "1239908 Rev J_DFMEA_Irrigation Sets"
            },
            {
                "question": "Extract the Indication for Use for product {product_code}.",
                "column": "20",
                "row": "14",
                "dictionary_element": "Indication for Use",
                "prompt_template": "indication_for_use_Risk",
                "document_id": "1239908 Rev J_DFMEA_Irrigation Sets"
            },
            {
                "question": "Extract the Contraindications for product {product_code}.",
                "column": "20",
                "row": "15",
                "dictionary_element": "Contraindications",
                "prompt_template": "contraindications_Risk",
                "document_id": "1239908 Rev J_DFMEA_Irrigation Sets"
            },
            #third document set
            {
                "column": "21",
                "row": "13",
                "dictionary_element": "Date",
                "document_id": "1277545 Rev F_HAZOP_Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277545 Rev F_HAZOP_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277545 Rev F_HAZOP_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the intended purpose section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "column": "21",
                "row": "14",
                "dictionary_element": "Date",
                "document_id": "1277545 Rev F_HAZOP_Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277545 Rev F_HAZOP_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277545 Rev F_HAZOP_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the Indication for Use section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "column": "21",
                "row": "15",
                "dictionary_element": "Date",
                "document_id": "1277545 Rev F_HAZOP_Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277545 Rev F_HAZOP_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277545 Rev F_HAZOP_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the Contraindications section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "question": "Extract the intended purpose for product {product_code}",
                "column": "22",
                "row": "13",
                "dictionary_element": "Intended Use",
                "prompt_template": "intended_purpose_Risk",
                "document_id": "1277545 Rev F_HAZOP_Irrigation Sets"
            },
            {
                "question": "Extract the Indication for Use for product {product_code}.",
                "column": "22",
                "row": "14",
                "dictionary_element": "Indication for Use",
                "prompt_template": "indication_for_use_Risk",
                "document_id": "1277545 Rev F_HAZOP_Irrigation Sets"
            },
            {
                "question": "Extract the Contraindications for product {product_code}.",
                "column": "22",
                "row": "15",
                "dictionary_element": "Contraindications",
                "prompt_template": "contraindications_Risk",
                "document_id": "1277545 Rev F_HAZOP_Irrigation Sets"
            },
            #fourth set of questions
            {
                "column": "23",
                "row": "13",
                "dictionary_element": "Date",
                "document_id": "1266804_Rev B_RMP Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1266804_Rev B_RMP Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1266804_Rev B_RMP Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the intended purpose section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "column": "23",
                "row": "14",
                "dictionary_element": "Date",
                "document_id": "1266804_Rev B_RMP Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1266804_Rev B_RMP Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1266804_Rev B_RMP Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the Indication for Use section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "column": "23",
                "row": "15",
                "dictionary_element": "Date",
                "document_id": "1266804_Rev B_RMP Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1266804_Rev B_RMP Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1266804_Rev B_RMP Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the Contraindications section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "question": "Extract the intended purpose for product {product_code}",
                "column": "24",
                "row": "13",
                "dictionary_element": "Intended Use",
                "prompt_template": "intended_purpose_Risk",
                "document_id": "1266804_Rev B_RMP Irrigation Sets"
            },
            {
                "question": "Extract the Indication for Use for product {product_code}.",
                "column": "24",
                "row": "14",
                "dictionary_element": "Indication for Use",
                "prompt_template": "indication_for_use_Risk",
                "document_id": "1266804_Rev B_RMP Irrigation Sets"
            },
            {
                "question": "Extract the Contraindications for product {product_code}.",
                "column": "24",
                "row": "15",
                "dictionary_element": "Contraindications",
                "prompt_template": "contraindications_Risk",
                "document_id": "1266804_Rev B_RMP Irrigation Sets"
            },
            #fifth set of questions
            {
                "column": "25",
                "row": "13",
                "dictionary_element": "Date",
                "document_id": "1277308 Rev C RBA_Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277308 Rev C RBA_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277308 Rev C RBA_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the intended purpose section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "column": "25",
                "row": "14",
                "dictionary_element": "Date",
                "document_id": "1277308 Rev C RBA_Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277308 Rev C RBA_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277308 Rev C RBA_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the Indication for Use section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "column": "25",
                "row": "15",
                "dictionary_element": "Date",
                "document_id": "1277308 Rev C RBA_Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277308 Rev C RBA_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277308 Rev C RBA_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the Contraindications section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "question": "Extract the intended purpose for product {product_code}",
                "column": "26",
                "row": "13",
                "dictionary_element": "Intended Use",
                "prompt_template": "intended_purpose_Risk",
                "document_id": "1277308 Rev C RBA_Irrigation Sets"
            },
            {
                "question": "Extract the Indication for Use for product {product_code}.",
                "column": "26",
                "row": "14",
                "dictionary_element": "Indication for Use",
                "prompt_template": "indication_for_use_Risk",
                "document_id": "1277308 Rev C RBA_Irrigation Sets"
            },
            {
                "question": "Extract the Contraindications for product {product_code}.",
                "column": "26",
                "row": "15",
                "dictionary_element": "Contraindications",
                "prompt_template": "contraindications_Risk",
                "document_id": "1277308 Rev C RBA_Irrigation Sets"
            },
            #sixth set of questions
            {
                "column": "27",
                "row": "13",
                "dictionary_element": "Date",
                "document_id": "1277312 Rev B RMR_Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277312 Rev B RMR_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277312 Rev B RMR_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the intended purpose section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "column": "27",
                "row": "14",
                "dictionary_element": "Date",
                "document_id": "1277312 Rev B RMR_Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277312 Rev B RMR_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277312 Rev B RMR_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the Indication for Use section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "column": "27",
                "row": "15",
                "dictionary_element": "Date",
                "document_id": "1277312 Rev B RMR_Irrigation Sets",
                "type":"group",
                "group": [
                    {
                        "question": "Extract the document id and revision for product {product_code}.",
                        "prompt_template": "document_id_and_revision_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277312 Rev B RMR_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header\"}}]}",
                    },
                    {
                        "question": "Extract the issued date for product {product_code}.",
                        "prompt_template": "issued_date_Risk",
                        "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"1277312 Rev B RMR_Irrigation Sets\"}}, {\"type\": {\"$eq\": \"header-date\"}}]}",
                    },
                    {
                        "question": "Extract the Contraindications section number for product {product_code}.",
                        "prompt_template": "section_number_Risk"
                    }
                ]
            },
            {
                "question": "Extract the intended purpose for product {product_code}",
                "column": "28",
                "row": "13",
                "dictionary_element": "Intended Use",
                "prompt_template": "intended_purpose_Risk",
                "document_id": "1277312 Rev B RMR_Irrigation Sets"
            },
            {
                "question": "Extract the Indication for Use for product {product_code}.",
                "column": "28",
                "row": "14",
                "dictionary_element": "Indication for Use",
                "prompt_template": "indication_for_use_Risk",
                "document_id": "1277312 Rev B RMR_Irrigation Sets"
            },
            {
                "question": "Extract the Contraindications for product {product_code}.",
                "column": "28",
                "row": "15",
                "dictionary_element": "Contraindications",
                "prompt_template": "contraindications_Risk",
                "document_id": "1277312 Rev B RMR_Irrigation Sets"
            }
        ]
    }

    return QUESTION_TEMPLATES

