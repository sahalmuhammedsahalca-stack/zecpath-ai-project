def normalize_score(score):

    score = float(score)

    if score < 0:
        return 0.0

    if score > 100:
        return 100.0

    return round(score, 2)


def detect_scoring_anomaly(score):

    score = normalize_score(score)

    return "Normal" if 0 <= score <= 100 else "Anomaly"