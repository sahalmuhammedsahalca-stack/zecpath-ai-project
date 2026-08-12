from hr_screening.question_bank import QUESTION_BANK

def build_conversation():
    conversation = []

    for question in QUESTION_BANK:
        conversation.append({
            "question_id": question["id"],
            "question": question["question"],
            "category": question["category"]
        })

    return conversation