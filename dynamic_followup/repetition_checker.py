def remove_duplicates(history, question):

    if question in history:
        return False

    history.append(question)
    return True