def determine_recommendation(
    overall_score,
    behavioral_score,
    integrity_risk_score
):
    """
    Determine the candidate's hiring recommendation
    using score and risk-based rules.
    """

    if integrity_risk_score >= 80:
        return "Rejected"

    if overall_score >= 80 and behavioral_score >= 70:
        return "Selected"

    if overall_score >= 60 and behavioral_score >= 60:
        return "Hold / Review"

    return "Rejected"