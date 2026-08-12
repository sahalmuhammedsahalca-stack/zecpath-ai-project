def sentiment(answer):

    positive = ["confident", "success", "completed", "achieved"]

    score = sum(answer.lower().count(word) for word in positive)

    return min(25, 15 + score * 5)