import openai

# Set your OpenAI API key
openai.api_key = "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"
# Call the o4-mini model
response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the weather like on Mars?"}
    ],
    temperature=0.7,
    max_tokens=200
)

# Print the model's response
print(response.choices[0].message["content"])
