from technical_interview.adaptive_question_logic import select_next_question


questions = [
    {
        "level": 1,
        "question": "What is a variable in Python?"
    },
    {
        "level": 2,
        "question": "What is a Python list comprehension?"
    },
    {
        "level": 3,
        "question": "How would you optimize a slow Python program?"
    },
    {
        "level": 4,
        "question": "How would you debug a production Python application?"
    },
    {
        "level": 5,
        "question": "How would you design a scalable Python backend?"
    }
]


print("=" * 50)
print("ADAPTIVE QUESTION SELECTION")
print("=" * 50)

print(
    select_next_question(
        current_level=2,
        answer_score=90,
        available_questions=questions
    )
)

print(
    select_next_question(
        current_level=3,
        answer_score=40,
        available_questions=questions
    )
)

print(
    select_next_question(
        current_level=2,
        answer_score=65,
        available_questions=questions
    )
)