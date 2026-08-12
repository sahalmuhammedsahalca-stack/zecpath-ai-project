def detect_inconsistency(difference):

    if difference > 5:
        return "Scoring inconsistency detected"

    return "No significant inconsistency"