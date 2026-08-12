def evaluate_task(
    correctness,
    efficiency,
    code_quality,
    problem_solving
):
    """
    Evaluate a candidate's machine test performance.
    """

    score = (
        correctness
        + efficiency
        + code_quality
        + problem_solving
    ) / 4

    if score >= 80:
        classification = "Strong Technical Performance"

    elif score >= 60:
        classification = "Moderate Technical Performance"

    else:
        classification = "Weak Technical Performance"

    return {
        "correctness": correctness,
        "efficiency": efficiency,
        "code_quality": code_quality,
        "problem_solving": problem_solving,
        "task_score": round(score, 2),
        "classification": classification
    }