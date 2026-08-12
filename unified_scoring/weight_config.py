DEFAULT_WEIGHTS = {
    "ats": 30,
    "screening": 30,
    "hr_interview": 40
}


ROLE_WEIGHTS = {
    "Data Analyst": {
        "ats": 35,
        "screening": 25,
        "hr_interview": 40
    },
    "Software Developer": {
        "ats": 30,
        "screening": 30,
        "hr_interview": 40
    },
    "HR Executive": {
        "ats": 25,
        "screening": 30,
        "hr_interview": 45
    }
}


def get_weights(job_role):

    return ROLE_WEIGHTS.get(
        job_role,
        DEFAULT_WEIGHTS
    )