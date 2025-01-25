import ollama


stream = ollama.chat(
    model='deepseek-r1',
    messages=[
        {
            "role": "system",
            "content": "You are a helpful Python coder."
        },
        {
            "role": "user",
            "content": "Implement heap sort. Return thinking process and python code in MARKDOWN format"
        }
    ],
    stream=True,
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)