def generate_explanation(scores):

    return {
        "ats_score": scores.get("ats_score"),
        "screening_score": scores.get("screening_score"),
        "hr_interview_score": scores.get("hr_interview_score"),
        "explanation": (
            "Final hiring evaluation is based on "
            "job-related assessment scores."
        )
    }