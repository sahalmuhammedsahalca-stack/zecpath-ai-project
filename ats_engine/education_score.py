def calculate_education_score(match_result):
    """
    Calculates the final education score.
    """

    score = match_result["education_score"]

    if score >= 90:
        level = "Excellent"

    elif score >= 70:
        level = "Good"

    elif score >= 50:
        level = "Average"

    else:
        level = "Poor"

    return {
        "education_score": score,
        "level": level
    }