from ddgs import DDGS


def web_search(query: str, max_results: int = 6) -> str:
    """
    Search the internet and return text snippets.
    No answering logic here — just raw information.
    """
    snippets = []

    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                body = r.get("body")
                if body:
                    snippets.append(body)
    except Exception as e:
        return f"Search error: {e}"

    return "\n".join(snippets)


def summarize_text(text: str, max_length: int = 200) -> str:
    """
    Lightweight summarizer for short texts.
    (You can later replace this with an LLM.)
    """
    text = text.strip()

    if len(text) <= max_length:
        return text

    return text[:max_length].rsplit(" ", 1)[0] + "..."




