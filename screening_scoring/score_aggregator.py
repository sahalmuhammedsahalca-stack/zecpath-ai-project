from screening_scoring.score_normalizer import normalize_score

def aggregate_scores(question_scores):

    total = sum(item["Total"] for item in question_scores)
    maximum = sum(item["Max"] for item in question_scores)

    return {
        "raw_score": total,
        "normalized_score": normalize_score(total, maximum)
    }