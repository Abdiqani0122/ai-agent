from .countries import COUNTRIES

def summarize_text(text: str) -> str:
    return text[:150] + "..."

def answer_question(text: str) -> str:

    for country, info in COUNTRIES.items():
        if country in text:
            if "capital" in text:
                return f"The capital of {country.title()} is {info['capital']}."
            if "currency" in text:
                return f"The currency of {country.title()} is the {info['currency']}."
            if "continent" in text:
                return f"{country.title()} is in {info['continent']}."
            if "population" in text:
                return f"{country.title()} has a population of {info['population']}."

    return "I don't know the answer yet."