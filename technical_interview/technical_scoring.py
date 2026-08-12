def calculate_technical_score(
    technical_knowledge,
    practical_experience,
    problem_solving,
    conceptual_understanding,
    scenario_handling
):
    """
    Calculate the overall technical interview score.
    """

    scores = [
        technical_knowledge,
        practical_experience,
        problem_solving,
        conceptual_understanding,
        scenario_handling
    ]

    # Validate scores
    if any(score < 0 or score > 100 for score in scores):
        raise ValueError("Each score must be between 0 and 100.")

    final_score = sum(scores) / len(scores)

    if final_score >= 85:
        recommendation = "Highly Recommended"
    elif final_score >= 70:
        recommendation = "Recommended"
    elif final_score >= 50:
        recommendation = "Needs Review"
    else:
        recommendation = "Not Recommended"

    return {
        "technical_score": round(final_score, 2),
        "recommendation": recommendation
    }