def summarize_text(text: str) -> str:
    return text[:150] + "..."

def answer_question(text: str) -> str:
    if "capital of norway" in text.lower():
        return "The capital of Norway is Oslo."
    if "capital of sweden" in text:
        return "The capital of Sweden is Stockholm."
    if "capital of spain" in text:
        return "The capital of Spain is Madrid."
    
    return "I don't know the answer yet."