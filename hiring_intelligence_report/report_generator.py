def generate_hiring_report(
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
    Generate a structured hiring intelligence report.
    """

    scores = {
        "ATS Score": ats_score,
        "Screening Score": screening_score,
        "HR Interview Score": hr_interview_score,
        "Technical Score": technical_score,
        "Behavioral Score": behavioral_score
    }

    strengths = []

    for area, score in scores.items():
        if score >= 80:
            strengths.append(area)

    weaknesses = []

    for area, score in scores.items():
        if score < 60:
            weaknesses.append(area)

    risk_indicators = []

    if integrity_risk_score >= 80:
        risk_indicators.append("High integrity risk")

    if behavioral_score < 60:
        risk_indicators.append("Behavioral concerns")

    if not risk_indicators:
        risk_indicators.append("No major risk indicators detected")

    if not strengths:
        strengths.append("No major strengths identified")

    if not weaknesses:
        weaknesses.append("No major weaknesses identified")

    recruiter_summary = (
        f"{candidate_name} is being evaluated for the "
        f"{job_role} role. The final recommendation is "
        f"{final_recommendation} with a confidence score of "
        f"{confidence_score}."
    )

    return {
        "candidate_id": candidate_id,
        "candidate_name": candidate_name,
        "job_role": job_role,
        "scores": scores,
        "hiring_fit_percentage": hiring_fit_percentage,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "risk_indicators": risk_indicators,
        "final_recommendation": final_recommendation,
        "confidence_score": confidence_score,
        "recruiter_summary": recruiter_summary
    }