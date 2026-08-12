def select_next_question(
    current_level,
    answer_score,
    available_questions
):
    """
    Select the next technical interview question
    based on candidate performance.
    """

    if answer_score >= 80:
        next_level = min(current_level + 1, 5)

    elif answer_score < 50:
        next_level = max(current_level - 1, 1)

    else:
        next_level = current_level

    suitable_questions = [
        question
        for question in available_questions
        if question["level"] == next_level
    ]

    if not suitable_questions:
        suitable_questions = [
            question
            for question in available_questions
            if question["level"] == current_level
        ]

    if not suitable_questions:
        return {
            "level": next_level,
            "question": None,
            "status": "No suitable question found"
        }

    return {
        "level": next_level,
        "question": suitable_questions[0]["question"],
        "status": "Question selected"
    }
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