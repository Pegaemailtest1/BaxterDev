import ast
import logging
import json

# ----------------------------------------
# Helper: handle "group" type questions
# ----------------------------------------
def handle_group_questions(q_template, q_type, product_code, form_dict_input_fn, query_llama_fn, config):
    document_id = q_template["document_id"]
    dictionary_element = q_template["dictionary_element"]
    column = int(q_template["column"])
    row = int(q_template.get("row")) if "row" in q_template else None
    repeat = q_template.get("repeat", False)

    group_responses = []
    for sub_q in q_template["group"]:
        question_text = sub_q["question"].format(document_id=document_id, product_code=product_code)
        prompt_template = sub_q["prompt_template"]
        full_document_search = sub_q.get("full_document_search", False)
        where_filter = sub_q.get("where_filter")
        max_results = int(sub_q.get("max_results", q_template.get("max_results", config["max_results"])))
        where_document = sub_q.get("where_document")

        response = query_llama_fn(
            question_text,
            document_id,
            prompt_template,
            full_document_search,
            where_filter,
            where_document,
            max_results,
            config
        )
        if response:
            group_responses.append(str(response).strip())

    combined_response = ", ".join(group_responses)
    form_dict_input_fn(dictionary_element, combined_response, column, row, repeat, q_type)


# ----------------------------------------
# Helper: handle "single" type questions
# ----------------------------------------
def handle_single_question(q_template, q_type, product_code, form_dict_input_fn, query_llama_fn, config):
    document_id = q_template["document_id"]
    dictionary_element = q_template["dictionary_element"]
    column = int(q_template["column"])
    row = int(q_template.get("row")) if "row" in q_template else None
    repeat = q_template.get("repeat", False)
    question_text = q_template["question"].format(document_id=document_id, product_code=product_code)
    prompt_template = q_template["prompt_template"]
    full_document_search = q_template.get("full_document_search", False)
    where_filter = q_template.get("where_filter")
    max_results = int(q_template.get("max_results", config["max_results"]))
    where_document = q_template.get("where_document")

    response = query_llama_fn(
        question_text,
        document_id,
        prompt_template,
        full_document_search,
        where_filter,
        where_document,
        max_results,
        config
    )

    if not response:
        return

    if isinstance(response, str):
        try:
            parsed = ast.literal_eval(response.strip())
            response = parsed
        except Exception:
            response = response.strip()

    form_dict_input_fn(dictionary_element, response, column, row, repeat, q_type)


# ----------------------------------------
# Main: supports single, group, and link
# ----------------------------------------
def process_question_templates(questions_fn, product_code, form_dict_input_fn, query_llama_fn, dict_data, config):
    try:
        question_templates = questions_fn()
        for q_template in question_templates["Questions"]:
            q_type = q_template.get("type", "single")

            if q_type == "group":
                handle_group_questions(q_template, q_type, product_code, form_dict_input_fn, query_llama_fn, config)

            elif q_type == "link":
                # 1. Ask the root-level link question
                handle_single_question(q_template, q_type, product_code, form_dict_input_fn, query_llama_fn, config)

                # 2. Process each linked sub-question
                for link_sub_q in q_template.get("link", []):
                    sub_type = link_sub_q.get("type", "single")
                    link_sub_q.setdefault("document_id", q_template["document_id"])  # inherit from parent
                    link_sub_q.setdefault("dictionary_element", q_template["dictionary_element"])
                    link_sub_q.setdefault("column", q_template["column"])
                    link_sub_q.setdefault("row", q_template.get("row"))
                    link_sub_q.setdefault("repeat", q_template.get("repeat", False))

                    if sub_type == "group":
                        handle_group_questions(link_sub_q, sub_type, product_code, form_dict_input_fn, query_llama_fn, config)
                    else:
                        handle_single_question(link_sub_q, sub_type, product_code, form_dict_input_fn, query_llama_fn, config)

            else:
                handle_single_question(q_template, q_type, product_code, form_dict_input_fn, query_llama_fn, config)

    except Exception as e:
        logging.info(f"Error while processing question templates: {e}")

    logging.info(f"dict data: {json.dumps(dict_data, indent=2)}")
