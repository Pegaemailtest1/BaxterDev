import ast
import logging
import json

def process_question_templates(questions_fn, product_code, form_dict_input_fn, query_llama_fn, config, dict_data):
    try:
        question_templates = questions_fn()
        for i, q_template in enumerate(question_templates["Questions"]):
            q_type = q_template.get("type", "single")
            dictionary_element = q_template["dictionary_element"]
            column = int(q_template["column"])
            row = int(q_template.get("row")) if "row" in q_template else None
            repeat = q_template.get("repeat", False)

            if q_type == "group":
                group_responses = []
                for sub_q in q_template["group"]:
                    question_text = sub_q["question"].format(product_code=product_code)
                    prompt_template = sub_q["prompt_template"]
                    document_id = q_template["document_id"]
                    full_document_search = sub_q.get("full_document_search", False)
                    where_filter = sub_q.get("where_filter")
                    max_results = int(sub_q.get("max_results", q_template.get("max_results", config["MAX_RESULTS"])))

                    response = query_llama_fn(
                        question_text,
                        document_id,
                        prompt_template,
                        full_document_search,
                        where_filter,
                        config["OLLAMA_URL"],
                        config["EMBED_MODEL"],
                        config["CHROMA_HOST"],
                        config["CHROMA_PORT"],
                        config["COLLECTION_NAME"],
                        config["FM_MODEL"],
                        max_results,
                        config["temperature"],
                        config["max_tokens"]
                    )
                    if response:
                        group_responses.append(str(response).strip())

                combined_response = ", ".join(group_responses)
                form_dict_input_fn(dictionary_element, combined_response, column, row, repeat, q_type)

            else:
                question_text = q_template["question"].format(product_code=product_code)
                prompt_template = q_template["prompt_template"]
                document_id = q_template["document_id"]
                full_document_search = q_template.get("full_document_search", False)
                where_filter = q_template.get("where_filter")
                max_results = int(q_template.get("max_results", config["MAX_RESULTS"]))

                response = query_llama_fn(
                    question_text,
                    document_id,
                    prompt_template,
                    full_document_search,
                    where_filter,
                    config["OLLAMA_URL"],
                    config["EMBED_MODEL"],
                    config["CHROMA_HOST"],
                    config["CHROMA_PORT"],
                    config["COLLECTION_NAME"],
                    config["FM_MODEL"],
                    max_results,
                    config["temperature"],
                    config["max_tokens"]
                )

                if not response:
                    continue

                if isinstance(response, str):
                    try:
                        parsed = ast.literal_eval(response.strip())
                        response = parsed
                    except Exception:
                        response = response.strip()

                form_dict_input_fn(dictionary_element, response, column, row, repeat, q_type)

    except Exception as e:
        logging.info(f"Error while processing question templates: {e}")

    logging.info(f"dict data: {json.dumps(dict_data, indent=2)}")
