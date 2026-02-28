from gpt4all import GPT4All
import json
import re

model = GPT4All(
    "mistral-7b-openorca.gguf2.Q4_0",
    allow_download=True
)

def local_understand_user(text: str) -> dict:
    prompt = f"""
You extract structured data from user input.

Return ONLY JSON with this schema:
{{
  "intent": "answer | summarize | unknown",
  "topic": "capital | currency | population | continent | null",
  "country": "string or null"
}}

User input:
{text}
"""

    response = model.generate(
        prompt,
        max_tokens=200,
        temp=0
    )

    match = re.search(r"\{.*\}", response, re.DOTALL)

    if not match:
        return {"intent": "unknown", "topic": None, "country": None}

    try:
        return json.loads(match.group())
    except json.JSONDecodeError:
        return {"intent": "unknown", "topic": None, "country": None}