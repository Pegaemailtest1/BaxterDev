def questions():
    QUESTION_TEMPLATES = {
	
        "Questions":[
            
            {
                "question":"Extract the Part Number, Rev and Date from the Label IFU (0719004306) document for product {product_code}.",
                "column":"3",
                "repeat":"True",
                "dictionary_element":"Date"
            },
            {
                "question":"Extract the Part Number, Rev and Date from the Label Pouch (0736003737) document for product {product_code}.",
                "column":"5",
                "repeat":"True",
                "dictionary_element":"Date"
            },
            {
                "question":"Extract the Part Number, Rev and Date from the Label Carton (0738002356) document for product {product_code}.",
                "column":"7",
                "repeat":"True",
                "dictionary_element":"Date"
            },
            {
                "question":"Extract the intended purpose from the Label IFU (0719004306) document for product {product_code}  under Column 1 section",
                "column":"4",
                "row":"13",
                "dictionary_element":"Intended Use"
            },
            {
                "question":"Extract the intended purpose from the label Pouch (0736003737) document for product {product_code}.",
                "column":"6",
                "row":"13",
                "dictionary_element":"Intended Use"
            },
            {
                "question":"Extract the intended purpose from the Label Carton (0738002356) document for product {product_code}.",
                "column":"8",
                "row":"13",
                "dictionary_element":"Intended Use"
            },
            {
                "question":"Extract the Indication for Use from the Label IFU (0719004306) document for product {product_code}.",
                "column":"4",
                "row":"14",
                "dictionary_element":"Indication for Use"
            },
            {
                "question":"Extract the Indication for Use from the label Pouch (0736003737) document for product {product_code}.",
                "column":"6",
                "row":"14",
                "dictionary_element":"Indication for Use"
            },
            {
                "question":"Extract the Indication for Use from the Label Carton (0738002356) document for product {product_code}.",
                "column":"8",
                "row":"14",
                "dictionary_element":"Indication for Use"
            },
            {
                "question":"Extract the Contraindications from the Label IFU (0719004306) document for product {product_code}.",
                "column":"4",
                "row":"15",
                "dictionary_element":"Contraindications"
            },
            {
                "question":"Extract the Contraindications from the label Pouch (0736003737) document for product {product_code}.",
                "column":"6",
                "row":"15",
                "dictionary_element":"Contraindications"
            },
            {
                "question":"Extract the Contraindications from the Label Carton (0738002356) document for product {product_code}.",
                "column":"8",
                "row":"15",
                "dictionary_element":"Contraindications"
            },
            {
                "question":"Extract the Claims from the Label IFU (0719004306) document for product {product_code} under Claims section.",
                "column":"4",
                "dictionary_element":"Claims"
            },
            {
                "question":"Extract the Claims from the label Pouch (0736003737) document for product {product_code} under Claims section.",
                "column":"6",
                "dictionary_element":"Claims"
            },
            {
                "question":"Extract the Claims from the Label Carton (0738002356) document for product {product_code} under Claims section.",
                "column":"8",
                "dictionary_element":"Claims"
            },
            {
                "question":"Extract the Notes from the Label IFU (0719004306) document for product {product_code} under Notes section",
                "column":"4",
                "dictionary_element":"Warnings"
            },
            {
                "question":"Extract the Notes from the label Pouch (0736003737) document for product {product_code} under Notes section",
                "column":"6",
                "dictionary_element":"Warnings"
            },
            {
                "question":"Extract the Notes from the Label Carton (0738002356) document for product {product_code} under Notes section",
                "column":"8",
                "dictionary_element":"Warnings"
            },
            {
                "question":"Extract the Cautions from the Label IFU (0719004306) document for product {product_code} under Cautions section",
                "column":"4",
                "dictionary_element":"Cautions"
            },
            {
                "question":"Extract the Cautions from the label Pouch (0736003737) document for product {product_code} under Cautions section",
                "column":"6",
                "dictionary_element":"Cautions"
            },
            {
                "question":"Extract the Cautions from the Label Carton (0738002356) document for product {product_code} under Cautions section",
                "column":"8",
                "dictionary_element":"Cautions"
            }
        ]
    }
    return QUESTION_TEMPLATES


def priority():
    priority_list = ["Intended Use","Indication for Use","Contraindications","Claims","Warnings","Cautions","Date"]
    return priority_list
