def analyze_round_consistency(round_scores):
    """
    Analyze score consistency across interview rounds.
    """

    if not round_scores:
        return {
            "average_score": 0,
            "score_variation": 0,
            "consistency": "No Data",
            "explanation": "No round scores were provided."
        }

    average_score = sum(round_scores) / len(round_scores)

    score_variation = max(round_scores) - min(round_scores)

    if score_variation <= 10:
        consistency = "High"

    elif score_variation <= 20:
        consistency = "Moderate"

    else:
        consistency = "Low"

    return {
        "average_score": round(average_score, 2),
        "score_variation": score_variation,
        "consistency": consistency,
        "explanation": (
            "Cross-round consistency is determined by the "
            "variation between round scores."
        )
    }