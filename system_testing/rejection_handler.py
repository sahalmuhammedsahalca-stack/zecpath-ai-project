def reduce_false_rejection(status, score):

    if status == "Rejected" and score >= 60:
        return "Review"

    return status