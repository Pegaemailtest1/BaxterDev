from jinja2 import Template
import re
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

def extract_components(context, query: str):
    document_match = re.search(r'from the (.*?) \((\d+)\) document', query)
    product_match = re.search(r'for product (\w+)', query)
    field_match = re.search(r'Extract the (.*?) from', query)
    
    #logging.info(f"field_match: {field_match}")

    return {
        "document_type" : document_match.group(1) if document_match else None,
        "document_id" : document_match.group(2) if document_match else None,
        "product_code": product_match.group(1) if product_match else None,
        "field": field_match.group(1) if field_match else None,
        "context": context
    }

def generate_prompt_template(context, query):

    fields = extract_components(context, query)

    # Jinja template string
    template_str = """
    You are a helpful assistant that extracts specific information from a set of documents.

    Context:
    {{ context }}

    Task:
    Extract the "{{ field }}".
    
    Please apply the following formatting rules:
    - Format part number as: "<value>_{{ document_type.split()[1] }}"
    - If the **rev** field is empty then don't take "proofread" value, return: "Not found".
    - The date field is in DDMMMYY format and convert that into the format: "DD-MMM-YYYY" example: "04-DEC-2024"

    Return the values in the same order, comma-separated.    
    If a field value is missing, return "Not found" in its place.
    
    {% set result_string = "" %}
    {% set sep = "" %}

    {% for field in fields %}
        {% if field.lower() == "part number" %}
            {% if part_number %}
                {% set part_number_clean = part_number.split('_')[0] %}
                {% set value = part_number_clean ~ '_' ~ document_type.split()[1] %}
            {% else %}
                {% set value = "Not found" %}
            {% endif %}
        {% elif field.lower() == "rev" %}
            {% if rev and rev.strip()|length > 0 and "proofread" not in context.lower() %}
                {% set value = 'Rev ' ~ rev.strip() %}
            {% else %}
                {% set value = "Not found" %}
            {% endif %}
        {% elif field.lower() == "date" %}
            {% if date and date|length == 7 %}
                {% set day = date[0:2] %}
                {% set month = date[2:5].upper() %}
                {% set year_suffix = date[5:] %}
                {% if year_suffix.isdigit() %}
                    {% set year_number = year_suffix|int %}
                    {% if year_number < 50 %}
                        {% set year = "20" ~ "%02d"|format(year_number) %}
                    {% else %}
                        {% set year = "19" ~ "%02d"|format(year_number) %}
                    {% endif %}
                    {% set value = day ~ "-" ~ month ~ "-" ~ year %}
                {% else %}
                    {% set value = "Not found" %}
                {% endif %}
            {% else %}
                {% set value = "Not found" %}
            {% endif %}
        {% else %}
            {% set value = "Not found" %}
        {% endif %}

        {% set result_string = result_string + sep + value %}
        {% set sep = ", " %}
    {% endfor %}

    {{ result_string }}

    ⛔ Do not include any additional text or explanation.
    ✅ Respond ONLY with this exact JSON format:
    {
    "response": "{{ result_string }}"
    }

    """

    # Render template
    template = Template(template_str)
    final_prompt = template.render(fields)

    return final_prompt


def generate_prompt_template_for_intentended(context, query):

    fields = extract_components(context, query)

    # Jinja template string
    template_str = """
        You are a helpful assistant that extracts specific information from a set of documents.

        Context:
        {{ context }}

        Task:
        Extract the "{{ field }}" field from the document.

        Please apply the following formatting rules:
        - Extract the complete English sentence or paragraph that contains "{{ field }}".
        - If it's split across lines or segments, combine them. 
        - Ignore non-English text (e.g., German, Spanish). If not found, return: "No Trace".
        - Example: "For the delivery of irrigation solutions from the fluid container to the irrigation site."

        ⛔ Do not include any additional text or explanation.
        ✅ Respond ONLY with this exact JSON format:
        {
        "response": "<your extracted sentence here>"
        }
        """


    # Render template
    template = Template(template_str)
    final_prompt = template.render(fields)

    return final_prompt

def generate_prompt_template_for_indication_for_use(context, query):

    if not context:
        response = '{"response": "No Trace"}'
        return response
    
    fields = extract_components(context, query)

    # Jinja template string
    template_str = """
        You are a helpful assistant that extracts specific information from a set of documents.

        Context:
        {{ context }}

        Task:
        Extract the "{{ field }}" field from the document.

        Please apply the following formatting rules:
        - Extract the complete English sentence or paragraph that contains "{{ field }}".
        - If it's split across lines or segments, combine them. 
        - Ignore non-English text (e.g., German, Spanish). If not found, return: "No Trace".
        
        ⛔ Do not include any additional text or explanation.
        ✅ Respond ONLY with this exact JSON format:
        {
        "response": "<your extracted sentence here>"
        }
        """


    # Render template
    template = Template(template_str)
    final_prompt = template.render(fields)

    return final_prompt

def generate_prompt_template_for_contraindications(context, query):

    if not context:
        response = '{"response": "No Trace"}'
        return response
    
    fields = extract_components(context, query)

    # Jinja template string
    template_str = """
        You are a helpful assistant that extracts specific information from a set of documents.

        Context:
        {{ context }}

        Task:
        Extract the "{{ field }}" field from the document.

        Please apply the following formatting rules:
        - Extract the complete English sentence or paragraph that contains "{{ field }}".
        - If it's split across lines or segments, combine them. 
        - Ignore non-English text (e.g., German, Spanish). If not found, return: "No Trace".
        
        ⛔ Do not include any additional text or explanation.
        ✅ Respond ONLY with this exact JSON format:
        {
        "response": "<your extracted sentence here>"
        }
        """


    # Render template
    template = Template(template_str)
    final_prompt = template.render(fields)

    return final_prompt

def generate_prompt_template_for_list(context, query):

    if not context:
        return '{"response": ["No Trace"]}'
    
    fields = extract_components(context, query)
   
    template_str = """
        Context:
        {{ context }}

        Task:
        Extract all English bullet points listed under the "{{ field }}" section of the document.

        Instructions:
        - Bullet points begin with the symbol "•" and may span multiple lines — include the full text as a single item.
        - Join multi-line bullets into one complete sentence.
        - Extract all bullet points exactly as they appear, even if they are short or general (e.g., references, glossary notes).
        - Each bullet point must end with a period.
        - Exclude any text not starting with "•".
        - If no bullet points are found under "{{ field }}", return: ["No Trace"].

        Output Format:
        Return a JSON object structured as:
        {
        "response": [
            "First bullet point.",
            "Second bullet point.",
            ...
        ]
        }

        ⛔ Do not include bullet characters ("•") in the final output.
        ⛔ Do not include extra explanation or metadata.
        ✅ Only return the exact JSON object as specified.
        """

    # Render template
    template = Template(template_str)
    final_prompt = template.render(fields)

    return final_prompt


def generate_prompt_template_for_context_list(context, query):

    if not context:
        return '{"response": ["No Trace"]}'
    
    fields = extract_components(context, query)
   
    template_str = """
        Context:
        {{ context }}

        Task:
        Extract all medical warnings from the context.

        Instructions:
        - Bullet points begin with the symbol "•" and may span multiple lines — include the full text as a single item.
        - Join multi-line bullets into one complete sentence.
        - A medical warning refers to any instruction related to storage, handling, disposal, usage intervals, or precautions for safe use of the product.
        - Include any bullet point that addresses how the product should be used, stored, replaced, or discarded.
        - Do NOT include bullet points that only mention material composition, manufacturing claims, or glossary references.
        - Each bullet point must end with a period.
        - If no applicable medical warnings are found, return: ["No Trace"].

        Output Format:
        Return a JSON object structured as:
        {
            "response": [
                "First medical warning.",
                "Second medical warning.",
                ...
            ]
        }

        ⛔ Do not include bullet characters ("•") in the final output.
        ⛔ Do not include extra explanation or metadata.
        ✅ Only return the exact JSON object as specified.
        """
    # Render template
    template = Template(template_str)
    final_prompt = template.render(fields)

    return final_prompt


def generate_default_prompt_template(context, query):
    
    fields = extract_components(context, query)
   
    template_str = """
        Context:
        {{ context }}

        Task:
        {{ query }}

        Instructions:
        - Extract only the text that appears under "{{ query }}" in the context.
        - Return the exact text block as-is, preserving punctuation and paragraph breaks.
        - If no matching section is found, return: ["No Trace"].

        Output Format:
        Return a JSON object structured as:
        {
            "response": [
                "Extracted text block here."
            ]
        }

        ⛔ Do not include extra explanation or metadata.
        ✅ Only return the exact JSON object as specified.
        """

    # Render template
    template = Template(template_str)
    final_prompt = template.render(fields)

    return final_prompt

def select_prompt_template(context, query):
    
    fields = extract_components(context, query)

    # If only "intended purpose" is requested, use the specific template
    field = fields.get("field", "")
    #field = str(field).strip()
    field = field.lower() if isinstance(field, str) else ""
    #logging.info(f"Field: {field}")
    if field in ("intended purpose"):
        return generate_prompt_template_for_intentended(context, query)
    elif field in ("notes", "cautions", "claims"):
        return generate_prompt_template_for_list(context, query)
    elif "indication for use" in field:
        return generate_prompt_template_for_indication_for_use(context, query)
    elif "contraindications" in field:
        return generate_prompt_template_for_contraindications(context, query)
    elif "part number" in field:
        return generate_prompt_template(context, query)
    elif field in ("all medical warnings", "all medical cautions", "all medical claims"):
        return generate_prompt_template_for_context_list(context, query)
    else:
        return generate_default_prompt_template(context, query)
    


def test_prompt_template(context,prompt):
    return f"""You are an intelligent assistant. Use the following context to answer the user's question.

            Context:
            {context}

            {prompt}"""