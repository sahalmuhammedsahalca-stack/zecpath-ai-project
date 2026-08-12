def next_state(answer):

    answer = answer.lower().strip()

    if answer == "":
        return "RETRY"

    if answer == "repeat":
        return "FOLLOWUP"

    if "don't know" in answer or "dont know" in answer:
        return "FOLLOWUP"

    return "QUESTION"