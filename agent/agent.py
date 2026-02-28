from .tools import summarize_text, answer_question

class Agent:
    # Question topics
    FOLLOW_UP_TOPICS = {"capital", "population", "currency", "continent"}

    def __init__(self):
        self.last_topic = None # 🧠 memory

    def decide(self, text: str):
        text = text.lower()

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
            return "answer", "I remembered the previous question.", "I plan to use my memory."

        return "unknown", "I did not understand the request.", "I do not have a plan."

    def act(self, text: str):
        decision, reason, plan = self.decide(text)

        if decision == "answer":
            if "what about" in text and self.last_topic:
                country = text.replace("what about", "").strip()

                if self.last_topic in self.FOLLOW_UP_TOPICS:
                    rebuilt = f"{self.last_topic} of {country}"
                    result = answer_question(rebuilt)
                else:
                    result = "I can't use my memory for that kind of request."
            else:
                result = answer_question(text)

        elif decision == "summarize":
            result = summarize_text(text)

        else:
            result = "I don't know how to do that yet."

        return f"{plan}\n{reason}\n\n{result}"