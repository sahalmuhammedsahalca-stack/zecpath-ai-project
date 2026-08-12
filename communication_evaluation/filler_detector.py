def filler(answer):

    fillers = ["um", "uh", "like"]

    count = sum(answer.lower().split().count(word) for word in fillers)

    return max(0, 10 - count)