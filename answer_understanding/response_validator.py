def validate_answer(answer):

    if len(answer.strip()) == 0:
        return "Missing Answer"

    if len(answer.split()) < 3:
        return "Vague Answer"

    if "football" in answer.lower():
        return "Off Topic"

    return "Valid"