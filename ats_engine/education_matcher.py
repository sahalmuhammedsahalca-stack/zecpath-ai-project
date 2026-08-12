def calculate_education_match(resume_education, jd_education):
    """
    Compares candidate education with
    job description education requirement.
    """

    resume_text = " ".join(resume_education).lower()
    jd_text = jd_education.lower()

    if jd_text in resume_text:
        score = 100
    elif any(word in resume_text for word in jd_text.split()):
        score = 70
    else:
        score = 30

    return {
        "required_education": jd_education,
        "candidate_education": resume_education,
        "education_score": score
    }