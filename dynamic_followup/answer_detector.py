def detect_answer(answer):

    if len(answer.split()) < 4:
        return "Incomplete"

    return "Complete"