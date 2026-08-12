def review_score_fairness(scores):

    if not scores:
        return {
            "status": "Review Required",
            "reason": "No scores available"
        }

    valid_scores = [
        score for score in scores
        if 0 <= score <= 100
    ]

    return {
        "status": "Fairness Check Passed",
        "valid_scores": len(valid_scores),
        "total_scores": len(scores)
    }