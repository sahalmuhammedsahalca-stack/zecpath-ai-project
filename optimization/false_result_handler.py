def reduce_false_results(score, threshold=70):

    if score >= threshold:
        return "Eligible"

    return "Review"