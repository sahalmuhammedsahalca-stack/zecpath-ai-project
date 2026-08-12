def final_score(ats, interview, communication, confidence):

    score = (
        ats * 0.40 +
        interview * 0.30 +
        communication * 0.20 +
        confidence * 0.10
    )

    return round(score, 2)