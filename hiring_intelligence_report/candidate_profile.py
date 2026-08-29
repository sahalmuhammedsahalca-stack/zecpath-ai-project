from hiring_intelligence_report.report_generator import (
    generate_hiring_report
)


def generate_candidate_profile(
    candidate_id,
    candidate_name,
    job_role,
    ats_score,
    screening_score,
    hr_interview_score,
    technical_score,
    behavioral_score,
    integrity_risk_score,
    hiring_fit_percentage,
    final_recommendation,
    confidence_score
):
    """
    Generate the complete AI candidate profile.
    """

    report = generate_hiring_report(
        candidate_id,
        candidate_name,
        job_role,
        ats_score,
        screening_score,
        hr_interview_score,
        technical_score,
        behavioral_score,
        integrity_risk_score,
        hiring_fit_percentage,
        final_recommendation,
        confidence_score
    )

    report["profile_status"] = "Complete"

    return report