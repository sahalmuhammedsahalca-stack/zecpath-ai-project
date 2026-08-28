from final_recommendation.recommendation_logic import (
    determine_recommendation
)

from final_recommendation.confidence_calculator import (
    calculate_confidence
)


def generate_final_decision(
    candidate_id,
    candidate_name,
    overall_score,
    behavioral_score,
    integrity_risk_score
):
    """
    Generate the final hiring recommendation.
    """

    recommendation = determine_recommendation(
        overall_score,
        behavioral_score,
        integrity_risk_score
    )

    confidence = calculate_confidence(
        overall_score,
        behavioral_score,
        integrity_risk_score
    )

    risk_factors = []

    if behavioral_score < 60:
        risk_factors.append("Behavioral concerns")

    if integrity_risk_score >= 80:
        risk_factors.append("High integrity risk")

    if not risk_factors:
        risk_factors.append("No major risk factors detected")

    explanation = (
        f"Final recommendation is {recommendation} "
        f"based on overall score, behavioral score, "
        f"and integrity risk."
    )

    return {
        "candidate_id": candidate_id,
        "candidate_name": candidate_name,
        "overall_score": overall_score,
        "behavioral_score": behavioral_score,
        "integrity_risk_score": integrity_risk_score,
        "recommendation": recommendation,
        "confidence_score": confidence,
        "risk_factors": risk_factors,
        "explanation": explanation
    }