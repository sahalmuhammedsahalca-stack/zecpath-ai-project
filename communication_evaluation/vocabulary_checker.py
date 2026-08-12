def vocabulary(answer):

    words = len(set(answer.lower().split()))

    return 22 if words >= 8 else 16