def normalize_score(score):
    """
    Ensures ATS scores remain between 0 and 100.
    """

    if score < 0:
        return 0

    if score > 100:
        return 100

    return round(score, 2)