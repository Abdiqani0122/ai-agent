from .tools import summarize_text, answer_question

class Agent:
    def decide(self, text: str):
        text = text.lower()

        if "summarize" in text:
            return "summarize"
        if "capital" in text:
            return "answer"
        
        return "unknown"

    def act(self, text: str):
        decision = self.decide(text)

        if decision == "summarize":
            return summarize_text(text)
        
        if decision == "answer":
            return answer_question(text)

        return "I don't know how to do that yet."
    