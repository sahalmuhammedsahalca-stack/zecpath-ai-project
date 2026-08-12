import re


FILLER_WORDS = [
    "um",
    "uh",
    "like",
    "you know",
    "actually"
]


def clean_text(text):

    text = text.lower()

    for word in FILLER_WORDS:
        text = re.sub(r"\b" + re.escape(word) + r"\b", "", text)

    text = " ".join(text.split())

    if text:
        text = text[0].upper() + text[1:]

    if text and text[-1] not in ".!?":
        text += "."

    return text