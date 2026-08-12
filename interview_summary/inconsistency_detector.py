def detect_inconsistencies(candidate):

    inconsistencies = []

    if abs(
        candidate["technical_score"]
        - candidate["interview_score"]
    ) >= 25:
        inconsistencies.append(
            "Large difference between technical and interview performance"
        )

    return inconsistencies