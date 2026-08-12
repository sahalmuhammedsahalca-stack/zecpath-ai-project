def recommend(score):

    if score >= 85:
        return "Strong Communication"

    elif score >= 70:
        return "Good Communication"

    elif score >= 50:
        return "Needs Improvement"

    return "Poor Communication"