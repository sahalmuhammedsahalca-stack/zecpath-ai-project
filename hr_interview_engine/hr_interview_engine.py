from hr_interview_engine.question_generator import generate_questions
from hr_interview_engine.state_manager import create_state
from hr_interview_engine.conversation_phase import PHASES

def start_interview(level, role_type):

    questions = generate_questions(level, role_type)

    states = []

    for i, question in enumerate(questions, start=1):
        state = create_state(i)
        state["question"] = question
        states.append(state)

    return {
        "phases": PHASES,
        "questions": states
    }