from eligibility_engine.rules import check_eligibility


def generate_decision(candidate):

    status = check_eligibility(
        candidate["job_role"],
        candidate["ats_score"],
        candidate["skills"],
        candidate["experience"]
    )

    candidate["status"] = status

    return candidate