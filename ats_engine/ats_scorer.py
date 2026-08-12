def calculate_ats_score(
    skill_score=0,
    experience_score=0,
    education_score=0,
    semantic_score=0,
    weights=None
):
    """
    Calculates the final ATS score with
    configurable weights.
    """

    if weights is None:
        weights = {
            "skills": 40,
            "experience": 25,
            "education": 15,
            "semantic": 20
        }

    final_score = (
        skill_score * weights["skills"] +
        experience_score * weights["experience"] +
        education_score * weights["education"] +
        semantic_score * weights["semantic"]
    ) / 100

    explanation = {
        "Skill Match": f"{skill_score}% × {weights['skills']}%",
        "Experience": f"{experience_score}% × {weights['experience']}%",
        "Education": f"{education_score}% × {weights['education']}%",
        "Semantic": f"{semantic_score}% × {weights['semantic']}%"
    }

    return {
        "final_score": round(final_score, 2),
        "weights": weights,
        "explanation": explanation
    }