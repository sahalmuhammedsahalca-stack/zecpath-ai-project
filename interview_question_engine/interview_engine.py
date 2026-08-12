from interview_question_engine.role_selector import select_questions
from interview_question_engine.duplicate_checker import remove_duplicates
from interview_question_engine.followup_generator import followup

def generate_interview(role):

    questions = remove_duplicates(select_questions(role))

    return {
        "questions": questions,
        "followup": followup(questions[0]) if questions else "No questions available."
    }