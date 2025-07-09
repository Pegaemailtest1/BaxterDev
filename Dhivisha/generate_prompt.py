import sys
import logging
from jinja2 import Template
from .prompts.prompt_manager import PromptManager
from .prompts.utils import extract_components, extract_components_bulk

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

def select_prompt_template(context, query):
    fields = extract_components_bulk(context, query)
    field = fields.get("field", "")
    field = field.lower() if isinstance(field, str) else ""

    logging.info(f"Extracted fields: {fields}")
    logging.info(f"Field for intent mapping: {field}")

    # # Intent mapping logic
    # if field in ("intended purpose", "indication for use", "contraindications"):
    #     intent = "description"
    # elif field in ("notes", "cautions", "claims"):
    #     intent = "list"
    # elif field in ("all medical warnings", "all medical cautions", "all medical claims"):
    #     intent = "medical_context_list"
    # elif "part number" in field:
    #     intent = "part_number"
    # elif "harmonized standards" in field:
    #     intent = "ISO_standards"
    # else:
    #     intent = "default"
    
    intent ="default"
    #intent = "part_number_label"
    logging.info(f"Selected intent: {intent}")

    # Ensure 'fields' key is present for the prompt template
    if intent == "part_number_label":
        logging.info("Intent is part_number_label. Setting document type fields.")
        
        # Add fields to context_vars only if the intent is "part_number_label"
        context_vars = fields.copy()
        context_vars.setdefault("field", fields.get("field", ""))
        context_vars.setdefault("fields", [f.strip() for f in context_vars.get("field", "").split(",") if f.strip()])
        context_vars.setdefault("part_number", fields.get("part_number", ""))
        context_vars.setdefault("document_type", fields.get("document_type", "UNKNOWN TYPE"))
        context_vars.setdefault("rev", fields.get("rev", ""))
        context_vars.setdefault("date", fields.get("date", ""))

        logging.info(f"Context vars for part_number_label: {context_vars}")
    else:
        # If intent is not "part_number_label", just use the fields as usual
        context_vars = fields.copy()

    if "fields" not in context_vars:
        field_str = context_vars.get("field", "")
        if isinstance(field_str, str):
            context_vars["fields"] = [f.strip() for f in field_str.split(",") if f.strip()]
        else:
            context_vars["fields"] = []

    prompt_manager = PromptManager()
    context_vars.setdefault("context", context)
    context_vars.setdefault("field", fields.get("field", ""))
    # context_vars.setdefault("fields", [f.strip() for f in context_vars.get("field", "").split(",") if f.strip()])
    # context_vars.setdefault("part_number", fields.get("part_number", ""))
    # context_vars.setdefault("document_type", fields.get("document_type", "UNKNOWN TYPE"))
    # context_vars.setdefault("rev", fields.get("rev", ""))
    # context_vars.setdefault("date", fields.get("date", ""))
    # logging.info(f"Context vars passed to template: {context_vars}")
    prompt = prompt_manager.get_prompt(intent, context_vars)

    return prompt

def bulk_prompt_template(context, query, prompt_template):
    fields = extract_components_bulk(context, query)
    field = fields.get("field", "")
    field = field.lower() if isinstance(field, str) else ""

    if prompt_template:
        intent = prompt_template
    else:
        intent = "default"

    
    # Ensure 'fields' key is present for the prompt template
    if intent == "part_number_label":
        logging.info("Intent is part_number_label. Setting document type fields.")
        
        # Add fields to context_vars only if the intent is "part_number_label"
        context_vars = fields.copy()
        context_vars.setdefault("field", fields.get("field", ""))
        context_vars.setdefault("fields", [f.strip() for f in context_vars.get("field", "").split(",") if f.strip()])
        context_vars.setdefault("part_number", fields.get("part_number", ""))
        context_vars.setdefault("document_type", fields.get("document_type", "UNKNOWN TYPE"))
        context_vars.setdefault("rev", fields.get("rev", ""))
        context_vars.setdefault("date", fields.get("date", ""))

        logging.info(f"Context vars for part_number_label: {context_vars}")
    else:
        # If intent is not "part_number_label", just use the fields as usual
        context_vars = fields.copy()

    if "fields" not in context_vars:
        field_str = context_vars.get("field", "")
        if isinstance(field_str, str):
            context_vars["fields"] = [f.strip() for f in field_str.split(",") if f.strip()]
        else:
            context_vars["fields"] = []

    prompt_manager = PromptManager()
    
    # Build context vars robustly
    #context_vars = fields.copy()
    context_vars.setdefault("context", context)
    prompt = prompt_manager.get_prompt(intent, context_vars)

    return prompt

def raw_prompt_template(context, prompt):
    return f"""You are an intelligent assistant. Use the following context to answer the user's question.

    Context:
    {context}

    {prompt}
    """
