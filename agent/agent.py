from .tools import summarize_text, answer_question

class Agent:
    def decide(self, task: str):
        if "summarize" in task.lower():
            return "summarize"
        
        if "answer" in task:
            return "answer"
        
        return "unknown"

    def act(self, task: str, text: str):
        decision = self.decide(task)

        if decision == "summarize":
            return summarize_text(text)
        
        if decision == "answer":
            return answer_question(text)

        return "I don't know how to do that yet."
    