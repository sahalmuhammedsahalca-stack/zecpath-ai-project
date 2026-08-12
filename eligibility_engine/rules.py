from eligibility_engine.config import RULES


def check_eligibility(
    job_role,
    ats_score,
    candidate_skills,
    experience
):

    rule = RULES[job_role]

    # Score Check
    if ats_score < rule["minimum_score"]:
        return "Rejected"

    # Experience Check
    if experience < rule["minimum_experience"]:
        return "Review"

    # Skills Check
    missing_skills = []

    for skill in rule["mandatory_skills"]:

        if skill not in candidate_skills:
            missing_skills.append(skill)

    if len(missing_skills) > 0:
        return "Review"

    return "Eligible"