def detect_language(text):

    if "/" in text:
        return "Mixed"

    return "Single"