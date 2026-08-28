from unified_scoring.score_normalizer import normalize_scores


DEFAULT_WEIGHTS = {
    "ATS": 20,
    "Screening": 15,
    "HR Interview": 15,
    "Technical Interview": 25,
    "Machine Test": 25,
}


ROLE_WEIGHTS = {
    "Data Analyst": {
        "ATS": 15,
        "Screening": 15,
        "HR Interview": 15,
        "Technical Interview": 25,
        "Machine Test": 30,
    },
    "Python Developer": {
        "ATS": 10,
        "Screening": 10,
        "HR Interview": 10,
        "Technical Interview": 30,
        "Machine Test": 40,
    },
    "Business Analyst": {
        "ATS": 20,
        "Screening": 20,
        "HR Interview": 20,
        "Technical Interview": 20,
        "Machine Test": 20,
    },
}


def get_role_weights(role):
    """
    Return scoring weights for the selected role.
    """

    if role in ROLE_WEIGHTS:
        return ROLE_WEIGHTS[role].copy()

    return DEFAULT_WEIGHTS.copy()


def validate_weights(weights):
    """
    Ensure all scoring weights add up to 100%.
    """

    required_rounds = {
        "ATS",
        "Screening",
        "HR Interview",
        "Technical Interview",
        "Machine Test",
    }

    if set(weights.keys()) != required_rounds:
        raise ValueError(
            "Weights must contain all required evaluation rounds."
        )

    total = sum(weights.values())

    if total != 100:
        raise ValueError(
            f"Weight total must equal 100. Current total: {total}"
        )

    return True


def calculate_hiring_fit_score(scores, weights):
    """
    Calculate the weighted Hiring Fit Score.
    """

    normalized_scores = normalize_scores(scores)

    validate_weights(weights)

    weighted_scores = {}

    for round_name, weight in weights.items():
        weighted_scores[round_name] = round(
            normalized_scores[round_name] * (weight / 100),
            2
        )

    hiring_fit_score = round(
        sum(weighted_scores.values()),
        2
    )

    return {
        "normalized_scores": normalized_scores,
        "weights": weights,
        "weighted_scores": weighted_scores,
        "hiring_fit_score": hiring_fit_score,
    }