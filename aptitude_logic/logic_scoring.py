def score(answer):

    keywords = [
        "analyze",
        "plan",
        "communicate",
        "solve"
    ]

    total = sum(
        1 for word in keywords
        if word in answer.lower()
    )

    return total * 25