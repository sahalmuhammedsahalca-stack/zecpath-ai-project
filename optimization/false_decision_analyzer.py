def analyze_decision(ai_decision, expected_decision):
    """
    Analyze an AI decision against the expected decision.

    Returns whether the decision is correct and identifies
    false positive or false negative cases.
    """

    if ai_decision == expected_decision:
        return {
            "ai_decision": ai_decision,
            "expected_decision": expected_decision,
            "decision_status": "Correct",
            "error_type": None,
            "explanation": "AI decision matches the expected decision."
        }

    if ai_decision == "Selected" and expected_decision == "Rejected":
        return {
            "ai_decision": ai_decision,
            "expected_decision": expected_decision,
            "decision_status": "Incorrect",
            "error_type": "False Positive",
            "explanation": (
                "AI selected the candidate when the expected decision "
                "was rejection."
            )
        }

    if ai_decision == "Rejected" and expected_decision == "Selected":
        return {
            "ai_decision": ai_decision,
            "expected_decision": expected_decision,
            "decision_status": "Incorrect",
            "error_type": "False Negative",
            "explanation": (
                "AI rejected the candidate when the expected decision "
                "was selection."
            )
        }

    return {
        "ai_decision": ai_decision,
        "expected_decision": expected_decision,
        "decision_status": "Incorrect",
        "error_type": "Decision Mismatch",
        "explanation": (
            "AI decision does not match the expected decision."
        )
    }