def analyze_culture(candidate):

    if candidate["communication_score"] >= 80 and candidate["confidence_score"] >= 80:
        return "Positive cultural fit indicators"

    return "Cultural fit requires further review"