def communication_metrics(text):

    words = len(text.split())

    return {
        "response_length": words,
        "pace": "Normal"
    }