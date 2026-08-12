def assign_confidence(skills):
    """
    Assigns confidence scores to extracted skills.
    """

    skill_scores = {}

    for skill in skills:
        skill_scores[skill] = 1.0

    return skill_scores