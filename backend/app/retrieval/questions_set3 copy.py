def questions():
    QUESTION_TEMPLATES = {
        "Questions": [
            {
                "dictionary_element": "ISO Codes",
                "document_id": "BXU601670_MDR_CER,A",
                "full_document_search":"True",
                "question": "Extract the all ISO standards for product {product_code}.",
                "type":"table",
                "match":"True",
                "prompt_template": "ISO_standards",
                "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU601670_MDR_CER,A\"}}, {\"type\": {\"$eq\": \"table\"}}]}",
                "mapping": [
                    {
                        "header_name":"description",
                        "column": "2"					
                    },
                    {
                        "header_name":"ISO Code",
                        "column": "3"					
                    }
                ]
            },
            {
                "dictionary_element": "ISO Codes",
                "document_id": "BXU535425 Rev D_User Needs",
                "full_document_search":"True",
                "question": "Extract the all ISO standards for product {product_code}.",
                "type":"table",
                "match":"True",
                "prompt_template": "ISO_standards",
                "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU535425 Rev D_User Needs\"}}, {\"type\": {\"$eq\": \"table\"}}]}",
                "mapping": [
                    {
                        "header_name":"description",
                        "column": "2",
                        "check":"True"
                        
                    },
                    {
                        "header_name":"ISO Code",
                        "column": "4"					
                    }
                ]
            },
            {
                "dictionary_element": "ISO Codes",
                "document_id": "BXU535427 Rev D_Design Input - Requirements",
                "full_document_search":"True",
                "question": "Extract the all ISO standards for product {product_code}.",
                "type":"table",
                "match":"True",
                "prompt_template": "ISO_standards",
                "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU535427 Rev D_Design Input - Requirements\"}}, {\"type\": {\"$eq\": \"table\"}}]}",
                "mapping": [
                    {
                        "header_name":"description",
                        "column": "2",
                        "check":"True"					
                    },
                    {
                        "header_name":"ISO Code",
                        "column": "5"					
                    }
                ]
            },
            {
                "dictionary_element": "ISO Codes",
                "document_id": "BXU535428 Rev J_DESIGN INPUTS – LABELLING REQUIREMENTS",
                "full_document_search":"True",
                "question": "Extract the all ISO standards for product {product_code}.",
                "type":"table",
                "match":"True",
                "prompt_template": "ISO_standards",
                "where_filter": "{\"$and\": [{\"document_id\": {\"$eq\": \"BXU535428 Rev J_DESIGN INPUTS – LABELLING REQUIREMENTS\"}}, {\"type\": {\"$eq\": \"table\"}}]}",
                "mapping": [
                    {
                        "header_name":"description",
                        "column": "2",
                        "check":"True"					
                    },
                    {
                        "header_name":"ISO Code",
                        "column": "6"					
                    }
                ]
            },
        ]
    }

    return QUESTION_TEMPLATES


def priority():
    priority_list = ["ISO Codes"]
    return priority_list
