def recommendation(score):

    if score >= 85:
        return "Highly Recommended"

    if score >= 70:
        return "Recommended"

    return "Needs Review"