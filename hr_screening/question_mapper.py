from hr_screening.question_bank import QUESTION_BANK

def get_questions_by_category(category):
    return [
        question
        for question in QUESTION_BANK
        if question["category"] == category
    ]