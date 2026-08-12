def uncertainty(answer):

    phrases = ["maybe", "perhaps", "i think", "not sure"]

    count = sum(answer.lower().count(p) for p in phrases)

    return max(5, 25 - count * 5)