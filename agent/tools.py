def summarize_text(text: str) -> str:
    return text[:150] + "..."

def answer_question(text: str) -> str:
    
    # Capital questions
    if "capital of norway" in text.lower():
        return "The capital of Norway is Oslo."
    if "capital of sweden" in text:
        return "The capital of Sweden is Stockholm."
    if "capital of spain" in text:
        return "The capital of Spain is Madrid."
    
    # Population questions
    if "population of norwat" in text.lower():
        return "Norway has a population of 5.5 million people."
    if "population of sweden" in text:
        return "Sweden has a population of about 10.5 million people."
    if "population of spain" in text:
        return "Spain has a population of about 49.6 million people."
    
    # Currency questions
    if "currency of norway" in text:
        return "The currency of Norway is the Norwegian Krone."
    if "currency of sweden" in text:
        return "The currency of Sweden is the Swedish Krona."
    if "currency of spain" in text:
        return "The currency of Spain is the Euro."
    
    # Continent questions
    if "where is norway" in text or "which continent is norway in" in text:
        return "Norway is in Europe."
    if "where is sweden" in text or "which continent is sweden in" in text:
        return "Sweden is in Europe."
    if "where is spain" in text or "which continent is spain in" in text:
        return "Spain is in Europe."
    
    
    return "I don't know the answer yet."