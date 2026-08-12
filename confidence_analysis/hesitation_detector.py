def hesitation(answer):

    repeated = len(answer.split()) - len(set(answer.split()))

    if repeated >= 2:
        return 15

    return 25