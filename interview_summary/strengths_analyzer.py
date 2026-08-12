def analyze_strengths(candidate):

    strengths = []

    if candidate["communication_score"] >= 80:
        strengths.append("Strong communication skills")

    if candidate["confidence_score"] >= 80:
        strengths.append("Good confidence")

    if candidate["technical_score"] >= 80:
        strengths.append("Strong technical knowledge")

    return strengths