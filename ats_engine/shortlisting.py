def shortlist_candidate(score):
    """
    Categorizes candidates based on ATS score.
    """

    if score >= 85:
        return "Shortlisted"

    elif score >= 70:
        return "Review"

    else:
        return "Rejected"