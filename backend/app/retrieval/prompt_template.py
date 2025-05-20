
def generate_prompt_template(question, context):
    
    if "Date" in question:
        prompt = f"""You are a helpful assistant. Analyze the following technical document excerpts and extract the following information:

                    1. Date
                    
                    If either date is not found, respond with "Not Available".

                    ### Document Context:
                    {context}

                    ### Instructions:
                    Find and return the Date in the following format:

                    Date: <date>
                    """
    elif "intended purpose" in question:
        prompt = f"""You are a helpful assistant. Analyze the following technical document excerpts and extract the following information:

                    1. intended purpose
                    
                    If either intended purpose is not found, respond with "Not Available".

                    ### Document Context:
                    {context}

                    ### Instructions:
                    Find and return the intended purpose in the following format:

                    intended purpose: <intended purpose>
                    """
    else:
        prompt = f"""Answer the question based on the context below. 
                Context: {context}
                Question: {question}
                Answer:"""
    return prompt