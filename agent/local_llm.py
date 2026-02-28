from gpt4all import GPT4All

model = GPT4All(
    "mistral-7b-openorca.gguf2.Q4_0",
    allow_download=True
)

def call_llm(prompt: str) -> str:
    response = model.generate(
        prompt,
        max_tokens=400,
        temp=0.3
    )
    return response.strip()