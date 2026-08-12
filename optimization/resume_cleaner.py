import re


def clean_resume(text):

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # Remove extra blank lines
    text = re.sub(r"\n+", "\n", text)

    # Remove unwanted symbols
    text = re.sub(r"[^\w\s@.,:/()-]", "", text)

    return text.strip()