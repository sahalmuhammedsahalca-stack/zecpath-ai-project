def evaluate_thresholds(score):
    """
    Classify a candidate score using refined thresholds.
    """

    if score >= 85:
        return "Highly Recommended"

    if score >= 70:
        return "Recommended"

    if score >= 60:
        return "Needs Review"

    return "Not Recommended"


def compare_thresholds(score):
    """
    Compare the refined scoring classification with
    the existing score ranges.
    """

    refined_classification = evaluate_thresholds(score)

    return {
        "score": score,
        "refined_classification": refined_classification,
        "explanation": (
            "Refined scoring thresholds provide clearer separation "
            "between strong, acceptable, review, and weak candidates."
        )
    }