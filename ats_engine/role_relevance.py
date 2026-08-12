def calculate_role_relevance(experience_data, target_role):
    """
    Calculates relevance score based on previous job titles.
    """

    relevance_scores = []

    target = target_role.lower()

    for job in experience_data:

        title = job["job_title"].lower()

        if target in title:
            score = 100
        elif any(word in title for word in target.split()):
            score = 70
        else:
            score = 30

        relevance_scores.append({
            "job_title": job["job_title"],
            "score": score
        })

    return relevance_scores