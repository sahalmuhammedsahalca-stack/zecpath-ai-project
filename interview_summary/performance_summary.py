def summarize_performance(candidate):

    scores = [
        candidate["technical_score"],
        candidate["interview_score"],
        candidate["communication_score"],
        candidate["confidence_score"]
    ]

    average = sum(scores) / len(scores)

    if average >= 85:
        return "Excellent overall HR performance"

    if average >= 70:
        return "Good overall HR performance"

    if average >= 60:
        return "Average overall HR performance"

    return "Needs improvement"