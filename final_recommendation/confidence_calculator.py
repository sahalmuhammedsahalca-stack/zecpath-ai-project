def calculate_confidence(
    overall_score,
    behavioral_score,
    integrity_risk_score
):
    """
    Calculate confidence in the final recommendation.
    """

    score_confidence = overall_score

    behavioral_confidence = behavioral_score

    integrity_confidence = 100 - integrity_risk_score

    confidence = (
        score_confidence
        + behavioral_confidence
        + integrity_confidence
    ) / 3

    return round(max(0, min(100, confidence)), 2)