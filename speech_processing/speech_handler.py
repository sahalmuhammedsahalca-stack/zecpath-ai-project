def handle_partial_answer(text):

    if len(text.split()) < 3:
        return "Partial Answer"

    return "Complete Answer"