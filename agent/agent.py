from .tools import summarize_text, answer_question

class Agent:
    def decide(self, text: str):
        text = text.lower()

        if "summarize" in text:
            return "summarize", "I saw the word 'summarize'.", "I plan to summarize the text."

        if "capital" in text:
            return "answer", "I saw the word 'capital'.", "I plan to answer a geography question."

        if "population" in text:
            return "answer", "I saw the word 'population'.", "I plan to answer a population question."

        if "currency" in text:
            return "answer", "I saw the word 'currency'.", "I plan to answer a currency question."

        if "continent" in text or "where is" in text:
            return "answer", "I saw a location question.", "I plan to answer a location question."

        return "unknown", "I did not understand the request.", "I do not have a plan."

    def act(self, text: str):
        decision, reason, plan = self.decide(text)

        if decision == "summarize":
            result = summarize_text(text)
        
        elif decision == "answer":
            result = answer_question(text)
        
        else:
            result = "I don't know how to do that yet."

        return f"{reason}\n\n{result}"
    