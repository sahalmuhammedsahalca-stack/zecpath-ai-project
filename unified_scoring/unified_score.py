from unified_scoring.scoring_engine import calculate_unified_score
from unified_scoring.hiring_fit import calculate_hiring_fit
from unified_scoring.weight_config import get_weights


def generate_unified_score(
    candidate_name,
    job_role,
    ats_score,
    screening_score,
    hr_interview_score
):

    weights = get_weights(job_role)

    unified_score = calculate_unified_score(
        ats_score,
        screening_score,
        hr_interview_score,
        job_role
    )

    hiring_fit = calculate_hiring_fit(
        unified_score
    )

    return {
        "candidate_name": candidate_name,
        "job_role": job_role,
        "ats_score": ats_score,
        "screening_score": screening_score,
        "hr_interview_score": hr_interview_score,
        "weights": weights,
        "unified_score": unified_score,
        "hiring_fit_percentage": hiring_fit[
            "hiring_fit_percentage"
        ],
        "fit_category": hiring_fit["fit_category"]
    }