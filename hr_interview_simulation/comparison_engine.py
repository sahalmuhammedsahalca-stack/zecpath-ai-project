def compare(ai_score, manual_score):

    difference = abs(ai_score - manual_score)

    if difference <= 5:
        status = "Consistent"
    else:
        status = "Inconsistent"

    return {
        "difference": difference,
        "status": status
    }