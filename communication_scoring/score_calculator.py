def calculate_score(confidence, sentiment, hesitation):

    score = 100

    if confidence == "Low":
        score -= 20

    if sentiment == "Negative":
        score -= 20

    score -= hesitation * 5

    if score < 0:
        score = 0

    return score