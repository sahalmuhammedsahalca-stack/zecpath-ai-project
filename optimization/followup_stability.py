def stabilize_followup(previous_question, candidate_answer):

    if not candidate_answer or not candidate_answer.strip():
        return {
            "action": "follow_up",
            "reason": "Missing answer"
        }

    if len(candidate_answer.strip()) < 10:
        return {
            "action": "follow_up",
            "reason": "Answer too short"
        }

    return {
        "action": "continue",
        "reason": "Answer sufficient"
    }