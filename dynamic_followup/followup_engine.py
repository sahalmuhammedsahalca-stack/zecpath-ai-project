from dynamic_followup.answer_detector import detect_answer
from dynamic_followup.followup_generator import generate_followup
from dynamic_followup.difficulty_adapter import adapt
from dynamic_followup.repetition_checker import remove_duplicates
from dynamic_followup.state_tracker import create_state

def evaluate(answer, confidence):

    state = create_state()

    status = detect_answer(answer)

    question = generate_followup(status)

    remove_duplicates(state["history"], question)

    return {
        "answer_status": status,
        "difficulty": adapt(confidence),
        "followup": question,
        "state": state
    }