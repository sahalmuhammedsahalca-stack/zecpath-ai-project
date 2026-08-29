def normalize_intent(intent):
    """
    Normalize candidate intent into a consistent category.
    """

    if not intent:
        return "Unknown"

    normalized = intent.strip().lower()

    intent_map = {
        "technical": "Technical",
        "technical question": "Technical",
        "coding": "Technical",
        "behavioral": "Behavioral",
        "behavioral question": "Behavioral",
        "hr": "HR",
        "hr question": "HR",
        "general": "General",
        "general question": "General"
    }

    return intent_map.get(normalized, "Unknown")


def analyze_intent_consistency(intents):
    """
    Analyze consistency across detected intents.
    """

    normalized_intents = [
        normalize_intent(intent)
        for intent in intents
    ]

    known_intents = [
        intent for intent in normalized_intents
        if intent != "Unknown"
    ]

    if not known_intents:
        consistency = "Low"

    elif len(set(known_intents)) == 1:
        consistency = "High"

    else:
        consistency = "Moderate"

    return {
        "normalized_intents": normalized_intents,
        "consistency": consistency,
        "explanation": (
            "Intent consistency is evaluated using normalized "
            "intent categories."
        )
    }