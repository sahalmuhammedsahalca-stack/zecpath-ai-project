def detect_hesitation(text):

    words = ["um", "uh", "maybe", "probably"]

    count = sum(text.lower().count(word) for word in words)

    return count