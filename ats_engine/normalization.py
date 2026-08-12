import re

def normalize_text(text):
    """
    Normalize resume text for fair comparison.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove special characters (keep letters, numbers and spaces)
    text = re.sub(r"[^a-z0-9 ]", "", text)

    return text.strip()