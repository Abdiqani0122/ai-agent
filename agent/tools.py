def summarize_text(text: str) -> str:
    return text[:150] + "..."

def answer_question(text: str) -> str:
    if "capital of norway" in text.lower():
        return "The capital of Norway is Oslo."
    return "I don't know the answer yet."