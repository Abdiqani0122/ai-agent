import json
import os

from .local_llm import call_llm
from .tools import summarize_text, web_search


class Agent:
    """
    Internet-enabled agent:
    - For normal questions: web_search -> LLM answer using results
    - For summarization: summarize_text (or you can also use LLM)
    - Stores lightweight memory (last query) in memory.json
    """

    def __init__(self):
        self.last_query = None
        self.load_memory()

    def load_memory(self):
        if os.path.exists("memory.json"):
            try:
                with open("memory.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                self.last_query = data.get("last_query")
            except Exception:
                # If memory.json is corrupted, ignore it
                self.last_query = None

    def save_memory(self):
        with open("memory.json", "w", encoding="utf-8") as f:
            json.dump({"last_query": self.last_query}, f, indent=2)

    def decide(self, text: str):
        t = text.strip().lower()

        # Very light routing; not "hard-coded Q&A", just action selection.
        if t.startswith("summarize:") or t.startswith("summary:"):
            return "summarize"

        # Default behavior: answer anything with web+LLM
        return "web_answer"

    def web_answer(self, question: str) -> str:
        # 1) Search the internet
        results = web_search(question, max_results=6)

        # 2) Ask the LLM to answer using the search results
        prompt = f"""You are a helpful assistant.
Use the search results to answer the question.
If results are weak or conflicting, say so and give the best supported answer.

Question:
{question}

Search results (snippets):
{results}

Answer:"""

        return call_llm(prompt).strip()

    def act(self, text: str):
        decision = self.decide(text)

        if decision == "summarize":
            # Strip prefix if present
            clean = text.split(":", 1)[1].strip() if ":" in text else text
            result = summarize_text(clean)
        else:
            self.last_query = text.strip()
            result = self.web_answer(text.strip())

        self.save_memory()
        return result



