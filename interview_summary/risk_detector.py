def detect_risks(candidate):

    risks = []

    if candidate["communication_score"] < 60:
        risks.append("Low communication score")

    if candidate["confidence_score"] < 60:
        risks.append("Low confidence score")

    if candidate["technical_score"] < 60:
        risks.append("Low technical score")

    return risks