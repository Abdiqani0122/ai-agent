from gpt4all import GPT4All

model = GPT4All(
    "Meta-Llama-3-8B-Instruct.Q4_0.gguf",
    allow_download=True
)

def call_llm(prompt: str) -> str:
    response = model.generate(
        prompt,
        max_tokens=150,
        temp=0.2
    )
    return response.strip()