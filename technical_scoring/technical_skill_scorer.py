def calculate_technical_score(
    accuracy,
    depth,
    logical_reasoning,
    real_world_applicability
):
    """
    Calculate a technical skill score based on four evaluation parameters.
    """

    score = (
        accuracy
        + depth
        + logical_reasoning
        + real_world_applicability
    ) / 4

    return round(score, 2)


def classify_technical_depth(
    accuracy,
    depth,
    logical_reasoning,
    real_world_applicability
):
    """
    Classify the quality of a technical answer.
    """

    score = calculate_technical_score(
        accuracy,
        depth,
        logical_reasoning,
        real_world_applicability
    )

    if score >= 80:
        return "Deep Technical Understanding"

    elif score >= 60:
        return "Moderate Technical Understanding"

    else:
        return "Shallow Technical Understanding"


def get_question_type_weight(question_type):
    """
    Return the scoring weight for each technical question type.
    """

    weights = {
        "conceptual": 1.00,
        "coding": 1.05,
        "practical": 1.05,
        "debugging": 1.10,
        "scenario_based": 1.10,
        "architecture": 1.15,
        "system_design": 1.20
    }

    return weights.get(question_type.lower(), 1.00)


def normalize_score(score, difficulty_level):
    """
    Normalize technical scores according to question difficulty.
    """

    difficulty_weights = {
        1: 1.00,
        2: 1.00,
        3: 1.05,
        4: 1.10,
        5: 1.15
    }

    weight = difficulty_weights.get(difficulty_level, 1.00)

    normalized_score = score * weight

    return round(min(normalized_score, 100), 2)


def calculate_question_score(
    accuracy,
    depth,
    logical_reasoning,
    real_world_applicability,
    question_type,
    difficulty_level
):
    """
    Calculate a normalized technical question score.
    """

    base_score = calculate_technical_score(
        accuracy,
        depth,
        logical_reasoning,
        real_world_applicability
    )

    type_weight = get_question_type_weight(question_type)

    weighted_score = base_score * type_weight

    normalized_score = normalize_score(
        weighted_score,
        difficulty_level
    )

    return normalized_score


def generate_technical_evaluation(
    accuracy,
    depth,
    logical_reasoning,
    real_world_applicability
):
    """
    Generate an explainable technical evaluation.
    """

    score = calculate_technical_score(
        accuracy,
        depth,
        logical_reasoning,
        real_world_applicability
    )

    depth_classification = classify_technical_depth(
        accuracy,
        depth,
        logical_reasoning,
        real_world_applicability
    )

    return {
        "accuracy": accuracy,
        "depth": depth,
        "logical_reasoning": logical_reasoning,
        "real_world_applicability": real_world_applicability,
        "technical_score": score,
        "technical_depth": depth_classification,
        "explanation": (
            "Technical score is based on accuracy, depth, "
            "logical reasoning, and real-world applicability."
        )
    }


def generate_technical_report(
    candidate_name,
    question_type,
    difficulty_level,
    accuracy,
    depth,
    logical_reasoning,
    real_world_applicability
):
    """
    Generate a structured technical evaluation report.
    """

    score = calculate_question_score(
        accuracy,
        depth,
        logical_reasoning,
        real_world_applicability,
        question_type,
        difficulty_level
    )

    if score >= 80:
        depth_classification = "Deep Technical Understanding"
    elif score >= 60:
        depth_classification = "Moderate Technical Understanding"
    else:
        depth_classification = "Shallow Technical Understanding"

    return {
        "candidate": candidate_name,
        "question_type": question_type,
        "difficulty_level": difficulty_level,
        "technical_score": score,
        "technical_depth": depth_classification,
        "skill_breakdown": {
            "accuracy": accuracy,
            "depth": depth,
            "logical_reasoning": logical_reasoning,
            "real_world_applicability": real_world_applicability
        },
        "explanation": (
            "The technical evaluation is based on accuracy, "
            "depth, logical reasoning, real-world applicability, "
            "question type, and difficulty level."
        )
    }