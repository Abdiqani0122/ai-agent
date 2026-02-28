from .tools import summarize_text, answer_question
from .countries import COUNTRIES
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
        text = text.lower()

        country = self.extract_country(text)
        if country:
            self.last_country = country

        if "summarize" in text:
            self.last_topic = "summarize"
            return "summarize", "I saw the word 'summarize'.", "I plan to summarize the text."

        if "capital" in text:
            self.last_topic = "capital"
            return "answer", "I saw the word 'capital'.", "I plan to answer a geography question."

        if "population" in text:
            self.last_topic = "population"
            return "answer", "I saw the word 'population'.", "I plan to answer a population question."

        if "currency" in text:
            self.last_topic = "currency"
            return "answer", "I saw the word 'currency'.", "I plan to answer a currency question."

        if "continent" in text or "where is" in text:
            self.last_topic = "continent"
            return "answer", "I saw a location question.", "I plan to answer a location question."

        if "what about" in text and self.last_topic:
            return "answer", "I used context memory.", "I plan to reuse the previous topic."

        return "unknown", "I did not understand the request.", "I do not have a plan."

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