from unified_scoring.weight_config import get_weights


def calculate_unified_score(
    ats_score,
    screening_score,
    hr_interview_score,
    job_role
):

    weights = get_weights(job_role)

    unified_score = (
        ats_score * weights["ats"] / 100
        + screening_score * weights["screening"] / 100
        + hr_interview_score * weights["hr_interview"] / 100
    )

    return round(unified_score, 2)