from .tools import summarize_text, answer_question

class Agent:
    def decide(self, text: str):
        text = text.lower()

        if "summarize" in text:
            return "summarize", "I saw the word 'summarize'."
        if "capital" in text:
            return "answer", "I saw the word 'capital'."
        
        return "unknown", "I did not understand the request."

    def act(self, text: str):
        decision, reason = self.decide(text)

        if decision == "summarize":
            result = summarize_text(text)
        
        elif decision == "answer":
            result = answer_question(text)
        
        else:
            result = "I don't know how to do that yet."

        return f"{reason}\n\n{result}"
    