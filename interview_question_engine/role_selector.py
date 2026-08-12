from interview_question_engine.question_bank import QUESTIONS

def select_questions(role):
    return QUESTIONS.get(role, [])