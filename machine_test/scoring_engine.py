def calculate_machine_test_score(
    correctness,
    efficiency,
    code_quality,
    problem_solving,
    time_score
):
    """
    Calculate the final machine test score.
    """

    technical_score = (
        correctness
        + efficiency
        + code_quality
        + problem_solving
    ) / 4

    final_score = (
        technical_score * 0.8
        + time_score * 0.2
    )

    return round(final_score, 2)


def classify_machine_test_score(score):
    """
    Classify overall machine test performance.
    """

    if score >= 80:
        return "Highly Recommended"

    elif score >= 60:
        return "Recommended"

    else:
        return "Needs Review"