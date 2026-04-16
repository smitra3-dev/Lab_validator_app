from ollama import chat

response = chat(
    model="qwen2.5:1.5b",
    messages=[{"role":"user", "content": "Explain S21 in RF in one line"}]
    )
print (response["message"]["content"])
