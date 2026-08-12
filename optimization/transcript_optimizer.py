FILLER_WORDS = [
    "um",
    "uh",
    "like",
    "you know",
    "actually"
]


def clean_transcript(text):

    if not text:
        return ""

    cleaned = text.strip()

    for filler in FILLER_WORDS:
        cleaned = cleaned.replace(filler, "")

    cleaned = " ".join(cleaned.split())

    if cleaned:
        cleaned = cleaned[0].upper() + cleaned[1:]

    return cleaned