def normalize_score(score):
    """
    Normalize a candidate score to a 0-100 scale.
    """

    try:
        score = float(score)
    except (TypeError, ValueError):
        raise ValueError("Score must be a numeric value.")

    return round(max(0.0, min(100.0, score)), 2)


def normalize_scores(scores):
    """
    Normalize all evaluation round scores to a 0-100 scale.
    """

    if not isinstance(scores, dict):
        raise ValueError("Scores must be provided as a dictionary.")

    return {
        round_name: normalize_score(score)
        for round_name, score in scores.items()
    }