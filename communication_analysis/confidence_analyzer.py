def analyze_confidence(text):

    text = text.lower()

    uncertainty = ["maybe", "probably", "i think", "not sure"]

    if any(word in text for word in uncertainty):
        return "Low"

    return "High"