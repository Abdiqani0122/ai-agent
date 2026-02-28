from .tools import summarize_text

class Agent:
    def decide(self, task: str):
        if "summarize" in task.lower():
            return "summarize"
        return "unknown"

    def act(self, task: str, text: str):
        decision = self.decide(task)

        if decision == "summarize":
            return summarize_text(text)

        return "I don't know how to do that yet."