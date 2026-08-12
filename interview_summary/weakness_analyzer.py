def analyze_weaknesses(candidate):

    weaknesses = []

    if candidate["communication_score"] < 70:
        weaknesses.append("Communication needs improvement")

    if candidate["confidence_score"] < 70:
        weaknesses.append("Confidence needs improvement")

    if candidate["technical_score"] < 70:
        weaknesses.append("Technical knowledge needs improvement")

    return weaknesses