import re


def clean_text(text):
    """
    Cleans the extracted resume text by removing
    extra spaces, blank lines, and unnecessary whitespace.
    """

    # Replace multiple spaces with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Replace multiple blank lines with a single newline
    text = re.sub(r"\n+", "\n", text)

    # Remove leading and trailing whitespace
    text = text.strip()

    return text