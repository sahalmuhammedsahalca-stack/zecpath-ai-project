from unified_scoring.hiring_fit_calculator import (
    get_role_weights,
    calculate_hiring_fit_score,
)


def classify_hiring_fit(score):
    """
    Classify the final Hiring Fit Score.
    """

    if score >= 85:
        return "Excellent Hiring Fit"

    elif score >= 75:
        return "Strong Hiring Fit"

    elif score >= 60:
        return "Moderate Hiring Fit"

    else:
        return "Low Hiring Fit"


def aggregate_candidate_scores(candidate_id, candidate_name, role, scores):
    """
    Aggregate all recruitment round scores into
    one unified candidate evaluation.
    """

    required_rounds = {
        "ATS",
        "Screening",
        "HR Interview",
        "Technical Interview",
        "Machine Test",
    }

    if not required_rounds.issubset(scores.keys()):
        missing_rounds = required_rounds - set(scores.keys())

        raise ValueError(
            f"Missing evaluation rounds: {sorted(missing_rounds)}"
        )

    weights = get_role_weights(role)

    calculation = calculate_hiring_fit_score(
        scores,
        weights
    )

    hiring_fit_score = calculation["hiring_fit_score"]

    classification = classify_hiring_fit(
        hiring_fit_score
    )

    return {
        "candidate_id": candidate_id,
        "candidate_name": candidate_name,
        "role": role,
        "round_scores": scores,
        "normalized_scores": calculation["normalized_scores"],
        "weights": calculation["weights"],
        "weighted_scores": calculation["weighted_scores"],
        "hiring_fit_score": hiring_fit_score,
        "classification": classification,
        "explanation": (
            "Hiring Fit Score is calculated by normalizing "
            "all recruitment round scores and applying "
            "role-specific weights."
        ),
    }