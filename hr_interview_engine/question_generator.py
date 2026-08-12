from hr_interview_engine.question_bank import QUESTION_BANK

def generate_questions(level, role_type):
    return QUESTION_BANK[level][role_type]