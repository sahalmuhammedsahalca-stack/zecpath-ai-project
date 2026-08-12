from conversation_flow.decision_tree import next_state
from conversation_flow.fallback_handler import fallback_question
from conversation_flow.followup_engine import followup


def process_answer(answer):

    state = next_state(answer)

    if state == "RETRY":
        return {
            "state": state,
            "message": fallback_question()
        }

    if state == "FOLLOWUP":
        return {
            "state": state,
            "message": followup()
        }

    return {
        "state": "QUESTION",
        "message": "Proceed to the next question."
    }