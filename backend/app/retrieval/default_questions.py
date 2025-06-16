def questions():
    QUESTION_TEMPLATES = {
	
        "Questions":[
            
            {
                "question":"Extract the Part Number, Rev and Date for product {product_code}.",
                "column":"3",
                "repeat":"True",
                "dictionary_element":"Date",
                "prompt_template":"part_number",
                "document_id":"0719004306"
            },
            {
                "question":"Extract the Part Number, Rev and Date for product {product_code}.",
                "column":"5",
                "repeat":"True",
                "dictionary_element":"Date",
                "prompt_template":"part_number",
                "document_id":"0736003737"
            },
            {
                "question":"Extract the Part Number, Rev and Date for product {product_code}.",
                "column":"7",
                "repeat":"True",
                "dictionary_element":"Date",
                "prompt_template":"part_number",
                "document_id":"0738002356"
            },
            {
                "question":"Extract the intended purpose for product {product_code} under Column 1 section",
                "column":"4",
                "row":"13",
                "dictionary_element":"Intended Use",
                "prompt_template":"description",
                "document_id":"0719004306"
            },
            {
                "question":"Extract the intended purpose for product {product_code}.",
                "column":"6",
                "row":"13",
                "dictionary_element":"Intended Use",
                "prompt_template":"description",
                "document_id":"0736003737"
            },
            {
                "question":"Extract the intended purpose for product {product_code}.",
                "column":"8",
                "row":"13",
                "dictionary_element":"Intended Use",
                "prompt_template":"description",
                "document_id":"0738002356"
            },
            {
                "question":"Extract the Indication for Use for product {product_code} under Indication for Use section.",
                "column":"4",
                "row":"14",
                "dictionary_element":"Indication for Use",
                "prompt_template":"description",
                "document_id":"0719004306"
            },
            {
                "question":"Extract the Indication for Use for product {product_code} under Indication for Use section.",
                "column":"6",
                "row":"14",
                "dictionary_element":"Indication for Use",
                "prompt_template":"description",
                "document_id":"0736003737"
            },
            {
                "question":"Extract the Indication for Use for product {product_code} under Indication for Use section.",
                "column":"8",
                "row":"14",
                "dictionary_element":"Indication for Use",
                "prompt_template":"description",
                "document_id":"0738002356"
            },
            {
                "question":"Extract the Contraindications for product {product_code} under Contraindications section.",
                "column":"4",
                "row":"15",
                "dictionary_element":"Contraindications",
                "prompt_template":"description",
                "document_id":"0719004306"
            },
            {
                "question":"Extract the Contraindications for product {product_code} under Contraindications section.",
                "column":"6",
                "row":"15",
                "dictionary_element":"Contraindications",
                "prompt_template":"description",
                "document_id":"0736003737"
            },
            {
                "question":"Extract the Contraindications for product {product_code} under Contraindications section.",
                "column":"8",
                "row":"15",
                "dictionary_element":"Contraindications",
                "prompt_template":"description",
                "document_id":"0738002356"
            },
            {
                "question":"Extract the Claims for product {product_code} under Claims section.",
                "column":"4",
                "dictionary_element":"Claims",
                "prompt_template":"list",
                "document_id":"0719004306"
            },
            {
                "question":"Extract the Claims for product {product_code} under Claims section.",
                "column":"6",
                "dictionary_element":"Claims",
                "prompt_template":"list",
                "document_id":"0736003737"
            },
            {
                "question":"Extract the Claims for product {product_code} under Claims section.",
                "column":"8",
                "dictionary_element":"Claims",
                "prompt_template":"list",
                "document_id":"0738002356"
            },
            {
                "question":"Extract the Notes for product {product_code} under Notes section",
                "column":"4",
                "dictionary_element":"Warnings",
                "prompt_template":"medical_context_list",
                "document_id":"0719004306"
            },
            {
                "question":"Extract the Notes for product {product_code} under Notes section",
                "column":"6",
                "dictionary_element":"Warnings",
                "prompt_template":"medical_context_list",
                "document_id":"0736003737"
            },
            {
                "question":"Extract the Notes for product {product_code} under Notes section",
                "column":"8",
                "dictionary_element":"Warnings",
                "prompt_template":"medical_context_list",
                "document_id":"0738002356"
            },
            {
                "question":"Extract the Cautions for product {product_code} under Cautions section",
                "column":"4",
                "dictionary_element":"Cautions",
                "prompt_template":"list",
                "document_id":"0719004306"
            },
            {
                "question":"Extract the Cautions for product {product_code} under Cautions section",
                "column":"6",
                "dictionary_element":"Cautions",
                "prompt_template":"list",
                "document_id":"0736003737"
            },
            {
                "question":"Extract the Cautions for product {product_code} under Cautions section",
                "column":"8",
                "dictionary_element":"Cautions",
                "prompt_template":"list",
                "document_id":"0738002356"
            }
        ]
    }
    return QUESTION_TEMPLATES


def priority():
    priority_list = ["Intended Use","Indication for Use","Contraindications","Claims","Warnings","Cautions","Date"]
    return priority_list
