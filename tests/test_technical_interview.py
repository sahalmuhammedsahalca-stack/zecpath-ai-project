from technical_interview.adaptive_question_logic import select_next_question
from technical_interview.technical_scoring import calculate_technical_score


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
print("TECHNICAL INTERVIEW INTEGRATION TEST")
print("=" * 50)

print()
print("ADAPTIVE QUESTION")

question_result = select_next_question(
    current_level=2,
    answer_score=90,
    available_questions=questions
)

print(question_result)

print()
print("TECHNICAL SCORING")

score_result = calculate_technical_score(
    technical_knowledge=90,
    practical_experience=85,
    problem_solving=88,
    conceptual_understanding=92,
    scenario_handling=87
)

print(score_result)

print()
print("INTEGRATION STATUS")

if (
    question_result["status"] == "Question selected"
    and score_result["recommendation"] == "Highly Recommended"
):
    print("Technical Interview Integration: PASSED")
else:
    print("Technical Interview Integration: REVIEW REQUIRED")