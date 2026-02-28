from .tools import summarize_text, answer_question
from .countries import COUNTRIES
from .local_llm import local_understand_user
import json
import os

class Agent:
    FOLLOW_UP_TOPICS = {"capital", "population", "currency", "continent"}

    def __init__(self):
        self.last_topic = None
        self.last_country = None
        self.load_memory()

    def load_memory(self):
        if os.path.exists("memory.json"):
            with open("memory.json", "r") as f:
                data = json.load(f)
                self.last_topic = data.get("last_topic")
                self.last_country = data.get("last_country")

    def save_memory(self):
        with open("memory.json", "w") as f:
            json.dump(
                {
                    "last_topic": self.last_topic,
                    "last_country": self.last_country
                },
                f,
                indent=2
            )

    def extract_country(self, text: str):
        for country in COUNTRIES.keys():
            if country in text:
                return country
        return None

    def decide(self, text: str):
        data = local_understand_user(text)

        intent = data.get("intent")
        topic = data.get("topic")
        country = data.get("country")

        # Update memory first
        if topic:
            self.last_topic = topic
        if country:
            self.last_country = country

        # 1️⃣ Summarization still explicit
        if intent == "summarize":
            return "summarize", "AI detected summarization.", "I plan to summarize the text."

        # 2️⃣ If we have enough context, ALWAYS try to answer
        if self.last_topic and (intent == "answer" or topic or country or "what about" in text):
            return "answer", f"Using topic '{self.last_topic}'.", "I plan to answer using tools."

        # 3️⃣ Otherwise unknown
        return "unknown", "AI was unsure.", "I do not have a plan."
    
    def act(self, text: str):
        decision, reason, plan = self.decide(text)

        if decision == "answer":
            if "what about" in text and self.last_topic:
                country = self.extract_country(text) or self.last_country

                if country:
                    self.last_country = country
                    rebuilt = f"{self.last_topic} of {country}"
                    result = answer_question(rebuilt)
                else:
                    result = "I don't know which country you mean."
            else:
                result = answer_question(text)

        elif decision == "summarize":
            result = summarize_text(text)

        else:
            result = "I don't know how to do that yet."

        self.save_memory()
        return f"{plan}\n{reason}\n\n{result}"